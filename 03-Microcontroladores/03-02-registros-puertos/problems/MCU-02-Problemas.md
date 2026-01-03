<!--
::METADATA::
type: problem
topic_id: mcu-02-registros-puertos
file_id: problemas-gpio
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, microcontrolador, GPIO, puertos]
search_keywords: "ejercicios, problemas, GPIO, puertos"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-02-Metodos-GPIO.md) | [Respuestas →](../solutions/MCU-02-Respuestas.md)

---

# Problemas: Registros y Puertos GPIO

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Qué significan las siglas GPIO?

### Problema 1.2
En un AVR, ¿cuáles son los tres registros asociados a cada puerto GPIO?

### Problema 1.3
¿Por qué se necesitan resistencias pull-up en entradas de botones?

---

## Nivel 2: Configuración de Dirección

### Problema 2.1
Escribe el código AVR para configurar:
- PB0, PB1, PB2 como salidas
- PB3, PB4 como entradas con pull-up
- PB5-PB7 como entradas sin pull-up

### Problema 2.2
¿Qué valor debe tener DDRB para que los pines pares sean salidas y los impares entradas?

### Problema 2.3
Un pin configurado como entrada tiene DDRx = 0 y PORTx = 1. ¿Qué significa esto?

---

## Nivel 3: Escritura de Salidas

### Problema 3.1
Escribe código AVR para:
a) Poner PB3 en HIGH
b) Poner PB3 en LOW
c) Invertir (toggle) PB3
Sin modificar los otros bits de PORTB.

### Problema 3.2
¿Cuál es el problema con este código en una ISR?
```c
PORTB |= (1 << PB0);
```

### Problema 3.3
¿Cómo se hace un toggle atómico en AVR moderno?

---

## Nivel 4: Lectura de Entradas

### Problema 4.1
Escribe código para leer el estado de PD2 y guardarlo en una variable.

### Problema 4.2
Un botón está conectado entre PB0 y GND con pull-up activo. ¿Qué valor lee PINB cuando el botón está presionado?

### Problema 4.3
Escribe una función que espere hasta que PD3 cambie de LOW a HIGH.

---

## Nivel 5: Manipulación de Bits

### Problema 5.1
¿Qué hace cada una de estas operaciones?
```c
a) PORTB |= 0x0F;
b) PORTB &= 0xF0;
c) PORTB ^= 0x55;
d) PORTB = (PORTB & 0xF0) | 0x05;
```

### Problema 5.2
Escribe una macro para establecer múltiples bits a la vez.

### Problema 5.3
Dado `PINC = 0b10110100`, escribe expresiones para extraer:
a) Los 4 bits bajos
b) Los 4 bits altos
c) El bit 5 solamente

---

## Nivel 6: Aplicación LED

### Problema 6.1
Diseña un sistema con 8 LEDs en PORTB que muestre un patrón de "luz que viaja" (un LED encendido que se mueve de izquierda a derecha).

### Problema 6.2
Modifica el programa anterior para que la luz rebote en los extremos.

### Problema 6.3
Implementa un contador binario visible en 4 LEDs (PB0-PB3) que incremente cada segundo.

---

## Nivel 7: Aplicación Botones

### Problema 7.1
Implementa debounce por software para un botón en PD2. La función debe retornar 1 solo cuando detecta una pulsación válida.

### Problema 7.2
Diseña un sistema donde:
- Botón 1 (PD2) incrementa un contador
- Botón 2 (PD3) decrementa el contador
- El contador se muestra en 4 LEDs (PB0-PB3)

### Problema 7.3
Implementa detección de pulsación corta vs larga (>2 segundos) para un botón.

---

## Nivel 8: Display 7 Segmentos

### Problema 8.1
¿Qué valor debe tener PORTB para mostrar el número "5" en un display de 7 segmentos de cátodo común conectado a PB0(a)-PB6(g)?

### Problema 8.2
Diseña el código para multiplexar 4 displays de 7 segmentos mostrando un número de 0000 a 9999.

### Problema 8.3
Implementa un reloj digital (MM:SS) usando 4 displays multiplexados.

---

## Nivel 9: Teclado Matricial

### Problema 9.1
Explica cómo funciona el escaneo de un teclado matricial 4x4.

### Problema 9.2
Escribe el código para detectar qué tecla está presionada en una matriz 4x4.

### Problema 9.3
Implementa un sistema de ingreso de PIN de 4 dígitos con teclado matricial.

---

## Nivel 10: Proyecto Integrador

### Problema 10.1
Diseña un sistema de cerradura electrónica con:
- Teclado matricial 4x3 para ingresar código
- LED verde (correcto) y rojo (incorrecto)
- 3 intentos antes de bloqueo de 30 segundos
- Display de 7 segmentos mostrando intentos restantes

### Problema 10.2
Diseña un "Simon Says" con:
- 4 LEDs de colores (PB0-PB3)
- 4 botones correspondientes (PD0-PD3)
- Secuencia aleatoria que incrementa
- Display mostrando nivel actual

### Problema 10.3
Implementa un medidor de tiempo de reacción:
- LED se enciende en momento aleatorio
- Usuario presiona botón lo más rápido posible
- Muestra tiempo en ms en display de 4 dígitos
- Guarda mejor tiempo en memoria

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre GPIO y puertos
RESPUESTAS: Ver archivo solutions/MCU-02-Respuestas.md
HERRAMIENTAS: AVR-GCC, simulador Proteus
-->
