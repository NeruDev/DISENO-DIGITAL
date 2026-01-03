<!--
::METADATA::
type: solution_index
topic_id: mcu-06-protocolos-i2c-spi
file_id: solucion-index-i2c-spi
status: complete
audience: student
last_updated: 2026-01-03
tags: [soluciones, MCU, I2C, SPI, bus, índice]
-->

> 🏠 **Navegación:** [← Respuestas Rápidas](../MCU-06-Respuestas.md) | [Problemas →](../../problems/MCU-06-Problemas.md)

---

# Soluciones Detalladas: Protocolos I2C y SPI (MCU-06)

## Estructura de Niveles de Solución

| Nivel | Ubicación | Contenido |
|:-----:|-----------|-----------|
| **1** | `MCU-06-Respuestas.md` | Respuestas directas |
| **2** | Esta carpeta (`prob-01/`) | Código y análisis |
| **3** | Secciones "Conceptos Clave" | Teoría de protocolos |

---

## Índice de Soluciones Detalladas

### Nivel 1-2: Conceptos y Direccionamiento ⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 1.1 | Hilos I2C | En respuestas |
| 1.2 | Diferencia I2C vs SPI | En respuestas |
| 1.3 | Open-drain | En respuestas |
| 2.1 | Diagnóstico NACK | En respuestas |
| 2.2 | Dirección 8-bit | En respuestas |

### Nivel 3-4: Timing y Modos SPI ⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 3.1 | Cálculo TWBR | [MCU-06-Sol-Problema-3.1.md](./MCU-06-Sol-Problema-3.1.md) |
| 3.2 | Frecuencia SPI | En respuestas |
| 4.1 | CPOL/CPHA | [MCU-06-Sol-Problema-4.1.md](./MCU-06-Sol-Problema-4.1.md) |
| 4.2 | Modo SPI 3 | En respuestas |

### Nivel 5-6: Código y Hardware ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 5.1 | Lectura registro I2C | En respuestas |
| 5.2 | Transferencia SPI | En respuestas |
| 6.1 | Valores pull-up | En respuestas |
| 6.2 | Conflicto CS | En respuestas |

### Nivel 7-10: Debug y Aplicaciones ⭐⭐⭐

| # | Problema | Archivo |
|:-:|----------|---------|
| 7.1 | Síntomas pull-up | En respuestas |
| 8.1 | Secuencia TMP102 | En respuestas |
| 9.1 | Puente UART-I2C | En respuestas |
| 10.1 | Estación meteorológica | En respuestas |

---

## Referencia Rápida

### Comparativa I2C vs SPI

| Característica | I2C | SPI |
|----------------|:---:|:---:|
| **Hilos** | 2 (SDA, SCL) | 4+ (MOSI, MISO, SCK, CS) |
| **Velocidad** | 100k-400k-1M | Hasta 50 MHz |
| **Direccionamiento** | Por dirección (7-bit) | Por línea CS |
| **Tipo de línea** | Open-drain | Push-pull |
| **Pull-ups** | Requeridos | No necesarios |
| **Multi-master** | Sí | Complejo |
| **Distancia** | Corta (~1m) | Muy corta (~30cm) |
| **Complejidad** | Media | Baja |

### Diagrama I2C

```
         VCC
          │
         ┌┴┐ ┌┴┐
    Rp   │ │ │ │  Rp (4.7kΩ típico)
         └┬┘ └┬┘
          │   │
 Master ──┴───┴── SDA ───┬─── Slave 1 (0x50)
          │              ├─── Slave 2 (0x68)
 Master ──────── SCL ────┴─── Slave 3 (0x3C)
```

### Diagrama SPI

```
              ┌──────────┐
              │  Master  │
              │   MCU    │
              └────┬─────┘
                   │
      ┌────────────┼────────────┐
      │            │            │
   ┌──┴──┐     ┌───┴──┐     ┌───┴──┐
   │CS0  │     │CS1   │     │CS2   │
   ├─────┤     ├──────┤     ├──────┤
   │Slave│     │Slave │     │Slave │
   │  1  │     │  2   │     │  3   │
   └──┬──┘     └───┬──┘     └───┬──┘
      │            │            │
      └────────────┼────────────┘
                   │
              MOSI ┼ MISO ┼ SCK (compartidos)
```

### Modos SPI (CPOL/CPHA)

```
          CPOL=0               CPOL=1
    SCK idle LOW          SCK idle HIGH

    CPHA=0 (Modo 0)       CPHA=0 (Modo 2)
    ┌─┐   ┌─┐             ─┐ ┌───┐ ┌───
    │ │   │ │              │ │   │ │
    ┘ └───┘ └───          ─┘ └───┘ └───
    ↑     ↑               ↑     ↑
  Sample               Sample

    CPHA=1 (Modo 1)       CPHA=1 (Modo 3)
    ┌─┐   ┌─┐             ─┐ ┌───┐ ┌───
    │ │   │ │              │ │   │ │
    ┘ └───┘ └───          ─┘ └───┘ └───
      ↑     ↑               ↑     ↑
    Sample               Sample
```

| Modo | CPOL | CPHA | Flanco de muestreo |
|:----:|:----:|:----:|:------------------:|
| 0 | 0 | 0 | Subida |
| 1 | 0 | 1 | Bajada |
| 2 | 1 | 0 | Bajada |
| 3 | 1 | 1 | Subida |

### Secuencia I2C

```
START → ADDR+W → ACK → REG → ACK → DATA → ACK → STOP
  │        │       │     │     │      │     │      │
  └────────┴───────┴─────┴─────┴──────┴─────┴──────┘
       Master envía              Slave responde
```

### Fórmulas

| Concepto | Fórmula |
|----------|---------|
| I2C TWBR | $TWBR = \frac{f_{CPU} - 16 \times f_{I2C}}{2 \times Prescaler \times f_{I2C}}$ |
| SPI freq | $f_{SPI} = \frac{f_{CPU}}{Prescaler}$ |

---

## Navegación

| Anterior | Arriba | Siguiente |
|:--------:|:------:|:---------:|
| [UART](../../../03-05-comunicacion-serial/solutions/prob-01/) | [Módulo MCU](../../00-Index.md) | [Aplicaciones](../../../03-07-aplicaciones/solutions/prob-01/) |
