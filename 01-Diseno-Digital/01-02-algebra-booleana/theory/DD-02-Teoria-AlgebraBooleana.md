<!--
::METADATA::
type: theory
topic_id: dd-02-algebra-booleana
file_id: teoria-algebra-booleana
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [boole, logica, simplificacion, teoremas, postulados]
search_keywords: "álgebra booleana, teoremas, simplificación, postulados, leyes de Morgan"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-02-Intro.md) | [Métodos →](../methods/DD-02-Metodos-Simplificacion.md)

---

# Álgebra Booleana

## 1. Introducción

El **Álgebra Booleana** es un sistema matemático desarrollado por George Boole (1854) que trabaja con variables que solo pueden tomar dos valores: **0** (falso) y **1** (verdadero).

Es la base matemática de todos los circuitos digitales y sistemas de lógica computacional.

---

## 2. Operaciones Fundamentales

### 2.1 Operación AND (Producto Lógico)

Símbolo: $\cdot$ , $\land$ , o simplemente concatenación

$$A \cdot B = Y$$

| A | B | Y = A·B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Interpretación:** La salida es 1 solo cuando TODAS las entradas son 1.

### 2.2 Operación OR (Suma Lógica)

Símbolo: $+$ , $\lor$

$$A + B = Y$$

| A | B | Y = A+B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Interpretación:** La salida es 1 cuando AL MENOS una entrada es 1.

### 2.3 Operación NOT (Complemento)

Símbolo: $\overline{A}$ , $A'$ , $\lnot A$

$$\overline{A} = Y$$

| A | Y = Ā |
|---|-------|
| 0 | 1 |
| 1 | 0 |

**Interpretación:** Invierte el valor de la variable.

---

## 3. Operaciones Derivadas

### 3.1 NAND (NOT-AND)

$$\overline{A \cdot B}$$

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 3.2 NOR (NOT-OR)

$$\overline{A + B}$$

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

### 3.3 XOR (OR Exclusivo)

Símbolo: $\oplus$

$$A \oplus B = A\overline{B} + \overline{A}B$$

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Interpretación:** La salida es 1 cuando las entradas son DIFERENTES.

### 3.4 XNOR (Equivalencia)

Símbolo: $\odot$

$$A \odot B = AB + \overline{A}\overline{B}$$

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Interpretación:** La salida es 1 cuando las entradas son IGUALES.

---

## 4. Postulados del Álgebra Booleana

Los postulados son verdades fundamentales que no requieren demostración:

### 4.1 Postulados de Huntington

| # | AND | OR |
|---|-----|-----|
| P1 | $0 \cdot 0 = 0$ | $1 + 1 = 1$ |
| P2 | $1 \cdot 1 = 1$ | $0 + 0 = 0$ |
| P3 | $0 \cdot 1 = 1 \cdot 0 = 0$ | $1 + 0 = 0 + 1 = 1$ |
| P4 | Si $A = 0$ entonces $\overline{A} = 1$ | Si $A = 1$ entonces $\overline{A} = 0$ |

---

## 5. Teoremas Fundamentales

### 5.1 Teoremas de Una Variable

| # | Teorema | Dual |
|---|---------|------|
| T1 | $A + 0 = A$ | $A \cdot 1 = A$ |
| T2 | $A + 1 = 1$ | $A \cdot 0 = 0$ |
| T3 | $A + A = A$ | $A \cdot A = A$ |
| T4 | $A + \overline{A} = 1$ | $A \cdot \overline{A} = 0$ |
| T5 | $\overline{\overline{A}} = A$ | (Involución) |

### 5.2 Teoremas de Dos Variables

| # | Teorema | Dual |
|---|---------|------|
| T6 | $A + B = B + A$ | $A \cdot B = B \cdot A$ |
| T7 | $A + (B + C) = (A + B) + C$ | $A(BC) = (AB)C$ |
| T8 | $A(B + C) = AB + AC$ | $A + BC = (A + B)(A + C)$ |
| T9 | $A + AB = A$ | $A(A + B) = A$ |
| T10 | $A + \overline{A}B = A + B$ | $A(\overline{A} + B) = AB$ |

