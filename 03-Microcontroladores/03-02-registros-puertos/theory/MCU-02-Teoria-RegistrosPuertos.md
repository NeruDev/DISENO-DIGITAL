<!--
::METADATA::
type: theory
topic_id: mcu-02-registros-puertos
file_id: teoria-registros-puertos
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [microcontrolador, GPIO, registros, puertos, entrada/salida]
search_keywords: "GPIO, registros, puertos, DDR, PORT, PIN"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-02-Intro.md) | [Métodos →](../methods/MCU-02-Metodos-GPIO.md)

---

# Registros y Puertos GPIO

## 1. Introducción a GPIO

### 1.1 ¿Qué es GPIO?

**GPIO (General Purpose Input/Output)** son pines del microcontrolador que pueden configurarse como:
- **Entrada:** Leer señales externas
- **Salida:** Enviar señales al exterior

### 1.2 Estructura de un Puerto

```
                 MCU
    ┌─────────────────────────────┐
    │                             │
    │  ┌───────────────────────┐  │
    │  │    Registros GPIO     │  │
    │  │  ┌─────┬─────┬─────┐  │  │
    │  │  │ DDR │ PORT│ PIN │  │  │
    │  │  └──┬──┴──┬──┴──┬──┘  │  │
    │  └─────┼─────┼─────┼─────┘  │
    │        │     │     │        │
    │        ▼     ▼     ▼        │
    │     ┌─────────────────┐     │
    │     │  Lógica de Pin  │     │
    │     └────────┬────────┘     │
    └──────────────┼──────────────┘
                   │
                   ▼
              Pin Físico
                 PA0
```

---

## 2. Registros de Control GPIO

### 2.1 AVR (ATmega)

Cada puerto tiene 3 registros de 8 bits:

| Registro | Nombre | Función |
|----------|--------|---------|
| DDRx | Data Direction Register | Configura dirección (0=entrada, 1=salida) |
| PORTx | Port Output Register | Valor de salida o pullup |
| PINx | Port Input Register | Lee estado del pin |

```
Ejemplo Puerto B (ATmega328):
DDRB  = 0b00001111  // PB0-PB3 salidas, PB4-PB7 entradas
PORTB = 0b11110001  // PB0 HIGH, PB4-PB7 pullup activado
valor = PINB        // Leer estado actual
```

### 2.2 ARM Cortex-M (STM32)

Cada puerto tiene múltiples registros de 32 bits:

| Registro | Función |
|----------|---------|
| GPIOx_MODER | Modo (entrada, salida, alterno, analógico) |
| GPIOx_OTYPER | Tipo de salida (push-pull, open-drain) |
| GPIOx_OSPEEDR | Velocidad de salida |
| GPIOx_PUPDR | Pull-up/pull-down |
| GPIOx_IDR | Datos de entrada (lectura) |
| GPIOx_ODR | Datos de salida (escritura) |
| GPIOx_BSRR | Set/Reset atómico |

### 2.3 PIC

| Registro | Función |
|----------|---------|
| TRISx | Dirección (0=salida, 1=entrada) |
| PORTx | Lectura de pin |
| LATx | Escritura de salida |

---

## 3. Configuración de Dirección

### 3.1 Pin como Salida

**AVR:**
```c
// PB0 como salida
DDRB |= (1 << PB0);    // Set bit 0 de DDRB
```

**STM32:**
```c
// PA5 como salida push-pull
GPIOA->MODER &= ~(3 << (5*2));  // Limpiar bits
GPIOA->MODER |= (1 << (5*2));   // Modo salida
```

**PIC:**
```c
// RB0 como salida
TRISBbits.TRISB0 = 0;
```

### 3.2 Pin como Entrada

**AVR:**
```c
// PB0 como entrada
DDRB &= ~(1 << PB0);   // Clear bit 0 de DDRB

// Con pull-up interno
PORTB |= (1 << PB0);   // Activar pull-up
```

