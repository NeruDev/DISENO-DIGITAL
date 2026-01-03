<!--
::METADATA::
type: theory
topic_id: mcu-03-timers-interrupciones
file_id: teoria-timers-int
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, timer, contador, interrupción, PWM]
search_keywords: "timer, contador, interrupción, PWM, ISR"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-03-Intro.md) | [Métodos →](../methods/MCU-03-Metodos-Timers.md)

---

# Timers e Interrupciones

## 1. Introducción a Timers

### 1.1 ¿Qué es un Timer?

Un **Timer/Counter** es un periférico que:
- Cuenta pulsos de reloj (Timer)
- Cuenta eventos externos (Counter)
- Opera independiente de la CPU

### 1.2 Estructura Básica

```
                    ┌───────────────────────────┐
    F_CPU ─────────▶│       Prescaler           │
                    │  (/1, /8, /64, /256, /1024)│
                    └───────────┬───────────────┘
                                │
                                ▼
                    ┌───────────────────────────┐
  Evento ext. ────▶│      Registro TCNTn       │
  (modo counter)   │    (8 o 16 bits)          │
                    └───────────┬───────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        ┌──────────┐      ┌──────────┐      ┌──────────┐
        │  OCRnA   │      │  OCRnB   │      │  ICRn    │
        │(Compare) │      │(Compare) │      │(Capture) │
        └────┬─────┘      └────┬─────┘      └────┬─────┘
             │                 │                 │
             ▼                 ▼                 ▼
        Interrupción      Interrupción      Interrupción
          o PWM             o PWM            (Capture)
```

---

## 2. Modos de Operación

### 2.1 Modo Normal

El contador cuenta desde 0 hasta MAX (255 o 65535), luego hace overflow y vuelve a 0.

```
      MAX ─────────────────────────────────────
         │                    │
  Valor  │                    │
   TCNT  │   /│   /│   /│   /│
         │  / │  / │  / │  /
       0 ──┴───┴───┴───┴───────────────────────
                                    Tiempo
                  ▲
              Overflow
           (Interrupción)
```

### 2.2 Modo CTC (Clear Timer on Compare)

El contador se reinicia cuando TCNTn = OCRnA.

```
   OCRnA ─────┬─────┬─────┬─────┬──────────────
         │   /│   /│   /│   /│
  Valor  │  / │  / │  / │  / │
   TCNT  │ /  │ /  │ /  │ /  │
       0 ──┴───┴───┴───┴───────────────────────
                                    Tiempo
              ▲     ▲     ▲
           Compare Match
           (Interrupción)
```

**Frecuencia de interrupción:**
$$f_{int} = \frac{f_{CPU}}{Prescaler \times (OCRnA + 1)}$$

### 2.3 Modo PWM Rápido (Fast PWM)

```
   TOP  ─────────────────────────────────────
        │         /│         /│         /
  TCNT  │       /  │       /  │       /
        │     /    │     /    │     /
   OCR ─│───/──────│───/──────│───/──────────
        │ /        │ /        │ /
      0 ──┴─────────┴─────────┴───────────────
                                    Tiempo
   PWM  ████░░░░░░░████░░░░░░░████░░░░░░░
        │←─ DC ─→│
```

**Duty Cycle:**
$$DC = \frac{OCRnx + 1}{TOP + 1} \times 100\%$$

### 2.4 Modo PWM con Fase Correcta

El contador sube y baja, resultando en PWM simétrico.

```
   TOP  ─────┬─────┬─────┬─────┬──────────────
        │   /\    /\    /\    /\
  TCNT  │  /  \  /  \  /  \  /  \
        │ /    \/    \/    \/    \
      0 ──┴──────────────────────────────────
                                    Tiempo
```

---

## 3. Prescaler

### 3.1 ¿Qué es el Prescaler?

Divide la frecuencia de entrada para permitir períodos más largos.

| Prescaler | Freq. Timer (16MHz CPU) | Período por tick |
|-----------|------------------------|------------------|
| 1 | 16 MHz | 62.5 ns |
| 8 | 2 MHz | 500 ns |
| 64 | 250 kHz | 4 µs |
| 256 | 62.5 kHz | 16 µs |
| 1024 | 15.625 kHz | 64 µs |

