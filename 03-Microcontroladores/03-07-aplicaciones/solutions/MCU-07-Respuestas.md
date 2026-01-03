<!--
::METADATA::
type: solution
topic_id: mcu-07-aplicaciones
file_id: respuestas-aplicaciones
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, proyectos, integración]
search_keywords: "respuestas aplicaciones microcontroladores"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-07-Problemas.md)

---

# Respuestas: Aplicaciones

## Nivel 1

1.1 Bloques: sensor temp, ADC, control PWM, actuador (ventilador), UI (botones/UART), fuente.

1.2 ADC para sensor; PWM + transistor/MOSFET para ventilador; GPIO para botones.

1.3 Timestamp, variable(s) medidas, estado, checksum opcional.

---

## Nivel 2

2.1 Bajar F_CPU, sleep modes, apagar periféricos, apagar LEDs.

2.2 Modo "external interrupt" (p.ej. INT0 wake). En AVR: Power-down con INTx.

2.3 Baja consumo, pero aumenta tiempo de ejecución → menos throughput.

---

## Nivel 3

3.1 Tareas: sense(50ms), control(50ms), comm(200ms). Usar tick 1ms y comparar.

3.2 Acumula atraso (deriva); puede perder deadlines; usar watchdog o medir tiempos.

3.3 Medir tiempo de loop y compararlo con periodo; si loop > periodo, sobrecarga.

---

## Nivel 4

4.1 I2C: simple, 2 hilos, suficiente para sensores lentos.

4.2 SPI: más rápido para displays; full duplex; menor latencia.

4.3 Añadir checksum/CRC; protocolo con ACK; timeouts; repetir si error.

---

## Nivel 5

5.1 Habilitar después de init estable; alimentar en tareas críticas o tick principal.

5.2 Definir timeout; si expira, STOP + reinit bus; reintentos limitados.

5.3 Revisar alimentación, polaridad, protecciones (diodos), temperatura del driver.

---

## Nivel 6

6.1 Medir en punto bajo y alto; guardar raw_min/raw_max; interpolar lineal.

6.2 Promedio reduce ruido; mediana útil si hay outliers.

6.3 Descartar outliers (ventana); usar saturación a rangos válidos; contar eventos erróneos.

---

## Nivel 7

7.1 PWM = Kp*(error); saturar 0-100%; ejemplo: Kp=2%/°C.

7.2 Motor: 10-20 kHz; LED: 500 Hz-2 kHz.

7.3 Usar timer dedicado; multiplexar >200 Hz total; duty por dígito para brillo.

---

## Nivel 8

8.1 CSV: "t_ms,temp,set,pwm\n".

8.2 Medir tiempo entre ticks con captura; calcular jitter = stddev(tick).

8.3 Contar exec de ISR por segundo; si cae abruptamente, posible bloqueo.

---

## Nivel 9

9.1 Prioridad: 1) Sensores críticos; 2) Control; 3) Almacenamiento SPI; 4) UART.

9.2 No bloquear SPI; usar buffers y ejecutar en huecos; limitar duración de transacciones.

9.3 Guardar CRC por bloque; verificar al leer; manejar sectores defectuosos.

---

## Nivel 10

10.1 Ejemplo: muestreo cada 1s; sensores I2C; guardar frame de 16B en buffer; cada 64 muestras, escribir página SPI; dormir en power-down entre muestras; UART solo bajo comando para ahorrar energía.

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas de integración
-->
