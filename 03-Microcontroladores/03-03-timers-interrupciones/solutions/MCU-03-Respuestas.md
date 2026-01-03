<!--
::METADATA::
type: solution
topic_id: mcu-03-timers-interrupciones
file_id: respuestas-timers
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, microcontrolador, timer, interrupción]
search_keywords: "respuestas, soluciones, timer, interrupción"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-03-Problemas.md)

---

# Respuestas: Timers e Interrupciones

## Nivel 1: Conceptos Básicos

### Respuesta 1.1

| Timer | Counter |
|-------|---------|
| Cuenta pulsos del reloj interno | Cuenta eventos externos |
| Fuente: F_CPU / prescaler | Fuente: pin externo (T0, T1) |
| Uso: temporización | Uso: contar eventos |

### Respuesta 1.2

El **prescaler** divide la frecuencia del reloj para permitir períodos más largos.

Sin prescaler (16 MHz, 8 bits): máx 256 × 62.5ns = 16 µs
Con prescaler /1024: máx 256 × 64 µs = 16.4 ms

### Respuesta 1.3

Un timer de 8 bits tiene **256 valores** diferentes (0 a 255).

---

## Nivel 2: Cálculos de Timer

### Respuesta 2.1

```
T_tick = Prescaler / F_CPU
T_tick = 64 / 16,000,000
T_tick = 4 µs

Cada incremento del timer = 4 microsegundos
```

### Respuesta 2.2

```
f_int = F_CPU / (Prescaler × (OCR + 1))
100 Hz = 16,000,000 / (64 × (OCR + 1))
OCR + 1 = 16,000,000 / (64 × 100) = 2500
OCR = 2499

Verificar: 2499 < 65535 ✓ (cabe en 16 bits)
```

### Respuesta 2.3

```
T_max = (2^8 × Prescaler) / F_CPU
T_max = (256 × 1024) / 8,000,000
T_max = 262,144 / 8,000,000
T_max = 32.768 ms
```

---

## Nivel 3: Configuración de Timer

### Respuesta 3.1

```c
void timer0_ctc_init(void) {
    // Modo CTC (WGM01 = 1)
    TCCR0A = (1 << WGM01);
    
    // Prescaler /64 (CS01 = 1, CS00 = 1)
    TCCR0B = (1 << CS01) | (1 << CS00);
    
    // Valor de comparación
    OCR0A = 124;
    
    // Habilitar interrupción
    TIMSK0 = (1 << OCIE0A);
}
```

### Respuesta 3.2

Para Fast PWM con TOP = 0xFF:
```
WGM02 = 0
WGM01 = 1
WGM00 = 1

TCCR0A = (1 << WGM01) | (1 << WGM00);
TCCR0B sin WGM02
```

### Respuesta 3.3

```c
void timer1_overflow_init(void) {
    // Modo Normal (WGM = 0000)
    TCCR1A = 0;
    
    // Prescaler /256
    TCCR1B = (1 << CS12);
    
    // Habilitar interrupción overflow
    TIMSK1 = (1 << TOIE1);
    
    sei();
}

ISR(TIMER1_OVF_vect) {
    // Código de interrupción
}
```

---

## Nivel 4: Interrupciones

### Respuesta 4.1

`volatile` es necesario porque:
1. El compilador optimiza variables que "no cambian"
2. Sin volatile, puede cachear el valor en un registro
3. Los cambios en ISR no serían visibles en main()

```c
volatile uint8_t flag;  // Correctamente declarado

ISR(...) {
    flag = 1;  // Este cambio será visible
}

while (!flag);  // Lee el valor real de memoria
```

### Respuesta 4.2

**Problemas:**
1. `_delay_ms()` en ISR bloquea el sistema
2. Otras interrupciones no pueden ejecutarse
3. El sistema parece "colgado"

**Solución:**
```c
volatile uint8_t overflow_flag = 0;

ISR(TIMER0_OVF_vect) {
    overflow_flag = 1;  // Solo marcar flag
}

int main(void) {
    while(1) {
        if (overflow_flag) {
            overflow_flag = 0;
            _delay_ms(100);  // Delay en main, no en ISR
            PORTB ^= 0xFF;
        }
    }
}
```

### Respuesta 4.3

```c
volatile uint16_t overflow_count = 0;
volatile uint8_t timer_flag = 0;

ISR(TIMER0_OVF_vect) {
    overflow_count++;
    if (overflow_count >= 1000) {
        overflow_count = 0;
        timer_flag = 1;
    }
}
```

