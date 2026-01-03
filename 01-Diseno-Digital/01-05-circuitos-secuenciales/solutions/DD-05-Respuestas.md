<!--
::METADATA::
type: solution
topic_id: dd-05-circuitos-secuenciales
file_id: respuestas-circuitos-secuenciales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, circuitos secuenciales"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-05-Problemas.md)

---

# Respuestas: Circuitos Secuenciales

## Nivel 1: Latches

### Respuestas 1.1

**a) Tabla SR-NOR:**
| S | R | Q+ |
|---|---|-----|
| 0 | 0 | Q |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | Prohibido |

**c)** Prohibido porque ambas salidas Q y Q̄ serían 0, violando la condición Q̄ = NOT Q

### Respuestas 1.2

**a)** Conectar: S=D, R=D̄ (a través de NOT)

**c)** Ventaja: elimina estado prohibido (D y D̄ nunca son iguales)

### Respuestas 1.3

**c)** Cuando E=0: el latch mantiene su estado anterior (memoria)

---

## Nivel 2: Flip-Flops

### Respuestas 2.1

**b)** Secuencia de D: 1,0,1,1,0
Q después de cada flanco: 1,0,1,1,0
Q final = **0**

### Respuestas 2.2

**b)** J=K=1: El flip-flop hace **toggle** (cambia de estado)

### Respuestas 2.3

**a) JK → D:**
- J = D
- K = D̄

**b) D → T:**
- D = T ⊕ Q

**c) JK → T:**
- J = T
- K = T

### Respuestas 2.4

**a)** PRE (Preset): Fuerza Q=1 asíncronamente
    CLR (Clear): Fuerza Q=0 asíncronamente

**c)** Prioridad: CLR/PRE > CLK (asíncronas tienen prioridad)

---

## Nivel 3: Análisis

### Respuestas 3.1

**a)** $D = X \oplus Q$

**b)** Tabla de transición:
| Q | X | Q+ |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**c)** Función: **Flip-flop T** (toggle cuando X=1)

### Respuestas 3.2

**a)** Ecuaciones:
- $J_1 = X \cdot Q_0$, $K_1 = 1$
- $J_0 = X \cdot \overline{Q_1}$, $K_0 = 1$

**d)** Función: **Contador módulo 3** (cuenta 0→1→2→0)

### Respuestas 3.3

Tabla de estados:
| Q | X | Q+ | Y |
|---|---|-----|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Función: Detecta X=1 cuando Q=1 (dos 1s consecutivos)

---

## Nivel 4: Detectores de Secuencia

### Respuestas 4.1 (Detector "110")

**Estados:** S0 (inicial), S1 (recibido 1), S2 (recibido 11), S3 (recibido 110, Z=1)

**Tabla de estados:**
| Estado | X=0 | X=1 | Z |
|--------|-----|-----|---|
| S0 | S0 | S1 | 0 |
| S1 | S0 | S2 | 0 |
| S2 | S3 | S2 | 0 |
| S3 | S0 | S1 | 1 |

**Asignación:** S0=00, S1=01, S2=11, S3=10

**Ecuaciones (D flip-flops):**
- $D_1 = Q_0 \cdot X + Q_1 \cdot \overline{X}$
- $D_0 = X$
- $Z = Q_1 \cdot \overline{Q_0}$

### Respuestas 4.2 (Detector "1010" con solapamiento)

Moore requiere 5 estados, Mealy puede hacerse con 4 estados.

Con Mealy, la salida Z=1 aparece en la transición, no en el estado.

### Respuestas 4.3 (Más 1s que 0s en últimos 3)

8 estados para recordar los últimos 3 bits.
Salida Z=1 cuando suma de bits > 1.

---

## Nivel 5: Controladores

### Respuestas 5.1 (Máquina Expendedora)

**Estados:** WAIT(0¢), FIVE(5¢), TEN(10¢)

**Tabla:**
| Estado | 5¢ | 10¢ | PRODUCTO |
|--------|-----|-----|----------|
| WAIT | FIVE | TEN | 0 |
| FIVE | TEN | PROD→WAIT | 0 |
| TEN | PROD→WAIT | PROD→WAIT | 0→1 |

### Respuestas 5.2 (Semáforo)

**Estados con codificación:**
- VERDE = 00
- AMARILLO = 01
- ROJO = 10
- ROJO_AMARILLO = 11

