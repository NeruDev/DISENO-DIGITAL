<!--
::METADATA::
type: reference
topic_id: mcu-04-adc-dac
file_id: resumen-adc
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, microcontrolador, ADC, DAC, conversión]
search_keywords: "resumen, ADC, DAC, conversión, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-04-Intro.md)

---

# 📋 Cheatsheet: ADC y DAC

## Fórmulas Fundamentales

### Conversión ADC
$$Digital = \frac{V_{in} \times 2^n}{V_{REF}}$$

$$V_{in} = \frac{Digital \times V_{REF}}{2^n}$$

### LSB (Resolución)
$$LSB = \frac{V_{REF}}{2^n}$$

---

## Resolución Típica

| Bits | Niveles | LSB (5V) |
|------|---------|----------|
| 8 | 256 | 19.5 mV |
| 10 | 1024 | 4.88 mV |
| 12 | 4096 | 1.22 mV |

---

## Configuración ADC (AVR)

```c
// Inicialización
ADMUX = (1 << REFS0);  // AVCC ref
ADCSRA = (1 << ADEN) | 
         (1 << ADPS2) | 
         (1 << ADPS1) | 
         (1 << ADPS0);  // /128
```

---

## Lectura ADC

```c
uint16_t adc_read(uint8_t ch) {
    ADMUX = (ADMUX & 0xF0) | ch;
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    return ADC;
}
```

---

## Referencias (AVR)

| REFS1 | REFS0 | Referencia |
|-------|-------|------------|
| 0 | 0 | AREF |
| 0 | 1 | AVCC |
| 1 | 1 | 1.1V int |

---

## Prescaler ADC

| ADPS | División | @ 16MHz |
|------|----------|---------|
| 111 | 128 | 125 kHz ✓ |
| 110 | 64 | 250 kHz |
| 101 | 32 | 500 kHz |

*Óptimo: 50-200 kHz*

---

## Conversión a Voltaje

```c
// Milivoltios (sin float)
uint16_t mv = adc_val * 5000 / 1024;

// Con float
float v = adc_val * 5.0 / 1024.0;
```

---

## Sensores Comunes

| Sensor | Salida | Fórmula |
|--------|--------|---------|
| LM35 | 10mV/°C | T = mV/10 |
| TMP36 | 10mV/°C +500mV | T = (mV-500)/10 |
| NTC | R variable | Steinhart-Hart |

---

## Divisor de Voltaje

```
V_in ──R1──┬── V_ADC
           R2
           │
          GND

V_ADC = V_in × R2/(R1+R2)
```

---

## Promediado

```c
uint16_t avg(uint8_t ch, uint8_t n) {
    uint32_t sum = 0;
    for (uint8_t i = 0; i < n; i++)
        sum += adc_read(ch);
    return sum / n;
}
```

---

## PWM como DAC

```c
// V_out = (OCR/255) × V_CC
OCR0A = 127;  // ≈ 2.5V
```

Filtro RC: f_c << f_PWM

---

## Reducir Ruido

1. ✅ DIDR0 = (1 << ADCnD)
2. ✅ Promediar lecturas
3. ✅ Cap desacople AVCC
4. ✅ Filtro RC entrada

---

## Valores de Referencia

| Condición | ADC (10-bit, 5V) |
|-----------|------------------|
| 0V | 0 |
| 2.5V | 512 |
| 5V | 1023 |
| 1V | 205 |

---

## Calibración

```c
// 2 puntos conocidos
cal.raw_low = read @ V_low
cal.raw_high = read @ V_high

// Interpolar
val = (raw - raw_low) × 
      (phys_high - phys_low) /
      (raw_high - raw_low) + 
      phys_low
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante trabajo con ADC
-->
