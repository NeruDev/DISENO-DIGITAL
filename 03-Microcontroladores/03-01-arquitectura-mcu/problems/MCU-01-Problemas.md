<!--
::METADATA::
type: problem
topic_id: mcu-01-arquitectura
file_id: problemas-arquitectura-mcu
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, microcontrolador, arquitectura]
search_keywords: "ejercicios, problemas, arquitectura MCU"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-01-Metodos-Arquitectura.md) | [Respuestas →](../solutions/MCU-01-Respuestas.md)

---

# Problemas: Arquitectura de Microcontroladores

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Cuál es la diferencia principal entre un microcontrolador y un microprocesador?

### Problema 1.2
Nombra al menos 5 periféricos comúnmente integrados en un microcontrolador.

### Problema 1.3
¿Qué significa que un MCU tenga arquitectura Harvard? ¿Qué ventaja tiene sobre Von Neumann?

---

## Nivel 2: Componentes de la CPU

### Problema 2.1
¿Cuáles son las funciones principales de la ALU?

### Problema 2.2
Un MCU tiene un registro de estado (STATUS) con los siguientes flags: Z, C, N, V. Explica qué representa cada uno.

### Problema 2.3
¿Cuál es la función del contador de programa (PC)?

---

## Nivel 3: Sistema de Memoria

### Problema 3.1
Un ATmega328P tiene:
- 32 KB de Flash
- 2 KB de SRAM
- 1 KB de EEPROM

¿Para qué se usa cada tipo de memoria?

### Problema 3.2
Si un MCU tiene un bus de direcciones de 16 bits, ¿cuál es el máximo espacio de memoria que puede direccionar?

### Problema 3.3
¿Por qué la RAM es volátil y la Flash no lo es? ¿Cómo afecta esto al diseño de sistemas embebidos?

---

## Nivel 4: Sistema de Reloj

### Problema 4.1
Un MCU puede usar:
- Oscilador RC interno (8 MHz, ±10%)
- Cristal externo (16 MHz, ±20 ppm)

¿Cuándo elegirías cada opción?

### Problema 4.2
Si el reloj del sistema es de 16 MHz, ¿cuánto tiempo toma ejecutar una instrucción de 1 ciclo?

### Problema 4.3
Un MCU tiene prescalers de reloj de 1, 2, 4, 8. Si la frecuencia base es 20 MHz, ¿cuáles son las frecuencias disponibles para los periféricos?

---

## Nivel 5: Selección de MCU

### Problema 5.1
Para un proyecto que requiere:
- 10 entradas digitales
- 4 salidas PWM
- 2 entradas analógicas
- Comunicación UART
- Bajo costo

¿Qué familia de MCU recomendarías y por qué?

### Problema 5.2
Compara un PIC16F, ATmega328 y STM32F103 en términos de:
- Arquitectura
- Ancho de datos
- Ecosistema de desarrollo

### Problema 5.3
¿Qué factores considerarías para elegir entre un MCU de 8 bits y uno de 32 bits?

---

## Nivel 6: Cálculos de Recursos

### Problema 6.1
Un programa embebido tiene:
- Código: 12 KB
- Variables globales: 500 bytes
- Stack estimado: 200 bytes
- Buffers: 256 bytes

¿Es suficiente un MCU con 16 KB Flash y 1 KB RAM?

### Problema 6.2
Un sistema debe muestrear una señal a 10 kHz con un ADC de 10 bits. ¿Cuál es la mínima frecuencia de CPU recomendada si cada conversión toma 13 ciclos de reloj del ADC?

### Problema 6.3
Calcula la capacidad de batería necesaria para un dispositivo que:
- Consume 25 mA en modo activo (10% del tiempo)
- Consume 50 µA en modo sleep (90% del tiempo)
- Debe operar 30 días sin recargar

---

## Nivel 7: Mapa de Memoria

### Problema 7.1
Dado el siguiente mapa de memoria de un MCU:
```
0x0000-0x001F: Registros de CPU
0x0020-0x005F: Registros de I/O
0x0060-0x00FF: SRAM (160 bytes)
```
¿En qué dirección colocarías una variable que debe ser accedida frecuentemente?

### Problema 7.2
Un MCU usa direccionamiento de 8 bits para I/O y 16 bits para memoria. ¿Cuántos dispositivos de I/O puede direccionar?

### Problema 7.3
¿Por qué los vectores de interrupción generalmente se colocan al inicio de la memoria Flash?

---

## Nivel 8: Consumo de Energía

### Problema 8.1
Un MCU tiene los siguientes modos:
- Active: 5 mA @ 8 MHz
- Idle: 1 mA
- Power-down: 1 µA

Si la aplicación está activa 1% del tiempo e idle 99%, ¿cuál es el consumo promedio?

### Problema 8.2
¿Cómo reducirías el consumo de un sistema que usa UART a 9600 baud?

### Problema 8.3
Un sensor envía datos cada 10 segundos. Diseña una estrategia de bajo consumo usando modos de sleep.

---

## Nivel 9: Diseño de Sistema

### Problema 9.1
Diseña la asignación de pines para un sistema con:
- 4 LEDs
- 2 botones con interrupción
- UART para debug
- I2C para sensor
- 1 entrada analógica

Usa un ATmega328P (28 pines).

### Problema 9.2
Dibuja el diagrama de bloques de un sistema de control de temperatura que incluya:
- Sensor de temperatura (analógico)
- Display de 7 segmentos (4 dígitos)
- Relé para calefactor
- Comunicación con PC

### Problema 9.3
¿Qué componentes externos necesita un MCU típico para funcionar? Dibuja el circuito mínimo.

---

## Nivel 10: Integración

### Problema 10.1
Un proyecto requiere:
- Lectura de 8 sensores analógicos cada 100 ms
- Control de 4 motores con PWM
- Comunicación I2C con memoria EEPROM
- Comunicación UART con módulo Bluetooth
- 2 entradas de interrupción externa
- Funcionamiento con batería de 3.7V

Selecciona un MCU apropiado, justifica tu elección y realiza:
a) Estimación de memoria necesaria
b) Cálculo de consumo
c) Asignación de pines

### Problema 10.2
Compara las siguientes opciones para un proyecto IoT:
- ATmega328P + módulo WiFi externo
- ESP32 (WiFi integrado)
- STM32 + módulo LoRa

Considera: costo, consumo, alcance, complejidad.

### Problema 10.3
Diseña la arquitectura de software (diagrama de flujo y estructura de archivos) para un sistema que:
- Lee temperatura y humedad cada segundo
- Muestra valores en LCD
- Envía datos por UART cada 10 segundos
- Responde a comandos recibidos por UART
- Activa alarma si temperatura > umbral

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre arquitectura de microcontroladores
RESPUESTAS: Ver archivo solutions/MCU-01-Respuestas.md
HERRAMIENTAS: Datasheets, calculadora
-->
