<!--
::METADATA::
type: method
topic_id: mcu-05-comunicacion-serial
file_id: metodos-uart
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, metodología, UART, serial, comunicación]
search_keywords: "metodología UART, serial, comunicación"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-05-Teoria-UART.md) | [Problemas →](../problems/MCU-05-Problemas.md)

---

# Métodos: Comunicación Serial (UART)

## Método 1: Biblioteca UART Completa

```c
#ifndef UART_H
#define UART_H

#include <avr/io.h>
#include <avr/interrupt.h>

#define UART_BAUD 9600
#define UART_UBRR ((F_CPU / 16 / UART_BAUD) - 1)
#define UART_RX_BUFFER_SIZE 64
#define UART_TX_BUFFER_SIZE 64

void uart_init(void);
void uart_putc(char c);
void uart_puts(const char *s);
void uart_puts_P(const char *s);  // PROGMEM
uint8_t uart_available(void);
char uart_getc(void);
void uart_flush(void);

#endif
```

```c
// uart.c
#include "uart.h"
#include <avr/pgmspace.h>

static volatile uint8_t rx_buffer[UART_RX_BUFFER_SIZE];
static volatile uint8_t rx_head = 0;
static volatile uint8_t rx_tail = 0;

static volatile uint8_t tx_buffer[UART_TX_BUFFER_SIZE];
static volatile uint8_t tx_head = 0;
static volatile uint8_t tx_tail = 0;

void uart_init(void) {
    UBRR0H = (UART_UBRR >> 8);
    UBRR0L = UART_UBRR;
    UCSR0B = (1 << RXEN0) | (1 << TXEN0) | (1 << RXCIE0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

ISR(USART_RX_vect) {
    uint8_t data = UDR0;
    uint8_t next = (rx_head + 1) % UART_RX_BUFFER_SIZE;
    if (next != rx_tail) {
        rx_buffer[rx_head] = data;
        rx_head = next;
    }
}

ISR(USART_UDRE_vect) {
    if (tx_head != tx_tail) {
        UDR0 = tx_buffer[tx_tail];
        tx_tail = (tx_tail + 1) % UART_TX_BUFFER_SIZE;
    } else {
        UCSR0B &= ~(1 << UDRIE0);  // Desactivar int
    }
}

void uart_putc(char c) {
    uint8_t next = (tx_head + 1) % UART_TX_BUFFER_SIZE;
    while (next == tx_tail);  // Esperar espacio
    tx_buffer[tx_head] = c;
    tx_head = next;
    UCSR0B |= (1 << UDRIE0);  // Activar int TX
}

void uart_puts(const char *s) {
    while (*s) uart_putc(*s++);
}

void uart_puts_P(const char *s) {
    char c;
    while ((c = pgm_read_byte(s++))) uart_putc(c);
}

uint8_t uart_available(void) {
    return (rx_head - rx_tail + UART_RX_BUFFER_SIZE) % UART_RX_BUFFER_SIZE;
}

char uart_getc(void) {
    while (rx_head == rx_tail);
    char c = rx_buffer[rx_tail];
    rx_tail = (rx_tail + 1) % UART_RX_BUFFER_SIZE;
    return c;
}

void uart_flush(void) {
    rx_head = rx_tail = 0;
}
```

---

## Método 2: Printf por UART

```c
#include <stdio.h>

// Función para stdio
static int uart_putchar(char c, FILE *stream) {
    if (c == '\n') uart_putc('\r');
    uart_putc(c);
    return 0;
}

static int uart_getchar(FILE *stream) {
    return uart_getc();
}

// Stream para printf/scanf
static FILE uart_stream = FDEV_SETUP_STREAM(
    uart_putchar, uart_getchar, _FDEV_SETUP_RW
);

void uart_stdio_init(void) {
    uart_init();
    stdout = &uart_stream;
    stdin = &uart_stream;
}

// Uso
int main(void) {
    uart_stdio_init();
    sei();
    
    printf("Valor: %d\n", 42);
    printf("Float: %.2f\n", 3.14);  // Requiere -lprintf_flt
}
```

---

## Método 3: Imprimir Números sin Printf

```c
// Imprimir entero sin signo
void uart_print_uint(uint32_t n) {
    char buf[11];
    int8_t i = 0;
    
    if (n == 0) {
        uart_putc('0');
        return;
    }
    
    while (n > 0) {
        buf[i++] = '0' + (n % 10);
        n /= 10;
    }
    
    while (i > 0) {
        uart_putc(buf[--i]);
    }
}

// Imprimir entero con signo
void uart_print_int(int32_t n) {
    if (n < 0) {
        uart_putc('-');
        n = -n;
    }
    uart_print_uint(n);
}

// Imprimir hexadecimal
void uart_print_hex(uint32_t n, uint8_t digits) {
    uart_puts("0x");
    for (int8_t i = digits - 1; i >= 0; i--) {
        uint8_t nibble = (n >> (i * 4)) & 0x0F;
        uart_putc(nibble < 10 ? '0' + nibble : 'A' + nibble - 10);
    }
}

// Imprimir con decimales (×100)
void uart_print_decimal(int16_t n, uint8_t decimals) {
    if (n < 0) {
        uart_putc('-');
        n = -n;
    }
    
    int16_t divisor = 1;
    for (uint8_t i = 0; i < decimals; i++) divisor *= 10;
    
    uart_print_uint(n / divisor);
    uart_putc('.');
    
    uint16_t frac = n % divisor;
    for (uint8_t i = 1; i < decimals; i++) {
        if (frac < divisor / 10) uart_putc('0');
        divisor /= 10;
    }
    uart_print_uint(frac);
}
```

