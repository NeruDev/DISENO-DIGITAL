<!--
::METADATA::
type: reference
topic_id: mcu-01-arquitectura
file_id: resumen-arquitectura-mcu
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, microcontrolador, arquitectura]
search_keywords: "resumen, arquitectura, MCU, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-01-Intro.md)

---

# 📋 Cheatsheet: Arquitectura de Microcontroladores

## MCU vs Microprocesador

| MCU | µP |
|-----|-----|
| Todo en un chip | Solo CPU |
| Memoria integrada | Memoria externa |
| Bajo costo/consumo | Alto rendimiento |

---

## Arquitecturas

| Von Neumann | Harvard |
|-------------|---------|
| Bus único | Buses separados |
| Memoria compartida | Flash + RAM separados |
| Cuello de botella | Mayor rendimiento |

---

## Componentes del MCU

```
┌─────────────────────────────┐
│           MCU               │
│  ┌─────┐ ┌─────┐ ┌───────┐ │
│  │ CPU │ │Flash│ │  RAM  │ │
│  └──┬──┘ └─────┘ └───────┘ │
│     │                       │
│  ┌──┴──────────────────┐   │
│  │    Periféricos      │   │
│  │ GPIO Timer UART ADC │   │
│  └─────────────────────┘   │
└─────────────────────────────┘
```

---

## Registros de CPU

| Registro | Función |
|----------|---------|
| PC | Dirección siguiente instrucción |
| SP | Puntero de pila |
| ACC/W | Acumulador |
| STATUS | Flags (Z, C, N, V) |

---

## Flags del Registro de Estado

| Flag | Significado |
|------|-------------|
| Z | Resultado = 0 |
| C | Carry/Borrow |
| N | Negativo |
| V | Overflow |

---

## Tipos de Memoria

| Tipo | Volátil | Uso |
|------|---------|-----|
| Flash | No | Programa |
| SRAM | Sí | Variables |
| EEPROM | No | Config |

---

## Fórmulas de Reloj

```
Período = 1 / Frecuencia

T_instrucción = Ciclos × T_clk

F_periférico = F_CPU / Prescaler
```

---

## Fuentes de Reloj

| Fuente | Precisión |
|--------|-----------|
| RC interno | ±1-10% |
| Cristal | ±20 ppm |
| Resonador | ±0.5% |

---

## Cálculo de Consumo

```
I_promedio = Σ(I_modo × %tiempo)

Duración = Capacidad / I_promedio
```

---

## Modos de Bajo Consumo

| Modo | CPU | Periféricos | Despertar |
|------|-----|-------------|-----------|
| Run | ON | ON | - |
| Idle | OFF | ON | INT |
| Sleep | OFF | Algunos | INT |
| Power-down | OFF | OFF | Reset/WDT |

---

## Periféricos Comunes

| Periférico | Función |
|------------|---------|
| GPIO | I/O digital |
| Timer | Temporización |
| UART | Serial asíncrono |
| SPI | Serial síncrono (4 hilos) |
| I2C | Serial síncrono (2 hilos) |
| ADC | Analog → Digital |
| PWM | Modulación |
| WDT | Watchdog |

---

## Espacio de Direcciones

```
Direcciones = 2^n bits

8 bits  → 256 bytes
16 bits → 64 KB
32 bits → 4 GB
```

---

## Familias Populares

| Familia | Bits | Fabricante |
|---------|------|------------|
| PIC | 8/16/32 | Microchip |
| AVR | 8 | Microchip |
| STM32 | 32 | ST |
| ESP32 | 32 | Espressif |
| MSP430 | 16 | TI |

---

## Circuito Mínimo

```
VCC ─┬─ MCU VCC
     │
    100nF
     │
GND ─┴─ MCU GND

RESET ─ 10kΩ ─ VCC
```

---

## Checklist de Selección

- [ ] GPIO suficientes
- [ ] Periféricos necesarios
- [ ] Memoria adecuada (margen 20%)
- [ ] Consumo aceptable
- [ ] Herramientas disponibles
- [ ] Costo apropiado

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño con MCU
-->
