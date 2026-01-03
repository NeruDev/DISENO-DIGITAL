<!--
::METADATA::
type: reference
topic_id: mcu-07-aplicaciones
file_id: resumen-aplicaciones
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, integración, proyecto]
search_keywords: "resumen aplicaciones MCU cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-07-Intro.md)

---

# 📋 Cheatsheet: Aplicaciones Integradas

## Flujo de Proyecto

1) Traer-up: clock, GPIO, UART
2) Drivers: timers, ADC, I2C/SPI
3) Integración gradual
4) Pruebas y logs

## Scheduler Simple

```
if (now >= next_task) { tarea(); next += periodo; }
```

## Energía

- Bajar F_CPU cuando posible
- Sleep + wake por interrupción
- Apagar periféricos/LEDs
- Watchdog para recuperación

## Control PWM

- Motor: 10-20 kHz
- LED: 500-2 kHz
- Servo: 50 Hz, pulso 1-2 ms

## Calibración 2 Puntos

```
val_fis = (raw - raw_min) * (fis_max - fis_min) /
          (raw_max - raw_min) + fis_min
```

## Logs

- CSV: t_ms, vars, estado
- Añadir checksum si es crítico

## Robustez

- Timeouts en I/O
- Reintentos limitados
- Safe mode en fallas
- Brown-out detect si disponible

---

<!-- IA_CONTEXT
TIPO: Referencia rápida para integración de proyectos
-->
