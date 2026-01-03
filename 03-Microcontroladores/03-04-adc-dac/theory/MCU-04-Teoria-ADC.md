<!--
::METADATA::
type: theory
topic_id: mcu-04-adc-dac
file_id: teoria-adc-dac
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, ADC, DAC, conversión, analógico]
search_keywords: "ADC, DAC, conversión analógica, muestreo"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-04-Intro.md) | [Métodos →](../methods/MCU-04-Metodos-ADC.md)

---

# Conversión Analógica-Digital (ADC) y Digital-Analógica (DAC)

## 1. Introducción

### 1.1 ¿Por qué Conversión A/D?

El mundo real es **analógico**, pero los MCU procesan **digital**.

```
Mundo Real              MCU                 Actuadores
┌──────────┐        ┌──────────┐        ┌──────────┐
│Temperatura│──ADC──▶│ Procesa  │──DAC──▶│  Motor   │
│  Luz     │        │ Digital  │  PWM   │ Display  │
│ Sonido   │        └──────────┘        │ Speaker  │
└──────────┘                            └──────────┘
```

---

## 2. Convertidor Analógico-Digital (ADC)

### 2.1 Conceptos Fundamentales

| Concepto | Descripción |
|----------|-------------|
| **Resolución** | Número de bits del resultado |
| **V_REF** | Voltaje de referencia (rango máximo) |
| **LSB** | Mínimo cambio detectable |
| **Sampling Rate** | Muestras por segundo |

### 2.2 Resolución y LSB

$$LSB = \frac{V_{REF}}{2^n}$$

Para ADC de 10 bits con V_REF = 5V:
$$LSB = \frac{5V}{1024} = 4.88mV$$

### 2.3 Fórmula de Conversión

$$Digital = \frac{V_{in} \times 2^n}{V_{REF}}$$

$$V_{in} = \frac{Digital \times V_{REF}}{2^n}$$

---

## 3. Arquitectura del ADC

### 3.1 ADC de Aproximaciones Sucesivas (SAR)

Tipo más común en MCU.

```
V_in ─────┬─────────────────────────────────
          │                                 
          │     ┌───────────────────┐       
          ├────▶│   Comparador      │───┐   
          │     └───────────────────┘   │   
          │              ▲              │   
          │              │              │   
          │     ┌────────┴────────┐     │   
          │     │    DAC Interno  │     │   
          │     └────────▲────────┘     │   
          │              │              │   
          │     ┌────────┴────────┐     │   
          │     │  Registro SAR   │◀────┘   
          │     │ (Aprox. Sucesiva)│        
          │     └────────┬────────┘        
          │              │                  
          │              ▼                  
          │      Resultado Digital         
```

### 3.2 Proceso de Conversión (10 bits)

```
Ejemplo: V_in = 3.3V, V_REF = 5V

Paso 1: Probar bit 9 (512) → 2.5V < 3.3V ✓ → 1_________
Paso 2: Probar bit 8 (256) → 3.75V > 3.3V ✗ → 10________
Paso 3: Probar bit 7 (128) → 3.125V < 3.3V ✓ → 101_______
... continúa 10 pasos

Resultado: aproximadamente 675 (0x2A3)
```

---

## 4. ADC en AVR (ATmega328P)

### 4.1 Características

- Resolución: 10 bits
- 6 canales (8 en TQFP)
- Referencia: AVCC, Internal 1.1V, o AREF
- Tiempo de conversión: 13-260 µs

### 4.2 Registros

| Registro | Función |
|----------|---------|
| ADMUX | Selección de canal y referencia |
| ADCSRA | Control y estado |
| ADCL, ADCH | Resultado (10 bits) |
| ADCSRB | Trigger source |

### 4.3 Bits de ADMUX

```
┌─────┬─────┬──────┬──────┬─────┬─────┬─────┬─────┐
│REFS1│REFS0│ADLAR │  -   │MUX3 │MUX2 │MUX1 │MUX0 │
└─────┴─────┴──────┴──────┴─────┴─────┴─────┴─────┘
  Referencia  Ajuste        Selección de canal
```

| REFS1 | REFS0 | Referencia |
|-------|-------|------------|
| 0 | 0 | AREF externo |
| 0 | 1 | AVCC |
| 1 | 1 | Internal 1.1V |

### 4.4 Bits de ADCSRA

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ADEN │ADSC │ADATE│ADIF │ADIE │ADPS2│ADPS1│ADPS0│
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
Enable Start Auto  Flag  Int.    Prescaler
              Trig
