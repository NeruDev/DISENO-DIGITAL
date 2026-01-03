<!--
::METADATA::
type: theory
topic_id: dd-07-memorias
file_id: teoria-memorias
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [memoria, RAM, ROM, EPROM, EEPROM, Flash, SRAM, DRAM]
search_keywords: "memorias, RAM, ROM, semiconductor, almacenamiento"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-07-Intro.md) | [Métodos →](../methods/DD-07-Metodos-Memorias.md)

---

# Memorias Semiconductoras

## 1. Introducción

### 1.1 Definición

Una **memoria** es un dispositivo que almacena información binaria organizada en palabras, accesibles mediante direcciones.

### 1.2 Terminología

| Término | Descripción |
|---------|-------------|
| Celda | Unidad básica de almacenamiento (1 bit) |
| Palabra | Grupo de bits accesados juntos |
| Dirección | Ubicación única de una palabra |
| Capacidad | Cantidad total de almacenamiento |
| Bus de datos | Líneas para entrada/salida de datos |
| Bus de direcciones | Líneas para selección de ubicación |

### 1.3 Capacidad

$$\text{Capacidad} = 2^n \times m \text{ bits}$$

Donde:
- n = número de líneas de dirección
- m = tamaño de palabra (bits)

**Notación:** 1K = $2^{10}$ = 1024

---

## 2. Clasificación

### 2.1 Por Volatilidad

| Tipo | Característica |
|------|----------------|
| Volátil | Pierde datos sin alimentación (RAM) |
| No Volátil | Retiene datos sin alimentación (ROM) |

### 2.2 Por Acceso

| Tipo | Acceso |
|------|--------|
| RAM | Random Access (cualquier ubicación) |
| Secuencial | Debe accederse en orden |

### 2.3 Árbol de Clasificación

```
Memorias
├── RAM (Read-Write)
│   ├── SRAM (Static)
│   └── DRAM (Dynamic)
│
└── ROM (Read Only)
    ├── ROM (Mask)
    ├── PROM (Programmable)
    ├── EPROM (Erasable)
    ├── EEPROM (Electrically Erasable)
    └── Flash
```

---

## 3. Memoria ROM

### 3.1 Características

- Solo lectura (programada en fábrica o una vez)
- No volátil
- Usada para firmware, tablas de lookup

### 3.2 Estructura Interna

```
        A0 A1 ... An-1  (Direcciones)
            │
      ┌─────┴─────┐
      │ Decodifica-│
      │    dor    │
      └─────┬─────┘
            │
    ┌───────┼───────┐
    │   Matriz de   │
    │    Celdas     │
    │   (fusibles)  │
    └───────┬───────┘
            │
        D0 D1 ... Dm-1  (Datos)
```

### 3.3 Tipos de ROM

| Tipo | Programación | Borrado |
|------|--------------|---------|
| Mask ROM | Fábrica | No |
| PROM | Usuario (una vez) | No |
| EPROM | Usuario | UV (todo) |
| EEPROM | Usuario | Eléctrico (byte) |
| Flash | Usuario | Eléctrico (sector) |

### 3.4 ROM como Circuito Combinacional

Una ROM de 2ⁿ × m implementa m funciones de n variables.

**Ejemplo:** ROM 8×4 (3 direcciones, 4 bits)
- Implementa 4 funciones de 3 variables
- Cada dirección = una fila de la tabla de verdad

---

## 4. Memoria PROM

### 4.1 Estructura

Matriz de fusibles que el usuario puede "quemar".

### 4.2 Programación

1. Verificar que esté en blanco (todos 1s)
2. Aplicar pulsos de alta corriente para quemar fusibles
3. Verificar programación

### 4.3 Aplicaciones

- Prototipos
- Producción baja cantidad
- Almacenamiento de código fijo

---

## 5. Memoria EPROM

### 5.1 Características

- Borrable con luz ultravioleta
- Ventana de cuarzo para borrado
- Múltiples ciclos programa/borra

### 5.2 Tecnología

**FAMOS (Floating Gate Avalanche MOS)**
- Compuerta flotante almacena carga
- Carga = 0 lógico
- Sin carga = 1 lógico

### 5.3 Ciclo de Uso

1. Borrar (UV, 15-20 min)
2. Programar
3. Usar
4. Repetir

### 5.4 CIs Típicos

| CI | Capacidad |
|----|-----------|
| 2716 | 2K × 8 |
| 2732 | 4K × 8 |
| 2764 | 8K × 8 |
| 27128 | 16K × 8 |
| 27256 | 32K × 8 |

---

## 6. Memoria EEPROM

### 6.1 Características

- Borrado eléctrico (sin UV)
- Borrado por byte
- ~100,000 ciclos de escritura
- Más lenta para escribir

### 6.2 Ventajas sobre EPROM

- No requiere equipo especial
- Borrado selectivo
- Programación in-circuit

### 6.3 CIs Típicos

| CI | Capacidad | Interface |
|----|-----------|-----------|
| 28C16 | 2K × 8 | Paralelo |
| 28C64 | 8K × 8 | Paralelo |
| 24LC256 | 32K × 8 | I²C |
| 93C46 | 1K | SPI |

---

## 7. Memoria Flash

### 7.1 Características

- Borrado por sector (no por byte)
- Alta densidad
- ~100,000 ciclos por sector
- Más rápida que EEPROM

### 7.2 Tipos

| Tipo | Característica |
|------|----------------|
| NOR | Acceso aleatorio, código |
| NAND | Acceso secuencial, almacenamiento |

### 7.3 Aplicaciones

- BIOS de PC
- Firmware de dispositivos
- USB drives
- SSD

---

