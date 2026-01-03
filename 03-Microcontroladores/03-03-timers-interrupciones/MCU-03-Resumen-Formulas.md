<!--
::METADATA::
type: reference
topic_id: mcu-03-timers-interrupciones
file_id: resumen-timers
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, microcontrolador, timer, interrupción, PWM]
search_keywords: "resumen, timer, interrupción, PWM, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-03-Intro.md)

---

# 📋 Cheatsheet: Timers e Interrupciones

## Modos de Timer

| Modo | Descripción | TOP |
|------|-------------|-----|
| Normal | 0→MAX→0 | MAX |
| CTC | 0→OCR→0 | OCRnA |
| Fast PWM | 0→TOP→0 | MAX/ICR |
| Phase PWM | 0→TOP→0→... | MAX/ICR |

---

## Fórmulas

### Frecuencia de Interrupción (CTC)
$$f_{int} = \frac{f_{CPU}}{Prescaler \times (OCR + 1)}$$

### Cálculo de OCR
$$OCR = \frac{f_{CPU}}{Prescaler \times f_{deseada}} - 1$$

### Frecuencia PWM Fast
$$f_{PWM} = \frac{f_{CPU}}{Prescaler \times 256}$$

### Duty Cycle
$$DC = \frac{OCR + 1}{256} \times 100\%$$

---

## Prescalers AVR

| CS02:01:00 | Prescaler |
|------------|-----------|
| 001 | 1 |
| 010 | 8 |
| 011 | 64 |
| 100 | 256 |
| 101 | 1024 |

---

## Timer0 Config (AVR)

```c
// CTC Mode
TCCR0A = (1 << WGM01);
TCCR0B = (1 << CS01);  // /8
OCR0A = valor;
TIMSK0 = (1 << OCIE0A);
```

---

## PWM Config

```c
// Fast PWM, non-inverting
TCCR0A = (1 << COM0A1) | 
         (1 << WGM01) | 
         (1 << WGM00);
TCCR0B = (1 << CS01);
OCR0A = duty;  // 0-255
```

---

## ISR Template

```c
volatile uint8_t flag = 0;

ISR(TIMER0_COMPA_vect) {
    flag = 1;  // Solo marcar
}

int main(void) {
    // config...
    sei();
    
    while(1) {
        if (flag) {
            flag = 0;
            // trabajo aquí
        }
    }
}
```

---

## Vectores de Interrupción

```c
ISR(TIMER0_OVF_vect)   // Overflow
ISR(TIMER0_COMPA_vect) // Compare A
ISR(TIMER1_OVF_vect)
ISR(TIMER1_COMPA_vect)
ISR(TIMER1_CAPT_vect)  // Capture
```

---

## Frecuencias Comunes (16MHz)

| Objetivo | Prescaler | OCR |
|----------|-----------|-----|
| 1 Hz | 256 | 62499 (16-bit) |
| 100 Hz | 64 | 2499 (16-bit) |
| 1 kHz | 64 | 249 (8-bit) |
| PWM 1kHz | 64 | - |

---

## Input Capture

```c
// Captura en flanco
TCCR1B |= (1 << ICES1);  // Rising
// TCCR1B &= ~(1 << ICES1); // Falling

ISR(TIMER1_CAPT_vect) {
    uint16_t capture = ICR1;
}
```

---

## Watchdog

```c
#include <avr/wdt.h>

wdt_enable(WDTO_1S);  // 1 segundo
wdt_reset();          // Alimentar
wdt_disable();        // Desactivar
```

---

## Reglas ISR

1. ⚡ Corta y rápida
2. 🚫 No usar delay
3. ✅ Variables volatile
4. 🚫 No printf/float
5. ✅ Solo marcar flags

---

## Habilitar Interrupciones

```c
sei();  // Enable global
cli();  // Disable global
```

---

## Período Máximo

| Timer | Prescaler | T_max |
|-------|-----------|-------|
| 8-bit | 1024 | 16 ms (16M) |
| 16-bit | 1024 | 4.2 s (16M) |

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante programación de timers
-->
