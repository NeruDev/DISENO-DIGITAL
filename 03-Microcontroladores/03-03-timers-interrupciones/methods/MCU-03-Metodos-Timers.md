<!--
::METADATA::
type: method
topic_id: mcu-03-timers-interrupciones
file_id: metodos-timers
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, metodología, timer, interrupción]
search_keywords: "metodología timer, interrupción, PWM"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-03-Teoria-TimersInt.md) | [Problemas →](../problems/MCU-03-Problemas.md)

---

# Métodos: Timers e Interrupciones

## Método 1: Cálculo de Valores para Timer

### Fórmula General

```
Para interrupción periódica:

OCR = (F_CPU / (Prescaler × F_deseada)) - 1

Pasos:
1. Determinar frecuencia deseada
2. Probar prescalers hasta que OCR sea válido
3. Verificar que OCR < MAX del timer
```

### Tabla de Cálculo (16 MHz)

| F_deseada | Prescaler | OCR (8-bit) | OCR (16-bit) |
|-----------|-----------|-------------|--------------|
| 1 Hz | 256 | N/A | 62499 |
| 10 Hz | 256 | N/A | 6249 |
| 100 Hz | 64 | N/A | 2499 |
| 1 kHz | 64 | 249 | 249 |
| 10 kHz | 8 | 199 | 199 |

### Código de Verificación

```c
// Macro para calcular OCR
#define CALC_OCR(fpu, prescaler, freq) \
    (((fpu) / ((prescaler) * (freq))) - 1)

// Verificar en compilación
#if CALC_OCR(F_CPU, 256, 1) > 65535
    #error "Valor OCR fuera de rango"
#endif
```

---

## Método 2: Plantilla de Timer Periódico

```c
#include <avr/io.h>
#include <avr/interrupt.h>

// Configuración
#define TIMER_FREQ_HZ 1000

volatile uint32_t timer_millis = 0;

void timer_init(void) {
    // Timer0 en modo CTC
    TCCR0A = (1 << WGM01);
    
    // Prescaler /64
    TCCR0B = (1 << CS01) | (1 << CS00);
    
    // OCR para 1 kHz
    OCR0A = (F_CPU / 64 / TIMER_FREQ_HZ) - 1;  // = 249
    
    // Habilitar interrupción
    TIMSK0 = (1 << OCIE0A);
    
    sei();
}

ISR(TIMER0_COMPA_vect) {
    timer_millis++;
}

uint32_t millis(void) {
    uint32_t m;
    cli();
    m = timer_millis;
    sei();
    return m;
}
```

---

## Método 3: PWM para Control de Motor/LED

### Inicialización PWM

```c
// PWM en Timer0, canal A (pin OC0A = PD6)
void pwm_init(void) {
    // Pin como salida
    DDRD |= (1 << PD6);
    
    // Fast PWM, non-inverting, 8-bit
    TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
    
    // Prescaler /64 → ~1 kHz PWM
    TCCR0B = (1 << CS01) | (1 << CS00);
    
    OCR0A = 0;
}

void pwm_set_percent(uint8_t percent) {
    if (percent > 100) percent = 100;
    OCR0A = (uint8_t)((uint16_t)percent * 255 / 100);
}
```

### Tabla de Frecuencias PWM (Timer0, 16MHz)

| Prescaler | Fast PWM | Phase Correct |
|-----------|----------|---------------|
| 1 | 62.5 kHz | 31.25 kHz |
| 8 | 7.8 kHz | 3.9 kHz |
| 64 | 976 Hz | 488 Hz |
| 256 | 244 Hz | 122 Hz |
| 1024 | 61 Hz | 30 Hz |

---

## Método 4: Generador de Tonos

