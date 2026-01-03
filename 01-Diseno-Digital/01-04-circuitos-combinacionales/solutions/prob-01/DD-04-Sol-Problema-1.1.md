<!--
::METADATA::
type: detailed_solution
topic_id: dd-04-circuitos-combinacionales
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, multiplexor, mux, combinacional]
-->

> 🏠 **Navegación:** [← Respuestas](../DD-04-Respuestas.md) | [Problema 1.2 →](./DD-04-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Diseñar un multiplexor 4:1 (MUX) usando compuertas básicas y obtener su tabla de verdad.

---

## Paso 1: Especificación del MUX 4:1

### Entradas y Salidas
| Elemento | Nombre | Descripción |
|----------|--------|-------------|
| Entradas de datos | $I_0, I_1, I_2, I_3$ | 4 líneas de datos |
| Selectores | $S_1, S_0$ | 2 líneas de selección |
| Salida | Y | 1 línea de salida |

### Función
El MUX selecciona una de las 4 entradas basándose en el valor de los selectores:
- $S_1S_0 = 00 \rightarrow Y = I_0$
- $S_1S_0 = 01 \rightarrow Y = I_1$
- $S_1S_0 = 10 \rightarrow Y = I_2$
- $S_1S_0 = 11 \rightarrow Y = I_3$

---

## Paso 2: Ecuación Booleana

$$Y = \bar{S_1}\bar{S_0}I_0 + \bar{S_1}S_0I_1 + S_1\bar{S_0}I_2 + S_1S_0I_3$$

Cada término representa una entrada habilitada por una combinación única de selectores.

---

## Paso 3: Tabla de Verdad

### Tabla Funcional (Simplificada)

| $S_1$ | $S_0$ | Y |
|:-----:|:-----:|:-:|
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

### Tabla Completa (para $I_0=1, I_1=0, I_2=1, I_3=0$)

| $S_1$ | $S_0$ | $I_0$ | $I_1$ | $I_2$ | $I_3$ | Y |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-:|
| 0 | 0 | 1 | 0 | 1 | 0 | **1** |
| 0 | 1 | 1 | 0 | 1 | 0 | **0** |
| 1 | 0 | 1 | 0 | 1 | 0 | **1** |
| 1 | 1 | 1 | 0 | 1 | 0 | **0** |

---

## Paso 4: Circuito con Compuertas

```
                    ┌─────────────┐
                    │   DECODER   │
         S1 ───────►│    2:4      │
         S0 ───────►│             │
                    └──┬──┬──┬──┬─┘
                       │  │  │  │
                    D0 │D1│D2│D3│
                       │  │  │  │
       I0 ──────┐     │  │  │  │
                │  ┌──▼┐ │  │  │
                └─►│AND├─┤  │  │
                   └──┬┘ │  │  │
                      │  │  │  │
       I1 ──────┐     │ ┌▼─┐│  │
                └─────┼►│AND├┤  │
                      │ └──┬┘│  │
                      │    │ │  │
       I2 ──────┐     │    │┌▼─┐│
                └─────┼────┼►│AND├
                      │    │└──┬┘│
                      │    │   │ │
       I3 ──────┐     │    │   │┌▼─┐
                └─────┼────┼───┼►│AND│
                      │    │   │└──┬┘
                      │    │   │   │
                      │    │   │   │
                   ┌──▼────▼───▼───▼──┐
                   │       OR         │
                   │     (4 ent)      │
                   └────────┬─────────┘
                            │
                            ▼
                            Y
```

---

## Paso 5: Lista de Compuertas

| Compuerta | Cantidad | Uso |
|-----------|:--------:|-----|
| NOT | 2 | Complementar $S_1$ y $S_0$ |
| AND (3 ent) | 4 | Habilitar cada entrada |
| OR (4 ent) | 1 | Combinar salidas |
| **Total** | **7** | |

---

## Paso 6: Desglose de cada AND

| AND | Entradas | Habilita |
|-----|----------|----------|
| AND₀ | $\bar{S_1}, \bar{S_0}, I_0$ | Entrada 0 |
| AND₁ | $\bar{S_1}, S_0, I_1$ | Entrada 1 |
| AND₂ | $S_1, \bar{S_0}, I_2$ | Entrada 2 |
| AND₃ | $S_1, S_0, I_3$ | Entrada 3 |

---

## Verificación

### Caso: $S_1=1, S_0=0$
- AND₀: $\bar{1} \cdot \bar{0} \cdot I_0 = 0 \cdot 1 \cdot I_0 = 0$
- AND₁: $\bar{1} \cdot 0 \cdot I_1 = 0 \cdot 0 \cdot I_1 = 0$
- AND₂: $1 \cdot \bar{0} \cdot I_2 = 1 \cdot 1 \cdot I_2 = I_2$ ✓
- AND₃: $1 \cdot 0 \cdot I_3 = 0$

$$Y = 0 + 0 + I_2 + 0 = I_2 \checkmark$$

---

## Aplicaciones del MUX

1. **Selector de datos:** Elegir entre múltiples fuentes
2. **Generador de funciones:** Implementar cualquier función de n variables
3. **Conversor paralelo-serie:** Serializar datos
4. **Routing en FPGA:** Interconexión programable

---

## Implementación de Funciones con MUX

Un MUX 4:1 puede implementar **cualquier función de 2 variables**:

Para $F(A,B)$, conectar:
- $S_1 = A$, $S_0 = B$
- $I_0 = F(0,0)$
- $I_1 = F(0,1)$
- $I_2 = F(1,0)$
- $I_3 = F(1,1)$

### Ejemplo: XOR con MUX 4:1
| A | B | XOR |
|---|---|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Conectar: $I_0=0, I_1=1, I_2=1, I_3=0$

---

## Conceptos Clave Aplicados

1. **Decodificación:** Los selectores activan solo un AND
2. **Habilitación:** Cada dato pasa solo cuando está seleccionado
3. **Combinación:** La OR une todas las posibles salidas
4. **Universalidad:** Un MUX puede implementar cualquier función

---

> 💡 **Tip:** Un MUX $2^n:1$ puede implementar cualquier función de n variables.