---

## Nivel 5: PWM

### Respuesta 5.1

```
Duty Cycle = (OCR + 1) / 256 × 100%
DC = (127 + 1) / 256 × 100%
DC = 128 / 256 × 100%
DC = 50%
```

### Respuesta 5.2

```c
void pwm_init(void) {
    // Pin OC0A (PD6) como salida
    DDRD |= (1 << PD6);
    
    // Fast PWM, non-inverting
    TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
    
    // Prescaler /64 → f_PWM = 16M / 64 / 256 ≈ 976 Hz
    TCCR0B = (1 << CS01) | (1 << CS00);
    
    OCR0A = 0;  // Duty cycle inicial
}
```

### Respuesta 5.3

Para 50 Hz con Timer1 (16 bits):
```
TOP = F_CPU / (Prescaler × 50) - 1

Con prescaler /8:
TOP = 16M / (8 × 50) - 1 = 39999

Resolución = log2(40000) ≈ 15.3 bits efectivos
```

---

## Nivel 6: Aplicaciones de Timer

### Respuesta 6.1: LED a 2 Hz

```c
#include <avr/io.h>
#include <avr/interrupt.h>

#define LED_PIN PB5

ISR(TIMER1_COMPA_vect) {
    PINB = (1 << LED_PIN);  // Toggle
}

int main(void) {
    DDRB |= (1 << LED_PIN);
    
    // CTC mode, toggle cada 250 ms → 2 Hz
    TCCR1B = (1 << WGM12) | (1 << CS12);  // CTC, /256
    OCR1A = 15624;  // 16M / 256 / 4 - 1 (4 Hz para toggle = 2 Hz)
    TIMSK1 = (1 << OCIE1A);
    
    sei();
    
    while(1);
}
```

### Respuesta 6.2: Función millis()

```c
volatile uint32_t ms_counter = 0;

void millis_init(void) {
    // Timer0 CTC, 1 kHz
    TCCR0A = (1 << WGM01);
    TCCR0B = (1 << CS01) | (1 << CS00);  // /64
    OCR0A = 249;  // (16M / 64 / 1000) - 1
    TIMSK0 = (1 << OCIE0A);
    sei();
}

ISR(TIMER0_COMPA_vect) {
    ms_counter++;
}

uint32_t millis(void) {
    uint32_t m;
    cli();
    m = ms_counter;
    sei();
    return m;
}
```

### Respuesta 6.3: Generador 440 Hz

```c
// Toggle en OC1A (PB1) a 440 Hz
void tone_440_init(void) {
    DDRB |= (1 << PB1);
    
    // CTC, toggle OC1A
    TCCR1A = (1 << COM1A0);
    TCCR1B = (1 << WGM12) | (1 << CS11);  // CTC, /8
    
    // f = F_CPU / (2 × Prescaler × (OCR + 1))
    // 440 = 16M / (2 × 8 × (OCR + 1))
    // OCR = 2272
    OCR1A = 2272;
}
```

---

## Nivel 7: PWM Aplicado

### Respuesta 7.3: Control de Servo

```c
void servo_init(void) {
    DDRB |= (1 << PB1);  // OC1A
    
    // Fast PWM, ICR1 como TOP
    TCCR1A = (1 << COM1A1) | (1 << WGM11);
    TCCR1B = (1 << WGM13) | (1 << WGM12) | (1 << CS11);  // /8
    
    // 20 ms período
    ICR1 = 39999;  // (16M / 8 / 50) - 1
}

void servo_angle(uint8_t angle) {
    // 1 ms = 2000 ticks, 2 ms = 4000 ticks
    // 0° = 2000, 180° = 4000
    uint16_t pulse = 2000 + ((uint32_t)angle * 2000 / 180);
    OCR1A = pulse;
}
```

---

## Nivel 9: Watchdog

### Respuesta 9.2: WDT 2 segundos

```c
#include <avr/wdt.h>

void wdt_init(void) {
    wdt_enable(WDTO_2S);  // Timeout de 2 segundos
}

int main(void) {
    wdt_init();
    
    while(1) {
        // Si esto no se ejecuta en 2s, MCU resetea
        wdt_reset();
        
        hacer_tareas();
    }
}
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de timers e interrupciones
NOTA: Pueden existir soluciones alternativas válidas
-->
