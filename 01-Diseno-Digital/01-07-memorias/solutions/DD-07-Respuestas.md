<!--
::METADATA::
type: solution
topic_id: dd-07-memorias
file_id: respuestas-memorias
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, memorias"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-07-Problemas.md)

---

# Respuestas: Memorias

## Nivel 1: Conceptos Básicos

### Respuestas 1.1

**a)** 2716 (2K × 8):
- Líneas de dirección: 11 ($2^{11}$ = 2048 = 2K)
- Capacidad: 2K × 8 = 16,384 bits = 16 Kbits

**b)** 6264 (8K × 8):
- Ubicaciones: 8,192
- Capacidad: 8K × 8 bits = 64 Kbits = 8 KB

**c)** 27C256: 256 Kbits = 32K × 8

### Respuestas 1.2

**a)** Ubicaciones: $2^{14}$ = 16,384 = 16K

**b)** Capacidad: 16K × 16 = 262,144 bits

**c)** En KB: 262,144 / 8 / 1024 = 32 KB

### Respuestas 1.3

**c)** Volátiles: SRAM, DRAM
    No volátiles: ROM, PROM, EPROM, EEPROM, Flash

---

## Nivel 2: Estructura Interna

### Respuestas 2.1

**a)** 4 líneas de dirección ($2^4$ = 16)

**b)** 4 líneas de datos

### Respuestas 2.2

**a)** SRAM: 6 transistores (flip-flop), DRAM: 1 transistor + 1 capacitor

**b)** El capacitor pierde carga por fugas, necesita reescribirse periódicamente

**c)** SRAM es más rápida porque no requiere ciclo de refresh

### Respuestas 2.3

**b)** Pines de control:
- $\overline{CE}$: Chip Enable
- $\overline{OE}$: Output Enable
- Vpp: Voltaje de programación

---

## Nivel 3: Expansión de Memoria

### Respuestas 3.1

**a)** 4 chips (4K/1K = 4)

**c)** Decodificación:
| A11 | A10 | Chip |
|-----|-----|------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 2 |
| 1 | 1 | 3 |

### Respuestas 3.2

**a)** 4 chips (16/4 = 4 bits/chip)

**b)** Todos comparten direcciones y control, cada uno maneja 4 bits de datos

### Respuestas 3.3

**a)** 8 chips:
- 8K/2K = 4 (expansión de palabras)
- 16/8 = 2 (expansión de bits)
- Total: 4 × 2 = 8 chips

---

## Nivel 4: Decodificación de Direcciones

### Respuestas 4.1

**a)** A15: 0=RAM, 1=ROM

**b)** 
- $\overline{CS_{RAM}}$ = A15
- $\overline{CS_{ROM}}$ = $\overline{A15}$

### Respuestas 4.2

**a)** Bits A15, A14, A13

**b)** Ecuaciones:
- RAM: $\overline{A15} \cdot \overline{A14}$
- I/O: $\overline{A15} \cdot A14 \cdot \overline{A13}$
- ROM: A15

**c)** Sí, 6000-7FFF sin usar

### Respuestas 4.3

Con 74LS138:
- A, B, C = A15, A14, A13
- $\overline{G1}$ = 0 (tierra)
- G2A, G2B conectados apropiadamente
- Y0-Y7 → $\overline{CS}$ de cada memoria

---

## Nivel 5: ROM como Circuito Combinacional

### Respuestas 5.1

**a)** ROM 8×1 (3 entradas, 1 salida)

**b)** Contenido:
| Dir | F |
|-----|---|
| 000 | 0 |
| 001 | 1 |
| 010 | 1 |
| 011 | 0 |
| 100 | 1 |
| 101 | 0 |
| 110 | 0 |
| 111 | 1 |

### Respuestas 5.2

**a)** ROM 16×7 (4 entradas BCD, 7 salidas para segmentos)

**b)** 10 direcciones válidas (0-9), resto don't care

### Respuestas 5.3

**a)** 8 entradas, 8 salidas

**b)** ROM 256×8

**c)** Es práctico para lookup table, alternativa: multiplicador dedicado

