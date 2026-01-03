<!--
::METADATA::
type: reference
topic_id: dd-02-algebra-booleana
file_id: resumen-formulas-algebra-booleana
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, formulas, resumen, teoremas]
search_keywords: "resumen, fórmulas, teoremas, De Morgan, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-02-Intro.md)

---

# 📋 Cheatsheet: Álgebra Booleana

## Operaciones Básicas

| Operación | Símbolo | Resultado |
|-----------|---------|-----------|
| AND | $A \cdot B$ | 1 si ambos son 1 |
| OR | $A + B$ | 1 si alguno es 1 |
| NOT | $\overline{A}$ | Invierte |
| XOR | $A \oplus B$ | 1 si son diferentes |
| XNOR | $A \odot B$ | 1 si son iguales |

---

## Tablas de Verdad

### AND, OR, NOT
```
A B │ A·B  A+B  Ā
────┼─────────────
0 0 │  0    0   1
0 1 │  0    1   1
1 0 │  0    1   0
1 1 │  1    1   0
```

### XOR, XNOR, NAND, NOR
```
A B │ A⊕B  A⊙B  NAND  NOR
────┼─────────────────────
0 0 │  0    1    1     1
0 1 │  1    0    1     0
1 0 │  1    0    1     0
1 1 │  0    1    0     0
```

---

## Teoremas de Una Variable

| AND | OR |
|-----|-----|
| $A \cdot 1 = A$ | $A + 0 = A$ |
| $A \cdot 0 = 0$ | $A + 1 = 1$ |
| $A \cdot A = A$ | $A + A = A$ |
| $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ |

$$\overline{\overline{A}} = A \text{ (Involución)}$$

---

## Teoremas de Dos Variables

| Propiedad | AND | OR |
|-----------|-----|-----|
| Conmutativa | $AB = BA$ | $A+B = B+A$ |
| Asociativa | $(AB)C = A(BC)$ | $(A+B)+C = A+(B+C)$ |
| Distributiva | $A(B+C) = AB+AC$ | $A+BC = (A+B)(A+C)$ |

---

## Teoremas de Absorción

$$A + AB = A$$
$$A(A + B) = A$$
$$A + \overline{A}B = A + B$$
$$A(\overline{A} + B) = AB$$

---

## Leyes de De Morgan ⚠️

$$\overline{A + B} = \overline{A} \cdot \overline{B}$$
$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

**Generalizado:**
$$\overline{A_1 + A_2 + \cdots} = \overline{A_1} \cdot \overline{A_2} \cdots$$
$$\overline{A_1 \cdot A_2 \cdots} = \overline{A_1} + \overline{A_2} + \cdots$$

---

## Teorema del Consenso

$$AB + \overline{A}C + BC = AB + \overline{A}C$$

El término $BC$ es redundante.

---

## Formas Canónicas

### Minterms (3 variables)
| $m_i$ | ABC | Expresión |
|-------|-----|-----------|
| $m_0$ | 000 | $\overline{A}\overline{B}\overline{C}$ |
| $m_1$ | 001 | $\overline{A}\overline{B}C$ |
| $m_2$ | 010 | $\overline{A}B\overline{C}$ |
| $m_3$ | 011 | $\overline{A}BC$ |
| $m_4$ | 100 | $A\overline{B}\overline{C}$ |
| $m_5$ | 101 | $A\overline{B}C$ |
| $m_6$ | 110 | $AB\overline{C}$ |
| $m_7$ | 111 | $ABC$ |

### Notación
- **SOP:** $F = \sum m(i, j, k)$
- **POS:** $F = \prod M(i, j, k)$

---

## Mapa de Karnaugh

### 3 Variables
```
        BC
      00  01  11  10
    ┌────┬────┬────┬────┐
A=0 │ m₀ │ m₁ │ m₃ │ m₂ │
    ├────┼────┼────┼────┤
A=1 │ m₄ │ m₅ │ m₇ │ m₆ │
    └────┴────┴────┴────┘
```

### 4 Variables
```
          CD
        00  01  11  10
      ┌────┬────┬────┬────┐
AB=00 │ m₀ │ m₁ │ m₃ │ m₂ │
      ├────┼────┼────┼────┤
AB=01 │ m₄ │ m₅ │ m₇ │ m₆ │
      ├────┼────┼────┼────┤
AB=11 │m₁₂ │m₁₃ │m₁₅ │m₁₄ │
      ├────┼────┼────┼────┤
AB=10 │ m₈ │ m₉ │m₁₁ │m₁₀ │
      └────┴────┴────┴────┘
```

### Reglas K-Map
1. Grupos: 1, 2, 4, 8, 16 celdas
2. Solo adyacentes (incluye bordes)
3. Grupos más grandes = menos términos
4. Se permite solapamiento
5. Don't care (X) = usar según convenga

---

## Precedencia

1. Paréntesis `()`
2. NOT `¯`
3. AND `·`
4. OR `+`

$$A + BC = A + (B \cdot C)$$

---

## Conversiones NAND/NOR

### Solo NAND
$$AB = \overline{\overline{AB}}$$
$$A + B = \overline{\overline{A} \cdot \overline{B}}$$

### Solo NOR
$$A + B = \overline{\overline{A + B}}$$
$$AB = \overline{\overline{A} + \overline{B}}$$

---

## Identidades XOR

$$A \oplus 0 = A$$
$$A \oplus 1 = \overline{A}$$
$$A \oplus A = 0$$
$$A \oplus \overline{A} = 1$$
$$A \oplus B = \overline{A}B + A\overline{B}$$

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante exámenes o resolución de problemas
-->
