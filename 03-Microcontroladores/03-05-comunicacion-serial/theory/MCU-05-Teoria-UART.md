<!--
::METADATA::
type: theory
topic_id: mcu-05-comunicacion-serial
file_id: teoria-uart
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, UART, serial, RS232, comunicación]
search_keywords: "UART, serial, RS232, comunicación, baud rate"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-05-Intro.md) | [Métodos →](../methods/MCU-05-Metodos-UART.md)

---

# Comunicación Serial (UART)

## 1. Introducción a la Comunicación Serial

### 1.1 ¿Qué es UART?

**UART** = Universal Asynchronous Receiver/Transmitter

Características:
- Comunicación **asíncrona** (sin reloj compartido)
- **Full duplex** (TX y RX simultáneos)
- Solo necesita **2 cables** (TX, RX)
- Estándar de facto para debugging

### 1.2 Conexión Básica

```
  MCU A                           MCU B
┌────────┐                    ┌────────┐
│        │ TX ──────────── RX │        │
│        │ RX ──────────── TX │        │
│        │ GND ────────── GND │        │
└────────┘                    └────────┘

Nota: TX de uno conecta a RX del otro (cruzado)
```

---

## 2. Formato de Trama UART

### 2.1 Estructura

```
     ┌─────┬───┬───┬───┬───┬───┬───┬───┬───┬─────┬─────┐
     │Start│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │Parity│Stop │
     │ Bit │   │   │   │   │   │   │   │   │(opt) │Bit(s)│
     └─────┴───┴───┴───┴───┴───┴───┴───┴───┴─────┴─────┘
       │                                           │
     ┌─┘                                           └─┐
     │                                               │
IDLE ───┐   ┌───┐   ┌───────┐   ┌───┐   ┌───────────────
(HIGH)  │   │   │   │       │   │   │   │  IDLE (HIGH)
        └───┘   └───┘       └───┘   └───┘
        START   D0  D1  ... D7  PARITY  STOP
```

### 2.2 Componentes de la Trama

| Componente | Bits | Descripción |
|------------|------|-------------|
| Start | 1 | Siempre 0 (LOW), indica inicio |
| Data | 5-9 | Generalmente 8 bits |
| Parity | 0-1 | Detección de errores (opcional) |
| Stop | 1-2 | Siempre 1 (HIGH), indica fin |

### 2.3 Configuración Típica

**8N1** = 8 bits de datos, No paridad, 1 bit de stop

```
Total bits por byte = 1 + 8 + 0 + 1 = 10 bits
```

---

## 3. Baud Rate

### 3.1 ¿Qué es Baud Rate?

Velocidad de transmisión en **símbolos por segundo**.

Para UART (2 niveles), **baud = bits/segundo**.

### 3.2 Baud Rates Comunes

| Baud Rate | Uso Típico |
|-----------|------------|
| 9600 | Default, muy común |
| 19200 | Moderadamente rápido |
| 38400 | GPS, módulos |
| 57600 | Rápido |
| 115200 | Muy rápido, moderno |
| 230400+ | Alta velocidad |

### 3.3 Cálculo del Período de Bit

$$T_{bit} = \frac{1}{Baud Rate}$$

Para 9600 baud:
$$T_{bit} = \frac{1}{9600} = 104.17 \mu s$$

### 3.4 Tiempo de Transmisión por Byte

$$T_{byte} = \frac{Bits_{total}}{Baud Rate}$$

Para 8N1 a 9600:
$$T_{byte} = \frac{10}{9600} = 1.04 ms$$

---

## 4. Paridad

### 4.1 Tipos de Paridad

| Tipo | Descripción |
|------|-------------|
| None | Sin bit de paridad |
| Even | Total de 1s debe ser par |
| Odd | Total de 1s debe ser impar |

### 4.2 Ejemplo de Paridad Par

```
Dato: 0b01001011 (5 unos → impar)
Paridad par: 1 (para hacer 6 unos → par)

Dato: 0b01001010 (4 unos → par)
Paridad par: 0 (mantiene 4 unos → par)
```

### 4.3 Limitaciones

- Solo detecta errores de 1 bit
- No corrige errores
- Añade overhead (10% más)

---

## 5. UART en AVR (ATmega328P)

### 5.1 Registros USART

| Registro | Función |
|----------|---------|
| UDR0 | Buffer de datos (TX/RX) |
| UCSR0A | Status (flags) |
| UCSR0B | Control (habilitar TX/RX, interrupciones) |
| UCSR0C | Formato de trama |
| UBRR0H/L | Baud rate (16 bits) |

### 5.2 Cálculo de UBRR

Para modo normal (U2X = 0):
$$UBRR = \frac{F_{CPU}}{16 \times Baud} - 1$$

Para modo doble velocidad (U2X = 1):
$$UBRR = \frac{F_{CPU}}{8 \times Baud} - 1$$

### 5.3 Tabla UBRR (16 MHz)

| Baud | UBRR (U2X=0) | Error |
|------|--------------|-------|
| 9600 | 103 | 0.2% |
| 19200 | 51 | 0.2% |
| 38400 | 25 | 0.2% |
| 57600 | 16 | 2.1% |
| 115200 | 8 | -3.5% |

*Error > 2% puede causar problemas*

---

## 6. Configuración UART

### 6.1 Inicialización Básica

```c
#define F_CPU 16000000UL
#define BAUD 9600
#define UBRR_VALUE ((F_CPU / 16 / BAUD) - 1)

void uart_init(void) {
    // Configurar baud rate
    UBRR0H = (UBRR_VALUE >> 8);
    UBRR0L = UBRR_VALUE;
    
    // Habilitar TX y RX
    UCSR0B = (1 << TXEN0) | (1 << RXEN0);
    
    // Formato: 8N1
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}
```