**Salidas (Moore):**
| Estado | R | A | V |
|--------|---|---|---|
| VERDE | 0 | 0 | 1 |
| AMARILLO | 0 | 1 | 0 |
| ROJO | 1 | 0 | 0 |
| ROJO_AMARILLO | 1 | 1 | 0 |

### Respuestas 5.3 (Motor)

4 estados con transiciones controladas por entradas START, STOP, sensores.

---

## Nivel 6: Temporización

### Respuestas 6.1

**a)** $f_{max} = \frac{1}{t_{CQ} + t_{comb} + t_{setup}} = \frac{1}{8 + 15 + 5} = \frac{1}{28ns} = 35.7 MHz$

**b)** Violación de setup time → datos incorrectos capturados (metaestabilidad)

**c)** Reducir $t_{comb}$ con pipelining o lógica más rápida

### Respuestas 6.3

**a)** $f_{max} = \frac{1}{t_{CQ} + 30ns + t_{setup}}$ (aprox 30MHz)

**b)** Con 2 etapas de pipeline: $f_{max} = \frac{1}{t_{CQ} + 15ns + t_{setup}}$ (aprox 50MHz)

---

## Nivel 7: Implementación

### Respuestas 7.1

**Con 74LS74 (D):** 2 flip-flops + ~5 compuertas
**Con 74LS76 (JK):** 2 flip-flops + ~3 compuertas (menos lógica por los don't cares)

### Respuestas 7.3

**a) Power-on reset:**
```
VCC ──[R]──┬──[C]──GND
           │
           └── RESET
```
Tiempo RC determina duración del reset.

---

## Nivel 8: Análisis Avanzado

### Respuestas 8.1

**a)** Registro de desplazamiento de 3 bits con XOR

**b)** 8 estados posibles ($2^3$)

**c)** Con X=1: genera secuencia pseudoaleatoria (LFSR)

### Respuestas 8.2

**b)** Es **Moore** (salida Z depende solo del estado Q1Q0)

**c)** Detecta secuencia "11" (dos 1s consecutivos)

### Respuestas 8.3

A y C son equivalentes → fusionar en un solo estado.
Estados minimizados: {A/C, B, D, E} = 4 estados

---

## Nivel 9: Integradores

### Respuestas 9.1 (Cerradura)

**Estados:** IDLE, GOT_1, GOT_12, OPEN

**Tabla simplificada:**
| Estado | btn1 | btn2 | btn3 | ABRIR |
|--------|------|------|------|-------|
| IDLE | GOT_1 | IDLE | IDLE | 0 |
| GOT_1 | IDLE | GOT_12 | IDLE | 0 |
| GOT_12 | IDLE | IDLE | OPEN | 0 |
| OPEN | - | - | - | 1 |

### Respuestas 9.2 (Detector de Flancos)

Usar flip-flop D para capturar estado anterior:
- $RISE = X \cdot \overline{Q}$
- $FALL = \overline{X} \cdot Q$
- $D = X$

### Respuestas 9.3 (Generador de Patrones)

Patrón: 110100 (6 bits, período 6)

6 estados, salida = bit correspondiente del patrón.

---

## Nivel 10: Diseño Completo

### Respuestas 10.1 (Elevador)

**Estados principales:** PISO1, PISO2, PISO3, SUBIENDO, BAJANDO

**Entradas:** P1, P2, P3, SENSOR1, SENSOR2, SENSOR3

**Salidas:** MOTOR_UP, MOTOR_DOWN, PUERTA

Requiere ~8 estados con memoria de destino.

### Respuestas 10.2 (Árbitro Round-Robin)

**Estados:** IDLE, GNT0, GNT1

**Lógica:** Prioridad alterna basada en último servido.

| Estado | REQ0 | REQ1 | GNT0 | GNT1 | Next |
|--------|------|------|------|------|------|
| IDLE | 1 | 0 | 1 | 0 | GNT0 |
| IDLE | 0 | 1 | 0 | 1 | GNT1 |
| GNT0 | - | 1 | 0 | 1 | GNT1 |
| GNT1 | 1 | - | 1 | 0 | GNT0 |

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para verificación de ejercicios secuenciales
NOTA: Pueden existir soluciones alternativas válidas
-->
