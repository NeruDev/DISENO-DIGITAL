<!--
::METADATA::
type: theory
topic_id: dd-05-circuitos-secuenciales
file_id: teoria-circuitos-secuenciales
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [secuencial, flip-flop, latch, FSM, sincronico, asincronico]
search_keywords: "circuitos secuenciales, flip-flop, latch, máquina de estados, FSM"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-05-Intro.md) | [Métodos →](../methods/DD-05-Metodos-FSM.md)

---

# Circuitos Secuenciales

## 1. Introducción

Un **circuito secuencial** es aquel cuya salida depende de las entradas actuales Y del historial de entradas anteriores (estado).

$$Y = f(X, Q)$$
$$Q_{next} = g(X, Q)$$

**Características:**
- Tiene elementos de memoria
- Las salidas dependen del estado
- Puede ser síncrono o asíncrono

---

## 2. Elementos de Memoria Básicos

### 2.1 Latch SR (Set-Reset)

**Implementación con NOR:**

```
S ────[NOR]──┬── Q
        ┌────┘
        │
R ────[NOR]──┬── Q̄
        └────┘
```

**Tabla de Operación:**

| S | R | Q | $\overline{Q}$ | Acción |
|---|---|---|----------------|--------|
| 0 | 0 | Q | $\overline{Q}$ | Mantener |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | 0 | 0 | **Prohibido** |

**Ecuación característica:**
$$Q_{next} = S + \overline{R}Q \quad \text{(con } SR = 0\text{)}$$

### 2.2 Latch SR con Enable

```
     ┌─────────┐
S ───┤         │
     │  SR     ├── Q
E ───┤  Latch  │
     │         ├── Q̄
R ───┤         │
     └─────────┘
```

| E | S | R | Q |
|---|---|---|---|
| 0 | X | X | Q (mantiene) |
| 1 | 0 | 0 | Q |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | Prohibido |

### 2.3 Latch D (Data/Delay)

Elimina la condición prohibida del SR.

$$D = S, \quad R = \overline{D}$$

| E | D | Q |
|---|---|---|
| 0 | X | Q |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Ecuación característica:**
$$Q_{next} = D \quad \text{(cuando E=1)}$$

---

## 3. Flip-Flops

### 3.1 Diferencia Latch vs Flip-Flop

| Característica | Latch | Flip-Flop |
|----------------|-------|-----------|
| Disparo | Por nivel | Por flanco |
| Transparencia | Sí (cuando habilitado) | No |
| Sincronización | Asíncrona | Síncrona |

### 3.2 Flip-Flop D (Edge-Triggered)

Captura el valor de D en el flanco del reloj.

```
     ┌─────────┐
D ───┤    D    ├── Q
     │         │
CLK ─┤>        ├── Q̄
     └─────────┘
```

**Tabla de operación:**

| CLK | D | Q |
|-----|---|---|
| ↑ | 0 | 0 |
| ↑ | 1 | 1 |
| No ↑ | X | Q |

**CI típico:** 74LS74 (dual D flip-flop)

### 3.3 Flip-Flop JK

Elimina la condición prohibida del SR permitiendo toggle.

```
     ┌─────────┐
J ───┤    J    ├── Q
     │         │
CLK ─┤>   K    ├── Q̄
     │         │
K ───┤         │
     └─────────┘
```

**Tabla de operación:**

| J | K | $Q_{next}$ | Acción |
|---|---|------------|--------|
| 0 | 0 | Q | Mantener |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | $\overline{Q}$ | Toggle |

**Ecuación característica:**
$$Q_{next} = J\overline{Q} + \overline{K}Q$$

**CI típico:** 74LS76 (dual JK flip-flop)

### 3.4 Flip-Flop T (Toggle)

Caso especial del JK con J=K=T.

| T | $Q_{next}$ |
|---|------------|
| 0 | Q |
| 1 | $\overline{Q}$ |

**Ecuación característica:**
$$Q_{next} = T \oplus Q$$

**CI típico:** 74LS109 (dual JK, usar como T)

---

## 4. Entradas Asíncronas

### 4.1 Preset (PR) y Clear (CLR)

Permiten forzar el estado independientemente del reloj.

| $\overline{PR}$ | $\overline{CLR}$ | Q |
|-----------------|------------------|---|
| 0 | 1 | 1 (Set) |
| 1 | 0 | 0 (Reset) |
| 0 | 0 | Prohibido |
| 1 | 1 | Operación normal |

### 4.2 Uso Típico

- **Power-on reset:** Inicializar a estado conocido
- **Reset global:** Reiniciar el sistema

---

## 5. Temporización

### 5.1 Parámetros de Tiempo

| Parámetro | Descripción |
|-----------|-------------|
| $t_{setup}$ | Tiempo que D debe estar estable ANTES del flanco |
| $t_{hold}$ | Tiempo que D debe estar estable DESPUÉS del flanco |
| $t_{CQ}$ | Retardo de reloj a salida Q |
| $t_{pd}$ | Retardo de propagación |