---

## Nivel 6: SRAM

### Respuestas 6.1

**c)** Conflicto de bus - no debe ocurrir, puede dañar el chip o producir datos incorrectos

### Respuestas 6.2

**a)** 2 chips (uno para byte bajo, otro para byte alto)

**b)** A0 puede usarse para selección de byte en modo byte

### Respuestas 6.3

**a)** Tiempo de ciclo: 1/8MHz = 125ns

**b)** Tiempo disponible ≈ 100ns (considerando setup)

**c)** SRAM de 70ns: ✓ OK, sin estados de espera

---

## Nivel 7: DRAM

### Respuestas 7.1

**a)** Reduce pines (n bits de dirección en n/2 pines)

**b)** Secuencia:
1. Poner dirección de fila
2. Activar RAS
3. Poner dirección de columna
4. Activar CAS
5. Datos disponibles

### Respuestas 7.2

**a)** $\sqrt{1M}$ = 1024 filas

**b)** 1024 refreshes / 64ms = 16,000 refreshes/segundo

**c)** 64ms / 1024 = 62.5µs entre refreshes

### Respuestas 7.3

**Para 1MB = 8Mbits:**
- 1M×1: 8 chips, 10 pines dirección
- 256K×4: 2 chips, 9 pines dirección

256K×4 es mejor: menos chips, diseño más simple

---

## Nivel 8: EEPROM y Flash

### Respuestas 8.1

**a)** ~5ms por byte típico

**b)** 1K bytes × 5ms = 5 segundos

**c)** ~100,000 ciclos

### Respuestas 8.2

| Característica | EEPROM | Flash |
|----------------|--------|-------|
| Unidad borrado | Byte | Sector (4K-64K) |
| Velocidad | Lenta | Media |
| Aplicación | Config pequeña | Firmware, almacenamiento |

### Respuestas 8.3

**a)** SDA, SCL, VCC, GND

**c)** Polling: leer hasta que coincida, o verificar ACK

---

## Nivel 9: Diseño de Sistema de Memoria

### Respuestas 9.1

**a)** Mapa propuesto:
```
0000-3FFF: ROM (16K)
4000-4FFF: RAM (4K)
5000-50FF: EEPROM (256B)
```

**b)** Chips:
- ROM: 27128 (16K×8)
- RAM: 6116 (2K×8) × 2
- EEPROM: 28C256 (256B usado)

### Respuestas 9.2

**a)** Tipos:
- Boot: Mask ROM o OTP
- Firmware: Flash
- Variables: SRAM
- Config: EEPROM

### Respuestas 9.3

**a)** Teórico: 32 bits × 100M = 3.2 Gbps = 400 MB/s

**b)** Real: 400 × 0.6 = 240 MB/s

**c)** 1080p@60fps ≈ 373 MB/s → ¡NO suficiente!

---

## Nivel 10: Problemas Avanzados

### Respuestas 10.1

**a)** Chips:
- RAM: 512K / 128K = 4 chips
- ROM: 256K / 64K = 4 chips

**b)** Mapa:
```
00000-7FFFF: RAM (512K)
80000-BFFFF: ROM (256K)
C0000-CFFFF: I/O (64K)
D0000-FFFFF: (reservado)
```

### Respuestas 10.2

**a)** Bloques: 1KB / 16B = 64 bloques

**b)** Dirección 16 bits:
- Offset: 4 bits (16 bytes)
- Índice: 6 bits (64 bloques)
- Tag: 6 bits (16-4-6)

### Respuestas 10.3

**a)** Tiempo promedio:
$$t = 0.95 \times 1 + 0.05 \times (0.8 \times 4 + 0.2 \times 50)$$
$$t = 0.95 + 0.05 \times (3.2 + 10) = 0.95 + 0.66 = 1.61ns$$

**b)** Con L1=90%:
$$t = 0.90 \times 1 + 0.10 \times 13.2 = 0.90 + 1.32 = 2.22ns$$

**c)** Degradación: 38% más lento

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para verificación de ejercicios de memorias
NOTA: Pueden existir soluciones alternativas válidas
-->
