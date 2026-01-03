<!--
::METADATA::
type: method
topic_id: mcu-02-registros-puertos
file_id: metodos-gpio
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [microcontrolador, metodología, GPIO, puertos]
search_keywords: "metodología GPIO, puertos, entrada salida"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-02-Teoria-RegistrosPuertos.md) | [Problemas →](../problems/MCU-02-Problemas.md)

---

# Métodos: Registros y Puertos GPIO

## Método 1: Macros para Manipulación de Bits

### Definir Macros Reutilizables

```c
// Macros genéricas
#define BIT_SET(reg, bit)    ((reg) |= (1 << (bit)))
#define BIT_CLEAR(reg, bit)  ((reg) &= ~(1 << (bit)))
#define BIT_TOGGLE(reg, bit) ((reg) ^= (1 << (bit)))
#define BIT_READ(reg, bit)   (((reg) >> (bit)) & 1)
#define BIT_WRITE(reg, bit, val) \
    ((val) ? BIT_SET(reg, bit) : BIT_CLEAR(reg, bit))

// Uso
BIT_SET(PORTB, 3);       // PORTB bit 3 = 1
BIT_CLEAR(DDRB, 5);      // DDRB bit 5 = 0
if (BIT_READ(PINB, 2))   // Leer bit 2
```

---

## Método 2: Abstracción de Hardware (HAL)

### Capa de Abstracción Simple

```c
// gpio.h
typedef enum {
    PIN_INPUT,
    PIN_OUTPUT,
    PIN_INPUT_PULLUP
} pin_mode_t;

typedef enum {
    PIN_LOW = 0,
    PIN_HIGH = 1
} pin_state_t;

void gpio_set_mode(uint8_t port, uint8_t pin, pin_mode_t mode);
void gpio_write(uint8_t port, uint8_t pin, pin_state_t state);
pin_state_t gpio_read(uint8_t port, uint8_t pin);
void gpio_toggle(uint8_t port, uint8_t pin);
```

### Implementación AVR

```c
// gpio.c
#include <avr/io.h>
#include "gpio.h"

static volatile uint8_t* get_ddr(uint8_t port) {
    switch(port) {
        case 'B': return &DDRB;
        case 'C': return &DDRC;
        case 'D': return &DDRD;
        default: return NULL;
    }
}

void gpio_set_mode(uint8_t port, uint8_t pin, pin_mode_t mode) {
    volatile uint8_t *ddr = get_ddr(port);
    volatile uint8_t *portr = ddr + 1;  // PORT está después de DDR
    
    switch(mode) {
        case PIN_OUTPUT:
            *ddr |= (1 << pin);
            break;
        case PIN_INPUT:
            *ddr &= ~(1 << pin);
            *portr &= ~(1 << pin);
            break;
        case PIN_INPUT_PULLUP:
            *ddr &= ~(1 << pin);
            *portr |= (1 << pin);
            break;
    }
}
```

---

## Método 3: Debounce de Botón por Software

### Debounce Simple (Blocking)

```c
#define DEBOUNCE_TIME_MS 50

uint8_t button_debounced_read(void) {
    if (button_raw_read()) {
        _delay_ms(DEBOUNCE_TIME_MS);
        if (button_raw_read()) {
            return 1;  // Confirmado presionado
        }
    }
    return 0;
}
```

### Debounce No-Blocking

```c
#define DEBOUNCE_SAMPLES 10

typedef struct {
    uint8_t history;
    uint8_t state;
} debounce_t;

uint8_t debounce_update(debounce_t *db, uint8_t raw) {
    db->history = (db->history << 1) | raw;
    
    if (db->history == 0xFF) {
        db->state = 1;  // Estable en HIGH
    } else if (db->history == 0x00) {
        db->state = 0;  // Estable en LOW
    }
    // Si no es todo 1s o 0s, mantener estado anterior
    
    return db->state;
}

// Llamar desde timer cada 5-10 ms
```

---

## Método 4: Matriz de Teclado

### Escaneo de Matriz 4x4

