<!--
::METADATA::
type: theory
topic_id: mcu-07-aplicaciones
file_id: teoria-aplicaciones
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [microcontrolador, proyecto, integración]
search_keywords: "aplicaciones microcontroladores, proyectos"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-07-Intro.md) | [Métodos →](../methods/MCU-07-Metodos-Aplicaciones.md)

---

# Aplicaciones Integradas con Microcontroladores

## 1. Enfoque de Sistema

1. Definir **requerimientos**: entradas, salidas, tiempos, consumo.
2. Seleccionar **MCU** y periféricos: GPIO, ADC, timers, UART/I2C/SPI.
3. Arquitectura de **software**: drivers, HAL, tareas.
4. **Plan de pruebas**: unitarias, integración, validación en hardware.

---

## 2. Arquitecturas de Software

- **Superloop**: bucle principal con tareas periódicas.
- **Cooperativo**: scheduler sencillo por ticks.
- **Preemptivo (RTOS)**: tareas con prioridad, timers de software, colas.

### Estados comunes

- INIT → RUN → ERROR → SAFE

---

## 3. Plan de Energía y Consumo

- Reducir F_CPU cuando sea posible.
- Apagar periféricos no usados.
- Usar modos sleep (idle, power-down) y wake-up por interrupción.
- LEDs/motores son mayores consumidores → PWM eficiente.

---

## 4. Sensado y Filtrado

- ADC con promedios/mediana.
- Filtros RC en entradas analógicas sensibles.
- Calibración de sensores (2 puntos o tabla).

---

## 5. Actuadores

- PWM para motores/LEDs/servos.
- H-bridge para motores DC (protección con diodos).
- MOSFET canal N para cargas: revisar Rds(on) y disipación.

---

## 6. Comunicación

- UART para debug/log.
- I2C para sensores lentos.
- SPI para memorias o displays.
- Considerar CRC/checksum en protocolos.

---

## 7. Seguridad y Robustez

- Watchdog para recuperación.
- Timeouts en I/O bloqueante.
- Debounce en entradas mecánicas.
- Detección de brown-out si MCU lo soporta.

---

## 8. Ejemplos de Aplicación

- Estación meteorológica: I2C sensores, SPI display, UART logs.
- Data logger: ADC + almacenamiento en Flash externa.
- Robot seguidor de línea: sensores analógicos, PWM motores, interrupciones para encoders.
- Termostato: ADC sensor, PWM ventilador, UI por UART o display.

---

## 9. Flujo de Desarrollo

1. Traer-up: clock, GPIO, UART debug.
2. Drivers: GPIO, timers, ADC, I2C/SPI.
3. Integración incremental: sensor → procesamiento → actuador.
4. Pruebas de estrés: ruido, temperatura, alimentación.

---

## 10. Métricas y Trazas

- Uso de CPU (%), latencia de ISR, jitter de timers.
- Uso de RAM (buffers), stack.
- Logs con timestamps (millis).

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: Todos los módulos previos
CONEXIONES: Proyectos finales, integración HW/SW
-->
