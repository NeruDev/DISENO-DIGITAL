<!--
::METADATA::
type: solution
topic_id: mcu-05-comunicacion-serial
file_id: respuestas-uart
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, microcontrolador, UART, serial]
search_keywords: "respuestas, soluciones, UART, serial"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-05-Problemas.md)

---

# Respuestas: Comunicación Serial (UART)

## Nivel 1: Conceptos Básicos

### Respuesta 1.1

**UART** = Universal Asynchronous Receiver/Transmitter

Características:
- Comunicación asíncrona (sin reloj)
- Full duplex (TX y RX simultáneos)
- Requiere solo 2 cables + GND
- Velocidad definida por baud rate
- Formato configurable (bits, paridad, stop)

### Respuesta 1.2

Conexión cruzada:
```
MCU A          MCU B
 TX ─────────── RX
 RX ─────────── TX
GND ─────────── GND
```

TX de un dispositivo conecta a RX del otro.

### Respuesta 1.3

8N1 significa:
- **8**: 8 bits de datos
- **N**: No paridad (None)
- **1**: 1 bit de stop

Total: 1(start) + 8(data) + 0(parity) + 1(stop) = 10 bits por byte

---

## Nivel 2: Cálculos de Baud Rate

### Respuesta 2.1

$$UBRR = \frac{F_{CPU}}{16 \times Baud} - 1 = \frac{16000000}{16 \times 9600} - 1 = 103.17$$

UBRR = 103

Verificación:
$$Baud_{real} = \frac{16000000}{16 \times (103 + 1)} = 9615.38$$
$$Error = \frac{9615.38 - 9600}{9600} \times 100\% = 0.16\%$$

### Respuesta 2.2

Con 8N1: 10 bits por byte

$$T_{byte} = \frac{10}{115200} = 86.8 \mu s$$

### Respuesta 2.3

$$UBRR = \frac{8000000}{16 \times 9600} - 1 = 51.08 \approx 51$$

$$Baud_{real} = \frac{8000000}{16 \times 52} = 9615.38$$

$$Error = 0.16\%$$ (aceptable, < 2%)

---

## Nivel 3: Formato de Trama

### Respuesta 3.1

'A' = 65 = 0x41 = 0b01000001

```
IDLE ───┐   ┌───┐       ┌───────┐   ┌───────────
(HIGH)  │   │   │       │       │   │  IDLE
        └───┘   └───────┘       └───┘
        START D0  D1  D2  D3  D4  D5  D6  D7  STOP
          0   1   0   0   0   0   0   1   0    1

Orden de bits: LSB primero
D0=1, D1=0, D2=0, D3=0, D4=0, D5=0, D6=1, D7=0
```

### Respuesta 3.2

Dato: 0b10110101 tiene 5 unos (impar)
Paridad par: 1 (para hacer 6 unos = par)

### Respuesta 3.3

Trama: 0-1-0-0-0-0-0-1-0-1
- Start: 0
- Datos: 10000010 (LSB first) = 0x41 = 'A'
- Paridad: 0
- Stop: 1

'A' tiene 2 unos, paridad par debería ser 0. ✓ No hay error.

---

## Nivel 4: Configuración Básica

### Respuesta 4.1

```c
#define F_CPU 16000000UL
#define BAUD 9600
#define UBRR_VAL ((F_CPU / 16 / BAUD) - 1)

void uart_init(void) {
    // Baud rate
    UBRR0H = (UBRR_VAL >> 8);
    UBRR0L = UBRR_VAL;
    
    // Habilitar TX y RX
    UCSR0B = (1 << TXEN0) | (1 << RXEN0);
    
    // 8 bits, no paridad, 1 stop
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}
```

### Respuesta 4.2

```c
void uart_transmit(uint8_t data) {
    // Esperar buffer vacío (UDRE = 1)
    while (!(UCSR0A & (1 << UDRE0)));
    
    // Enviar dato
    UDR0 = data;
}
```

### Respuesta 4.3

```c
uint8_t uart_receive(void) {
    // Esperar dato (RXC = 1)
    while (!(UCSR0A & (1 << RXC0)));
    
    // Retornar dato
    return UDR0;
}
```

---

## Nivel 5: Transmisión de Cadenas

### Respuesta 5.1

```c
void uart_puts(const char *str) {
    while (*str) {
        uart_transmit(*str++);
    }
}

// Con newline
void uart_println(const char *str) {
    uart_puts(str);
    uart_transmit('\r');
    uart_transmit('\n');
}
```

### Respuesta 5.2

```c
void uart_print_number(int16_t num) {
    char buf[7];  // -32768 + null
    int8_t i = 0;
    uint8_t neg = 0;
    
    if (num < 0) {
        neg = 1;
        num = -num;
    }
    
    if (num == 0) {
        uart_transmit('0');
        return;
    }
    
    while (num > 0) {
        buf[i++] = '0' + (num % 10);
        num /= 10;
    }
    
    if (neg) uart_transmit('-');
    
    while (i > 0) {
        uart_transmit(buf[--i]);
    }
}
```