```c
// Conexión:
// Filas (salidas): PB0-PB3
// Columnas (entradas con pull-up): PD0-PD3

#define ROWS 4
#define COLS 4

const char keymap[ROWS][COLS] = {
    {'1', '2', '3', 'A'},
    {'4', '5', '6', 'B'},
    {'7', '8', '9', 'C'},
    {'*', '0', '#', 'D'}
};

void keypad_init(void) {
    DDRB |= 0x0F;   // PB0-PB3 salidas
    DDRD &= 0xF0;   // PD0-PD3 entradas
    PORTD |= 0x0F;  // Pull-ups en columnas
}

char keypad_scan(void) {
    for (uint8_t row = 0; row < ROWS; row++) {
        // Activar una fila (LOW)
        PORTB = ~(1 << row) & 0x0F;
        _delay_us(10);  // Estabilización
        
        // Leer columnas
        uint8_t cols = ~PIND & 0x0F;
        
        for (uint8_t col = 0; col < COLS; col++) {
            if (cols & (1 << col)) {
                return keymap[row][col];
            }
        }
    }
    return 0;  // Ninguna tecla
}
```

---

## Método 5: Display de 7 Segmentos

### Control Directo

```c
// Segmentos en PORTB, dígitos en PORTD
//     a
//    ───
//   │   │ b
// f │ g │
//    ───
//   │   │ c
// e │   │
//    ───  • dp
//     d

const uint8_t digits[] = {
//  .gfedcba
    0b00111111,  // 0
    0b00000110,  // 1
    0b01011011,  // 2
    0b01001111,  // 3
    0b01100110,  // 4
    0b01101101,  // 5
    0b01111101,  // 6
    0b00000111,  // 7
    0b01111111,  // 8
    0b01101111   // 9
};

void display_digit(uint8_t pos, uint8_t value) {
    PORTD = ~(1 << pos);      // Activar dígito (ánodo común)
    PORTB = digits[value];     // Mostrar segmentos
}

// Multiplexar en ISR de timer (~1 kHz)
volatile uint8_t display_buffer[4];
volatile uint8_t current_digit = 0;

ISR(TIMER0_COMPA_vect) {
    display_digit(current_digit, display_buffer[current_digit]);
    current_digit = (current_digit + 1) % 4;
}
```

---

## Método 6: Lectura Analógica con GPIO Digital

### Técnica RC para Medir Resistencia

```c
// Pin conectado a RC: R + capacitor a GND

uint16_t measure_rc_time(void) {
    uint16_t count = 0;
    
    // 1. Descargar capacitor
    DDRB |= (1 << PB0);   // Salida
    PORTB &= ~(1 << PB0); // LOW
    _delay_ms(1);
    
    // 2. Cambiar a entrada y medir tiempo de carga
    DDRB &= ~(1 << PB0);  // Entrada
    PORTB |= (1 << PB0);  // Pull-up (carga el capacitor)
    
    // 3. Contar hasta que llegue a HIGH
    while (!(PINB & (1 << PB0)) && count < 65535) {
        count++;
    }
    
    return count;  // Proporcional a R
}
```

---

## Método 7: Protección de Pines

### Verificación de Dirección

```c
// Macro segura que verifica antes de escribir
#define SAFE_OUTPUT(port, ddr, pin, val) do { \
    if ((ddr) & (1 << (pin))) { \
        if (val) (port) |= (1 << (pin)); \
        else (port) &= ~(1 << (pin)); \
    } \
} while(0)

// Uso
SAFE_OUTPUT(PORTB, DDRB, PB0, 1);  // Solo escribe si es salida
```

### Configuración Inicial Defensiva

```c
void gpio_safe_init(void) {
    // Todos los pines como entrada con pull-up
    DDRB = 0x00;
    DDRC = 0x00;
    DDRD = 0x00;
    PORTB = 0xFF;
    PORTC = 0xFF;
    PORTD = 0xFF;
    
    // Luego configurar específicos
}
```

---

## Método 8: Simulación de Bus I/O

### Bus de 8 Bits Bidireccional

