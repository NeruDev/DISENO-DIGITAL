# 🔧 Aplicación: Controlador de Motor PWM (MCU)

```
::METADATA::
tipo: aplicacion
tema: MCU-03-timers-interrupciones
dificultad: intermedia
objetivo: Control de velocidad de motor DC con PWM
::END::
```

## 📋 Descripción del Proyecto

Implementar un controlador de velocidad para motor DC usando PWM generado por Timer del microcontrolador.

## 🎯 Objetivos de Aprendizaje

- Configurar Timer en modo PWM
- Calcular frecuencia y duty cycle
- Manejar interrupciones para control
- Implementar rampa de aceleración

## 📝 Especificaciones

### Hardware
| Componente | Conexión |
|------------|----------|
| Motor DC | OC0A (PD6) a través de driver |
| Potenciómetro | ADC0 (PA0) |
| LED indicador | PB0 |
| Botón Start/Stop | INT0 (PD2) |

### Requisitos
- Frecuencia PWM: ~1 kHz (audiblemente silencioso)
- Duty cycle: 0-100% controlado por potenciómetro
- Aceleración suave: rampa de 0 a target en 2 segundos

## 🔍 Configuración del Timer

### Cálculo de Frecuencia PWM

```
f_PWM = f_clk / (N × 256)

Para ATmega328P @ 16 MHz:
f_PWM = 16,000,000 / (64 × 256) = 976.56 Hz ≈ 1 kHz

Prescaler N = 64 → CS02:00 = 011
```

### Registros de Configuración

```c
// Timer0 en modo Fast PWM
TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
//        Clear OC0A on Compare Match, set at BOTTOM
//        Fast PWM mode (TOP = 0xFF)

TCCR0B = (0 << WGM02) | (0 << CS02) | (1 << CS01) | (1 << CS00);
//        Fast PWM      Prescaler = 64

// Duty cycle inicial = 0%
OCR0A = 0;

// Habilitar salida PWM
DDRD |= (1 << PD6);
```

## 📝 Código de Implementación

### Inicialización

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t target_duty = 0;
volatile uint8_t current_duty = 0;
volatile uint8_t motor_enabled = 0;

void PWM_init(void) {
    // Configurar Timer0 Fast PWM
    TCCR0A = (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
    TCCR0B = (0 << CS02) | (1 << CS01) | (1 << CS00);
    OCR0A = 0;
    DDRD |= (1 << PD6);
}

void ADC_init(void) {
    // Referencia AVCC, canal ADC0
    ADMUX = (1 << REFS0);
    // Habilitar ADC, prescaler = 128 (125 kHz @ 16 MHz)
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t ADC_read(uint8_t channel) {
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    ADCSRA |= (1 << ADSC);          // Iniciar conversión
    while (ADCSRA & (1 << ADSC));   // Esperar fin
    return ADC;
}
```

### Control con Rampa

```c
// Timer1 para rampa de aceleración (100 Hz = cada 10 ms)
void Ramp_Timer_init(void) {
    // CTC mode, prescaler 256
    TCCR1B = (1 << WGM12) | (1 << CS12);
    OCR1A = 624;  // 16MHz / 256 / 100Hz - 1
    TIMSK1 = (1 << OCIE1A);
}

ISR(TIMER1_COMPA_vect) {
    // Rampa: incremento gradual cada 10 ms
    // 2 segundos = 200 pasos para 0-255
    // Incremento = 255/200 ≈ 1.28, usar 1 o 2 alternando
    
    if (motor_enabled) {
        if (current_duty < target_duty) {
            current_duty++;
        } else if (current_duty > target_duty) {
            current_duty--;
        }
    } else {
        if (current_duty > 0) {
            current_duty--;  // Desaceleración suave
        }
    }
    OCR0A = current_duty;
}
```

### Interrupción de Botón

```c
void Button_init(void) {
    DDRD &= ~(1 << PD2);     // PD2 como entrada
    PORTD |= (1 << PD2);     // Pull-up interno
    
    EICRA = (1 << ISC01);    // INT0 en flanco de bajada
    EIMSK = (1 << INT0);     // Habilitar INT0
}

ISR(INT0_vect) {
    // Toggle motor enable
    motor_enabled ^= 1;
    
    // Indicador LED
    if (motor_enabled) {
        PORTB |= (1 << PB0);
    } else {
        PORTB &= ~(1 << PB0);
    }
}
```

### Loop Principal

```c
int main(void) {
    // Inicializaciones
    PWM_init();
    ADC_init();
    Ramp_Timer_init();
    Button_init();
    
    DDRB |= (1 << PB0);  // LED como salida
    
    sei();  // Habilitar interrupciones globales
    
    while (1) {
        // Leer potenciómetro y escalar a 0-255
        uint16_t adc_value = ADC_read(0);
        target_duty = adc_value >> 2;  // 10 bits → 8 bits
        
        // Pequeño delay para estabilidad de lectura
        _delay_ms(50);
    }
    
    return 0;
}
```

## 📐 Diagrama de Conexiones

```
                 ATmega328P
              ┌─────────────┐
         ┌────┤PD6 (OC0A)   │
         │    │             │
         │    │PD2 (INT0)───┼──── Botón ────┐
         │    │             │               │
         │    │PA0 (ADC0)───┼──── POT ──────┤
         │    │             │               │
         │    │PB0 ─────────┼──── LED ──────┤
         │    │             │               │
         │    │VCC ─────────┼───────────────┴── +5V
         │    │GND ─────────┼─────────────────── GND
         │    └─────────────┘
         │
         ▼
    ┌─────────┐
    │ DRIVER  │
    │ (L293D) │────── Motor DC
    └─────────┘
```

## ✅ Criterios de Éxito

- [ ] PWM a ~1 kHz (motor silencioso)
- [ ] Duty cycle 0-100% desde potenciómetro
- [ ] Aceleración/desaceleración suave (2 seg)
- [ ] Botón Start/Stop funcional
- [ ] LED indica estado del motor

## 📚 Recursos Relacionados

- [MCU-03-Intro.md](../MCU-03-Intro.md)
- [GLOSSARY: pwm](../../../GLOSSARY/README.md#pwm)
- [GLOSSARY: timer](../../../GLOSSARY/README.md#timer)
- [GLOSSARY: interrupcion](../../../GLOSSARY/README.md#interrupcion)

---

> 💡 **Tip**: Usar rampa evita picos de corriente en el arranque del motor
