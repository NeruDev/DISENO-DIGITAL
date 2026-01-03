<!--
::METADATA::
type: detailed_solution
topic_id: mcu-05-comunicacion-serial
problem_id: 4.1
file_id: solucion-problema-4-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, MCU, UART, inicialización, código]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 4.2 →](./MCU-05-Sol-Problema-4.2.md)

---

# Solución Detallada: Problema 4.1

## Enunciado
Escribe el código para inicializar UART a 9600 baud con F_CPU = 16 MHz.

---

## Paso 1: Cálculo de UBRR

### Fórmula

$$UBRR = \frac{f_{CPU}}{16 \times Baud} - 1$$

### Cálculo

$$UBRR = \frac{16,000,000}{16 \times 9600} - 1 = \frac{16,000,000}{153,600} - 1 = 104.17 - 1 = 103.17$$

Redondeando: **UBRR = 103**

### Verificación de Error

$$Baud_{real} = \frac{f_{CPU}}{16 \times (UBRR + 1)} = \frac{16,000,000}{16 \times 104} = 9615.38$$

$$Error = \frac{9615.38 - 9600}{9600} \times 100 = 0.16\%$$

✅ Error < 2% es aceptable.

---

## Paso 2: Código de Inicialización

```c
#include <avr/io.h>

#define F_CPU 16000000UL
#define BAUD 9600
#define UBRR_VALUE ((F_CPU / (16UL * BAUD)) - 1)

void uart_init(void) {
    // Configurar baud rate
    UBRR0H = (uint8_t)(UBRR_VALUE >> 8);
    UBRR0L = (uint8_t)(UBRR_VALUE);
    
    // Habilitar TX y RX
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    
    // Formato: 8 bits datos, 1 stop, sin paridad (8N1)
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}
```

---

## Paso 3: Análisis de Registros

### UBRR0H y UBRR0L (Baud Rate)

```
UBRR_VALUE = 103 = 0x0067

UBRR0H = 0x00 (bits [11:8])
UBRR0L = 0x67 (bits [7:0])
```

### UCSR0B (Control B)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│RXCIE│TXCIE│UDRIE│RXEN │TXEN │UCSZ2│ RXB8│ TXB8│
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│  0  │  0  │  0  │  1  │  1  │  0  │  0  │  0  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
         RXEN0=1: Habilita receptor
         TXEN0=1: Habilita transmisor
```

### UCSR0C (Control C)

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│UMSEL│UMSEL│ UPM1│ UPM0│ USBS│UCSZ1│UCSZ0│UCPOL│
│  1  │  0  │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│  0  │  0  │  0  │  0  │  0  │  1  │  1  │  0  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
  UMSEL=00: Modo asíncrono
  UPM=00: Sin paridad
  USBS=0: 1 bit de stop
  UCSZ=011: 8 bits de datos (combinado con UCSZ2=0)
```

---

## Paso 4: Código Completo con Funciones

```c
#include <avr/io.h>

#define F_CPU 16000000UL
#define BAUD 9600
#define UBRR_VALUE ((F_CPU / (16UL * BAUD)) - 1)

// Inicializar UART
void uart_init(void) {
    UBRR0H = (uint8_t)(UBRR_VALUE >> 8);
    UBRR0L = (uint8_t)(UBRR_VALUE);
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

// Transmitir un byte (bloqueante)
void uart_putc(char c) {
    while (!(UCSR0A & (1 << UDRE0)));  // Esperar buffer vacío
    UDR0 = c;
}

// Recibir un byte (bloqueante)
char uart_getc(void) {
    while (!(UCSR0A & (1 << RXC0)));   // Esperar dato
    return UDR0;
}

// Transmitir cadena
void uart_puts(const char *s) {
    while (*s) {
        uart_putc(*s++);
    }
}

// Ejemplo de uso
int main(void) {
    uart_init();
    
    uart_puts("Hello, UART!\r\n");
    
    while (1) {
        char c = uart_getc();   // Esperar carácter
        uart_putc(c);           // Echo
    }
}
```

---

## Diagrama de Flujo

```
┌─────────────────┐
│   uart_init()   │
└────────┬────────┘
         │
         ▼
┌────────────────────────────┐
│ Configurar UBRR (103)      │
│ 9600 baud @ 16MHz          │
└────────────────┬───────────┘
         │
         ▼
┌────────────────────────────┐
│ Habilitar TX y RX          │
│ UCSR0B = RXEN0 | TXEN0     │
└────────────────┬───────────┘
         │
         ▼
┌────────────────────────────┐
│ Formato 8N1                │
│ UCSR0C = UCSZ01 | UCSZ00   │
└────────────────┬───────────┘
         │
         ▼
┌─────────────────┐
│     LISTO       │
└─────────────────┘
```

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **UBRR** | Baud Rate Register - define velocidad |
| **UDRE0** | Data Register Empty - buffer TX listo |
| **RXC0** | Receive Complete - dato disponible |
| **UDR0** | Data Register - lectura/escritura datos |
| **8N1** | 8 data bits, No parity, 1 stop bit |

---

## Errores Comunes

| Error | Consecuencia | Solución |
|-------|--------------|----------|
| F_CPU incorrecto | Baud rate erróneo | Verificar cristal |
| No esperar UDRE | Datos perdidos | `while(!(UCSR0A & UDRE0))` |
| TX/RX cruzados | No comunica | TX→RX, RX→TX |
| Falta GND común | Datos corruptos | Conectar GND |

---

> 💡 **Tip:** Siempre prueba la comunicación con un terminal serial (PuTTY, minicom) antes de integrar con otro dispositivo.