## 8. Memoria SRAM

### 8.1 Concepto

**Static RAM:** Usa flip-flops (6 transistores por celda).

### 8.2 Características

- Volátil
- Rápida
- No requiere refresh
- Cara (por densidad)

### 8.3 Estructura de Celda

```
          Vcc
           │
    ┌──────┼──────┐
    │      │      │
   [P1]   [P2]   
    │      │
    ├──┬───┼──┬───┤
    │  │   │  │   │
   [N1]│  [N2]│   
    │  │   │  │   │
    └──┼───┴──┼───┘
       │      │
       WL     WL (Word Line)
       │      │
      BL     BL̄ (Bit Lines)
```

### 8.4 CIs Típicos

| CI | Capacidad | Acceso |
|----|-----------|--------|
| 6116 | 2K × 8 | 120ns |
| 6264 | 8K × 8 | 100ns |
| 62256 | 32K × 8 | 70ns |

### 8.5 Señales de Control

| Señal | Función |
|-------|---------|
| $\overline{CS}$ | Chip Select (habilita) |
| $\overline{OE}$ | Output Enable (lectura) |
| $\overline{WE}$ | Write Enable (escritura) |

---

## 9. Memoria DRAM

### 9.1 Concepto

**Dynamic RAM:** Usa capacitor + transistor (1T-1C).

### 9.2 Características

- Volátil
- Requiere refresh periódico
- Alta densidad
- Económica

### 9.3 Estructura de Celda

```
     BL (Bit Line)
      │
     [T]── WL (Word Line)
      │
     [C]── Gnd
```

### 9.4 Refresh

El capacitor pierde carga → Leer y reescribir periódicamente (~64ms todo el chip).

### 9.5 Multiplexado de Direcciones

Para reducir pines:
1. Enviar dirección de fila (RAS)
2. Enviar dirección de columna (CAS)

### 9.6 Tipos Modernos

| Tipo | Característica |
|------|----------------|
| SDRAM | Síncrona con CLK |
| DDR | Double Data Rate |
| DDR2/3/4/5 | Versiones mejoradas |

---

## 10. Organización de Memoria

### 10.1 Expansión de Palabras

Aumentar el número de ubicaciones.

**Ejemplo:** 2 memorias de 1K×8 → 2K×8

```
A10 ─────[NOT]─────┬─ CS̄ (Mem0)
         │         └─ CS̄ (Mem1)
         │
A0-A9 ───┴──────────→ Ambas memorias
D0-D7 ←─────────────→ Ambas memorias
```

### 10.2 Expansión de Bits

Aumentar el tamaño de palabra.

**Ejemplo:** 2 memorias de 1K×4 → 1K×8

```
A0-A9 ───────→ Ambas memorias
CS̄, OE, WE ──→ Ambas memorias

Mem0: D0-D3
Mem1: D4-D7
```

### 10.3 Expansión Combinada

**Ejemplo:** 4 memorias de 1K×4 → 2K×8

```
         │ Bits 0-3 │ Bits 4-7 │
─────────┼──────────┼──────────┤
Dir 0-1K │  Mem0    │  Mem1    │
─────────┼──────────┼──────────┤
Dir 1K-2K│  Mem2    │  Mem3    │
```

---

## 11. Decodificación de Direcciones

### 11.1 Concepto

Seleccionar el chip correcto según el rango de direcciones.

### 11.2 Ejemplo

Sistema con 4 memorias de 1K × 8 en espacio de 4K:

| Rango | A11 | A10 | Chip |
|-------|-----|-----|------|
| 0000-03FF | 0 | 0 | 0 |
| 0400-07FF | 0 | 1 | 1 |
| 0800-0BFF | 1 | 0 | 2 |
| 0C00-0FFF | 1 | 1 | 3 |

**Decodificador:** 2-to-4 (A11, A10 → $\overline{CS_0}$...$\overline{CS_3}$)

---

## 12. Mapa de Memoria

### 12.1 Concepto

Diagrama que muestra la asignación de direcciones a dispositivos.

### 12.2 Ejemplo Típico (Microcontrolador)

```
0xFFFF ┌──────────────┐
       │    ROM       │
       │  (32K)       │
0x8000 ├──────────────┤
       │    I/O       │
       │  Registers   │
0x4000 ├──────────────┤
       │    RAM       │
       │  (16K)       │
0x0000 └──────────────┘
```

---

## 13. Comparativa de Memorias

| Tipo | Volátil | Velocidad | Densidad | Costo | Uso |
|------|---------|-----------|----------|-------|-----|
| SRAM | Sí | Alta | Baja | Alto | Cache |
| DRAM | Sí | Media | Alta | Bajo | Principal |
| ROM | No | Alta | Media | Medio | Firmware |
| Flash | No | Media | Alta | Bajo | Almacenamiento |
| EEPROM | No | Baja | Baja | Alto | Config |

---

## 14. Parámetros de Tiempo

### 14.1 SRAM

- $t_{AA}$: Address to output valid
- $t_{OE}$: OE to output valid
- $t_{WC}$: Write cycle time

### 14.2 DRAM

- $t_{RAS}$: Row Address Strobe
- $t_{CAS}$: Column Address Strobe
- $t_{RC}$: Row Cycle time

---

## Referencias

- Mano, M. M. (2013). *Digital Design*. Pearson.
- Patterson, D. A. (2017). *Computer Organization and Design*. Morgan Kaufmann.

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 01-04 Circuitos Combinacionales, 01-05 Circuitos Secuenciales
CONEXIONES: Base para sistemas con microprocesadores
ERRORES_COMUNES: Confundir tipos, olvidar refresh DRAM, decodificación incorrecta
-->