### 3.2 Cálculo del Período Máximo

Para Timer de 8 bits (MAX = 255):
$$T_{max} = \frac{256 \times Prescaler}{f_{CPU}}$$

Para Timer de 16 bits (MAX = 65535):
$$T_{max} = \frac{65536 \times Prescaler}{f_{CPU}}$$

---

## 4. Interrupciones

### 4.1 ¿Qué es una Interrupción?

Evento que detiene la ejecución normal para atender una tarea urgente.

```
   main()    │        │         │
─────────────│────────│─────────│───────────────
             │        │         │
             │ IRQ    │         │ Retorna
             ▼        │         │
        ┌────────┐    │         │
   ISR  │ código │────┘         │
        │  ISR   │──────────────┘
        └────────┘
```

### 4.2 Tipos de Interrupciones de Timer

| Interrupción | Cuándo ocurre |
|--------------|---------------|
| Overflow (TOV) | TCNT pasa de MAX a 0 |
| Compare Match A (COMPA) | TCNT = OCRnA |
| Compare Match B (COMPB) | TCNT = OCRnB |
| Input Capture (CAPT) | Evento en pin ICP |

### 4.3 Vector de Interrupciones (AVR)

```c
// Vectores comunes ATmega328P
ISR(TIMER0_OVF_vect)   { }  // Timer0 Overflow
ISR(TIMER0_COMPA_vect) { }  // Timer0 Compare A
ISR(TIMER1_OVF_vect)   { }  // Timer1 Overflow
ISR(TIMER1_COMPA_vect) { }  // Timer1 Compare A
ISR(TIMER1_CAPT_vect)  { }  // Timer1 Input Capture
ISR(TIMER2_OVF_vect)   { }  // Timer2 Overflow
```

### 4.4 Habilitación de Interrupciones

```c
// 1. Configurar timer
TCCR0A = ...;
TCCR0B = ...;

// 2. Habilitar interrupción específica
TIMSK0 |= (1 << TOIE0);   // Overflow interrupt enable
// o
TIMSK0 |= (1 << OCIE0A);  // Compare A interrupt enable

// 3. Habilitar interrupciones globales
sei();  // Set Enable Interrupts
```

---

## 5. Registros de Timer (AVR ATmega328P)

### 5.1 Timer0 (8 bits)

| Registro | Función |
|----------|---------|
| TCCR0A | Control (modo, salida) |
| TCCR0B | Control (prescaler) |
| TCNT0 | Valor del contador |
| OCR0A | Valor de comparación A |
| OCR0B | Valor de comparación B |
| TIMSK0 | Máscara de interrupciones |
| TIFR0 | Flags de interrupción |

### 5.2 Bits de TCCR0A

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│COM0A│COM0A│COM0B│COM0B│  -  │  -  │WGM01│WGM00│
│  1  │  0  │  1  │  0  │     │     │     │     │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
  Salida OC0A   Salida OC0B         Modo
```

### 5.3 Modos de Generación de Forma de Onda (WGM)

| WGM02 | WGM01 | WGM00 | Modo | TOP |
|-------|-------|-------|------|-----|
| 0 | 0 | 0 | Normal | 0xFF |
| 0 | 1 | 0 | CTC | OCR0A |
| 0 | 1 | 1 | Fast PWM | 0xFF |
| 0 | 0 | 1 | PWM Phase Correct | 0xFF |

---

## 6. Configuración de PWM

### 6.1 PWM Hardware (AVR)

```c
// Fast PWM en OC0A (PD6) con 8 bits
void pwm_init(void) {
    // Pin como salida
    DDRD |= (1 << PD6);
    
    // Fast PWM, non-inverting
    TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
    
    // Prescaler /64 → ~1 kHz PWM @ 16MHz
    TCCR0B = (1 << CS01) | (1 << CS00);
    
    // Duty cycle inicial 0%
    OCR0A = 0;
}

