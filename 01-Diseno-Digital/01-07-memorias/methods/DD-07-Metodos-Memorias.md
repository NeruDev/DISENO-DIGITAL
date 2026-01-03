<!--
::METADATA::
type: method
topic_id: dd-07-memorias
file_id: metodos-memorias
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [diseño, memorias, decodificacion, expansion]
search_keywords: "diseño memorias, decodificación direcciones, expansión memoria"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-07-Teoria-Memorias.md) | [Problemas →](../problems/DD-07-Problemas.md)

---

# Métodos de Diseño con Memorias

## Método 1: Cálculo de Capacidad y Direcciones

### Fórmulas Básicas

**Número de direcciones:**
$$N = 2^n$$
donde n = bits de dirección

**Capacidad total:**
$$C = N \times m = 2^n \times m \text{ bits}$$
donde m = tamaño de palabra

### Ejemplo

Memoria con 16 líneas de dirección y palabra de 8 bits:
- N = $2^{16}$ = 65,536 = 64K ubicaciones
- C = 64K × 8 bits = 512 Kbits = 64 KB

---

## Método 2: Selección de Memoria

### Criterios de Selección

| Factor | Opciones |
|--------|----------|
| Volatilidad | RAM vs ROM/Flash |
| Velocidad | SRAM > DRAM > Flash > EEPROM |
| Densidad | DRAM > Flash > SRAM |
| Costo | DRAM < Flash < SRAM |
| Ciclos escritura | SRAM ∞ > DRAM ∞ > Flash 100K > EEPROM 100K |

### Árbol de Decisión

```
¿Retener sin energía?
├── SÍ → ¿Frecuentes escrituras?
│        ├── SÍ → Flash o EEPROM
│        └── NO → ROM o PROM
│
└── NO → ¿Máxima velocidad?
         ├── SÍ → SRAM
         └── NO → DRAM (si gran capacidad)
```

---

## Método 3: Expansión de Palabras

### Objetivo

Aumentar el número de ubicaciones direccionables.

### Procedimiento

1. Determinar bits de dirección adicionales
2. Usar decodificador para generar $\overline{CS}$
3. Conectar buses de datos en paralelo

### Ejemplo: 2K×8 a partir de 1K×8

```
         ┌────────────────────────────────┐
         │                                │
A10 ─────┼─[NOT]──┬── CS̄ (Mem0: 0000-03FF)│
         │        │                       │
         │        └── CS̄ (Mem1: 0400-07FF)│
         │                                │
A0-A9 ───┴────────────→ Mem0, Mem1        │
         │                                │
D0-D7 ←──┴────────────→ Mem0, Mem1        │
         │                                │
OE, WE ──┴────────────→ Mem0, Mem1        │
         └────────────────────────────────┘
```

---

## Método 4: Expansión de Bits

### Objetivo

Aumentar el tamaño de palabra.

### Procedimiento

1. Conectar todas las líneas de dirección en paralelo
2. Conectar líneas de control en paralelo
3. Cada memoria maneja un grupo de bits de datos

### Ejemplo: 1K×8 a partir de 1K×4

```
         Memoria 0 (bits 0-3)    Memoria 1 (bits 4-7)
         ┌─────────┐              ┌─────────┐
A0-A9 ───┤A0-A9    │          ───┤A0-A9    │
         │         │              │         │
D0-D3 ←──┤D0-D3    │              │         │
         │         │       D4-D7 ←┤D0-D3    │
         │         │              │         │
CS̄ ──────┤CS̄       │          ────┤CS̄       │
OE ──────┤OE       │          ────┤OE       │
WE ──────┤WE       │          ────┤WE       │
         └─────────┘              └─────────┘
```

---

## Método 5: Decodificación de Direcciones

### Decodificación Completa

Todas las combinaciones de bits superiores generan selección única.

### Ejemplo: 64K espacio, 4 memorias de 16K×8

| Dirección | A15 | A14 | Chip |
|-----------|-----|-----|------|
| 0000-3FFF | 0 | 0 | 0 |
| 4000-7FFF | 0 | 1 | 1 |
| 8000-BFFF | 1 | 0 | 2 |
| C000-FFFF | 1 | 1 | 3 |

**Circuito:**
```
A15, A14 ──>[Dec 2:4]──> CS̄0, CS̄1, CS̄2, CS̄3
```

### Decodificación Parcial

No todos los bits se decodifican (crea "imágenes" o aliases).

---

## Método 6: Diseño de Mapa de Memoria

### Procedimiento