### Respuesta 5.3

```c
void uart_print_hex(uint16_t num) {
    uart_transmit('0');
    uart_transmit('x');
    
    for (int8_t i = 3; i >= 0; i--) {
        uint8_t nibble = (num >> (i * 4)) & 0x0F;
        if (nibble < 10) {
            uart_transmit('0' + nibble);
        } else {
            uart_transmit('A' + nibble - 10);
        }
    }
}
```

---

## Nivel 6: Recepción con Buffer

### Respuesta 6.1

Razones para buffer circular:
1. ISR debe ser rápida, solo guarda dato
2. Datos llegan en cualquier momento
3. main() puede estar ocupado
4. Evita perder datos (overrun)
5. Permite procesar múltiples bytes

### Respuesta 6.2

```c
#define RX_BUFFER_SIZE 64

volatile uint8_t rx_buffer[RX_BUFFER_SIZE];
volatile uint8_t rx_head = 0;  // Donde escribe ISR
volatile uint8_t rx_tail = 0;  // Donde lee main

ISR(USART_RX_vect) {
    uint8_t data = UDR0;
    uint8_t next = (rx_head + 1) % RX_BUFFER_SIZE;
    
    // Solo guardar si hay espacio
    if (next != rx_tail) {
        rx_buffer[rx_head] = data;
        rx_head = next;
    }
}

void uart_init_int(void) {
    // ... config normal ...
    UCSR0B |= (1 << RXCIE0);  // Habilitar int RX
    sei();
}
```

### Respuesta 6.3

```c
uint8_t uart_available(void) {
    return (rx_head != rx_tail);
}

// También puede retornar cantidad:
uint8_t uart_count(void) {
    return (rx_head - rx_tail + RX_BUFFER_SIZE) % RX_BUFFER_SIZE;
}

char uart_getc(void) {
    // No bloqueante, verificar uart_available() antes
    char c = rx_buffer[rx_tail];
    rx_tail = (rx_tail + 1) % RX_BUFFER_SIZE;
    return c;
}

// Versión bloqueante
char uart_getc_blocking(void) {
    while (!uart_available());
    return uart_getc();
}
```

---

## Nivel 7: Manejo de Errores

### Respuesta 7.1

| Error | Flag | Causa |
|-------|------|-------|
| Frame Error (FE) | FE0 | Stop bit no es 1, baud incorrecto |
| Data Overrun (DOR) | DOR0 | Dato no leído antes del siguiente |
| Parity Error (UPE) | UPE0 | Paridad calculada no coincide |

### Respuesta 7.2

```c
typedef enum {
    UART_OK = 0,
    UART_FRAME_ERROR,
    UART_OVERRUN_ERROR,
    UART_PARITY_ERROR
} uart_error_t;

uart_error_t uart_receive_checked(uint8_t *data) {
    while (!(UCSR0A & (1 << RXC0)));
    
    uint8_t status = UCSR0A;
    *data = UDR0;  // Siempre leer para limpiar
    
    if (status & (1 << FE0)) return UART_FRAME_ERROR;
    if (status & (1 << DOR0)) return UART_OVERRUN_ERROR;
    if (status & (1 << UPE0)) return UART_PARITY_ERROR;
    
    return UART_OK;
}
```

### Respuesta 7.3

Para evitar Overrun:
1. Usar interrupciones con buffer
2. Procesar datos rápidamente
3. Usar control de flujo (RTS/CTS)
4. Reducir baud rate si necesario
5. Buffer suficientemente grande

---

## Nivel 8: Protocolos

### Respuesta 8.1

```
Formato de trama:
┌─────┬─────┬─────┬──────────┬─────────┬─────┐
│ STX │ LEN │ CMD │ DATA[0..n]│CHECKSUM │ ETX │
│0x02 │     │     │          │         │0x03 │
└─────┴─────┴─────┴──────────┴─────────┴─────┘

Ejemplo: Comando 0x10 con datos [0x01, 0x02]
02 02 10 01 02 EB 03
   │  │  └──┴──datos
   │  └──comando
   └──longitud (2 bytes)
```

### Respuesta 8.2

```c
uint8_t calc_checksum(uint8_t *data, uint8_t len) {
    uint8_t sum = 0;
    for (uint8_t i = 0; i < len; i++) {
        sum += data[i];
    }
    return (~sum) + 1;  // Complemento a 2
}

// Verificar: suma de todos los bytes + checksum = 0
uint8_t verify_checksum(uint8_t *data, uint8_t len, uint8_t checksum) {
    uint8_t sum = calc_checksum(data, len);
    return (sum == checksum);
}
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de UART
NOTA: Pueden existir soluciones alternativas válidas
-->