**STM32:**
```c
// PA5 como entrada con pull-up
GPIOA->MODER &= ~(3 << (5*2));  // Modo entrada (00)
GPIOA->PUPDR &= ~(3 << (5*2));
GPIOA->PUPDR |= (1 << (5*2));   // Pull-up
```

---

## 4. Escritura de Salidas

### 4.1 Métodos de Escritura

```c
// AVR - Escribir puerto completo
PORTB = 0xFF;          // Todos HIGH

// Escribir un bit (set)
PORTB |= (1 << PB0);   // PB0 = HIGH

// Escribir un bit (clear)
PORTB &= ~(1 << PB0);  // PB0 = LOW

// Toggle un bit
PORTB ^= (1 << PB0);   // Invertir PB0
```

### 4.2 Operaciones Atómicas (STM32)

```c
// Set PA5 (atómico, sin read-modify-write)
GPIOA->BSRR = (1 << 5);

// Reset PA5 (atómico)
GPIOA->BSRR = (1 << (5 + 16));

// O usando BRR
GPIOA->BRR = (1 << 5);
```

### 4.3 Problema Read-Modify-Write

```c
// PELIGRO en interrupciones:
// Interrupción puede ocurrir entre lectura y escritura
PORTB |= (1 << PB0);  // 1. Lee PORTB
                       // 2. OR con máscara
                       // 3. Escribe PORTB

// SOLUCIÓN AVR: usar PINx para toggle (atómico)
PINB = (1 << PB0);    // Toggle atómico
```

---

## 5. Lectura de Entradas

### 5.1 Lectura Simple

```c
// AVR
uint8_t estado = PINB;           // Leer puerto completo
uint8_t bit0 = (PINB & (1 << PB0)) ? 1 : 0;  // Leer un bit

// STM32
uint32_t estado = GPIOA->IDR;
uint8_t bit5 = (GPIOA->IDR & (1 << 5)) ? 1 : 0;

// PIC
uint8_t estado = PORTB;
uint8_t bit0 = PORTBbits.RB0;
```

### 5.2 Detección de Cambio

```c
// Detectar flanco de subida
uint8_t anterior = 0;
uint8_t actual;

while(1) {
    actual = PINB & (1 << PB0);
    
    if (actual && !anterior) {
        // Flanco de subida detectado
        hacer_algo();
    }
    
    anterior = actual;
}
```

---

## 6. Pull-up y Pull-down

### 6.1 ¿Por Qué Son Necesarios?

Sin resistencia de pull-up/down, una entrada no conectada queda "flotante" con valor indefinido.

```
Pull-up interno:
      VCC
       │
      [R] ← Resistencia interna (~20-50kΩ)
       │
       ├──── Pin
       │
     [SW] ← Botón
       │
      GND

Estado: HIGH cuando abierto, LOW cuando presionado
```

### 6.2 Configuración

**AVR:**
```c
DDRB &= ~(1 << PB0);   // Entrada
PORTB |= (1 << PB0);   // Pull-up ON

// Para desactivar pull-up
PORTB &= ~(1 << PB0);  // Pull-up OFF
```

**STM32:**
```c
// Pull-up
GPIOA->PUPDR |= (1 << (5*2));

// Pull-down
GPIOA->PUPDR |= (2 << (5*2));

// Sin pull (flotante)
GPIOA->PUPDR &= ~(3 << (5*2));
```

---

## 7. Funciones Alternativas

### 7.1 Multiplexación de Pines

Los pines pueden tener múltiples funciones:

```
Pin PA9 (STM32):
├── GPIO
├── USART1_TX
├── TIM1_CH2
└── I2C1_SCL

Solo una función activa a la vez.
```

### 7.2 Configuración de Función Alternativa

**AVR (automático):**
Los periféricos toman control del pin automáticamente al habilitarlos.

