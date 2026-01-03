<!--
::METADATA::
type: detailed_solution
topic_id: mcu-06-protocolos-i2c-spi
problem_id: 4.1
file_id: solucion-problema-4-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, MCU, SPI, CPOL, CPHA, modos]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 4.2 →](./MCU-06-Sol-Problema-4.2.md)

---

# Solución Detallada: Problema 4.1

## Enunciado
¿Qué significan CPOL=0, CPHA=1 en términos de flancos de muestreo?

---

## Respuesta Directa

- **CPOL = 0:** El reloj (SCK) está en **LOW** cuando está inactivo
- **CPHA = 1:** Los datos se **muestrean en el segundo flanco** (bajada)

Esto corresponde al **Modo SPI 1**.

---

## Análisis Detallado

### CPOL (Clock Polarity)

| CPOL | Estado Idle de SCK |
|:----:|:------------------:|
| 0 | LOW (0) |
| 1 | HIGH (1) |

### CPHA (Clock Phase)

| CPHA | Muestreo de datos |
|:----:|:-----------------:|
| 0 | Primer flanco (leading edge) |
| 1 | Segundo flanco (trailing edge) |

---

## Diagrama de Modo 1 (CPOL=0, CPHA=1)

```
         ┌───────────────── Período de bit ─────────────────┐
         │                                                   │
SCK      │  ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐         │
(CPOL=0) └──┘   └───┘   └───┘   └───┘   └───┘   └─────────
         │                                                   │
         │ ↑   ↓   ↑   ↓   ↑   ↓   ↑   ↓                   │
         │ │   │   │   │   │   │   │   │                   │
         │ │   S   │   S   │   S   │   S   ← Muestreo       │
         │                                   (CPHA=1)       │
         │                                                   │
MOSI/    ─┬───────┬───────┬───────┬───────┬───────          │
MISO     │  D7   │  D6   │  D5   │  D4   │...              │
         └───────┴───────┴───────┴───────┴─────            │
              ↑       ↑       ↑       ↑                     │
         Cambio en flanco de subida                         │
         Muestreo en flanco de bajada                       │
```

### Secuencia de Eventos

1. **SCK idle en LOW** (CPOL=0)
2. **Primer flanco (subida):** El transmisor **cambia** el dato
3. **Segundo flanco (bajada):** El receptor **muestrea** el dato
4. Repetir para cada bit

---

## Los 4 Modos SPI

| Modo | CPOL | CPHA | Flanco de muestreo | Dispositivos típicos |
|:----:|:----:|:----:|:------------------:|---------------------|
| **0** | 0 | 0 | Subida (primero) | SD Cards, muchos sensores |
| **1** | 0 | 1 | Bajada (segundo) | Algunos ADCs |
| **2** | 1 | 0 | Bajada (primero) | - |
| **3** | 1 | 1 | Subida (segundo) | MAX31855, algunos displays |

---

## Diagramas Comparativos

### Modo 0 (CPOL=0, CPHA=0)

```
SCK      ───┐   ┌───┐   ┌───┐   ┌───
            └───┘   └───┘   └───┘
               ↑       ↑       ↑    ← Muestreo en subida
Data     ───┬───────┬───────┬───────
            │  Bit  │  Bit  │  Bit
```

### Modo 1 (CPOL=0, CPHA=1) ← **Este problema**

```
SCK      ───┐   ┌───┐   ┌───┐   ┌───
            └───┘   └───┘   └───┘
                ↓       ↓       ↓   ← Muestreo en bajada
Data     ─────┬───────┬───────┬─────
              │  Bit  │  Bit  │
```

### Modo 2 (CPOL=1, CPHA=0)

```
SCK      ───┐   ┌───┐   ┌───┐   ┌───
            └───┘   └───┘   └───┘
            ↓       ↓       ↓       ← Muestreo en bajada
Data     ───┬───────┬───────┬───────
            │  Bit  │  Bit  │
```

### Modo 3 (CPOL=1, CPHA=1)

```
SCK      ───┐   ┌───┐   ┌───┐   ┌───
            └───┘   └───┘   └───┘
               ↑       ↑       ↑    ← Muestreo en subida
Data     ─────┬───────┬───────┬─────
              │  Bit  │  Bit  │
```

---

## Configuración en AVR

```c
#include <avr/io.h>

void spi_init_mode1(void) {
    // Configurar pines: MOSI, SCK como salida
    DDRB |= (1 << PB3) | (1 << PB5);  // MOSI, SCK
    DDRB &= ~(1 << PB4);              // MISO entrada
    
    // Configurar SPI: Master, Modo 1
    SPCR = (1 << SPE)    // SPI Enable
         | (1 << MSTR)   // Master mode
         | (0 << CPOL)   // CPOL = 0 (idle LOW)
         | (1 << CPHA)   // CPHA = 1 (segundo flanco)
         | (1 << SPR0);  // Prescaler /16
}

uint8_t spi_transfer(uint8_t data) {
    SPDR = data;                    // Enviar dato
    while (!(SPSR & (1 << SPIF)));  // Esperar fin
    return SPDR;                    // Retornar dato recibido
}
```

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **Leading edge** | Primer flanco desde estado idle |
| **Trailing edge** | Segundo flanco, regresa a idle |
| **Setup time** | Tiempo antes del muestreo |
| **Hold time** | Tiempo después del muestreo |

---

## ¿Qué pasa si los modos no coinciden?

Si maestro y esclavo usan modos diferentes:

| Problema | Consecuencia |
|----------|--------------|
| CPOL diferente | Datos invertidos o corridos |
| CPHA diferente | Muestreo en momento incorrecto |
| Ambos diferentes | Datos completamente corruptos |

```
Esperado (correcto):    0x5A = 0101 1010
Recibido (modo erróneo): 0xB4 = 1011 0100 (corrido 1 bit)
```

---

## Verificación en Analizador Lógico

Para verificar Modo 1:
1. SCK debe estar en **LOW** entre transferencias
2. Los datos deben **cambiar** en flancos de **subida**
3. Los datos deben ser **válidos** en flancos de **bajada**

---

> 💡 **Tip:** Siempre consulta el datasheet del dispositivo esclavo para conocer el modo SPI requerido. Si no está explícito, busca "CPOL" y "CPHA" o el diagrama de timing.
