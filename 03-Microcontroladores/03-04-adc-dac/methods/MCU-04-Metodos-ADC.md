<!--
::METADATA::
type: method
topic_id: mcu-04-adc-dac
file_id: metodos-adc
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, metodología, ADC, DAC, sensores]
search_keywords: "metodología ADC, conversión analógica, sensores"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-04-Teoria-ADC.md) | [Problemas →](../problems/MCU-04-Problemas.md)

---

# Métodos: ADC y DAC

## Método 1: Biblioteca ADC Completa

```c
#include <avr/io.h>
#include <util/delay.h>

typedef enum {
    ADC_REF_AREF  = 0x00,
    ADC_REF_AVCC  = 0x40,
    ADC_REF_INT   = 0xC0
} adc_ref_t;

void adc_init(adc_ref_t ref) {
    ADMUX = ref;
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
    
    // Primera conversión descartada
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
}

uint16_t adc_read(uint8_t channel) {
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    _delay_us(10);  // Estabilización
    
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    
    return ADC;
}

uint16_t adc_read_avg(uint8_t channel, uint8_t samples) {
    uint32_t sum = 0;
    for (uint8_t i = 0; i < samples; i++) {
        sum += adc_read(channel);
    }
    return sum / samples;
}
```

---

## Método 2: Conversión a Unidades Físicas

### Voltaje

```c
// Retorna milivoltios (evita floats)
uint16_t adc_to_mv(uint16_t adc_value, uint16_t vref_mv) {
    return (uint32_t)adc_value * vref_mv / 1024;
}

// Con punto decimal (×10 para un decimal)
uint16_t adc_to_mv_x10(uint16_t adc_value, uint16_t vref_mv) {
    return (uint32_t)adc_value * vref_mv * 10 / 1024;
}
```

### Temperatura (LM35)

```c
// LM35: 10mV/°C, retorna °C × 10
int16_t lm35_read_temp_x10(uint8_t channel) {
    uint16_t mv = adc_to_mv(adc_read_avg(channel, 8), 5000);
    return mv;  // 10mV/°C → mv = °C × 10
}

// Uso: temp_x10 = 235 significa 23.5°C
```

### Temperatura (NTC Termistor)

```c
// Steinhart-Hart simplificado
float ntc_read_temp(uint8_t channel, float r_serie) {
    uint16_t adc_val = adc_read(channel);
    
    // Calcular resistencia NTC
    float r_ntc = r_serie * adc_val / (1023 - adc_val);
    
    // Beta equation (B = 3950, R0 = 10k @ 25°C)
    const float B = 3950.0;
    const float R0 = 10000.0;
    const float T0 = 298.15;  // 25°C en Kelvin
    
    float temp_k = 1.0 / (1.0/T0 + log(r_ntc/R0)/B);
    return temp_k - 273.15;  // Celsius
}
```

---

## Método 3: Lectura de Múltiples Canales

```c
#define NUM_CHANNELS 4

typedef struct {
    uint8_t channel;
    uint16_t value;
    uint16_t min_val;
    uint16_t max_val;
} adc_channel_t;

adc_channel_t sensors[NUM_CHANNELS] = {
    {0, 0, 0, 1023},  // Pot
    {1, 0, 0, 1023},  // LDR
    {2, 0, 0, 1023},  // Temp
    {3, 0, 0, 1023}   // Extra
};

void read_all_sensors(void) {
    for (uint8_t i = 0; i < NUM_CHANNELS; i++) {
        sensors[i].value = adc_read(sensors[i].channel);
    }
}

// Mapear valor a rango específico
uint16_t map_value(adc_channel_t *s, uint16_t out_min, uint16_t out_max) {
    return (uint32_t)(s->value - s->min_val) * (out_max - out_min) / 
           (s->max_val - s->min_val) + out_min;
}
```

---

## Método 4: Filtro de Media Móvil

```c
#define FILTER_SIZE 8

typedef struct {
    uint16_t buffer[FILTER_SIZE];
    uint8_t index;
    uint32_t sum;
    uint8_t count;
} moving_avg_t;

void filter_init(moving_avg_t *f) {
    f->index = 0;
    f->sum = 0;
    f->count = 0;
}

uint16_t filter_add(moving_avg_t *f, uint16_t value) {
    // Restar valor antiguo si buffer lleno
    if (f->count >= FILTER_SIZE) {
        f->sum -= f->buffer[f->index];
    } else {
        f->count++;
    }
    
    // Agregar nuevo valor
    f->buffer[f->index] = value;
    f->sum += value;
    f->index = (f->index + 1) % FILTER_SIZE;
    
    return f->sum / f->count;
}

// Uso
moving_avg_t temp_filter;
filter_init(&temp_filter);

while(1) {
    uint16_t raw = adc_read(0);
    uint16_t filtered = filter_add(&temp_filter, raw);
}
```

---

## Método 5: PWM como DAC

```c
// Configurar PWM en Timer0 (8-bit)
void pwm_dac_init(void) {
    DDRD |= (1 << PD6);  // OC0A
    
    // Fast PWM, non-inverting
    TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
    TCCR0B = (1 << CS00);  // Sin prescaler = alta frecuencia
    
    OCR0A = 0;
}

void pwm_dac_write(uint8_t value) {
    OCR0A = value;  // 0-255 → 0-V_CC
}

// Calcular valor para voltaje específico
uint8_t voltage_to_pwm(uint16_t mv, uint16_t vcc_mv) {
    return (uint32_t)mv * 255 / vcc_mv;
}
```

### Filtro RC para PWM-DAC