**STM32:**
```c
// PA9 como USART1_TX (AF7)
GPIOA->MODER |= (2 << (9*2));     // Modo alterno
GPIOA->AFR[1] |= (7 << ((9-8)*4)); // AF7 para PA9
```

---

## 8. Características Eléctricas

### 8.1 Niveles Lógicos

| MCU | VIL (max) | VIH (min) | VOL (max) | VOH (min) |
|-----|-----------|-----------|-----------|-----------|
| AVR 5V | 0.3×VCC | 0.6×VCC | 0.7V | VCC-0.7V |
| STM32 3.3V | 0.3×VCC | 0.7×VCC | 0.4V | VCC-0.4V |

### 8.2 Corriente de Salida

| MCU | IOL (sink) | IOH (source) |
|-----|------------|--------------|
| ATmega328 | 20 mA | 20 mA |
| STM32F1 | 25 mA | 25 mA |

**Límite por puerto:** Típicamente 100-200 mA total.

### 8.3 Tipos de Salida

```
Push-Pull:
VCC ─┬─ [PMOS] ─┐
     │          ├─ Pin ─ Carga ─ GND
GND ─┴─ [NMOS] ─┘

- Puede conducir HIGH o LOW
- Más común

Open-Drain:
          ┌─ Pin ─ Rext ─ VCC
GND ─ [NMOS] ─┘

- Solo puede hundir corriente (LOW)
- Para buses compartidos (I2C)
```

---

## 9. Ejemplos Prácticos

### 9.1 LED en Salida

```c
// AVR: LED en PB5 (Arduino pin 13)
#define LED_PIN PB5

void led_init(void) {
    DDRB |= (1 << LED_PIN);   // Salida
}

void led_on(void) {
    PORTB |= (1 << LED_PIN);
}

void led_off(void) {
    PORTB &= ~(1 << LED_PIN);
}

void led_toggle(void) {
    PINB = (1 << LED_PIN);    // Toggle atómico
}
```

### 9.2 Botón en Entrada

```c
// AVR: Botón en PD2 con pull-up
#define BUTTON_PIN PD2

void button_init(void) {
    DDRD &= ~(1 << BUTTON_PIN);  // Entrada
    PORTD |= (1 << BUTTON_PIN);  // Pull-up
}

uint8_t button_pressed(void) {
    return !(PIND & (1 << BUTTON_PIN));  // Activo bajo
}
```

### 9.3 Lectura de DIP Switch

```c
// 4 switches en PC0-PC3
void dipsw_init(void) {
    DDRC &= 0xF0;    // PC0-PC3 entradas
    PORTC |= 0x0F;   // Pull-ups
}

uint8_t dipsw_read(void) {
    return (~PINC) & 0x0F;  // Invertir (activo bajo)
}
```

---

## 10. Acceso a Registros con Estructuras (C)

### 10.1 Acceso Directo (AVR)

```c
// Definido en <avr/io.h>
#define PORTB (*(volatile uint8_t *)0x25)
#define DDRB  (*(volatile uint8_t *)0x24)
#define PINB  (*(volatile uint8_t *)0x23)
```

### 10.2 Estructura de Registros (STM32)

```c
typedef struct {
    volatile uint32_t MODER;
    volatile uint32_t OTYPER;
    volatile uint32_t OSPEEDR;
    volatile uint32_t PUPDR;
    volatile uint32_t IDR;
    volatile uint32_t ODR;
    volatile uint32_t BSRR;
    volatile uint32_t LCKR;
    volatile uint32_t AFR[2];
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef *)0x40020000)
```

---

## Referencias

- Datasheets de ATmega328P, STM32F103
- AVR Libc Reference Manual
- STM32 Reference Manual (RM0008)

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: 03-01 Arquitectura MCU
CONEXIONES: Base para todos los periféricos
ERRORES_COMUNES: Olvidar configurar dirección, no usar pull-up, read-modify-write en ISR
-->
