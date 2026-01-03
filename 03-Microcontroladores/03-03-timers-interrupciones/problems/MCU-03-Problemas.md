<!--
::METADATA::
type: problem
topic_id: mcu-03-timers-interrupciones
file_id: problemas-timers
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, microcontrolador, timer, interrupción, PWM]
search_keywords: "ejercicios, problemas, timer, interrupción"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-03-Metodos-Timers.md) | [Respuestas →](../solutions/MCU-03-Respuestas.md)

---

# Problemas: Timers e Interrupciones

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Cuál es la diferencia entre un Timer y un Counter?

### Problema 1.2
¿Qué es un prescaler y por qué es necesario?

### Problema 1.3
Un timer de 8 bits cuenta de 0 a 255. ¿Cuántos valores diferentes puede tener?

---

## Nivel 2: Cálculos de Timer

### Problema 2.1
Con F_CPU = 16 MHz y prescaler = 64, ¿cuánto tiempo representa cada incremento del timer?

### Problema 2.2
Calcula el valor de OCR necesario para generar una interrupción cada 10 ms con:
- F_CPU = 16 MHz
- Timer de 16 bits
- Prescaler = 64

### Problema 2.3
¿Cuál es el período máximo que puede medir un Timer de 8 bits con F_CPU = 8 MHz y prescaler = 1024?

---

## Nivel 3: Configuración de Timer

### Problema 3.1
Escribe el código para configurar Timer0 en modo CTC con OCR0A = 124 y prescaler /64.

### Problema 3.2
¿Qué valores deben tener WGM02, WGM01, WGM00 para modo Fast PWM con TOP = 0xFF?

### Problema 3.3
Configura Timer1 para generar una interrupción por overflow con prescaler /256.

---

## Nivel 4: Interrupciones

### Problema 4.1
¿Por qué las variables compartidas entre ISR y main() deben ser `volatile`?

### Problema 4.2
¿Qué problema tiene este código?
```c
ISR(TIMER0_OVF_vect) {
    _delay_ms(100);
    PORTB ^= 0xFF;
}
```

### Problema 4.3
Escribe una ISR que incremente un contador cada vez que Timer0 hace overflow, y ponga un flag cuando llegue a 1000.

---

## Nivel 5: PWM

### Problema 5.1
¿Qué duty cycle tiene un PWM de 8 bits con OCR = 127?

### Problema 5.2
Configura PWM Fast en Timer0 canal A para:
- F_CPU = 16 MHz
- Frecuencia PWM ≈ 1 kHz
- Pin OC0A como salida

### Problema 5.3
¿Cuál es la resolución efectiva de PWM si usas Timer1 de 16 bits pero solo necesitas frecuencia de 50 Hz?

---

## Nivel 6: Aplicaciones de Timer

### Problema 6.1
Diseña un sistema que haga parpadear un LED a exactamente 2 Hz usando Timer1.

### Problema 6.2
Implementa una función `millis()` que retorne el tiempo en milisegundos desde el inicio.

### Problema 6.3
Crea un generador de onda cuadrada de 440 Hz (nota La) usando toggle de pin.

---

## Nivel 7: PWM Aplicado

### Problema 7.1
Implementa control de brillo de LED con PWM:
- Brillo controlado por potenciómetro (ADC)
- Rango de 0% a 100%

### Problema 7.2
Diseña control de velocidad de motor DC:
- Entrada: valor 0-255 por UART
- Salida: PWM proporcional

### Problema 7.3
Implementa control de servo:
- Pulso de 1 ms a 2 ms
- Período de 20 ms
- Entrada: ángulo 0-180°

---

## Nivel 8: Input Capture

### Problema 8.1
¿Para qué sirve el modo Input Capture de un timer?

### Problema 8.2
Implementa medición de frecuencia usando Input Capture:
- Medir período de señal externa
- Calcular frecuencia en Hz

### Problema 8.3
Diseña un medidor de ancho de pulso para señal RC (1-2 ms).

---

## Nivel 9: Watchdog y Modos de Bajo Consumo

### Problema 9.1
¿Qué es el Watchdog Timer y cuándo se usa?

### Problema 9.2
Configura el WDT para resetear el MCU si no hay actividad en 2 segundos.

### Problema 9.3
Diseña un sistema que duerma y despierte cada segundo usando el WDT.

---

## Nivel 10: Proyectos Integradores

### Problema 10.1
Diseña un reloj digital usando timers:
- Display de 4 dígitos 7 segmentos multiplexado
- Precisión de 1 segundo
- Botones para ajustar hora/minutos

### Problema 10.2
Implementa un cronómetro:
- Resolución de 10 ms
- Botón Start/Stop
- Botón Reset
- Display muestra MM:SS.dd

### Problema 10.3
Diseña un sistema de control de temperatura:
- Lee sensor cada 100 ms
- Control PWM de ventilador
- PID simple (proporcional)
- UART para monitoreo

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre timers e interrupciones
RESPUESTAS: Ver archivo solutions/MCU-03-Respuestas.md
HERRAMIENTAS: AVR-GCC, osciloscopio, simulador
-->