---

## Método 4: Parser de Comandos

```c
#define CMD_BUFFER_SIZE 32

char cmd_buffer[CMD_BUFFER_SIZE];
uint8_t cmd_index = 0;

typedef struct {
    const char *name;
    void (*handler)(char *args);
} command_t;

void cmd_led(char *args);
void cmd_adc(char *args);
void cmd_help(char *args);

command_t commands[] = {
    {"LED", cmd_led},
    {"ADC", cmd_adc},
    {"HELP", cmd_help},
    {NULL, NULL}
};

void process_command(void) {
    // Separar comando de argumentos
    char *cmd = cmd_buffer;
    char *args = NULL;
    
    for (uint8_t i = 0; cmd_buffer[i]; i++) {
        if (cmd_buffer[i] == ' ') {
            cmd_buffer[i] = '\0';
            args = &cmd_buffer[i + 1];
            break;
        }
    }
    
    // Buscar y ejecutar comando
    for (uint8_t i = 0; commands[i].name; i++) {
        if (strcasecmp(cmd, commands[i].name) == 0) {
            commands[i].handler(args);
            return;
        }
    }
    
    uart_puts("Comando desconocido\r\n");
}

void uart_process(void) {
    while (uart_available()) {
        char c = uart_getc();
        
        if (c == '\r' || c == '\n') {
            uart_puts("\r\n");
            if (cmd_index > 0) {
                cmd_buffer[cmd_index] = '\0';
                process_command();
                cmd_index = 0;
            }
        } else if (c == '\b' && cmd_index > 0) {
            cmd_index--;
            uart_puts("\b \b");
        } else if (cmd_index < CMD_BUFFER_SIZE - 1) {
            cmd_buffer[cmd_index++] = c;
            uart_putc(c);  // Echo
        }
    }
}

// Handlers de ejemplo
void cmd_led(char *args) {
    if (args && args[0] == '1') {
        PORTB |= (1 << PB5);
        uart_puts("LED ON\r\n");
    } else {
        PORTB &= ~(1 << PB5);
        uart_puts("LED OFF\r\n");
    }
}

void cmd_adc(char *args) {
    uint16_t val = adc_read(0);
    uart_puts("ADC: ");
    uart_print_uint(val);
    uart_puts("\r\n");
}
```

---

## Método 5: Protocolo con Checksum

```c
// Formato: <STX><LEN><CMD><DATA...><CHECKSUM><ETX>
#define STX 0x02
#define ETX 0x03

typedef struct {
    uint8_t cmd;
    uint8_t len;
    uint8_t data[16];
} packet_t;

uint8_t calc_checksum(packet_t *p) {
    uint8_t sum = p->cmd + p->len;
    for (uint8_t i = 0; i < p->len; i++) {
        sum += p->data[i];
    }
    return ~sum + 1;  // Complemento a 2
}

void send_packet(packet_t *p) {
    uart_putc(STX);
    uart_putc(p->len);
    uart_putc(p->cmd);
    for (uint8_t i = 0; i < p->len; i++) {
        uart_putc(p->data[i]);
    }
    uart_putc(calc_checksum(p));
    uart_putc(ETX);
}

uint8_t receive_packet(packet_t *p) {
    // Estado de la máquina de estados
    static uint8_t state = 0;
    static uint8_t idx = 0;
    static uint8_t checksum = 0;
    
    if (!uart_available()) return 0;
    
    uint8_t c = uart_getc();
    
    switch (state) {
        case 0:  // Esperar STX
            if (c == STX) state = 1;
            break;
        case 1:  // Recibir LEN
            p->len = c;
            state = 2;
            break;
        case 2:  // Recibir CMD
            p->cmd = c;
            idx = 0;
            state = (p->len > 0) ? 3 : 4;
            break;
        case 3:  // Recibir DATA
            p->data[idx++] = c;
            if (idx >= p->len) state = 4;
            break;
        case 4:  // Verificar checksum
            checksum = c;
            state = 5;
            break;
        case 5:  // Esperar ETX
            state = 0;
            if (c == ETX && calc_checksum(p) == checksum) {
                return 1;  // Paquete válido
            }
            break;
    }
    return 0;
}
```

---

## Método 6: Timeout de Recepción

