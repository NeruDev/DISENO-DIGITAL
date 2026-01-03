<!--
::METADATA::
type: detailed_solution
topic_id: mcu-02-registros-puertos
problem_id: 3.1
file_id: solucion-problema-3-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, MCU, GPIO, bitwise, toggle]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 3.2 →](./MCU-02-Sol-Problema-3.2.md)

---

# Solución Detallada: Problema 3.1

## Enunciado
Escribe código AVR para:
- a) Poner PB3 en HIGH
- b) Poner PB3 en LOW
- c) Invertir (toggle) PB3

Sin modificar los otros bits de PORTB.

---

## Prerequisitos
- PB3 debe estar configurado como salida: `DDRB |= (1 << PB3);`

---

## Parte A: Poner PB3 en HIGH (Set)

### Código

```c
PORTB |= (1 << PB3);
```

### Análisis Paso a Paso

```
Paso 1: (1 << PB3)
   1 << 3 = 0b00001000

Paso 2: PORTB |= 0b00001000

   Supongamos PORTB = 0b10100101
   
   PORTB:     1 0 1 0 0 1 0 1
   Máscara:   0 0 0 0 1 0 0 0   OR
   ─────────────────────────────
   Resultado: 1 0 1 0 1 1 0 1
                    ↑
                 PB3 = 1 (los demás NO cambian)
```

### Diagrama de Operación OR

```
  Bit original │ Máscara │ Resultado
  ─────────────┼─────────┼──────────
       0       │    0    │     0     (sin cambio)
       1       │    0    │     1     (sin cambio)
       X       │    1    │     1     (SIEMPRE 1)
```

---

## Parte B: Poner PB3 en LOW (Clear)

### Código

```c
PORTB &= ~(1 << PB3);
```

### Análisis Paso a Paso

```
Paso 1: (1 << PB3)
   1 << 3 = 0b00001000

Paso 2: ~(1 << PB3)
   ~0b00001000 = 0b11110111

Paso 3: PORTB &= 0b11110111

   Supongamos PORTB = 0b10101101
   
   PORTB:     1 0 1 0 1 1 0 1
   Máscara:   1 1 1 1 0 1 1 1   AND
   ─────────────────────────────
   Resultado: 1 0 1 0 0 1 0 1
                    ↑
                 PB3 = 0 (los demás NO cambian)
```

### Diagrama de Operación AND

```
  Bit original │ Máscara │ Resultado
  ─────────────┼─────────┼──────────
       X       │    1    │     X     (sin cambio)
       X       │    0    │     0     (SIEMPRE 0)
```

---

## Parte C: Invertir PB3 (Toggle)

### Código

```c
PORTB ^= (1 << PB3);
```

### Análisis Paso a Paso

```
Paso 1: (1 << PB3)
   1 << 3 = 0b00001000

Paso 2: PORTB ^= 0b00001000

   Caso 1: PB3 era 0
   PORTB:     1 0 1 0 0 1 0 1
   Máscara:   0 0 0 0 1 0 0 0   XOR
   ─────────────────────────────
   Resultado: 1 0 1 0 1 1 0 1   (PB3: 0→1)

   Caso 2: PB3 era 1
   PORTB:     1 0 1 0 1 1 0 1
   Máscara:   0 0 0 0 1 0 0 0   XOR
   ─────────────────────────────
   Resultado: 1 0 1 0 0 1 0 1   (PB3: 1→0)
```

### Diagrama de Operación XOR

```
  Bit original │ Máscara │ Resultado
  ─────────────┼─────────┼──────────
       X       │    0    │     X     (sin cambio)
       0       │    1    │     1     (invertido)
       1       │    1    │     0     (invertido)
```

---

## Alternativa: Toggle Atómico (AVR moderno)

En AVR con `PINx` escribible (ATmega328P y posteriores):

```c
PINB = (1 << PB3);  // Toggle atómico
```

### Ventaja
- **Atómico:** Se ejecuta en 1 ciclo de reloj
- **Seguro en ISR:** No hay problema de read-modify-write

---

## Resumen Visual

```
┌─────────────────────────────────────────────────────────────┐
│                  OPERACIONES BITWISE                         │
│                                                              │
│   SET (poner en 1):                                         │
│   PORTB |= (1 << n);   // OR con máscara de 1               │
│                                                              │
│   CLEAR (poner en 0):                                       │
│   PORTB &= ~(1 << n);  // AND con máscara de 0              │
│                                                              │
│   TOGGLE (invertir):                                        │
│   PORTB ^= (1 << n);   // XOR con máscara de 1              │
│                                                              │
│   TEST (verificar):                                         │
│   if (PINB & (1 << n)) // AND para aislar bit               │
└─────────────────────────────────────────────────────────────┘
```

---

## Código Completo de Ejemplo

```c
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    // Configurar PB3 como salida
    DDRB |= (1 << PB3);
    
    while (1) {
        // a) Encender LED (HIGH)
        PORTB |= (1 << PB3);
        _delay_ms(500);
        
        // b) Apagar LED (LOW)
        PORTB &= ~(1 << PB3);
        _delay_ms(500);
        
        // c) Toggle 4 veces
        for (int i = 0; i < 4; i++) {
            PORTB ^= (1 << PB3);
            _delay_ms(250);
        }
    }
}
```

---

## Conceptos Clave

| Operador | Nombre | Uso en GPIO |
|:--------:|--------|-------------|
| `\|` | OR | Set bits (poner en 1) |
| `&` | AND | Clear bits (poner en 0) |
| `^` | XOR | Toggle bits (invertir) |
| `~` | NOT | Invertir máscara |
| `<<` | Shift Left | Crear máscara |

---

## Errores Comunes

| Error | Problema | Solución |
|-------|----------|----------|
| `PORTB = (1<<PB3)` | Borra todos los demás bits | Usar `\|=` |
| `PORTB &= (1<<PB3)` | Solo deja PB3, borra resto | Usar `&= ~(...)` |
| Olvidar `DDRB` | Pin no responde | Configurar dirección primero |
| `~(1<<PB3)` en ISR | No atómico | Usar `PINB =` para toggle |

---

> 💡 **Tip:** Memoriza el patrón: OR para encender, AND NOT para apagar, XOR para toggle.
