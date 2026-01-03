<!--
::METADATA::
type: reference
topic_id: mcu-06-protocolos-i2c-spi
file_id: resumen-i2c-spi
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, I2C, SPI]
search_keywords: "resumen I2C SPI cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./03-06-Intro.md)

---

# 📋 Cheatsheet: I2C y SPI

## I2C

- START: SDA↓ mientras SCL=1
- STOP: SDA↑ mientras SCL=1
- ACK: SDA=0 en 9º pulso
- Dirección 7b + R/W
- Pull-ups típicos: 2.2k-10k

**Frecuencia:**
$$F_{SCL} = \frac{F_{CPU}}{16 + 2\,TWBR\,4^{Presc}}$$

## SPI

- Líneas: SCK, MOSI, MISO, CS
- Modo = CPOL/CPHA
- Prescalers AVR: /4, /16, /64, /128 (+SPI2X /2)
- Full duplex

**Frecuencia:**
$$f_{SPI} = \frac{F_{CPU}}{Prescaler} (\times 2\ si\ SPI2X)$$

## Modos SPI

| Modo | CPOL | CPHA | Muestreo |
|------|------|------|----------|
| 0 | 0 | 0 | Subida |
| 1 | 0 | 1 | Bajada |
| 2 | 1 | 0 | Bajada |
| 3 | 1 | 1 | Subida |

## Dirección I2C

- SLA+W = (addr<<1)|0
- SLA+R = (addr<<1)|1

## Secuencia Read Reg (I2C)
```
START → SLA+W → REG → RESTART → SLA+R → DATA → STOP
```

## CS en SPI

- CS LOW selecciona esclavo
- Desactivar CS tras transferencias
- Un CS por esclavo

## Debug Rápido

- I2C: mirar ACK/NACK, flancos lentos = pull-up alto
- SPI: verificar modo CPOL/CPHA y nivel de CS

---

<!-- IA_CONTEXT
TIPO: Referencia rápida I2C/SPI
-->