1. Listar todos los dispositivos (RAM, ROM, I/O)
2. Asignar rangos de direcciones
3. Diseñar decodificador
4. Verificar que no haya solapamientos

### Ejemplo: Sistema Mínimo

```
Dirección    Dispositivo    Tamaño
─────────────────────────────────────
0000-1FFF    RAM            8K
2000-3FFF    (vacío)        
4000-5FFF    I/O            8K (decodificado)
6000-7FFF    (vacío)        
8000-FFFF    ROM            32K
```

**Decodificación:**
- A15 = 1 → ROM
- A15 = 0, A14 = 0 → RAM
- A15 = 0, A14 = 1, A13 = 0 → I/O

---

## Método 7: ROM como Generador de Funciones

### Concepto

Una ROM de $2^n × m$ implementa m funciones booleanas de n variables.

### Procedimiento

1. Escribir tabla de verdad de las funciones
2. Cada fila = una dirección
3. Cada columna de salida = un bit de la palabra
4. Programar ROM con los valores

### Ejemplo: Sumador BCD

ROM 256×8 (8 direcciones, 8 salidas):
- Entradas: A(4 bits) + B(4 bits) = 8 bits de dirección
- Salidas: Suma(4 bits) + Carry(1 bit) = 5 bits

| A | B | S | C |
|---|---|---|---|
| 0000 | 0000 | 0000 | 0 |
| 0000 | 0001 | 0001 | 0 |
| ... | ... | ... | ... |
| 1001 | 1001 | 1000 | 1 | (9+9=18)

---

## Método 8: Interfaz con Microprocesador

### Señales Típicas

| MPU | Memoria |
|-----|---------|
| A0-An | A0-An |
| D0-Dm | D0-Dm |
| R/W̄ | WE (invertido si necesario) |
| φ2 o E | CS (con decodificación) |
| - | OE |

### Ciclo de Lectura

```
1. MPU pone dirección
2. Decodificador activa CS̄
3. MPU activa R/W̄ = Read
4. Memoria pone datos
5. MPU lee datos
```

### Ciclo de Escritura

```
1. MPU pone dirección y datos
2. Decodificador activa CS̄
3. MPU activa R/W̄ = Write (WE)
4. Memoria captura datos
```

---

## Método 9: Programación de EPROM/EEPROM

### EPROM (con programador)

1. Borrar con UV (15-20 min)
2. Verificar blank
3. Programar byte por byte (pulsos de 50ms típico)
4. Verificar

### EEPROM (in-circuit)

1. Escribir dirección
2. Escribir dato
3. Esperar tiempo de escritura (~5ms)
4. Verificar (opcional)

### Algoritmo de Escritura EEPROM (pseudo-código)

```
function escribir_byte(direccion, dato):
    # Secuencia de desbloqueo (algunos chips)
    escribir(0x5555, 0xAA)
    escribir(0x2AAA, 0x55)
    escribir(0x5555, 0xA0)
    
    # Escribir dato
    escribir(direccion, dato)
    
    # Esperar (polling o delay)
    mientras (leer(direccion) != dato):
        esperar(100us)
```

---

## Método 10: Cálculo de Tiempos

### Tiempo de Acceso en Lectura

$$t_{access} = t_{address} + t_{decode} + t_{mem}$$

### Verificar Compatibilidad con MPU

$$t_{access} < t_{ciclo\_mpu} - t_{setup}$$

### Ejemplo

- MPU: ciclo = 1µs, setup = 100ns
- Memoria disponible: 900ns
- SRAM de 100ns: ✓ Compatible
- EEPROM de 200ns: ✓ Compatible

---

## Método 11: Memoria Cache (Concepto)

### Principio

Memoria pequeña y rápida entre CPU y memoria principal.

### Jerarquía

```
CPU ←→ Cache L1 ←→ Cache L2 ←→ RAM ←→ Disco
        (rápido, pequeño)   (lento, grande)
```

### Tasa de Aciertos

$$t_{efectivo} = t_{hit} \times h + t_{miss} \times (1-h)$$

donde h = tasa de aciertos (típico 95%+)

---

## Resumen de Expansión

| Objetivo | Método | Circuito Adicional |
|----------|--------|--------------------|
| Más ubicaciones | Expansión de palabras | Decodificador |
| Palabra más ancha | Expansión de bits | Solo conexiones |
| Ambos | Combinado | Decodificador + conexiones |

---

<!-- IA_CONTEXT
USO: Referencia para diseño de sistemas de memoria
NIVEL: Intermedio (2/3)
HERRAMIENTAS: LogiSim, Proteus, programadores de EPROM
-->