```c
#include <util/delay.h>

// Recibir con timeout (ms)
int16_t uart_getc_timeout(uint16_t timeout_ms) {
    while (timeout_ms > 0) {
        if (uart_available()) {
            return uart_getc();
        }
        _delay_ms(1);
        timeout_ms--;
    }
    return -1;  // Timeout
}

// Recibir línea con timeout
uint8_t uart_gets_timeout(char *buf, uint8_t max_len, uint16_t timeout_ms) {
    uint8_t i = 0;
    int16_t c;
    
    while (i < max_len - 1) {
        c = uart_getc_timeout(timeout_ms);
        
        if (c < 0) {
            break;  // Timeout
        }
        
        if (c == '\r' || c == '\n') {
            if (i > 0) break;
            continue;
        }
        
        buf[i++] = c;
    }
    
    buf[i] = '\0';
    return i;
}
```

---

## Método 7: Multi-UART (Software UART)

```c
// Software UART en cualquier pin
#define SOFT_TX_PIN PD4
#define SOFT_TX_PORT PORTD
#define SOFT_TX_DDR DDRD

#define SOFT_BAUD 9600
#define SOFT_DELAY (F_CPU / SOFT_BAUD)

void soft_uart_init(void) {
    SOFT_TX_DDR |= (1 << SOFT_TX_PIN);
    SOFT_TX_PORT |= (1 << SOFT_TX_PIN);  // Idle high
}

void soft_uart_putc(uint8_t c) {
    uint8_t i;
    
    cli();  // Desactivar interrupciones
    
    // Start bit
    SOFT_TX_PORT &= ~(1 << SOFT_TX_PIN);
    _delay_loop_2(SOFT_DELAY / 4);
    
    // Data bits
    for (i = 0; i < 8; i++) {
        if (c & 1) {
            SOFT_TX_PORT |= (1 << SOFT_TX_PIN);
        } else {
            SOFT_TX_PORT &= ~(1 << SOFT_TX_PIN);
        }
        c >>= 1;
        _delay_loop_2(SOFT_DELAY / 4);
    }
    
    // Stop bit
    SOFT_TX_PORT |= (1 << SOFT_TX_PIN);
    _delay_loop_2(SOFT_DELAY / 4);
    
    sei();  // Reactivar interrupciones
}
```

---

## Método 8: Debug por UART

```c
// Macros de debug
#ifdef DEBUG
    #define DEBUG_INIT() uart_init(); sei()
    #define DEBUG_PRINT(s) uart_puts_P(PSTR(s))
    #define DEBUG_PRINTLN(s) uart_puts_P(PSTR(s "\r\n"))
    #define DEBUG_VAR(name, val) do { \
        uart_puts_P(PSTR(name " = ")); \
        uart_print_int(val); \
        uart_puts("\r\n"); \
    } while(0)
    #define DEBUG_HEX(name, val) do { \
        uart_puts_P(PSTR(name " = ")); \
        uart_print_hex(val, 4); \
        uart_puts("\r\n"); \
    } while(0)
#else
    #define DEBUG_INIT()
    #define DEBUG_PRINT(s)
    #define DEBUG_PRINTLN(s)
    #define DEBUG_VAR(name, val)
    #define DEBUG_HEX(name, val)
#endif

// Uso
void funcion(void) {
    DEBUG_PRINTLN("Iniciando funcion");
    
    uint16_t valor = adc_read(0);
    DEBUG_VAR("ADC", valor);
    
    DEBUG_HEX("PORTB", PORTB);
}
```

---

## Método 9: Comunicación con Módulos

```c
// Ejemplo: Módulo ESP8266
void esp_send_cmd(const char *cmd) {
    uart_puts(cmd);
    uart_puts("\r\n");
}

uint8_t esp_wait_response(const char *expected, uint16_t timeout_ms) {
    char buf[64];
    uint8_t idx = 0;
    
    while (timeout_ms > 0) {
        if (uart_available()) {
            char c = uart_getc();
            if (idx < sizeof(buf) - 1) {
                buf[idx++] = c;
                buf[idx] = '\0';
            }
            
            if (strstr(buf, expected)) {
                return 1;  // Encontrado
            }
            if (strstr(buf, "ERROR")) {
                return 0;  // Error
            }
        }
        _delay_ms(1);
        timeout_ms--;
    }
    return 0;  // Timeout
}

// Uso
void esp_init(void) {
    esp_send_cmd("AT");
    if (!esp_wait_response("OK", 1000)) {
        // Error de comunicación
    }
    
    esp_send_cmd("AT+CWMODE=1");
    esp_wait_response("OK", 1000);
}
```

---

## Método 10: Checklist UART

### Antes de Comunicar

- [ ] ¿Baud rate coincide en ambos lados?
- [ ] ¿TX conectado a RX y viceversa?
- [ ] ¿GND común entre dispositivos?
- [ ] ¿Niveles de voltaje compatibles?
- [ ] ¿Formato de trama igual (8N1)?

### Debugging

- [ ] Verificar con osciloscopio
- [ ] Probar con eco simple
- [ ] Revisar errores (FE, DOR, UPE)
- [ ] Verificar buffer suficiente

---

<!-- IA_CONTEXT
USO: Métodos prácticos para comunicación UART
NIVEL: Intermedio (2/3)
HERRAMIENTAS: AVR-GCC, terminal serial, analizador lógico
-->
