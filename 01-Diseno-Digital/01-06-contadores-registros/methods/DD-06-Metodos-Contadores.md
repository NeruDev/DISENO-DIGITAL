<!--
::METADATA::
type: method
topic_id: dd-06-contadores-registros
file_id: metodos-contadores
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [diseño, contador, registro, cascada]
search_keywords: "diseño contadores, registros desplazamiento, método"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-06-Teoria-ContadoresRegistros.md) | [Problemas →](../problems/DD-06-Problemas.md)

---

# Métodos de Diseño de Contadores y Registros

## Método 1: Diseño de Contador Síncrono

### Algoritmo Sistemático

**Pasos:**
1. Determinar número de estados (módulo N)
2. Determinar número de flip-flops: $n = \lceil \log_2 N \rceil$
3. Elegir tipo de flip-flop (D, JK, T)
4. Crear tabla de transición de estados
5. Aplicar tabla de excitación del FF
6. Obtener ecuaciones con mapas K
7. Dibujar circuito

### Ejemplo: Contador Módulo 5 (0-4)

**Paso 1-2:** 5 estados → 3 flip-flops ($2^3 = 8 > 5$)

**Paso 4:** Tabla de transición
| Q2 | Q1 | Q0 | Q2+ | Q1+ | Q0+ |
|----|----|----|-----|-----|-----|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 |

**Paso 5-6:** Con flip-flops D (D = Q+):
- $D_0 = \overline{Q_2} \cdot \overline{Q_0}$
- $D_1 = Q_0 \cdot \overline{Q_2}$
- $D_2 = Q_1 \cdot Q_0$

---

## Método 2: Contador Asíncrono con Reset

### Para Módulo N (No potencia de 2)

**Pasos:**
1. Usar contador binario de $\lceil \log_2 N \rceil$ bits
2. Detectar cuando cuenta = N
3. Aplicar reset

### Ejemplo: Módulo 6 con 74LS93

```
         74LS93
        ┌───────┐
CLK ────┤A      │
        │    Q0 ├───┬─── Q0
        │    Q1 ├───┼─── Q1
        │    Q2 ├───┼─── Q2
        │    Q3 ├───│
        │       │   │
        │  R0(1)├───┤
        │  R0(2)├───┘
        └───────┘
```

Detectar 110 (6): NAND(Q2, Q1) → Reset

**Nota:** Estado 110 aparece brevemente (glitch).

---

## Método 3: Contador con Carga Paralela

### Para Módulo N Exacto

**Pasos:**
1. Usar contador con carga paralela (ej. 74LS163)
2. Detectar estado N-1
3. En siguiente ciclo, cargar 0

### Ejemplo: Módulo 6 con 74LS163

```
           74LS163
          ┌───────┐
CLK ──────┤CLK    │
          │    QA ├─── Q0
          │    QB ├─── Q1
          │    QC ├─── Q2
          │    QD ├─── Q3
          │       │
    ┌─────┤LOAD   │
    │     │       │
    │  0──┤A      │
    │  0──┤B      │
    │  0──┤C      │
    │  0──┤D      │
    │     └───────┘
    │
    └──[NAND]── Q2·Q0 (detecta 5=0101)
```

---

## Método 4: Contadores en Cascada

### Para Rangos Grandes

**Pasos:**
1. Conectar RCO (Ripple Carry Out) del contador bajo al ENT del siguiente
2. ENP puede usarse para enable global

### Ejemplo: Contador 0-99 con 74LS163

```
   74LS163 (Unidades)      74LS163 (Decenas)
   ┌───────┐               ┌───────┐
CLK┤CLK    │           CLK ┤CLK    │
   │    QA ├─Q0            │    QA ├─Q4
   │    QB ├─Q1            │    QB ├─Q5
   │    QC ├─Q2            │    QC ├─Q6
   │    QD ├─Q3            │    QD ├─Q7
   │       │               │       │
1 ─┤ENP    │           1 ──┤ENP    │
1 ─┤ENT    │               │ENT    │
   │   RCO ├───────────────┤       │
   └───────┘               └───────┘
```

---

## Método 5: Contador Up/Down

### Diseño con Control de Dirección

**Lógica:**
- UP: Siguiente = Actual + 1
- DOWN: Siguiente = Actual - 1

**Con 74LS193:**
```
           74LS193
          ┌───────┐
      ────┤UP     │
      ────┤DOWN   │
          │       │
          │    QA ├─ Q0
          │    QB ├─ Q1
          │    QC ├─ Q2
          │    QD ├─ Q3
          │       │
          │ CARRY ├─ (desbordamiento arriba)
          │BORROW ├─ (desbordamiento abajo)
          └───────┘
```

### Diseño Personalizado

Con flip-flops JK:
- $J_n = K_n = (UP \cdot \prod Q_{<n}) + (DOWN \cdot \prod \overline{Q}_{<n})$

---

## Método 6: Contador de Anillo

### Diseño

