<!--
::METADATA::
type: problem
topic_id: mcu-07-aplicaciones
file_id: problemas-aplicaciones
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, proyecto, integración]
search_keywords: "problemas aplicaciones microcontroladores"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-07-Metodos-Aplicaciones.md) | [Respuestas →](../solutions/MCU-07-Respuestas.md)

---

# Problemas: Aplicaciones

## Nivel 1: Diseño

1.1 Define los bloques principales de un termostato con MCU.

1.2 ¿Qué periféricos usarías para leer un sensor de temperatura analógico y controlar un ventilador?

1.3 ¿Qué información mínima pondrías en un log por UART?

---

## Nivel 2: Energía

2.1 Lista tres técnicas para reducir consumo en reposo.

2.2 ¿Qué modo de sleep elegirías para despertar por interrupción externa?

2.3 ¿Cómo afecta bajar F_CPU al consumo y al tiempo de ejecución?

---

## Nivel 3: Scheduler

3.1 Diseña tareas y periodos para: sensado (50ms), control (50ms), comunicación (200ms).

3.2 ¿Qué pasa si una tarea tarda más que su periodo?

3.3 ¿Cómo detectar sobrecarga de CPU en un superloop?

---

## Nivel 4: Integración de Comunicaciones

4.1 ¿Qué protocolo usarías para un sensor lento y por qué (I2C vs SPI)?

4.2 ¿Qué protocolo para una pantalla rápida? Justifica.

4.3 ¿Cómo proteges la comunicación UART contra corrupción de datos?

---

## Nivel 5: Robustez

5.1 ¿Cuándo habilitarías el watchdog y cómo lo alimentarías?

5.2 Estrategia para manejar timeouts en lecturas I2C.

5.3 ¿Qué chequear antes de activar una carga de potencia (motor)?

---

## Nivel 6: Sensado y Calibración

6.1 Diseña un flujo para calibrar un sensor con dos puntos.

6.2 ¿Por qué promediar lecturas ADC y cuándo usar mediana?

6.3 ¿Cómo manejarías un sensor que ocasionalmente entrega lecturas fuera de rango?

---

## Nivel 7: Control y Actuación

7.1 Esboza un control proporcional simple para temperatura → PWM ventilador.

7.2 ¿Qué frecuencia de PWM usarías para motor DC vs LED?

7.3 ¿Cómo sincronizar multiplexado de display 7 segmentos con refresco sin parpadeo?

---

## Nivel 8: Debug y Logs

8.1 Diseña formato de log CSV: tiempo, temp, setpoint, PWM.

8.2 ¿Cómo medirías jitter de un timer de 1ms?

8.3 ¿Qué variable monitorearías para detectar cuelgues en ISR?

---

## Nivel 9: Integración Multibús

9.1 Mezcla I2C (sensores) y SPI (Flash) con UART debug. Define prioridad de tareas.

9.2 Estrategia para evitar que SPI bloquee la lectura de sensores I2C críticos.

9.3 ¿Cómo verificar integridad de datos guardados en Flash?

---

## Nivel 10: Proyecto Final

10.1 Diseña un data logger portátil:
- Sensores: temp, humedad (I2C), acelerómetro (I2C)
- Almacenamiento: Flash SPI
- UI: UART comandos
- Energía: dormir entre muestras

Incluye periodos, tamaño de buffers y estrategia de ahorro de energía.

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios de integración final
RESPUESTAS: Ver solutions/MCU-07-Respuestas.md
-->
