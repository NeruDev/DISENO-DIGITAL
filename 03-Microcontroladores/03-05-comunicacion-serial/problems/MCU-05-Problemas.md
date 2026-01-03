<!--
::METADATA::
type: problem
topic_id: mcu-05-comunicacion-serial
file_id: problemas-uart
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, microcontrolador, UART, serial, comunicación]
search_keywords: "ejercicios, problemas, UART, serial"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-05-Metodos-UART.md) | [Respuestas →](../solutions/MCU-05-Respuestas.md)

---

# Problemas: Comunicación Serial (UART)

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Qué significa UART y cuáles son sus principales características?

### Problema 1.2
En una comunicación UART, ¿cómo se conectan los pines TX y RX entre dos dispositivos?

### Problema 1.3
¿Qué significa la configuración "8N1"?

---

## Nivel 2: Cálculos de Baud Rate

### Problema 2.1
Con F_CPU = 16 MHz y baud rate de 9600:
- Calcula el valor de UBRR

### Problema 2.2
¿Cuánto tiempo tarda en transmitirse un byte a 115200 baud con formato 8N1?

### Problema 2.3
Con F_CPU = 8 MHz, ¿cuál es el error porcentual del baud rate 9600 usando UBRR calculado?

---

## Nivel 3: Formato de Trama

### Problema 3.1
Dibuja la trama UART para transmitir el carácter 'A' (ASCII 65 = 0x41) con formato 8N1.

### Problema 3.2
¿Cuál es el bit de paridad par para el dato 0b10110101?

### Problema 3.3
Si recibes la trama (en orden): 0-1-0-0-0-0-0-1-0-1
Con formato 8E1, ¿hay error de paridad?

---

## Nivel 4: Configuración Básica

### Problema 4.1
Escribe el código para inicializar UART a 9600 baud con F_CPU = 16 MHz.

### Problema 4.2
Implementa una función que transmita un byte esperando que el buffer esté vacío.

### Problema 4.3
Implementa una función de recepción bloqueante (espera hasta recibir un byte).

---

## Nivel 5: Transmisión de Cadenas

### Problema 5.1
Implementa `uart_puts()` para transmitir una cadena terminada en null.

### Problema 5.2
¿Cómo transmitirías un número entero sin usar printf?

### Problema 5.3
Implementa una función que imprima un número en formato hexadecimal.

---

## Nivel 6: Recepción con Buffer

### Problema 6.1
¿Por qué es importante usar un buffer circular para recepción UART?

### Problema 6.2
Implementa un buffer circular de 64 bytes para recepción con interrupciones.

### Problema 6.3
Implementa funciones `uart_available()` y `uart_getc()` no bloqueantes.

---

## Nivel 7: Manejo de Errores

### Problema 7.1
¿Cuáles son los tres tipos de errores que puede detectar el UART y qué los causa?

### Problema 7.2
Implementa una función de recepción que verifique errores antes de retornar el dato.

### Problema 7.3
¿Cómo evitarías el error de Overrun?

---

## Nivel 8: Protocolos

### Problema 8.1
Diseña un protocolo simple con:
- Byte de inicio (STX = 0x02)
- Longitud del mensaje
- Datos (máx 16 bytes)
- Checksum
- Byte de fin (ETX = 0x03)

### Problema 8.2
Implementa el cálculo de checksum como complemento a 2 de la suma de bytes.

### Problema 8.3
Implementa una máquina de estados para parsear el protocolo del problema 8.1.

---

## Nivel 9: Aplicaciones

### Problema 9.1
Diseña un sistema de comando/respuesta:
- Comando "LED ON" enciende LED
- Comando "LED OFF" apaga LED
- Comando "ADC" retorna lectura del canal 0

### Problema 9.2
Implementa un datalogger que:
- Lea temperatura cada segundo
- Envíe por UART en formato CSV: "timestamp,temperatura\n"

### Problema 9.3
Diseña comunicación con módulo GPS:
- Parsear sentencia NMEA $GPGGA
- Extraer latitud, longitud, altitud

---

## Nivel 10: Proyectos Integradores

### Problema 10.1
Diseña un terminal serial completo:
- Echo de caracteres
- Historial de comandos (flecha arriba)
- Autocompletado básico
- Comandos: HELP, LED, ADC, PWM, RESET

### Problema 10.2
Implementa comunicación entre dos MCU:
- Master envía comandos
- Slave ejecuta y responde
- Protocolo con reintentos si hay error

### Problema 10.3
Diseña un bridge UART-I2C:
- Recibe comandos por UART
- Lee/escribe dispositivos I2C
- Formato: "I2C R addr reg len" o "I2C W addr reg data..."

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre comunicación UART
RESPUESTAS: Ver archivo solutions/MCU-05-Respuestas.md
HERRAMIENTAS: AVR-GCC, terminal serial, analizador lógico
-->
