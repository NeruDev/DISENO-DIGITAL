<!--
::METADATA::
type: problem
topic_id: mcu-06-protocolos-i2c-spi
file_id: problemas-i2c-spi
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, I2C, SPI, bus, comunicación]
search_keywords: "problemas I2C SPI"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-06-Metodos-I2C-SPI.md) | [Respuestas →](../solutions/MCU-06-Respuestas.md)

---

# Problemas: I2C y SPI

## Nivel 1: Conceptos

1.1 ¿Cuántos hilos usa I2C y qué función cumple cada uno?

1.2 ¿Qué diferencia eléctrica clave hay entre I2C y SPI?

1.3 ¿Qué significa que I2C usa líneas open-drain?

---

## Nivel 2: Dirección y ACK

2.1 Un sensor I2C con dirección 0x68 no responde (NACK). Lista 3 causas probables.

2.2 ¿Qué dirección de 8 bits se envía para un write a un dispositivo con dirección 7-bit 0x50?

2.3 ¿Qué hace un dispositivo cuando quiere NACKear el último byte leído?

---

## Nivel 3: Timing

3.1 Calcula TWBR para F_CPU=16MHz, I2C=400kHz, prescaler=1.

3.2 Si SPI usa prescaler /16 con F_CPU=16MHz, ¿cuál es f_SPI?

3.3 Para 8N1 a 115200, ¿quién es más rápido transfiriendo 1 byte: I2C 400k o SPI 1MHz?

---

## Nivel 4: CPOL/CPHA

4.1 ¿Qué significan CPOL=0, CPHA=1 en términos de flancos de muestreo?

4.2 Un dispositivo requiere modo SPI 3. ¿Cuáles son CPOL y CPHA?

4.3 ¿Qué ocurre si maestro y esclavo difieren en CPOL/CPHA?

---

## Nivel 5: Código

5.1 Escribe una función que lea un registro de 8 bits por I2C (usa start, write reg, repeated start, read, stop).

5.2 Escribe una función que envíe dos bytes por SPI y reciba los dos bytes simultáneamente.

5.3 ¿Por qué es necesario controlar CS manualmente en SPI para múltiples esclavos?

---

## Nivel 6: Hardware

6.1 ¿Qué valores típicos de pull-up se usan en I2C y de qué depende su selección?

6.2 ¿Qué pasa si CS está siempre en LOW para dos esclavos SPI?

6.3 ¿Por qué es recomendable cablear GND común y cables cortos en SPI?

---

## Nivel 7: Debug

7.1 Lista 3 síntomas comunes de pull-up faltante o muy grande en I2C.

7.2 ¿Cómo detectar un error de "arbitration lost" en un micro maestro I2C?

7.3 ¿Qué revisar con el analizador lógico si un dispositivo SPI no responde?

---

## Nivel 8: Aplicaciones

8.1 Diseña la secuencia para leer temperatura de un sensor I2C (ej. TMP102): dirección, registro, bytes esperados.

8.2 Diseña la secuencia para leer 3 ejes de un IMU SPI (ej. LIS3DH): CS, comando de lectura, burst de 6 bytes.

8.3 ¿Cómo actualizarías a 3 dispositivos SPI sin interferencia? (pistas: CS, tiempo entre transacciones)

---

## Nivel 9: Integración

9.1 Implementa un puente: comando por UART → lee registro I2C y responde por UART.

9.2 Implementa logging de un acelerómetro I2C a 100 Hz y envía por SPI a una Flash externa.

9.3 Estrategia para manejar errores I2C: reintentos, reset de bus, timeout.

---

## Nivel 10: Proyecto

10.1 Diseña una estación meteorológica:
- I2C: sensor de presión
- I2C: sensor de humedad
- SPI: pantalla
- UART: debug
Incluye prioridades y frecuencias de sondeo.

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios progresivos sobre I2C/SPI
RESPUESTAS: Ver solutions/MCU-06-Respuestas.md
-->