```c
// Generar tono de frecuencia específica
void tone_init(uint16_t frequency) {
    // Timer1 en modo CTC, toggle OC1A
    TCCR1A = (1 << COM1A0);  // Toggle en compare
    TCCR1B = (1 << WGM12) | (1 << CS11);  // CTC, prescaler /8
    
    // OCR para frecuencia (toggle = divide por 2)
    OCR1A = (F_CPU / 8 / frequency / 2) - 1;
    
    // Pin como salida
    DDRB |= (1 << PB1);  // OC1A
}

void tone_off(void) {
    TCCR1A = 0;
    PORTB &= ~(1 << PB1);
}

// Notas musicales
#define NOTE_C4  262
#define NOTE_D4  294
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_G4  392
#define NOTE_A4  440
#define NOTE_B4  494
#define NOTE_C5  523
```

---

## Método 5: Medición de Ancho de Pulso (Input Capture)

```c
volatile uint16_t pulse_width = 0;
volatile uint8_t pulse_ready = 0;

void input_capture_init(void) {
    // Timer1 normal, prescaler /8
    TCCR1B = (1 << CS11);
    
    // Captura en flanco de subida
    TCCR1B |= (1 << ICES1);
    
    // Habilitar interrupción de captura
    TIMSK1 = (1 << ICIE1);
    
    sei();
}

ISR(TIMER1_CAPT_vect) {
    static uint16_t rising_edge = 0;
    static uint8_t waiting_for_falling = 0;
    
    if (!waiting_for_falling) {
        // Flanco de subida
        rising_edge = ICR1;
        TCCR1B &= ~(1 << ICES1);  // Siguiente: flanco bajada
        waiting_for_falling = 1;
    } else {
        // Flanco de bajada
        pulse_width = ICR1 - rising_edge;
        TCCR1B |= (1 << ICES1);  // Siguiente: flanco subida
        waiting_for_falling = 0;
        pulse_ready = 1;
    }
}

// Convertir a microsegundos (prescaler /8, 16 MHz)
uint16_t get_pulse_us(void) {
    return pulse_width / 2;  // 2 ticks = 1 µs
}
```

---

## Método 6: Scheduler Simple (Round-Robin)

```c
#define MAX_TASKS 8

typedef void (*task_func)(void);

typedef struct {
    task_func func;
    uint16_t period_ms;
    uint16_t countdown;
    uint8_t enabled;
} task_t;

task_t tasks[MAX_TASKS];
volatile uint16_t tick_ms = 0;

void scheduler_init(void) {
    // Timer para tick de 1 ms
    timer_init();  // Ver Método 2
}

void scheduler_add_task(uint8_t id, task_func func, uint16_t period_ms) {
    tasks[id].func = func;
    tasks[id].period_ms = period_ms;
    tasks[id].countdown = period_ms;
    tasks[id].enabled = 1;
}

void scheduler_run(void) {
    static uint16_t last_tick = 0;
    
    while (1) {
        if (tick_ms != last_tick) {
            last_tick = tick_ms;
            
            for (uint8_t i = 0; i < MAX_TASKS; i++) {
                if (tasks[i].enabled && tasks[i].func) {
                    tasks[i].countdown--;
                    if (tasks[i].countdown == 0) {
                        tasks[i].countdown = tasks[i].period_ms;
                        tasks[i].func();
                    }
                }
            }
        }
    }
}

// ISR actualiza tick_ms (ver Método 2)
```

---

## Método 7: Timeout No Bloqueante

```c
// Estructura para timeout
typedef struct {
    uint32_t start;
    uint32_t duration;
} timeout_t;

void timeout_start(timeout_t *t, uint32_t duration_ms) {
    t->start = millis();
    t->duration = duration_ms;
}

uint8_t timeout_expired(timeout_t *t) {
    return (millis() - t->start) >= t->duration;
}

// Uso
void ejemplo_timeout(void) {
    timeout_t timeout;
    
    // Esperar respuesta con timeout de 1 segundo
    timeout_start(&timeout, 1000);
    
    while (!respuesta_recibida()) {
        if (timeout_expired(&timeout)) {
            // Error: timeout
            return;
        }
    }
    // Respuesta recibida a tiempo
}
```

