<!--
::METADATA::
type: detailed_solution
topic_id: mcu-04-adc-dac
problem_id: 2.1
file_id: solucion-problema-2-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, MCU, ADC, conversión, cálculo]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 2.2 →](./MCU-04-Sol-Problema-2.2.md)

---

# Solución Detallada: Problema 2.1

## Enunciado
Con un ADC de 10 bits y V_REF = 5V:
- ¿Qué valor digital produce una entrada de 2.5V?
- ¿Qué voltaje representa el valor digital 768?

---

## Parte A: Voltaje → Digital (2.5V)

### Fórmula

$$ADC = \frac{V_{in} \times 2^n}{V_{REF}}$$

### Cálculo

$$ADC = \frac{2.5V \times 2^{10}}{5V} = \frac{2.5 \times 1024}{5} = \frac{2560}{5} = 512$$

### Verificación Visual

```
V_REF = 5V          ──────────────────── 1023
                    │
                    │
2.5V ───────────────┼──────────────────  512  (mitad)
                    │
                    │
GND = 0V            ──────────────────── 0
```

> ✅ **Respuesta:** 2.5V produce **ADC = 512**

---

## Parte B: Digital → Voltaje (768)

### Fórmula

$$V = \frac{ADC \times V_{REF}}{2^n}$$

### Cálculo

$$V = \frac{768 \times 5V}{1024} = \frac{3840}{1024} = 3.75V$$

### Verificación Visual

```
1023 ────────────── 5.00V
 │
768 ─────────────── 3.75V  ← Respuesta
 │
512 ─────────────── 2.50V
 │
256 ─────────────── 1.25V
 │
  0 ─────────────── 0.00V
```

> ✅ **Respuesta:** ADC = 768 representa **V = 3.75V**

---

## Análisis Adicional

### Resolución (LSB)

$$LSB = \frac{V_{REF}}{2^n} = \frac{5V}{1024} = 4.883\,mV$$

Esto significa que:
- Cada incremento de 1 en ADC = 4.883 mV
- El ADC no puede distinguir diferencias menores a ~5 mV

### Rango de Cuantización

Para ADC = 512:

$$V_{min} = 512 \times 4.883\,mV = 2.500V$$
$$V_{max} = 513 \times 4.883\,mV = 2.505V$$

Cualquier voltaje entre 2.500V y 2.505V producirá ADC = 512.

---

## Código de Conversión

```c
#include <avr/io.h>

#define V_REF 5.0
#define ADC_MAX 1024.0

// Convierte lectura ADC a voltaje
float adc_to_voltage(uint16_t adc_value) {
    return (adc_value * V_REF) / ADC_MAX;
}

// Convierte voltaje esperado a valor ADC
uint16_t voltage_to_adc(float voltage) {
    return (uint16_t)((voltage * ADC_MAX) / V_REF);
}

// Ejemplo de uso
int main(void) {
    // Parte A: 2.5V → ADC
    uint16_t resultado_a = voltage_to_adc(2.5);
    // resultado_a = 512
    
    // Parte B: ADC 768 → Voltaje
    float resultado_b = adc_to_voltage(768);
    // resultado_b = 3.75
    
    while(1);
}
```

---

## Tabla de Referencia Rápida

| Voltaje | ADC (10-bit) | Porcentaje |
|:-------:|:------------:|:----------:|
| 0.00V | 0 | 0% |
| 1.25V | 256 | 25% |
| 2.50V | **512** | 50% |
| 3.75V | **768** | 75% |
| 5.00V | 1023 | 100% |

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **Resolución** | $2^n$ niveles posibles |
| **LSB** | Mínimo cambio detectable |
| **Cuantización** | Discretización del voltaje |
| **Error máximo** | ±0.5 LSB = ±2.44 mV |

---

## Errores Comunes

| Error | Consecuencia | Solución |
|-------|--------------|----------|
| Usar 1024 en vez de 1023 para MAX | Offset pequeño | 1023 es el valor máximo, pero 1024 niveles |
| División entera | Pérdida de precisión | Usar `float` o escalar |
| V_REF incorrecto | Medición errónea | Verificar configuración |

---

## Fórmula Alternativa (Escalado Entero)

Para evitar punto flotante:

```c
// Voltaje en mV (sin punto flotante)
uint16_t adc_to_mv(uint16_t adc) {
    // V_REF = 5000mV, escalado por 1024
    return (uint32_t)adc * 5000 / 1024;
}
```

| ADC | Resultado (mV) |
|:---:|:--------------:|
| 512 | 2500 |
| 768 | 3750 |

---

> 💡 **Tip:** Para verificar rápidamente: ADC = 512 siempre es la mitad de V_REF, ADC = 256 es un cuarto, etc.
