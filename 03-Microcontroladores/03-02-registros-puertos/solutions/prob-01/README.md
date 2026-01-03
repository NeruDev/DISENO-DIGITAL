<!--
::METADATA::
type: solution_index
topic_id: mcu-02-registros-puertos
file_id: solucion-index-gpio
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, GPIO, puertos, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-02-Respuestas.md) | [Problemas →](../../problems/MCU-02-Problemas.md)

---

# Soluciones Detalladas: Registros y Puertos GPIO (MCU-02)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-02-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Paso a paso con código |
| **3** | Secciones "Conceptos Clave" | Teoría de registros |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos Básicos ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | Significado de GPIO | En respuestas |
| 1.2 | Registros DDRx, PORTx, PINx | [MCU-02-Sol-Problema-1.2.md](./MCU-02-Sol-Problema-1.2.md) |
| 1.3 | Pull-up en entradas | En respuestas |

### Nivel 2: Configuración de Dirección ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 2.1 | Config mixta I/O | [MCU-02-Sol-Problema-2.1.md](./MCU-02-Sol-Problema-2.1.md) |
| 2.2 | Cálculo de DDRB | En respuestas |
| 2.3 | DDR=0, PORT=1 | En respuestas |

### Nivel 3: Escritura de Salidas ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Set/Clear/Toggle bit | [MCU-02-Sol-Problema-3.1.md](./MCU-02-Sol-Problema-3.1.md) |
| 3.2 | Problema en ISR | En respuestas |
| 3.3 | Toggle atómico | En respuestas |

### Nivel 4: Lectura de Entradas ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 4.1 | Leer pin individual | En respuestas |
| 4.2 | Botón con pull-up | En respuestas |
| 4.3 | Esperar flanco | En respuestas |

### Nivel 5: Manipulación de Bits ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | Operaciones bitwise | [MCU-02-Sol-Problema-5.1.md](./MCU-02-Sol-Problema-5.1.md) |
| 5.2 | Macro para múltiples bits | En respuestas |
| 5.3 | Extracción de bits | En respuestas |

### Nivel 6-7: Aplicaciones ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 6.1 | LED viajero | En respuestas |
| 6.2 | LED rebote | En respuestas |
| 7.1 | Debounce software | En respuestas |

---

## Referencia Rápida

### Registros GPIO (AVR)

```
┌─────────────────────────────────────────────────────────────┐
│                    PUERTO B (ejemplo)                        │
│                                                              │
│   DDRx  ─► Dirección: 0=entrada, 1=salida                   │
│   PORTx ─► Salida: valor a escribir                         │
│            Entrada: 1=pull-up, 0=Hi-Z                       │
│   PINx  ─► Lectura del estado actual del pin                │
│                                                              │
│   ┌────┬────┬────┬────┬────┬────┬────┬────┐                │
│   │ 7  │ 6  │ 5  │ 4  │ 3  │ 2  │ 1  │ 0  │ ← Bit          │
│   ├────┼────┼────┼────┼────┼────┼────┼────┤                │
│   │PB7 │PB6 │PB5 │PB4 │PB3 │PB2 │PB1 │PB0 │ ← Pin          │
│   └────┴────┴────┴────┴────┴────┴────┴────┘                │
└─────────────────────────────────────────────────────────────┘
```

### Operaciones Bitwise

| Operación | Código C | Resultado |
|-----------|----------|-----------|
| Set bit n | `PORT \|= (1 << n)` | Pone bit n en 1 |
| Clear bit n | `PORT &= ~(1 << n)` | Pone bit n en 0 |
| Toggle bit n | `PORT ^= (1 << n)` | Invierte bit n |
| Test bit n | `if(PIN & (1 << n))` | ¿Bit n es 1? |

### Configuración Típica

| Función | DDRx | PORTx |
|---------|:----:|:-----:|
| Salida LOW | 1 | 0 |
| Salida HIGH | 1 | 1 |
| Entrada Hi-Z | 0 | 0 |
| Entrada Pull-up | 0 | 1 |

### Máscaras Comunes

```c
#define BIT(n)        (1 << (n))
#define SET_BIT(r,n)  ((r) |= BIT(n))
#define CLR_BIT(r,n)  ((r) &= ~BIT(n))
#define TGL_BIT(r,n)  ((r) ^= BIT(n))
#define GET_BIT(r,n)  (((r) >> (n)) & 1)
```

---

## Navegación

| Anterior | Arriba | Siguiente |
|:--------:|:------:|:---------:|
| [Arquitectura](../../../03-01-arquitectura-mcu/solutions/prob-01/) | [Módulo MCU](../../00-Index.md) | [Timers](../../../03-03-timers-interrupciones/solutions/prob-01/) |