---

## Método 8: Debounce con Timer

```c
#define DEBOUNCE_MS 50

typedef struct {
    volatile uint8_t state;
    volatile uint8_t changed;
    uint8_t counter;
    uint8_t pin_mask;
    volatile uint8_t *pin_reg;
} button_t;

button_t buttons[4];

// Llamar desde ISR de timer (cada 1 ms)
void debounce_update(void) {
    for (uint8_t i = 0; i < 4; i++) {
        uint8_t raw = (*buttons[i].pin_reg & buttons[i].pin_mask) ? 0 : 1;
        
        if (raw != buttons[i].state) {
            buttons[i].counter++;
            if (buttons[i].counter >= DEBOUNCE_MS) {
                buttons[i].state = raw;
                buttons[i].changed = 1;
                buttons[i].counter = 0;
            }
        } else {
            buttons[i].counter = 0;
        }
    }
}

uint8_t button_pressed(uint8_t id) {
    if (buttons[id].changed && buttons[id].state) {
        buttons[id].changed = 0;
        return 1;
    }
    return 0;
}
```

---

## Método 9: PWM Servo (1-2 ms pulsos)

```c
// Servo: pulso de 1-2 ms, período de 20 ms
// Timer1 16-bit para precisión

void servo_init(void) {
    // Fast PWM, ICR1 como TOP
    TCCR1A = (1 << COM1A1) | (1 << WGM11);
    TCCR1B = (1 << WGM13) | (1 << WGM12) | (1 << CS11);  // /8
    
    // TOP para 20 ms @ 16 MHz, /8
    ICR1 = 39999;  // (16M/8/50Hz) - 1
    
    // Pin OC1A como salida
    DDRB |= (1 << PB1);
}

// Ángulo 0-180 grados
void servo_set_angle(uint8_t angle) {
    // 1 ms = 1000 ticks, 2 ms = 4000 ticks
    uint16_t pulse = 2000 + ((uint32_t)angle * 2000 / 180);
    OCR1A = pulse;
}
```

---

## Método 10: Medir Tiempo de Ejecución

```c
// Usar timer para medir cuánto tarda una función

void measure_time_init(void) {
    // Timer1 en modo normal, prescaler /1
    TCCR1B = (1 << CS10);
}

uint16_t measure_start(void) {
    TCNT1 = 0;
    return TCNT1;
}

uint16_t measure_end(void) {
    return TCNT1;
}

// Uso
void test_funcion(void) {
    uint16_t start, end, cycles;
    
    start = measure_start();
    
    funcion_a_medir();
    
    end = measure_end();
    cycles = end - start;
    
    // cycles = número de ciclos de reloj
    // tiempo_us = cycles / (F_CPU / 1000000)
}
```

---

## Método 11: Checklist de Configuración de Timer

### Antes de Usar Timer

- [ ] ¿Qué timer usar? (8-bit vs 16-bit)
- [ ] ¿Qué modo? (Normal, CTC, PWM)
- [ ] ¿Prescaler correcto para la frecuencia?
- [ ] ¿OCR dentro del rango del timer?
- [ ] ¿Pin configurado como salida si usa PWM?
- [ ] ¿Interrupción habilitada si necesario?
- [ ] ¿sei() llamado?
- [ ] ¿ISR implementada?
- [ ] ¿Variables compartidas son volatile?

### Debug de Timer

```c
// Verificar que timer cuenta
void debug_timer(void) {
    printf("TCNT0 = %d\n", TCNT0);
    _delay_ms(100);
    printf("TCNT0 = %d\n", TCNT0);
}
```

---

<!-- IA_CONTEXT
USO: Métodos prácticos para timers e interrupciones
NIVEL: Intermedio (2/3)
HERRAMIENTAS: AVR-GCC, osciloscopio para verificar PWM
-->
