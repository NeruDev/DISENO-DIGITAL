<!--
::METADATA::
type: solution
topic_id: mcu-04-adc-dac
file_id: respuestas-adc
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, microcontrolador, ADC, DAC]
search_keywords: "respuestas, soluciones, ADC, conversión"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-04-Problemas.md)

---

# Respuestas: ADC y DAC

## Nivel 1: Conceptos Básicos

### Respuesta 1.1

Resolución de 10 bits significa:
- 2^10 = 1024 niveles de cuantización
- Valores digitales de 0 a 1023
- Puede distinguir 1024 niveles diferentes de voltaje

### Respuesta 1.2

| ADC | DAC |
|-----|-----|
| Analógico → Digital | Digital → Analógico |
| Entrada: voltaje | Entrada: número binario |
| Salida: número binario | Salida: voltaje |
| Ej: leer sensor | Ej: generar audio |

### Respuesta 1.3

$$LSB = \frac{V_{REF}}{2^n} = \frac{5V}{1024} = 4.88mV$$

---

## Nivel 2: Cálculos de Conversión

### Respuesta 2.1

Para entrada de 2.5V:
$$Digital = \frac{V_{in} \times 2^n}{V_{REF}} = \frac{2.5 \times 1024}{5} = 512$$

Para valor digital 768:
$$V_{in} = \frac{Digital \times V_{REF}}{2^n} = \frac{768 \times 5}{1024} = 3.75V$$

### Respuesta 2.2

LSB:
$$LSB = \frac{3.3V}{4096} = 0.806mV$$

Rango para código 1000:
- Límite inferior: 1000 × 0.806mV = 806mV
- Límite superior: 1001 × 0.806mV = 806.8mV

### Respuesta 2.3

$$Niveles = 2^8 = 256$$

---

## Nivel 3: Configuración de ADC (AVR)

### Respuesta 3.1

```c
void adc_init(void) {
    // Referencia AVCC
    ADMUX = (1 << REFS0);
    
    // Canal 0 (MUX = 0000)
    ADMUX &= 0xF0;
    
    // Habilitar, prescaler /128
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}
```

### Respuesta 3.2

Para referencia interna 1.1V:
```c
ADMUX |= (1 << REFS1) | (1 << REFS0);

// REFS1=1, REFS0=1 → Internal 1.1V
```

### Respuesta 3.3

El ADC SAR necesita tiempo para cada bit de aproximación. Con frecuencia muy alta, no tiene tiempo suficiente y pierde precisión. Con frecuencia muy baja, la conversión es innecesariamente lenta.

Para ATmega328P: 50-200 kHz óptimo
16 MHz / 128 = 125 kHz ✓

---

## Nivel 4: Lectura de Sensores

### Respuesta 4.1

```
Voltaje = (150 × 5V) / 1024 = 0.732V = 732mV
Temperatura = 732mV / 10mV/°C = 73.2°C
```

### Respuesta 4.2

ADC = 512 (mitad de 1024):
- Posición: 50% del recorrido
- Si R_total = 10kΩ, R_cursor = 5kΩ

### Respuesta 4.3

Divisor de voltaje 2:1:
```
10V ───R1=10k───┬─── A0 (ADC)
                │
               R2=10k
                │
               GND

V_ADC = V_in × R2/(R1+R2) = 10V × 0.5 = 5V máx
```

---

## Nivel 5: Filtrado y Promediado

### Respuesta 5.1

Razones para promediar:
1. Ruido eléctrico (EMI)
2. Ruido térmico del ADC
3. Fluctuaciones de alimentación
4. Mejora resolución efectiva (oversampling)

### Respuesta 5.2

```c
uint16_t adc_read_filtered(uint8_t channel) {
    uint16_t samples[16];
    uint32_t sum = 0;
    
    // Tomar 16 muestras
    for (uint8_t i = 0; i < 16; i++) {
        samples[i] = adc_read(channel);
    }
    
    // Ordenar (bubble sort simple)
    for (uint8_t i = 0; i < 15; i++) {
        for (uint8_t j = i+1; j < 16; j++) {
            if (samples[j] < samples[i]) {
                uint16_t temp = samples[i];
                samples[i] = samples[j];
                samples[j] = temp;
            }
        }
    }
    
    // Sumar del índice 2 al 13 (descarta 2 menores y 2 mayores)
    for (uint8_t i = 2; i < 14; i++) {
        sum += samples[i];
    }
    
    return sum / 12;
}
```

### Respuesta 5.3

