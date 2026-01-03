<!--
::METADATA::
type: reference
topic_id: mcu-05-comunicacion-serial
file_id: resumen-uart
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, microcontrolador, UART, serial, comunicación]
search_keywords: "resumen, UART, serial, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-05-Intro.md)

---

# 📋 Cheatsheet: Comunicación Serial (UART)

## Formato de Trama 8N1

```
│START│ D0 │ D1 │...│ D7 │STOP│
│  0  │    8 bits    │  1 │
```

10 bits total por byte

---

## Fórmulas

### UBRR
$$UBRR = \frac{F_{CPU}}{16 \times Baud} - 1$$

### Tiempo por byte
$$T = \frac{10}{Baud}$$

---

## UBRR Comunes (16 MHz)

| Baud | UBRR | Error |
|------|------|-------|
| 9600 | 103 | 0.2% |
| 19200 | 51 | 0.2% |
| 38400 | 25 | 0.2% |
| 115200 | 8 | -3.5% |

---

## Inicialización AVR

```c
void uart_init(void) {
    UBRR0H = (UBRR >> 8);
    UBRR0L = UBRR;
    UCSR0B = (1<<TXEN0) | 
             (1<<RXEN0);
    UCSR0C = (1<<UCSZ01) | 
             (1<<UCSZ00);
}
```

---

## Transmitir

```c
void uart_tx(uint8_t c) {
    while(!(UCSR0A & 
           (1<<UDRE0)));
    UDR0 = c;
}
```

---

## Recibir

```c
uint8_t uart_rx(void) {
    while(!(UCSR0A & 
           (1<<RXC0)));
    return UDR0;
}
```

---

## Flags de Estado

| Bit | Nombre | Significado |
|-----|--------|-------------|
| UDRE0 | Data Reg Empty | Puede TX |
| RXC0 | RX Complete | Dato listo |
| TXC0 | TX Complete | TX terminó |

---

## Errores

| Bit | Error | Causa |
|-----|-------|-------|
| FE0 | Frame | Baud malo |
| DOR0 | Overrun | No leído |
| UPE0 | Parity | Bit errado |

---

## Con Interrupciones

```c
// Habilitar
UCSR0B |= (1<<RXCIE0);
sei();

ISR(USART_RX_vect) {
    uint8_t c = UDR0;
    // procesar
}
```

---

## Buffer Circular

```c
#define SIZE 64
volatile uint8_t buf[SIZE];
volatile uint8_t head, tail;

// Escribir (ISR)
buf[head] = data;
head = (head+1) % SIZE;

// Leer (main)
data = buf[tail];
tail = (tail+1) % SIZE;

// Disponible
head != tail
```

---

## Conexión

```
MCU_A      MCU_B
TX ─────── RX
RX ─────── TX
GND ────── GND
```

⚠️ Cruzar TX↔RX

---

## Debug Rápido

```c
// Verificar TX
uart_tx('X');

// Verificar RX
if(UCSR0A & (1<<RXC0))
    dato = UDR0;
```

---

## Printf

```c
static FILE uart_str = 
  FDEV_SETUP_STREAM(
    uart_putc, NULL, 
    _FDEV_SETUP_WRITE);

stdout = &uart_str;
printf("Val: %d\n", x);
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante trabajo con UART
-->
