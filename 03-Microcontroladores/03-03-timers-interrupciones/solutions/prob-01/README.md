<!--
::METADATA::
type: solution_index
topic_id: mcu-03-timers-interrupciones
file_id: solucion-index-timers
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, timer, interrupción, PWM, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-03-Respuestas.md) | [Problemas →](../../problems/MCU-03-Problemas.md)

---

# Soluciones Detalladas: Timers e Interrupciones (MCU-03)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-03-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Cálculos y código detallado |
| **3** | Secciones "Conceptos Clave" | Teoría de timing |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos Básicos ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | Timer vs Counter | En respuestas |
| 1.2 | Prescaler | En respuestas |
| 1.3 | Timer 8 bits valores | En respuestas |

### Nivel 2: Cálculos de Timer ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 2.1 | Tiempo por tick | [MCU-03-Sol-Problema-2.1.md](./MCU-03-Sol-Problema-2.1.md) |
| 2.2 | Cálculo de OCR | [MCU-03-Sol-Problema-2.2.md](./MCU-03-Sol-Problema-2.2.md) |
| 2.3 | Período máximo | En respuestas |

### Nivel 3: Configuración de Timer ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Timer0 modo CTC | [MCU-03-Sol-Problema-3.1.md](./MCU-03-Sol-Problema-3.1.md) |
| 3.2 | Bits WGM para PWM | En respuestas |
| 3.3 | Timer1 overflow | En respuestas |

### Nivel 4: Interrupciones ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 4.1 | `volatile` en ISR | En respuestas |
| 4.2 | Problema con delay en ISR | En respuestas |
| 4.3 | ISR con contador | En respuestas |

### Nivel 5: PWM ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | Duty cycle cálculo | En respuestas |
| 5.2 | PWM 1 kHz | En respuestas |
| 5.3 | Resolución PWM 50 Hz | En respuestas |

### Nivel 6-7: Aplicaciones ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 6.1 | LED 2 Hz | En respuestas |
| 6.2 | Función millis() | En respuestas |
| 6.3 | Onda 440 Hz | En respuestas |

---

## Referencia Rápida

### Fórmulas de Timer

| Concepto | Fórmula |
|----------|---------|
| Tiempo por tick | $T_{tick} = \frac{Prescaler}{f_{CPU}}$ |
| Período de overflow | $T_{ovf} = T_{tick} \times (TOP + 1)$ |
| OCR para tiempo T | $OCR = \frac{T \times f_{CPU}}{Prescaler} - 1$ |
| Frecuencia CTC | $f_{CTC} = \frac{f_{CPU}}{2 \times Prescaler \times (OCR + 1)}$ |
| Duty Cycle PWM | $DC = \frac{OCR + 1}{TOP + 1} \times 100\%$ |

### Prescalers Disponibles (AVR)

| Timer0/2 (8-bit) | Timer1 (16-bit) |
|------------------|-----------------|
| 1, 8, 64, 256, 1024 | 1, 8, 64, 256, 1024 |

### Modos de Timer (WGM bits)

| Modo | WGM[2:0] | TOP | Uso |
|------|:--------:|:---:|-----|
| Normal | 000 | 0xFF | Overflow simple |
| CTC | 010 | OCRnA | Frecuencia exacta |
| Fast PWM | 011 | 0xFF | PWM rápido |
| Phase Correct | 001 | 0xFF | PWM centrado |

### Diagrama de Timer CTC

```
         ┌───┐       ┌───┐       ┌───┐
TCNT ────┤   ├───────┤   ├───────┤   ├────
         │   │       │   │       │   │
    0 ───┘   └─ OCR ─┘   └─ OCR ─┘   └───
              ↑           ↑           ↑
         Interrupción  Interrupción  ...
```

### Registros Clave

```
┌─────────────────────────────────────────────────────────────┐
│ TCCRnA: Control A                                           │
│   - COMnA[1:0]: Modo de comparación canal A                │
│   - COMnB[1:0]: Modo de comparación canal B                │
│   - WGMn[1:0]: Modo de operación (bits bajos)              │
├─────────────────────────────────────────────────────────────┤
│ TCCRnB: Control B                                           │
│   - WGMn2: Modo de operación (bit alto)                    │
│   - CSn[2:0]: Prescaler (000=stop, 001=/1, 010=/8...)      │
├─────────────────────────────────────────────────────────────┤
│ TCNTn: Contador actual                                      │
│ OCRnA/B: Valores de comparación                            │
│ TIMSKn: Máscara de interrupciones                          │
│ TIFRn: Flags de interrupción                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Navegación

| Anterior | Arriba | Siguiente |
|:--------:|:------:|:---------:|
| [Registros/Puertos](../../../03-02-registros-puertos/solutions/prob-01/) | [Módulo MCU](../../00-Index.md) | [ADC/DAC](../../../03-04-adc-dac/solutions/prob-01/) |
