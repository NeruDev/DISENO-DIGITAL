<!--
::METADATA::
type: solution_index
topic_id: mcu-05-comunicacion-serial
file_id: solucion-index-uart
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, UART, serial, comunicación, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-05-Respuestas.md) | [Problemas →](../../problems/MCU-05-Problemas.md)

---

# Soluciones Detalladas: Comunicación Serial UART (MCU-05)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-05-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Código completo |
| **3** | Secciones "Conceptos Clave" | Teoría de protocolos |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos Básicos ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | Qué es UART | En respuestas |
| 1.2 | Conexión TX/RX | En respuestas |
| 1.3 | Formato 8N1 | En respuestas |

### Nivel 2: Cálculos Baud Rate ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 2.1 | Cálculo UBRR | [MCU-05-Sol-Problema-2.1.md](./MCU-05-Sol-Problema-2.1.md) |
| 2.2 | Tiempo por byte | En respuestas |
| 2.3 | Error de baud rate | En respuestas |

### Nivel 3: Formato de Trama ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Diagrama de trama | En respuestas |
| 3.2 | Cálculo de paridad | En respuestas |
| 3.3 | Verificación paridad | En respuestas |

### Nivel 4: Configuración Básica ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 4.1 | Init UART | [MCU-05-Sol-Problema-4.1.md](./MCU-05-Sol-Problema-4.1.md) |
| 4.2 | Transmisión byte | En respuestas |
| 4.3 | Recepción bloqueante | En respuestas |

### Nivel 5-6: Cadenas y Buffer ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | uart_puts() | En respuestas |
| 5.2 | Transmitir entero | En respuestas |
| 6.1 | Por qué buffer circular | En respuestas |
| 6.2 | Buffer con ISR | En respuestas |

### Nivel 7-9: Errores y Aplicaciones ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 7.1 | Tipos de errores | En respuestas |
| 8.1 | Protocolo con checksum | En respuestas |
| 9.1 | Sistema comando/respuesta | En respuestas |

---

## Referencia Rápida

### Fórmulas UART

| Concepto | Fórmula |
|----------|---------|
| UBRR | $UBRR = \frac{f_{CPU}}{16 \times Baud} - 1$ |
| UBRR (U2X=1) | $UBRR = \frac{f_{CPU}}{8 \times Baud} - 1$ |
| Error % | $Error = \left(\frac{Baud_{real}}{Baud_{deseado}} - 1\right) \times 100$ |
| Tiempo/byte | $T = \frac{bits_{totales}}{Baud}$ |

### Formato de Trama UART

```
        ┌─────┬───┬───┬───┬───┬───┬───┬───┬───┬─────┬─────┐
        │START│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │(PAR)│STOP │
        │  0  │   │   │   │   │   │   │   │   │     │  1  │
        └─────┴───┴───┴───┴───┴───┴───┴───┴───┴─────┴─────┘
        │◄─────────────── 8N1: 10 bits ───────────────────►│
```

### Conexión Entre Dispositivos

```
    Dispositivo A          Dispositivo B
    ┌──────────┐          ┌──────────┐
    │       TX │──────────│ RX       │
    │       RX │──────────│ TX       │
    │      GND │──────────│ GND      │
    └──────────┘          └──────────┘
```

### Registros UART (AVR)

```
┌─────────────────────────────────────────────────────────────┐
│ UCSR0A: Status                                              │
│   - RXC0: Receive Complete                                  │
│   - TXC0: Transmit Complete                                 │
│   - UDRE0: Data Register Empty                              │
│   - FE0: Frame Error                                        │
│   - DOR0: Data Overrun                                      │
│   - UPE0: Parity Error                                      │
├─────────────────────────────────────────────────────────────┤
│ UCSR0B: Control B                                           │
│   - RXCIE0: RX Complete Interrupt Enable                    │
│   - TXCIE0: TX Complete Interrupt Enable                    │
│   - UDRIE0: Data Register Empty Interrupt Enable            │
│   - RXEN0: Receiver Enable                                  │
│   - TXEN0: Transmitter Enable                               │
├─────────────────────────────────────────────────────────────┤
│ UCSR0C: Control C                                           │
│   - UMSEL0[1:0]: Mode (00=Async)                           │
│   - UPM0[1:0]: Parity (00=none, 10=even, 11=odd)           │
│   - USBS0: Stop bits (0=1, 1=2)                            │
│   - UCSZ0[1:0]: Char size (011=8-bit)                      │
├─────────────────────────────────────────────────────────────┤
│ UBRR0H/L: Baud Rate Register                               │
│ UDR0: Data Register (TX/RX)                                │
└─────────────────────────────────────────────────────────────┘
```

### Tabla de UBRR Comunes (16 MHz)

| Baud Rate | UBRR | Error |
|:---------:|:----:|:-----:|
| 9600 | 103 | 0.2% |
| 19200 | 51 | 0.2% |
| 38400 | 25 | 0.2% |
| 57600 | 16 | 2.1% ⚠️ |
| 115200 | 8 | 3.7% ⚠️ |

> ⚠️ Para 57600+ usar U2X=1 para mejor precisión

---

## Navegación

| Anterior | Arriba | Siguiente |
|:--------:|:------:|:---------:|
| [ADC/DAC](../../../03-04-adc-dac/solutions/prob-01/) | [Módulo MCU](../../00-Index.md) | [I2C/SPI](../../../03-06-protocolos-i2c-spi/solutions/prob-01/) |