**Pasos:**
1. Usar n flip-flops D en cadena
2. Conectar $Q_{n-1}$ a $D_0$
3. Inicializar con un solo 1

### Circuito 4-bit

```
      ┌──────────────────────────────────┐
      │                                  │
      └──D[FF0]──Q0──D[FF1]──Q1──D[FF2]──Q2──D[FF3]──Q3
              CLK ────────────────────────────────────
```

**Inicialización:** CLR todos excepto FF0 (o usar preset en FF0)

---

## Método 7: Contador Johnson

### Diseño

**Pasos:**
1. Usar n flip-flops D en cadena
2. Conectar $\overline{Q}_{n-1}$ a $D_0$
3. Inicializar a 0000

### Circuito 4-bit

```
      ┌──────────────────────────────────┐
      │                                  │
    [NOT]                                │
      │                                  │
      └──D[FF0]──Q0──D[FF1]──Q1──D[FF2]──Q2──D[FF3]──Q3
              CLK ────────────────────────────────────
```

### Decodificación

| Estado | Código | Decodificación |
|--------|--------|----------------|
| 0 | 0000 | $\overline{Q_3} \cdot \overline{Q_0}$ |
| 1 | 1000 | $Q_0 \cdot \overline{Q_1}$ |
| 2 | 1100 | $Q_1 \cdot \overline{Q_2}$ |
| 3 | 1110 | $Q_2 \cdot \overline{Q_3}$ |
| 4 | 1111 | $Q_3 \cdot Q_0$ |
| 5 | 0111 | $\overline{Q_0} \cdot Q_1$ |
| 6 | 0011 | $\overline{Q_1} \cdot Q_2$ |
| 7 | 0001 | $\overline{Q_2} \cdot Q_3$ |

---

## Método 8: Registro SIPO

### Para Conversión Serial → Paralelo

**Pasos:**
1. Conectar entrada serial a D0
2. Encadenar flip-flops D
3. Después de n ciclos, dato disponible en paralelo

### Con 74LS164

```
         74LS164
        ┌───────┐
SER_IN ─┤A      │
   1 ───┤B      │  (A·B es la entrada real)
        │       │
CLK ────┤CLK    │
        │       │
        │    QA ├─ bit0 (primero recibido)
        │    QB ├─ bit1
        │    ...│
        │    QH ├─ bit7 (último recibido)
        └───────┘
```

---

## Método 9: Registro PISO

### Para Conversión Paralelo → Serial

**Pasos:**
1. Cargar datos en paralelo (LOAD)
2. Desplazar y leer salida serial

### Con 74LS165

```
         74LS165
        ┌───────┐
D0-D7 ──┤A-H    │
        │       │
SH/LD ──┤SH/LD  │  (0=Load, 1=Shift)
        │       │
CLK ────┤CLK    │
        │       │
SER_IN ─┤SER    │
        │       │
        │    QH ├─ Serial Out
        │   QH' ├─ Serial Out complementado
        └───────┘
```

---

## Método 10: Registro Universal (74LS194)

### Configuración por Modo

| S1 | S0 | Modo |
|----|----|------|
| 0 | 0 | Hold (mantener) |
| 0 | 1 | Shift Right |
| 1 | 0 | Shift Left |
| 1 | 1 | Parallel Load |

### Conexión Típica

```
           74LS194
          ┌───────┐
CTRL_S0 ──┤S0     │
CTRL_S1 ──┤S1     │
          │       │
SR_IN ────┤SR     │  (Serial Right input)
SL_IN ────┤SL     │  (Serial Left input)
          │       │
D0-D3 ────┤A-D    │  (Parallel inputs)
          │       │
CLK ──────┤CLK    │
CLR ──────┤CLR    │
          │       │
          │ QA-QD ├─ Outputs
          └───────┘
```

---

## Método 11: Divisor de Frecuencia

### Fórmula

$$f_{out} = \frac{f_{in}}{N}$$

Donde N es el módulo del contador.

### Ejemplo: Dividir 1 MHz entre 1000

Usar contador módulo 1000:
- 3 contadores BCD en cascada: 10 × 10 × 10 = 1000

```
1 MHz ─>[BCD]─>[BCD]─>[BCD]─> 1 kHz
```

---

## Resumen de Selección

### ¿Qué Contador Usar?

| Necesidad | CI Recomendado |
|-----------|----------------|
| Binario simple | 74LS93 (async) |
| Binario con control | 74LS163 (sync) |
| BCD/Década | 74LS90, 74LS160 |
| Up/Down | 74LS193 |
| Prescaler | 74LS93 |

### ¿Qué Registro Usar?

| Necesidad | CI Recomendado |
|-----------|----------------|
| Serial→Paralelo | 74LS164 |
| Paralelo→Serial | 74LS165 |
| Bidireccional | 74LS194 |
| 8-bit universal | 74LS299 |

---

<!-- IA_CONTEXT
USO: Referencia para diseño de contadores y registros
NIVEL: Intermedio (2/3)
HERRAMIENTAS: LogiSim, Digital, Quartus
-->