void pwm_set_duty(uint8_t duty) {
    OCR0A = duty;  // 0-255 → 0-100%
}
```

### 6.2 Frecuencia de PWM

**Fast PWM:**
$$f_{PWM} = \frac{f_{CPU}}{Prescaler \times 256}$$

**Phase Correct PWM:**
$$f_{PWM} = \frac{f_{CPU}}{Prescaler \times 510}$$

---

## 7. Input Capture

### 7.1 ¿Qué es Input Capture?

Captura el valor de TCNT cuando ocurre un evento en el pin ICP.

```
Señal ────────┐     ┌─────┐     ┌─────────────
              │     │     │     │
              └─────┘     └─────┘

TCNT  ──────────────────────────────────────
              ▲           ▲
           t1=1234     t2=3456

Período = t2 - t1 = 2222 ticks
```

### 7.2 Medición de Frecuencia

```c
volatile uint16_t periodo = 0;
volatile uint8_t captura_lista = 0;

ISR(TIMER1_CAPT_vect) {
    static uint16_t ultima_captura = 0;
    uint16_t captura_actual = ICR1;
    
    periodo = captura_actual - ultima_captura;
    ultima_captura = captura_actual;
    captura_lista = 1;
}

float calcular_frecuencia(void) {
    if (periodo > 0) {
        return (float)F_CPU / (float)periodo;
    }
    return 0;
}
```

---

## 8. Buenas Prácticas ISR

### 8.1 Reglas para ISR

1. **Mantenerla corta** - Mínimo código posible
2. **No usar delays** - Bloquean el sistema
3. **Variables `volatile`** - Para compartir con main()
4. **Evitar operaciones complejas** - No printf, no floating point
5. **Proteger variables compartidas** - Sección crítica si necesario

### 8.2 Ejemplo Correcto

```c
volatile uint8_t timer_flag = 0;
volatile uint16_t timer_count = 0;

ISR(TIMER0_OVF_vect) {
    timer_count++;
    if (timer_count >= 1000) {
        timer_flag = 1;
        timer_count = 0;
    }
}

int main(void) {
    // Configuración...
    
    while (1) {
        if (timer_flag) {
            timer_flag = 0;
            // Hacer trabajo pesado aquí, no en ISR
            hacer_algo_cada_segundo();
        }
    }
}
```

---

## 9. Watchdog Timer

### 9.1 ¿Qué es el WDT?

Timer especial que resetea el MCU si no es "alimentado" periódicamente.

```
                    ┌────────────────────┐
    RC 128kHz ─────▶│   Watchdog Timer   │
                    │                    │──▶ Reset MCU
                    └────────────────────┘
                              ▲
                              │
                        WDR (reset)
                        desde software
```

### 9.2 Uso del WDT

```c
#include <avr/wdt.h>

void wdt_init(void) {
    wdt_enable(WDTO_1S);  // Reset si no hay wdt_reset() en 1 segundo
}

int main(void) {
    wdt_init();
    
    while (1) {
        wdt_reset();  // "Alimentar" el watchdog
        
        // Código de aplicación
        hacer_tareas();
    }
}
```

---

## 10. Ejemplo Completo: Temporizador de 1 Segundo

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t segundo_flag = 0;

void timer1_init(void) {
    // Modo CTC, TOP = OCR1A
    TCCR1B = (1 << WGM12);
    
    // Prescaler /256
    TCCR1B |= (1 << CS12);
    
    // Para 1 segundo con 16 MHz:
    // OCR1A = (16000000 / 256) - 1 = 62499
    OCR1A = 62499;
    
    // Habilitar interrupción Compare A
    TIMSK1 = (1 << OCIE1A);
    
    // Habilitar interrupciones globales
    sei();
}

ISR(TIMER1_COMPA_vect) {
    segundo_flag = 1;
}

int main(void) {
    DDRB |= (1 << PB5);  // LED
    
    timer1_init();
    
    while (1) {
        if (segundo_flag) {
            segundo_flag = 0;
            PINB = (1 << PB5);  // Toggle LED
        }
    }
}
```

---

## Referencias

- ATmega328P Datasheet - Timers
- AVR130: Setup and Use of AVR Timers
- AVR131: Using the AVR's High-Speed PWM

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 03-01 y 03-02
CONEXIONES: Base para PWM, medición de tiempo, scheduling
ERRORES_COMUNES: ISR muy largas, olvidar sei(), prescaler incorrecto
-->
