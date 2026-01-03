<!--
::METADATA::
type: solution_index
topic_id: mcu-04-adc-dac
file_id: solucion-index-adc
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, ADC, DAC, sensores, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-04-Respuestas.md) | [Problemas →](../../problems/MCU-04-Problemas.md)

---

# Soluciones Detalladas: ADC y DAC (MCU-04)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-04-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Cálculos y código |
| **3** | Secciones "Conceptos Clave" | Teoría de conversión |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos Básicos ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | Resolución 10 bits | En respuestas |
| 1.2 | ADC vs DAC | En respuestas |
| 1.3 | Valor del LSB | [MCU-04-Sol-Problema-1.3.md](./MCU-04-Sol-Problema-1.3.md) |

### Nivel 2: Cálculos de Conversión ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 2.1 | Conversión V→Digital | [MCU-04-Sol-Problema-2.1.md](./MCU-04-Sol-Problema-2.1.md) |
| 2.2 | ADC 12 bits | En respuestas |
| 2.3 | Niveles de cuantización | En respuestas |

### Nivel 3: Configuración ADC ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Config ADMUX/ADCSRA | [MCU-04-Sol-Problema-3.1.md](./MCU-04-Sol-Problema-3.1.md) |
| 3.2 | Referencia interna | En respuestas |
| 3.3 | Frecuencia ADC | En respuestas |

### Nivel 4: Lectura de Sensores ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 4.1 | Sensor LM35 | En respuestas |
| 4.2 | Potenciómetro | En respuestas |
| 4.3 | Divisor de voltaje | En respuestas |

### Nivel 5: Filtrado ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | Por qué promediar | En respuestas |
| 5.2 | Promedio con descarte | En respuestas |
| 5.3 | Media móvil | En respuestas |

### Nivel 6-7: PWM como DAC ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 6.1 | PWM → Analog | En respuestas |
| 6.2 | Filtro RC | En respuestas |
| 7.1 | Termómetro digital | En respuestas |

---

## Referencia Rápida

### Fórmulas de ADC

| Concepto | Fórmula |
|----------|---------|
| LSB (resolución) | $LSB = \frac{V_{REF}}{2^n}$ |
| Voltaje → Digital | $ADC = \frac{V_{in} \times 2^n}{V_{REF}}$ |
| Digital → Voltaje | $V = \frac{ADC \times V_{REF}}{2^n}$ |
| Rango de código N | $[N \times LSB, (N+1) \times LSB)$ |

### Tabla de Resolución

| Bits | Niveles | LSB (5V) | LSB (3.3V) |
|:----:|:-------:|:--------:|:----------:|
| 8 | 256 | 19.53 mV | 12.89 mV |
| 10 | 1024 | 4.88 mV | 3.22 mV |
| 12 | 4096 | 1.22 mV | 0.81 mV |

### Registros ADC (AVR)

```
┌─────────────────────────────────────────────────────────────┐
│ ADMUX: Multiplexor                                          │
│   - REFS[1:0]: Referencia (00=AREF, 01=AVCC, 11=1.1V)      │
│   - ADLAR: Alineación (0=derecha, 1=izquierda)             │
│   - MUX[3:0]: Canal (0000=ADC0 ... 0111=ADC7)              │
├─────────────────────────────────────────────────────────────┤
│ ADCSRA: Control                                             │
│   - ADEN: ADC Enable                                        │
│   - ADSC: Start Conversion                                  │
│   - ADATE: Auto Trigger Enable                              │
│   - ADIF: Interrupt Flag                                    │
│   - ADIE: Interrupt Enable                                  │
│   - ADPS[2:0]: Prescaler (000=/2 ... 111=/128)             │
├─────────────────────────────────────────────────────────────┤
│ ADCL/ADCH: Resultado (10 bits)                              │
└─────────────────────────────────────────────────────────────┘
```

### Diagrama de Conversión

```
    V_in                                    Digital
      │                                        │
      ▼                                        ▼
  ┌───────┐    ┌─────────┐    ┌────────┐   ┌────┐
  │Sample │───►│ Compare │───►│Quantize│──►│ADCH│
  │ Hold  │    │  (SAR)  │    │        │   │ADCL│
  └───────┘    └─────────┘    └────────┘   └────┘
                    ▲
                    │
              V_REF ─┘
```

### Prescalers para 50-200 kHz

| F_CPU | Prescaler | f_ADC |
|:-----:|:---------:|:-----:|
| 16 MHz | /128 | 125 kHz ✓ |
| 8 MHz | /64 | 125 kHz ✓ |
| 1 MHz | /8 | 125 kHz ✓ |

---

## Navegación

| Anterior | Arriba | Siguiente |
|:--------:|:------:|:---------:|
| [Timers](../../../03-03-timers-interrupciones/solutions/prob-01/) | [Módulo MCU](../../00-Index.md) | [UART](../../../03-05-comunicacion-serial/solutions/prob-01/) |