```
f_corte = 1 / (2π × R × C)

Para PWM de 62.5 kHz, usar f_corte ≈ 100 Hz
R = 10 kΩ, C = 160 nF

Ripple ≈ V_CC / (f_PWM × R × C)
```

---

## Método 6: Generador de Señales con PWM

```c
// Tabla de seno (256 valores, 0-255)
const uint8_t sine_table[256] PROGMEM = {
    128, 131, 134, 137, 140, 143, 146, 149,
    // ... 256 valores ...
};

volatile uint8_t phase = 0;

void wave_init(uint16_t frequency) {
    pwm_dac_init();
    
    // Timer2 para tasa de muestreo
    TCCR2A = (1 << WGM21);  // CTC
    TCCR2B = (1 << CS21);   // /8
    
    // OCR2A para frecuencia deseada
    // f_out = f_sample / 256
    // f_sample = F_CPU / (8 × (OCR2A + 1))
    OCR2A = F_CPU / 8 / (frequency * 256) - 1;
    
    TIMSK2 = (1 << OCIE2A);
    sei();
}

ISR(TIMER2_COMPA_vect) {
    OCR0A = pgm_read_byte(&sine_table[phase++]);
}
```

---

## Método 7: Sensor con Calibración

```c
typedef struct {
    uint16_t raw_min;    // Valor ADC mínimo calibrado
    uint16_t raw_max;    // Valor ADC máximo calibrado
    int16_t phys_min;    // Valor físico mínimo
    int16_t phys_max;    // Valor físico máximo
} calibration_t;

calibration_t temp_cal = {100, 900, -20, 80};  // -20°C a 80°C

int16_t read_calibrated(uint8_t channel, calibration_t *cal) {
    uint16_t raw = adc_read_avg(channel, 4);
    
    // Limitar a rango
    if (raw < cal->raw_min) raw = cal->raw_min;
    if (raw > cal->raw_max) raw = cal->raw_max;
    
    // Mapear a valor físico
    return (int32_t)(raw - cal->raw_min) * (cal->phys_max - cal->phys_min) /
           (cal->raw_max - cal->raw_min) + cal->phys_min;
}

// Rutina de calibración
void calibrate_sensor(calibration_t *cal, uint8_t channel) {
    // Instrucción: poner sensor en punto mínimo
    _delay_ms(5000);
    cal->raw_min = adc_read_avg(channel, 16);
    
    // Instrucción: poner sensor en punto máximo
    _delay_ms(5000);
    cal->raw_max = adc_read_avg(channel, 16);
}
```

---

## Método 8: Detección de Umbral

```c
#define HYSTERESIS 20

typedef struct {
    uint16_t threshold;
    uint8_t state;
    uint8_t changed;
} threshold_t;

void threshold_check(threshold_t *t, uint16_t value) {
    uint8_t new_state;
    
    if (t->state == 0) {
        new_state = (value > t->threshold + HYSTERESIS) ? 1 : 0;
    } else {
        new_state = (value < t->threshold - HYSTERESIS) ? 0 : 1;
    }
    
    t->changed = (new_state != t->state);
    t->state = new_state;
}

// Uso para alarma de temperatura
threshold_t temp_alarm = {700, 0, 0};  // ~34°C

if (threshold_check(&temp_alarm, adc_read(0)), temp_alarm.changed) {
    if (temp_alarm.state) {
        activar_alarma();
    } else {
        desactivar_alarma();
    }
}
```

---

## Método 9: Batería Monitor

```c
// Divisor de voltaje 10k/10k para batería 7.4V
#define BATT_R1 10000
#define BATT_R2 10000
#define BATT_SCALE ((BATT_R1 + BATT_R2) * 1000 / BATT_R2)  // ×1000

uint16_t read_battery_mv(uint8_t channel) {
    uint16_t adc_mv = adc_to_mv(adc_read_avg(channel, 8), 5000);
    return (uint32_t)adc_mv * BATT_SCALE / 1000;
}

uint8_t battery_percent(uint16_t mv) {
    // Para LiPo 2S: 6.4V (0%) - 8.4V (100%)
    if (mv < 6400) return 0;
    if (mv > 8400) return 100;
    return (mv - 6400) * 100 / 2000;
}
```

---

## Método 10: ADC con DMA (STM32)

```c
// Ejemplo para STM32 HAL
#define NUM_CHANNELS 4
uint16_t adc_buffer[NUM_CHANNELS];

void adc_dma_init(void) {
    // Configuración en CubeMX:
    // - ADC en modo scan
    // - Múltiples canales
    // - DMA en modo circular
    
    HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_buffer, NUM_CHANNELS);
}

// Los valores se actualizan automáticamente en adc_buffer[]
uint16_t get_adc_channel(uint8_t ch) {
    return adc_buffer[ch];
}
```

---

## Método 11: Checklist ADC

### Configuración Hardware

- [ ] ¿Pin configurado como entrada analógica?
- [ ] ¿Señal en rango 0-V_REF?
- [ ] ¿Filtro anti-aliasing si señal rápida?
- [ ] ¿Condensador de desacople en AVCC?

### Configuración Software

- [ ] ¿Referencia correcta seleccionada?
- [ ] ¿Prescaler da frecuencia 50-200 kHz?
- [ ] ¿Primera conversión descartada?
- [ ] ¿Espera tiempo de estabilización al cambiar canal?

### Optimización

- [ ] ¿Promediado si se necesita más precisión?
- [ ] ¿DIDR activado para reducir ruido?
- [ ] ¿Conversiones en modo sleep si muy crítico?

---

<!-- IA_CONTEXT
USO: Métodos prácticos para ADC y DAC
NIVEL: Intermedio (2/3)
HERRAMIENTAS: AVR-GCC, osciloscopio, multímetro
-->