```

| ADPS2:1:0 | Prescaler | Freq @ 16MHz |
|-----------|-----------|--------------|
| 011 | 8 | 2 MHz (muy rápido) |
| 100 | 16 | 1 MHz |
| 101 | 32 | 500 kHz |
| 110 | 64 | 250 kHz |
| 111 | 128 | 125 kHz (recomendado) |

---

## 5. Configuración del ADC

### 5.1 Inicialización Básica

```c
void adc_init(void) {
    // Referencia AVCC, canal 0
    ADMUX = (1 << REFS0);
    
    // Habilitar ADC, prescaler /128
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t adc_read(uint8_t channel) {
    // Seleccionar canal
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    
    // Iniciar conversión
    ADCSRA |= (1 << ADSC);
    
    // Esperar que termine
    while (ADCSRA & (1 << ADSC));
    
    return ADC;  // Leer resultado
}
```

### 5.2 Conversión a Voltaje

```c
float adc_to_voltage(uint16_t adc_value) {
    return (adc_value * 5.0) / 1024.0;
}

// O con enteros (milivolts)
uint16_t adc_to_millivolts(uint16_t adc_value) {
    return (uint32_t)adc_value * 5000 / 1024;
}
```

---

## 6. Modos de Operación

### 6.1 Single Conversion (Manual)

```c
// Cada lectura requiere iniciar conversión
ADCSRA |= (1 << ADSC);
while (ADCSRA & (1 << ADSC));
resultado = ADC;
```

### 6.2 Free Running (Continuo)

```c
void adc_init_freerun(void) {
    ADMUX = (1 << REFS0);
    ADCSRA = (1 << ADEN) | (1 << ADATE) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
    ADCSRB = 0;  // Free running mode
    ADCSRA |= (1 << ADSC);  // Iniciar primera conversión
}

// El ADC convierte continuamente
// Solo leer ADC cuando necesites
```

### 6.3 Auto Trigger (por Timer/Interrupción)

```c
void adc_init_timer_trigger(void) {
    ADMUX = (1 << REFS0);
    ADCSRA = (1 << ADEN) | (1 << ADATE) | (1 << ADIE) | 
             (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
    ADCSRB = (1 << ADTS2) | (1 << ADTS1);  // Timer1 Compare Match B
}

ISR(ADC_vect) {
    uint16_t resultado = ADC;
    // Procesar resultado
}
```

---

## 7. Mejorando la Precisión

### 7.1 Oversampling

Tomar múltiples muestras y promediar.

```c
uint16_t adc_read_averaged(uint8_t channel, uint8_t samples) {
    uint32_t sum = 0;
    
    for (uint8_t i = 0; i < samples; i++) {
        sum += adc_read(channel);
    }
    
    return sum / samples;
}
```

### 7.2 Reducción de Ruido

```c
// 1. Desactivar digitales en pines analógicos
DIDR0 = (1 << ADC0D) | (1 << ADC1D);  // Deshabilitar digital en ADC0, ADC1

// 2. Modo Sleep para conversión
void adc_read_quiet(void) {
    set_sleep_mode(SLEEP_MODE_ADC);
    ADCSRA |= (1 << ADIE);  // Interrupción despierta
    sleep_mode();  // ADC convierte mientras duerme
}
```

### 7.3 Descarte de Primera Lectura

```c
void adc_init(void) {
    // ... configuración ...
    
    // Descartar primera conversión (cambio de canal)
    adc_read(0);
}
```

---

## 8. Conversión Digital-Analógica (DAC)

### 8.1 MCU sin DAC Hardware

Muchos MCU (como ATmega328P) no tienen DAC. Alternativas:

#### PWM como DAC

```
PWM ─────┬─────┐
         │     │ R
         │     ├───────── V_out
         │     │
         │    ─┴─ C
         │    ───
         │     │
        GND   GND

V_out = DC × V_HIGH
```

```c
// PWM como "DAC" de 8 bits
void dac_pwm_write(uint8_t value) {
    OCR0A = value;  // 0-255 → 0-5V (filtrado)
}
```

#### R-2R Ladder

```
D0 ──R──┬
        │
D1 ──R──┼──2R──┬
        │      │
D2 ──R──┼──2R──┼──2R──┬
        │      │      │
D3 ──R──┴──2R──┴──2R──┴── V_out
```

### 8.2 MCU con DAC (STM32, PIC)

```c
// Ejemplo STM32 HAL
HAL_DAC_SetValue(&hdac, DAC_CHANNEL_1, DAC_ALIGN_12B_R, valor);
HAL_DAC_Start(&hdac, DAC_CHANNEL_1);
```

---

## 9. Aplicaciones Comunes

### 9.1 Lectura de Sensor de Temperatura (LM35)

```c
// LM35: 10 mV/°C
float leer_temperatura_lm35(void) {
    uint16_t adc_val = adc_read_averaged(0, 10);
    float voltage = adc_val * 5.0 / 1024.0;
    return voltage * 100.0;  // °C
}
```

### 9.2 Lectura de Potenciómetro

```c
uint8_t leer_potenciometro_percent(void) {
    uint16_t adc_val = adc_read(0);
    return (uint8_t)((uint32_t)adc_val * 100 / 1023);
}
```

### 9.3 Sensor de Luz (LDR)

```c
// Con divisor de voltaje
uint16_t leer_luz(void) {
    return 1023 - adc_read(0);  // Invertir si LDR arriba
}
```

---

## 10. Consideraciones de Diseño

### 10.1 Rango de Entrada

| Caso | Solución |
|------|----------|
| V_in > V_REF | Divisor de voltaje |
| V_in < 0 | Offset + amplificador |
| Señal pequeña | Amplificador operacional |

### 10.2 Divisor de Voltaje

```
V_in ────R1────┬───── V_ADC
               │
              R2
               │
              GND

V_ADC = V_in × R2 / (R1 + R2)
```

---

## Referencias

- ATmega328P Datasheet - Analog to Digital Converter
- AVR120: Characterization and Calibration of ADC
- AN2834: How to get the best ADC accuracy

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 03-01, 03-02, 03-03
CONEXIONES: Sensores, audio, control de procesos
ERRORES_COMUNES: Referencia incorrecta, prescaler muy alto, no filtrar señal
-->