```c
// Bus en PORTC, señales de control en PORTB
#define DATA_PORT PORTC
#define DATA_DDR  DDRC
#define DATA_PIN  PINC

#define CTRL_PORT PORTB
#define RD_PIN    PB0
#define WR_PIN    PB1
#define CS_PIN    PB2

void bus_write(uint8_t data) {
    DATA_DDR = 0xFF;        // Bus como salida
    DATA_PORT = data;
    
    CTRL_PORT &= ~(1 << CS_PIN);  // CS activo
    CTRL_PORT &= ~(1 << WR_PIN);  // WR activo
    _delay_us(1);
    CTRL_PORT |= (1 << WR_PIN);   // WR inactivo
    CTRL_PORT |= (1 << CS_PIN);   // CS inactivo
}

uint8_t bus_read(void) {
    DATA_DDR = 0x00;        // Bus como entrada
    
    CTRL_PORT &= ~(1 << CS_PIN);  // CS activo
    CTRL_PORT &= ~(1 << RD_PIN);  // RD activo
    _delay_us(1);
    uint8_t data = DATA_PIN;
    CTRL_PORT |= (1 << RD_PIN);   // RD inactivo
    CTRL_PORT |= (1 << CS_PIN);   // CS inactivo
    
    return data;
}
```

---

## Método 9: Interrupciones Externas

### Configuración de INT0 (AVR)

```c
#include <avr/interrupt.h>

void ext_int_init(void) {
    // PD2 (INT0) como entrada con pull-up
    DDRD &= ~(1 << PD2);
    PORTD |= (1 << PD2);
    
    // Configurar flanco de bajada
    EICRA |= (1 << ISC01);   // ISC01=1, ISC00=0: falling edge
    EICRA &= ~(1 << ISC00);
    
    // Habilitar INT0
    EIMSK |= (1 << INT0);
    
    // Habilitar interrupciones globales
    sei();
}

ISR(INT0_vect) {
    // Código de la interrupción
    // Mantener breve
}
```

### Pin Change Interrupt (PCINT)

```c
void pcint_init(void) {
    // Habilitar PCINT0 (PB0)
    PCICR |= (1 << PCIE0);   // Habilitar grupo PCINT0-7
    PCMSK0 |= (1 << PCINT0); // Habilitar PCINT0 específico
    
    sei();
}

ISR(PCINT0_vect) {
    // Se ejecuta en cualquier cambio de PB0
    static uint8_t last_state = 0;
    uint8_t current = PINB & (1 << PB0);
    
    if (current && !last_state) {
        // Flanco de subida
    } else if (!current && last_state) {
        // Flanco de bajada
    }
    
    last_state = current;
}
```

---

## Método 10: Driver de LED RGB con PWM Software

```c
// LEDs en PB0 (R), PB1 (G), PB2 (B)
volatile uint8_t pwm_r = 0, pwm_g = 0, pwm_b = 0;
volatile uint8_t pwm_counter = 0;

void rgb_init(void) {
    DDRB |= (1 << PB0) | (1 << PB1) | (1 << PB2);
    
    // Timer para PWM software (~1 kHz * 256 = 256 kHz)
    TCCR0A = (1 << WGM01);  // CTC mode
    TCCR0B = (1 << CS00);   // No prescaler
    OCR0A = 62;             // ~256 kHz con 16 MHz
    TIMSK0 = (1 << OCIE0A);
    
    sei();
}

ISR(TIMER0_COMPA_vect) {
    pwm_counter++;
    
    if (pwm_counter < pwm_r) PORTB |= (1 << PB0);
    else PORTB &= ~(1 << PB0);
    
    if (pwm_counter < pwm_g) PORTB |= (1 << PB1);
    else PORTB &= ~(1 << PB1);
    
    if (pwm_counter < pwm_b) PORTB |= (1 << PB2);
    else PORTB &= ~(1 << PB2);
}

void rgb_set(uint8_t r, uint8_t g, uint8_t b) {
    pwm_r = r;
    pwm_g = g;
    pwm_b = b;
}
```

---

## Método 11: Checklist de Configuración GPIO

### Antes de Usar un Pin

- [ ] ¿Está configurada la dirección (DDR/TRIS/MODER)?
- [ ] ¿Necesita pull-up/pull-down?
- [ ] ¿Corriente de salida es suficiente para la carga?
- [ ] ¿El pin tiene función alternativa que interfiere?
- [ ] ¿Hay protección contra ESD?
- [ ] ¿La entrada necesita debounce?

### Verificación de Hardware

```c
// Test simple de GPIO
void gpio_test(void) {
    // Toggle visual para verificar conexiones
    while(1) {
        PORTB ^= 0xFF;
        _delay_ms(500);
    }
}
```

---

<!-- IA_CONTEXT
USO: Métodos prácticos para GPIO y puertos
NIVEL: Básico (1/3)
HERRAMIENTAS: AVR-GCC, STM32CubeIDE
-->
