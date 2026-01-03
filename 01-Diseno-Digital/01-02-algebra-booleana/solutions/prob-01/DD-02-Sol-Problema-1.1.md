<!--
::METADATA::
type: detailed_solution
topic_id: dd-02-algebra-booleana
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 1
tags: [solucion, algebra-booleana, simplificacion, teoremas]
-->

> 🏠 **Navegación:** [← Respuestas](../DD-02-Respuestas.md) | [Problema 1.2 →](./DD-02-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Simplificar las siguientes expresiones booleanas usando teoremas del álgebra de Boole:
- a) $A \cdot (A + B)$
- b) $A + A \cdot B$
- c) $(A + B) \cdot (A + \bar{B})$
- d) $A \cdot B + A \cdot \bar{B}$

---

## Teoremas Aplicados

| Teorema | Expresión | Nombre |
|---------|-----------|--------|
| T1 | $A \cdot (A + B) = A$ | Absorción |
| T2 | $A + A \cdot B = A$ | Absorción |
| T3 | $A + \bar{A} = 1$ | Complemento |
| T4 | $A \cdot \bar{A} = 0$ | Complemento |
| T5 | $A \cdot (B + C) = A \cdot B + A \cdot C$ | Distributiva |

---

## a) Simplificar $A \cdot (A + B)$

### Método 1: Teorema de Absorción (Directo)
$$A \cdot (A + B) = \boxed{A}$$

El teorema de absorción establece que $A \cdot (A + B) = A$.

### Método 2: Demostración paso a paso
$$A \cdot (A + B)$$
$$= A \cdot A + A \cdot B \quad \text{(Distributiva)}$$
$$= A + A \cdot B \quad \text{(Idempotencia: } A \cdot A = A \text{)}$$
$$= A \cdot (1 + B) \quad \text{(Factorizar)}$$
$$= A \cdot 1 \quad \text{(} 1 + B = 1 \text{)}$$
$$= \boxed{A}$$

### Verificación por tabla de verdad

| A | B | A + B | A · (A + B) |
|---|---|-------|-------------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 |

La columna $A \cdot (A + B)$ es idéntica a la columna $A$. ✓

---

## b) Simplificar $A + A \cdot B$

### Método 1: Teorema de Absorción (Directo)
$$A + A \cdot B = \boxed{A}$$

### Método 2: Demostración paso a paso
$$A + A \cdot B$$
$$= A \cdot 1 + A \cdot B \quad \text{(Identidad: } A = A \cdot 1 \text{)}$$
$$= A \cdot (1 + B) \quad \text{(Factorizar)}$$
$$= A \cdot 1 \quad \text{(} 1 + B = 1 \text{)}$$
$$= \boxed{A}$$

---

## c) Simplificar $(A + B) \cdot (A + \bar{B})$

### Paso 1: Expandir (Distributiva)
$$(A + B) \cdot (A + \bar{B})$$
$$= A \cdot A + A \cdot \bar{B} + B \cdot A + B \cdot \bar{B}$$

### Paso 2: Simplificar términos
$$= A + A \cdot \bar{B} + A \cdot B + 0$$
$$= A + A \cdot (\bar{B} + B)$$
$$= A + A \cdot 1$$
$$= A + A$$
$$= \boxed{A}$$

### Método alternativo: Consenso

Usando el teorema $(X + Y)(X + Z) = X + YZ$:
$$(A + B) \cdot (A + \bar{B}) = A + B \cdot \bar{B} = A + 0 = \boxed{A}$$

---

## d) Simplificar $A \cdot B + A \cdot \bar{B}$

### Paso 1: Factorizar A
$$A \cdot B + A \cdot \bar{B} = A \cdot (B + \bar{B})$$

### Paso 2: Aplicar complemento
$$= A \cdot 1 = \boxed{A}$$

### Interpretación
Esta expresión dice: "A está en 1 Y (B está en 1 Ó B está en 0)"

Dado que $B + \bar{B} = 1$ siempre es verdadero, la expresión se reduce a solo $A$.

---

## Resumen de Respuestas

| Expresión Original | Simplificada | Teorema Principal |
|-------------------|--------------|-------------------|
| $A \cdot (A + B)$ | $A$ | Absorción |
| $A + A \cdot B$ | $A$ | Absorción |
| $(A + B)(A + \bar{B})$ | $A$ | Consenso |
| $AB + A\bar{B}$ | $A$ | Complemento |

---

## Observación Importante

Todas las expresiones de este problema se simplifican a **A**. Esto demuestra cómo diferentes formas algebraicas pueden representar la misma función booleana.

---

## Conceptos Clave Aplicados

1. **Absorción:** La variable dominante "absorbe" los términos dependientes
2. **Complemento:** $X + \bar{X} = 1$ y $X \cdot \bar{X} = 0$
3. **Factorización:** Útil para identificar patrones de simplificación
4. **Verificación:** Las tablas de verdad confirman la equivalencia

---

> 💡 **Tip:** Memorizar los teoremas de absorción ahorra muchos pasos:
> - $A + AB = A$
> - $A(A + B) = A$
