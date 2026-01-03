<!--
::METADATA::
type: solution
topic_id: mcu-06-protocolos-i2c-spi
file_id: respuestas-i2c-spi
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, I2C, SPI]
search_keywords: "respuestas I2C SPI"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-06-Problemas.md)

---

# Respuestas: I2C y SPI

## Nivel 1

1.1 I2C: SCL (reloj), SDA (datos). Ambos bidireccionales con open-drain.

1.2 I2C usa open-drain + pull-ups; SPI usa push-pull (requiere CS por esclavo).

1.3 Open-drain: los nodos solo tiran a LOW; el HIGH lo fija la resistencia de pull-up.

---

## Nivel 2

2.1 Causas: sin pull-up adecuado; dirección incorrecta; bus ocupado; alimentación/masa faltante; velocidad fuera de rango.

2.2 SLA+W = 0x50 << 1 | 0 = 0xA0.

2.3 El maestro envía NACK (SDA=1 en 9º pulso) y luego STOP.

---

## Nivel 3

3.1 TWBR ≈ ((16MHz/400k) - 16)/2 = (40 - 16)/2 = 12.

3.2 f_SPI = 16MHz / 16 = 1MHz.

3.3 SPI 1MHz (10 bits ≈ 10µs) vs I2C 400k (9 bits/byte ≈ 22.5µs). SPI es más rápido.

---

## Nivel 4

4.1 CPOL=0, CPHA=1 → reloj idle en LOW; datos muestreados en flanco de bajada, cambian en subida.

4.2 Modo 3: CPOL=1, CPHA=1.

4.3 Los bits se muestrean en flanco incorrecto → datos corruptos.

---

## Nivel 5

5.1 Código típico (pseudoc):
```
i2c_start(addr<<1 | W);
i2c_write(reg);
i2c_start(addr<<1 | R);
val = i2c_read_nack();
i2c_stop();
```

5.2
```
uint8_t a = spi_transfer(tx1);
uint8_t b = spi_transfer(tx2);
// a,b contienen bytes recibidos simultáneamente
```

5.3 Porque cada esclavo requiere línea dedicada para ser seleccionado; evita que todos respondan a la vez.

---

## Nivel 6

6.1 2.2k-10k. Depende de capacidad de bus, longitud de cables, corriente de hundimiento de nodos.

6.2 Ambos esclavos activos simultáneamente → colisión en MISO; datos corruptos.

6.3 SPI es rápido; cables largos inducen ruido y desfase. GND común evita referencias flotantes.

---

## Nivel 7

7.1 Sin pulldown: flancos lentos, niveles indefinidos, NACK aleatorios, bus bloqueado en LOW.

7.2 Bit de estado de arbitraje en TWSR (p.ej. 0x38). O TWCR con TWINT y TWSTA set sin avance.

7.3 Revisar CS (baja correctamente), modo (CPOL/CPHA), reloj presente, MISO flotante.

---

## Nivel 8

8.1 Secuencia TMP102: START → SLA+W (0x48<<1|0) → reg=0x00 → RESTART → SLA+R → leer MSB (ACK) → leer LSB (NACK) → STOP.

8.2 LIS3DH SPI: CS LOW → cmd = 0x80 | 0x40 | OUT_X_L (lectura + auto-increment) → leer 6 bytes → CS HIGH.

8.3 Usar CS independiente; desactivar CS antes de cambiar dispositivo; respetar t_CS y t_SCLK off; esperar busy si aplica.

---

## Nivel 9

9.1 UART recibe comando → parsea addr/reg → i2c_read_reg → responde por UART con dato.

9.2 Tarea periódica 100 Hz lee I2C; buffer; tarea SPI escribe a Flash en páginas; usar flags y mutex/CS.

9.3 Reintentos (3); si falla, emitir STOP y reinit bus; timeout por byte; si se cuelga SDA LOW, togglear SCL para liberar.

---

## Nivel 10

10.1 Prios: 1) Sondeo presión/humedad cada 1s (I2C 100k suficiente); 2) Display SPI refresco 5-10 Hz; 3) UART debug a 115200 para logs; Pull-ups I2C ~4.7k; CS separados por dispositivo SPI.

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas a ejercicios I2C/SPI
-->