### 6.2 Transmisión

```c
void uart_transmit(uint8_t data) {
    // Esperar buffer vacío
    while (!(UCSR0A & (1 << UDRE0)));
    
    // Enviar dato
    UDR0 = data;
}

void uart_print(const char *str) {
    while (*str) {
        uart_transmit(*str++);
    }
}
```

### 6.3 Recepción

```c
uint8_t uart_receive(void) {
    // Esperar dato
    while (!(UCSR0A & (1 << RXC0)));
    
    return UDR0;
}

// No bloqueante
uint8_t uart_available(void) {
    return (UCSR0A & (1 << RXC0)) ? 1 : 0;
}
```

---

## 7. Interrupciones UART

### 7.1 Tipos de Interrupciones

| Interrupción | Flag | Cuándo |
|--------------|------|--------|
| RX Complete | RXC0 | Dato recibido |
| TX Complete | TXC0 | Transmisión terminada |
| Data Register Empty | UDRE0 | Buffer TX vacío |

### 7.2 Recepción con Interrupción

```c
#define RX_BUFFER_SIZE 64
volatile uint8_t rx_buffer[RX_BUFFER_SIZE];
volatile uint8_t rx_head = 0;
volatile uint8_t rx_tail = 0;

void uart_init_interrupt(void) {
    // ... configuración básica ...
    
    // Habilitar interrupción RX
    UCSR0B |= (1 << RXCIE0);
    sei();
}

ISR(USART_RX_vect) {
    uint8_t data = UDR0;
    uint8_t next = (rx_head + 1) % RX_BUFFER_SIZE;
    
    if (next != rx_tail) {  // Buffer no lleno
        rx_buffer[rx_head] = data;
        rx_head = next;
    }
}

uint8_t uart_read(void) {
    while (rx_head == rx_tail);  // Esperar dato
    
    uint8_t data = rx_buffer[rx_tail];
    rx_tail = (rx_tail + 1) % RX_BUFFER_SIZE;
    return data;
}
```

---

## 8. Errores de Comunicación

### 8.1 Tipos de Errores

| Error | Causa | Flag |
|-------|-------|------|
| Frame | Stop bit incorrecto | FE0 |
| Overrun | Dato no leído a tiempo | DOR0 |
| Parity | Error de paridad | UPE0 |

### 8.2 Verificación de Errores

```c
uint8_t uart_receive_safe(uint8_t *data) {
    // Esperar dato
    while (!(UCSR0A & (1 << RXC0)));
    
    // Verificar errores antes de leer
    uint8_t status = UCSR0A;
    *data = UDR0;  // Siempre leer para limpiar
    
    if (status & ((1 << FE0) | (1 << DOR0) | (1 << UPE0))) {
        return 0;  // Error
    }
    return 1;  // OK
}
```

---

## 9. RS-232 vs TTL

### 9.1 Niveles de Voltaje

| Nivel | TTL/CMOS | RS-232 |
|-------|----------|--------|
| HIGH (1) | 3.3-5V | -3 a -15V |
| LOW (0) | 0V | +3 a +15V |

### 9.2 Conexión a PC

```
  MCU (TTL)          MAX232          PC (RS-232)
┌────────┐        ┌────────┐        ┌────────┐
│  TX  ──┼───────▶│T1IN    │        │        │
│        │        │   T1OUT│───────▶│ RX     │
│  RX  ◀─┼────────│R1OUT   │        │        │
│        │        │   R1IN │◀───────│ TX     │
│  GND ──┼────────│GND     │────────│ GND    │
└────────┘        └────────┘        └────────┘
```

### 9.3 USB-Serial

Hoy en día, más común usar convertidores USB:
- CH340
- FT232
- CP2102

Conexión directa MCU TTL ↔ Adaptador USB-Serial

---

## 10. Ejemplo Completo: Terminal Serial

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>

#define F_CPU 16000000UL
#define BAUD 9600

// Buffer circular
#define BUFFER_SIZE 64
volatile char rx_buf[BUFFER_SIZE];
volatile uint8_t rx_in = 0, rx_out = 0;

void uart_init(void) {
    UBRR0H = ((F_CPU/16/BAUD) - 1) >> 8;
    UBRR0L = (F_CPU/16/BAUD) - 1;
    UCSR0B = (1 << RXEN0) | (1 << TXEN0) | (1 << RXCIE0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
    sei();
}

void uart_putc(char c) {
    while (!(UCSR0A & (1 << UDRE0)));
    UDR0 = c;
}

void uart_puts(const char *s) {
    while (*s) uart_putc(*s++);
}

ISR(USART_RX_vect) {
    char c = UDR0;
    uint8_t next = (rx_in + 1) % BUFFER_SIZE;
    if (next != rx_out) {
        rx_buf[rx_in] = c;
        rx_in = next;
    }
}

uint8_t uart_available(void) {
    return rx_in != rx_out;
}

char uart_getc(void) {
    while (!uart_available());
    char c = rx_buf[rx_out];
    rx_out = (rx_out + 1) % BUFFER_SIZE;
    return c;
}

int main(void) {
    uart_init();
    uart_puts("Terminal Ready\r\n");
    
    while (1) {
        if (uart_available()) {
            char c = uart_getc();
            uart_putc(c);  // Echo
            
            if (c == '\r') {
                uart_putc('\n');
            }
        }
    }
}
```

---

## Referencias

- ATmega328P Datasheet - USART
- RS-232 Standard
- AN-758: Software UART Using Timers

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 03-01, 03-02, 03-03
CONEXIONES: Debugging, comunicación con PC, módulos (GPS, Bluetooth)
ERRORES_COMUNES: Baud rate incorrecto, TX-RX no cruzados, niveles incompatibles
-->
