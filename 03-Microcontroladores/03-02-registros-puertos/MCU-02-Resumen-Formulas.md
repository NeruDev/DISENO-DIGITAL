<!--
::METADATA::
type: reference
topic_id: mcu-02-registros-puertos
file_id: resumen-gpio
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, microcontrolador, GPIO, puertos]
search_keywords: "resumen, GPIO, puertos, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-02-Intro.md)

---

# 📋 Cheatsheet: Registros y Puertos GPIO

## Registros AVR

| Registro | Función |
|----------|---------|
| DDRx | Dirección (0=in, 1=out) |
| PORTx | Salida / Pull-up |
| PINx | Lectura entrada |

---

## Registros STM32

| Registro | Función |
|----------|---------|
| MODER | Modo (in/out/alt/analog) |
| ODR | Salida |
| IDR | Entrada |
| BSRR | Set/Reset atómico |

---

## Operaciones de Bits

```c
// SET bit
REG |= (1 << BIT);

// CLEAR bit
REG &= ~(1 << BIT);

// TOGGLE bit
REG ^= (1 << BIT);

// READ bit
val = (REG >> BIT) & 1;
```

---

## Configuración Entrada/Salida (AVR)

```c
// SALIDA
DDRB |= (1 << PB0);

// ENTRADA
DDRB &= ~(1 << PB0);

// ENTRADA con PULL-UP
DDRB &= ~(1 << PB0);
PORTB |= (1 << PB0);
```

---

## Escribir Salida

```c
// HIGH
PORTB |= (1 << PB0);

// LOW
PORTB &= ~(1 << PB0);

// TOGGLE (atómico AVR)
PINB = (1 << PB0);
```

---

## Leer Entrada

```c
// Leer bit
if (PINB & (1 << PB0)) {
    // PB0 es HIGH
}

// Guardar estado
uint8_t estado = (PINB >> PB0) & 1;
```

---

## Pull-up/Pull-down

```
Con pull-up interno:
- Botón abierto → lee HIGH
- Botón cerrado (a GND) → lee LOW
```

---

## Macros Útiles

```c
#define BIT_SET(r,b)   ((r)|=(1<<(b)))
#define BIT_CLR(r,b)   ((r)&=~(1<<(b)))
#define BIT_TGL(r,b)   ((r)^=(1<<(b)))
#define BIT_RD(r,b)    (((r)>>(b))&1)
```

---

## Display 7 Segmentos

```
    a
   ───
f │   │ b
   ─g─
e │   │ c
   ───
    d    .dp

Dígitos (gfedcba):
0=3F, 1=06, 2=5B, 3=4F, 4=66
5=6D, 6=7D, 7=07, 8=7F, 9=6F
```

---

## Debounce

```c
// Simple (blocking)
if (boton_presionado()) {
    _delay_ms(50);
    if (boton_presionado()) {
        // Válido
    }
}
```

---

## Límites Eléctricos

| Parámetro | Típico |
|-----------|--------|
| VOH | VCC - 0.7V |
| VOL | 0.7V |
| IOH/IOL | 20 mA |
| I puerto | 100-200 mA |

---

## Tipos de Salida

| Push-Pull | Open-Drain |
|-----------|------------|
| Puede HIGH/LOW | Solo LOW |
| Más común | Para buses |

---

## Checklist

- [ ] DDR configurado
- [ ] Pull-up si entrada
- [ ] Corriente suficiente
- [ ] Debounce para botones

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante programación GPIO
-->