### 5.2 Diagrama de Tiempo

```
CLK  ────┐   ┌───┐   ┌───
         └───┘   └───┘

D    ──────┬─────────┬────
           │←tsetup→│←th→│
           │    ↑flanco   │

Q    ────────────┬─────────
                 │←tCQ→│
```

### 5.3 Frecuencia Máxima

$$f_{max} = \frac{1}{t_{CQ} + t_{comb} + t_{setup}}$$

Donde $t_{comb}$ es el retardo de lógica combinacional entre flip-flops.

---

## 6. Máquinas de Estados Finitos (FSM)

### 6.1 Definición

Una FSM es un modelo que describe el comportamiento de un sistema secuencial mediante:
- Conjunto finito de estados
- Entradas
- Salidas
- Función de transición
- Función de salida

### 6.2 Tipos de FSM

#### Máquina de Moore

Las salidas dependen SOLO del estado actual.

$$Y = f(Q)$$

```
┌─────────┐    ┌──────────┐    ┌─────────┐
│ Entrada │───>│  Lógica  │───>│ Estado  │
└─────────┘    │   Next   │    │  (Q)    │
               │  State   │    └────┬────┘
               └──────────┘         │
                    ↑               │
                    └───────────────┘
                                    │
                              ┌─────┴─────┐
                              │  Lógica   │
                              │  Salida   │
                              └─────┬─────┘
                                    │
                              ┌─────┴─────┐
                              │  Salida   │
                              └───────────┘
```

#### Máquina de Mealy

Las salidas dependen del estado actual Y las entradas.

$$Y = f(Q, X)$$

### 6.3 Diagrama de Estados

```
        ┌──────────────────┐
        │                  │
        ▼     a/0          │
    ┌──────┐          ┌──────┐
    │  S0  │─────────>│  S1  │
    │      │          │      │
    └──────┘<─────────└──────┘
        │     b/1          │
        │                  │
        └──────────────────┘
              c/0
```

### 6.4 Tabla de Estados

| Estado Actual | Entrada | Estado Siguiente | Salida |
|---------------|---------|------------------|--------|
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S0 | 1 |
| S1 | 1 | S1 | 0 |

---

## 7. Análisis de Circuitos Secuenciales

### 7.1 Procedimiento

1. Identificar flip-flops y sus tipos
2. Obtener ecuaciones de excitación (entradas a FF)
3. Obtener ecuaciones de estado siguiente
4. Obtener ecuaciones de salida
5. Construir tabla de estados
6. Dibujar diagrama de estados

### 7.2 Ecuaciones de Excitación

Para cada flip-flop, expresar sus entradas en función del estado actual y entradas del sistema.

---

## 8. Síntesis de Circuitos Secuenciales

### 8.1 Procedimiento

1. Definir el problema
2. Dibujar diagrama de estados
3. Crear tabla de estados
4. Asignar códigos a los estados
5. Crear tabla de transición
6. Obtener ecuaciones de excitación (mapas K)
7. Obtener ecuaciones de salida
8. Dibujar el circuito

### 8.2 Tablas de Excitación de Flip-Flops

#### Flip-Flop D

| Q | $Q_{next}$ | D |
|---|------------|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Regla:** $D = Q_{next}$

#### Flip-Flop JK

| Q | $Q_{next}$ | J | K |
|---|------------|---|---|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

#### Flip-Flop T

| Q | $Q_{next}$ | T |
|---|------------|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Regla:** $T = Q \oplus Q_{next}$

---

## 9. Asignación de Estados

### 9.1 Consideraciones

- Minimizar lógica combinacional
- Estados adyacentes con cambio de 1 bit (código Gray)
- Estados iniciales fáciles de generar

### 9.2 Ejemplo (3 estados)

| Estado | Código 1 | Código 2 |
|--------|----------|----------|
| S0 | 00 | 00 |
| S1 | 01 | 01 |
| S2 | 10 | 11 |

---

## 10. Circuitos Integrados

| CI | Descripción |
|----|-------------|
| 74LS74 | Dual D flip-flop |
| 74LS76 | Dual JK flip-flop |
| 74LS109 | Dual JK flip-flop |
| 74LS112 | Dual JK flip-flop (neg edge) |
| 74LS175 | Quad D flip-flop |
| 74LS273 | Octal D flip-flop con clear |

---

## Referencias

- Mano, M. M. (2013). *Digital Design*. Pearson.
- Wakerly, J. F. (2006). *Digital Design: Principles and Practices*. Pearson.

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 01-04 Circuitos Combinacionales
CONEXIONES: Base para contadores, registros y diseño de procesadores
ERRORES_COMUNES: Violación de setup/hold, estados no alcanzables, metaestabilidad
-->