### 5.3 Teoremas de De Morgan

> ⚠️ **Teoremas más importantes para simplificación**

**Primera Ley:**
$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

**Segunda Ley:**
$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

**Generalización (n variables):**
$$\overline{A_1 + A_2 + \cdots + A_n} = \overline{A_1} \cdot \overline{A_2} \cdots \overline{A_n}$$
$$\overline{A_1 \cdot A_2 \cdots A_n} = \overline{A_1} + \overline{A_2} + \cdots + \overline{A_n}$$

---

## 6. Principio de Dualidad

Toda identidad booleana tiene una **dual** que se obtiene:
1. Intercambiando $+$ por $\cdot$
2. Intercambiando $0$ por $1$
3. Manteniendo los complementos

**Ejemplo:**
- Original: $A + 0 = A$
- Dual: $A \cdot 1 = A$

---

## 7. Formas Canónicas

### 7.1 Minterms (Productos Canónicos)

Un **minterm** es un producto AND de todas las variables donde cada variable aparece exactamente una vez (complementada o no).

Para 3 variables $(A, B, C)$:

| Minterm | Notación | Expresión |
|---------|----------|-----------|
| $m_0$ | $m(0)$ | $\overline{A}\overline{B}\overline{C}$ |
| $m_1$ | $m(1)$ | $\overline{A}\overline{B}C$ |
| $m_2$ | $m(2)$ | $\overline{A}B\overline{C}$ |
| $m_3$ | $m(3)$ | $\overline{A}BC$ |
| $m_4$ | $m(4)$ | $A\overline{B}\overline{C}$ |
| $m_5$ | $m(5)$ | $A\overline{B}C$ |
| $m_6$ | $m(6)$ | $AB\overline{C}$ |
| $m_7$ | $m(7)$ | $ABC$ |

### 7.2 Maxterms (Sumas Canónicas)

Un **maxterm** es una suma OR de todas las variables donde cada variable aparece exactamente una vez.

| Maxterm | Notación | Expresión |
|---------|----------|-----------|
| $M_0$ | $M(0)$ | $A + B + C$ |
| $M_1$ | $M(1)$ | $A + B + \overline{C}$ |
| $M_2$ | $M(2)$ | $A + \overline{B} + C$ |
| ... | ... | ... |
| $M_7$ | $M(7)$ | $\overline{A} + \overline{B} + \overline{C}$ |

### 7.3 Suma de Productos (SOP)

$$F = \sum m(i, j, k, \ldots)$$

**Ejemplo:** $F(A,B,C) = \sum m(1, 3, 5, 7)$

### 7.4 Producto de Sumas (POS)

$$F = \prod M(i, j, k, \ldots)$$

**Relación:** $F = \sum m(i) \Leftrightarrow \overline{F} = \prod M(i)$

---

## 8. Tabla de Verdad

La tabla de verdad lista todas las combinaciones posibles de entradas y sus correspondientes salidas.

**Ejemplo:** Función mayoría de 3 variables

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

$$F = \sum m(3, 5, 6, 7) = \overline{A}BC + A\overline{B}C + AB\overline{C} + ABC$$

---

## 9. Precedencia de Operadores

1. **Paréntesis** (mayor precedencia)
2. **NOT** (complemento)
3. **AND** (producto)
4. **OR** (suma, menor precedencia)

**Ejemplo:** $A + B \cdot \overline{C} = A + (B \cdot (\overline{C}))$

---

## Referencias

- Mano, M. M. (2013). *Digital Design*. Pearson.
- Floyd, T. L. (2015). *Digital Fundamentals*. Pearson.

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: 01-01 Sistemas Numéricos (conceptos de binario)
CONEXIONES: Base para compuertas lógicas y simplificación de circuitos
ERRORES_COMUNES: Confundir + con OR (no suma aritmética), olvidar De Morgan
-->
