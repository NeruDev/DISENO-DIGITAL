<!--
::METADATA::
type: solution_index
topic_id: mcu-01-arquitectura
file_id: solucion-index-arquitectura
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, arquitectura, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-01-Respuestas.md) | [Problemas →](../../problems/MCU-01-Problemas.md)

---

# Soluciones Detalladas: Arquitectura de MCU (MCU-01)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-01-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Paso a paso detallado |
| **3** | Secciones "Conceptos Clave" | Teoría aplicada |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos Básicos ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | MCU vs Microprocesador | [MCU-01-Sol-Problema-1.1.md](./MCU-01-Sol-Problema-1.1.md) |
| 1.2 | Periféricos integrados | [MCU-01-Sol-Problema-1.2.md](./MCU-01-Sol-Problema-1.2.md) |
| 1.3 | Arquitectura Harvard | [MCU-01-Sol-Problema-1.3.md](./MCU-01-Sol-Problema-1.3.md) |

### Nivel 2: Componentes CPU ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 2.1 | Funciones de la ALU | En respuestas |
| 2.2 | Flags del registro STATUS | En respuestas |
| 2.3 | Contador de programa | En respuestas |

### Nivel 3: Sistema de Memoria ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Tipos de memoria ATmega328P | En respuestas |
| 3.2 | Cálculo espacio direccionable | En respuestas |
| 3.3 | RAM vs Flash volatilidad | En respuestas |

### Nivel 4: Sistema de Reloj ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 4.1 | Oscilador RC vs Cristal | En respuestas |
| 4.2 | Tiempo por instrucción | En respuestas |
| 4.3 | Prescalers de reloj | En respuestas |

### Nivel 5: Selección de MCU ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | Selección para proyecto | En respuestas |
| 5.2 | Comparativa PIC/AVR/STM32 | En respuestas |
| 5.3 | 8 bits vs 32 bits | En respuestas |

---

## Referencia Rápida

### Comparativa de Arquitecturas

```
┌─────────────────────────────────────────────────────────────┐
│                    MICROCONTROLADOR                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                        CPU                           │    │
│  │  ┌─────┐  ┌─────┐  ┌──────┐  ┌────────┐            │    │
│  │  │ ALU │  │ REG │  │  PC  │  │ STATUS │            │    │
│  │  └─────┘  └─────┘  └──────┘  └────────┘            │    │
│  └─────────────────────────────────────────────────────┘    │
│                           │                                  │
│  ┌────────────────────────┴────────────────────────┐        │
│  │                    BUS INTERNO                   │        │
│  └─┬──────┬──────┬──────┬──────┬──────┬──────┬────┘        │
│    │      │      │      │      │      │      │              │
│  ┌─┴──┐ ┌─┴──┐ ┌─┴──┐ ┌─┴──┐ ┌─┴──┐ ┌─┴──┐ ┌─┴──┐        │
│  │FLASH│ │SRAM│ │EEPROM│ │GPIO│ │TIMER│ │ADC │ │UART│        │
│  └────┘ └────┘ └─────┘ └────┘ └────┘ └────┘ └────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Tabla de Memorias

| Tipo | Volatilidad | Velocidad | Ciclos Escritura | Uso |
|------|:-----------:|:---------:|:----------------:|-----|
| Flash | No | Media | ~10,000 | Programa |
| SRAM | Sí | Alta | ∞ | Variables |
| EEPROM | No | Baja | ~100,000 | Config |

### Fórmulas Importantes

| Concepto | Fórmula |
|----------|---------|
| Espacio direccionable | $2^n$ bytes (n = bits de bus) |
| Tiempo por ciclo | $T = \frac{1}{f_{CPU}}$ |
| Frecuencia con prescaler | $f_{out} = \frac{f_{CPU}}{prescaler}$ |

---

## Navegación

| Anterior | Arriba | Siguiente |
|:--------:|:------:|:---------:|
| [Teoría](../../theory/) | [Módulo MCU](../../00-Index.md) | [Registros/Puertos](../../../03-02-registros-puertos/solutions/prob-01/) |