Filtro de media móvil:
- Mantiene buffer de N últimas muestras
- Retorna promedio del buffer
- Suaviza cambios bruscos
- Introduce retardo proporcional a N

---

## Nivel 6: PWM como DAC

### Respuesta 6.1

PWM como DAC:
1. PWM genera onda cuadrada con duty cycle variable
2. Filtro RC (paso bajo) promedia la señal
3. Voltaje de salida = DC × V_HIGH
4. Para DC=50%, V_out = 2.5V (si V_HIGH=5V)

### Respuesta 6.2

Para f_PWM = 62.5 kHz, f_corte debe ser << f_PWM:
```
f_corte = 100 Hz (recomendado)
f_c = 1 / (2π × R × C)

Con R = 10 kΩ:
C = 1 / (2π × 10000 × 100) = 159 nF ≈ 150 nF
```

### Respuesta 6.3

```c
void setup_25v_output(void) {
    // PWM Fast en OC0A
    DDRD |= (1 << PD6);
    TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
    TCCR0B = (1 << CS00);  // Sin prescaler
    
    // 50% duty cycle = 2.5V
    OCR0A = 127;  // 127/255 ≈ 50%
}

// Conectar: OC0A → R=10k → V_out → C=150nF → GND
```

---

## Nivel 7: Aplicaciones de Sensores

### Respuesta 7.1: Termómetro Digital

```c
#include <avr/io.h>
#include <util/delay.h>

// Asume funciones de display 7-seg disponibles

void adc_init(void) {
    ADMUX = (1 << REFS0);
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint8_t read_temperature(void) {
    uint32_t sum = 0;
    
    for (uint8_t i = 0; i < 8; i++) {
        ADCSRA |= (1 << ADSC);
        while (ADCSRA & (1 << ADSC));
        sum += ADC;
    }
    
    // Promedio × 5000 / 1024 / 10 = °C
    // Simplificado: × 500 / 1024
    uint16_t mv = sum * 500 / 1024;  // Ya dividido por 8 y × 10
    
    if (mv > 99) mv = 99;
    return (uint8_t)mv;
}

int main(void) {
    adc_init();
    display_init();
    
    while (1) {
        uint8_t temp = read_temperature();
        display_number(temp);
        _delay_ms(500);
    }
}
```

---

## Nivel 8: Conversión y Calibración

### Respuesta 8.2: Sensor de Presión

```c
// Sensor: 0.5-4.5V → 0-100 PSI
// Con ADC 10-bit, V_REF = 5V:
// 0.5V → ADC 102
// 4.5V → ADC 922

uint8_t read_psi(void) {
    uint16_t adc_val = adc_read(0);
    
    // Limitar a rango válido
    if (adc_val < 102) return 0;
    if (adc_val > 922) return 100;
    
    // Mapear: (adc - 102) × 100 / (922 - 102)
    return (uint8_t)((uint32_t)(adc_val - 102) * 100 / 820);
}
```

### Respuesta 8.3: Umbral con Histéresis

```c
#define TEMP_THRESHOLD 614   // ~30°C (30 × 10mV × 1024 / 5000)
#define HYSTERESIS 41        // ~2°C

volatile uint8_t fan_on = 0;

void check_temperature(void) {
    uint16_t temp_adc = adc_read_avg(0, 4);
    
    if (!fan_on && temp_adc > TEMP_THRESHOLD + HYSTERESIS) {
        fan_on = 1;
        PORTB |= (1 << PB0);  // Encender ventilador
    }
    else if (fan_on && temp_adc < TEMP_THRESHOLD - HYSTERESIS) {
        fan_on = 0;
        PORTB &= ~(1 << PB0);  // Apagar ventilador
    }
}
```

---

## Nivel 9: Optimización y Ruido

### Respuesta 9.1

Técnicas para reducir ruido:
1. **Promediado**: múltiples lecturas
2. **DIDR**: deshabilitar entrada digital
3. **Modo sleep**: ADC Noise Reduction
4. **Filtro hardware**: RC en entrada
5. **Referencia estable**: evitar AVCC ruidoso
6. **Desacople**: capacitor en AVCC

### Respuesta 9.2

```c
// DIDR0 = Digital Input Disable Register
// Desconecta el buffer digital del pin
// Reduce corriente de fuga y ruido

DIDR0 = (1 << ADC0D) | (1 << ADC1D);  // ADC0 y ADC1

// Usar cuando:
// - Pin SOLO se usa como entrada analógica
// - Se necesita máxima precisión
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de ADC y DAC
NOTA: Pueden existir soluciones alternativas válidas
-->
