<!--
::METADATA::
type: detailed_solution
topic_id: mcu-03-timers-interrupciones
problem_id: 2.2
file_id: solucion-problema-2-2
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, MCU, timer, CTC, OCR, cálculo]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 2.3 →](./MCU-03-Sol-Problema-2.3.md)

---

# Solución Detallada: Problema 2.2

## Enunciado
Calcula el valor de OCR necesario para generar una interrupción cada 10 ms con:
- F_CPU = 16 MHz
- Timer de 16 bits
- Prescaler = 64

---

## Paso 1: Fórmula General

Para modo CTC (Clear Timer on Compare Match):

$$OCR = \frac{T_{deseado} \times f_{CPU}}{Prescaler} - 1$$

---

## Paso 2: Sustitución de Valores

Datos:
- $T_{deseado} = 10\,ms = 0.01\,s$
- $f_{CPU} = 16\,MHz = 16,000,000\,Hz$
- $Prescaler = 64$

$$OCR = \frac{0.01 \times 16,000,000}{64} - 1$$

$$OCR = \frac{160,000}{64} - 1$$

$$OCR = 2,500 - 1 = 2,499$$

---

## Paso 3: Verificación

### ¿Cabe en 16 bits?

- Valor máximo de Timer1: $2^{16} - 1 = 65,535$
- OCR calculado: $2,499$
- ✅ **Sí cabe** ($2,499 < 65,535$)

### Comprobación Inversa

$$T_{real} = \frac{(OCR + 1) \times Prescaler}{f_{CPU}}$$

$$T_{real} = \frac{(2499 + 1) \times 64}{16,000,000}$$

$$T_{real} = \frac{2500 \times 64}{16,000,000} = \frac{160,000}{16,000,000} = 0.01\,s = 10\,ms$$

✅ **Exacto**

---

## Paso 4: Código de Implementación

```c
#include <avr/io.h>
#include <avr/interrupt.h>

// Variables globales
volatile uint8_t flag_10ms = 0;
volatile uint16_t contador_ms = 0;

void timer1_init(void) {
    // Modo CTC: WGM12 = 1, resto = 0
    TCCR1A = 0;
    TCCR1B = (1 << WGM12);  // CTC mode
    
    // Prescaler /64: CS11 = 1, CS10 = 1
    TCCR1B |= (1 << CS11) | (1 << CS10);
    
    // Valor de comparación para 10ms
    OCR1A = 2499;  // ← Valor calculado
    
    // Habilitar interrupción por comparación
    TIMSK1 |= (1 << OCIE1A);
    
    // Habilitar interrupciones globales
    sei();
}

// ISR cada 10ms
ISR(TIMER1_COMPA_vect) {
    flag_10ms = 1;
    contador_ms += 10;
}

int main(void) {
    timer1_init();
    
    while (1) {
        if (flag_10ms) {
            flag_10ms = 0;
            // Hacer algo cada 10ms
        }
    }
}
```

---

## Paso 5: Alternativas de Prescaler

¿Qué pasa si elegimos otro prescaler?

| Prescaler | OCR | ¿Válido? | Error |
|:---------:|:---:|:--------:|-------|
| 1 | 159,999 | ❌ > 65535 | - |
| 8 | 19,999 | ✅ | 0% |
| 64 | **2,499** | ✅ | 0% |
| 256 | 624 | ✅ | 0.16% |
| 1024 | 155.25 | ⚠️ | ~0.16% |

> 💡 **Nota:** Prescaler /8 también funciona perfectamente. /64 deja más "espacio" para ajustes.

---

## Diagrama de Operación

```
      0    500   1000  1500  2000  2499   0    500  ...
      │     │     │     │     │     │     │     │
TCNT1 ┼─────┼─────┼─────┼─────┼─────┤     ├─────┼───
      │                             │     │
      │         10 ms               │reset│
      │◄────────────────────────────►│     │
      │                             │     │
IRQ   ─────────────────────────────┬─────┬─────────
                                   │     │
                               Interrupción cada 10ms
```

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| CTC | Clear Timer on Compare - resetea al llegar a OCR |
| OCR1A | Output Compare Register - valor de comparación |
| OCIE1A | Output Compare Interrupt Enable - habilita IRQ |
| WGM12 | Waveform Generation Mode bit para CTC |
| CS1[2:0] | Clock Select - configura prescaler |

---

## Fórmulas Útiles

| Para encontrar | Fórmula |
|----------------|---------|
| OCR | $OCR = \frac{T \times f_{CPU}}{Prescaler} - 1$ |
| Tiempo | $T = \frac{(OCR + 1) \times Prescaler}{f_{CPU}}$ |
| Frecuencia | $f = \frac{f_{CPU}}{Prescaler \times (OCR + 1)}$ |
| Prescaler mínimo | $Prescaler \geq \frac{T \times f_{CPU}}{2^{bits}}$ |

---

## Errores Comunes

| Error | Consecuencia | Solución |
|-------|--------------|----------|
| Olvidar -1 | Timing incorrecto | OCR = cuenta - 1 |
| OCR > MAX | Timer no funciona | Aumentar prescaler |
| Sin `sei()` | ISR nunca ejecuta | Habilitar interrupciones |
| Sin `volatile` | Variable no actualiza | Agregar `volatile` |

---

> 💡 **Tip:** Siempre verifica que OCR calculado quepa en el timer (8 o 16 bits) y haz la comprobación inversa para confirmar el timing exacto.
