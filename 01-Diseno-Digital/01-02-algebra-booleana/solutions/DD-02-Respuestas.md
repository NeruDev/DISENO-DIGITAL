<!--
::METADATA::
type: solution
topic_id: dd-02-algebra-booleana
file_id: respuestas-algebra-booleana
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, álgebra booleana"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-02-Problemas.md)

---

# Respuestas: Álgebra Booleana

## Nivel 1: Tablas de Verdad

### Respuestas 1.1

**a) $F = AB + \overline{A}C$**

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

**b) $F = (A + B)(A + C)$**: Misma tabla que (a) - son equivalentes

**c) $F = A \oplus B$**: F=1 cuando A≠B → (0,1), (1,0)

**d) $F = \overline{A + B}$**: F=1 solo cuando A=0 Y B=0

### Respuestas 1.2

- a) **SOP:** $F = \overline{A}\overline{B}\overline{C} + \overline{A}B\overline{C} + \overline{A}BC + AB\overline{C} + ABC$
- b) **POS:** $F = (A + B + \overline{C})(A + \overline{B} + C)(\overline{A} + B + C)$
- c) **Minterms:** $F = \sum m(0, 2, 3, 6, 7)$
   **Maxterms:** $F = \prod M(1, 4, 5)$

---

## Nivel 2: Aplicación de Teoremas

### Respuestas 2.1 (Demostraciones)

**a) $A + AB = A$**
```
A + AB = A(1 + B) = A(1) = A
```

**b) $A + \overline{A}B = A + B$**
```
A + ĀB = (A + Ā)(A + B) = 1·(A + B) = A + B
```

**c) $(A + B)(A + C) = A + BC$**
```
(A + B)(A + C) = AA + AC + AB + BC
              = A + AC + AB + BC
              = A(1 + C + B) + BC
              = A + BC
```

**d) Consenso: $AB + \overline{A}C + BC = AB + \overline{A}C$**
```
BC = BC(A + Ā) = ABC + ĀBC
AB + ĀC + BC = AB + ĀC + ABC + ĀBC
             = AB(1 + C) + ĀC(1 + B)
             = AB + ĀC
```

### Respuestas 2.2 (Simplificación)

| | Expresión Original | Simplificada |
|--|-------------------|--------------|
| a) | $A\overline{B} + AB$ | $A$ |
| b) | $\overline{A}B + A\overline{B} + AB$ | $A + B$ |
| c) | $ABC + AB\overline{C} + A\overline{B}C + A\overline{B}\overline{C}$ | $A$ |
| d) | $(A + B)(\overline{A} + B)(A + \overline{B})$ | $AB$ |

### Respuestas 2.3 (De Morgan)

| | Original | Complemento |
|--|----------|-------------|
| a) | $AB + CD$ | $(\overline{A}+\overline{B})(\overline{C}+\overline{D})$ |
| b) | $(A+B)(C+D)$ | $\overline{A}\overline{B} + \overline{C}\overline{D}$ |
| c) | $A\overline{B} + \overline{A}B$ | $(A+\overline{B})(\overline{A}+B)$ ó $AB + \overline{A}\overline{B}$ |
| d) | $\overline{A}BC + A\overline{B}C + AB\overline{C}$ | $(A+\overline{B}+\overline{C})(\overline{A}+B+\overline{C})(\overline{A}+\overline{B}+C)$ |

---

## Nivel 3: Mapas de Karnaugh (2-3 Variables)

### Respuestas 3.1 (2 variables)

| | Minterms | Resultado |
|--|----------|-----------|
| a) | $\sum m(0, 1, 2)$ | $\overline{B} + \overline{A}$ |
| b) | $\sum m(1, 3)$ | $B$ |
| c) | $\sum m(0, 3)$ | $\overline{A}\overline{B} + AB$ ó $A \odot B$ |

### Respuestas 3.2 (3 variables)

| | Minterms | Resultado |
|--|----------|-----------|
| a) | $\sum m(0, 2, 4, 6)$ | $\overline{C}$ |
| b) | $\sum m(1, 3, 5, 7)$ | $C$ |
| c) | $\sum m(0, 1, 2, 3, 7)$ | $\overline{A} + BC$ |
| d) | $\sum m(2, 3, 4, 5)$ | $A\overline{B} + \overline{A}B$ ó $A \oplus B$ |

### Respuestas 3.3

**a) $F(A,B,C) = \sum m(0, 1, 6, 7)$**
- **SOP:** $F = \overline{A}\overline{B} + AB$
- **POS:** $F = (A + \overline{B})(\overline{A} + B)$

**b) $F(A,B,C) = \sum m(1, 2, 5, 6)$**
- **SOP:** $F = B\overline{C} + \overline{B}C$ ó $B \oplus C$
- **POS:** $F = (B + C)(\overline{B} + \overline{C})$

---

## Nivel 4: Mapas de Karnaugh (4 Variables)

### Respuestas 4.1

| | Minterms | Resultado |
|--|----------|-----------|
| a) | $\sum m(0-7)$ | $\overline{A}$ |
| b) | $\sum m(0, 2, 8, 10)$ | $\overline{B}\overline{D}$ |
| c) | $\sum m(1,3,5,7,9,11,13,15)$ | $D$ |
| d) | $\sum m(0,4,8,12,1,5,9,13)$ | $\overline{C}$ |

### Respuestas 4.2

| | Minterms | Resultado |
|--|----------|-----------|
| a) | $\sum m(0,1,4,5,6,7,8,9,14,15)$ | $\overline{A}\overline{B} + \overline{A}C + AB$ |
| b) | $\sum m(2,3,6,7,10,11,12,13)$ | $BC + A\overline{B}$ ó $B \oplus A$ (verificar) |
| c) | $\sum m(0,2,3,5,7,8,10,11,13,15)$ | $\overline{B}D + BD + \overline{C}$ (simplificar más) → $D + \overline{B}\overline{C}$ |

---

## Nivel 5: Condiciones Don't Care

### Respuestas 5.1

| | Función | Resultado |
|--|---------|-----------|
| a) | $\sum m(1,2,5) + d(0,3)$ | $\overline{A} + \overline{B}C$ (usando d(0,3)) → $\overline{A}$ |
| b) | $\sum m(0,4,6) + d(2,7)$ | $\overline{C}$ (usando d(2)) |

### Respuestas 5.2 (Segmento 'a')

Dígitos con segmento 'a' encendido: 0, 2, 3, 5, 6, 7, 8, 9

$F = \sum m(0,2,3,5,6,7,8,9) + d(10,11,12,13,14,15)$

**Resultado:** $F = A + C + B\overline{D} + \overline{B}D$ 

ó más simplificado: $F = A + C + (B \oplus D)$

### Respuestas 5.3

- **Sin don't cares:** $F = \overline{A}\overline{B}D + \overline{A}BD + A\overline{B}\overline{C}D$
- **Con don't cares:** $F = \overline{B}D + \overline{A}D$ → $F = D(\overline{A} + \overline{B})$

---

## Nivel 6: Implementación con Compuertas

### Respuestas 6.1

| | Expresión | AND | OR | NOT | Entradas Total |
|--|-----------|-----|-----|-----|----------------|
| a) | $AB + \overline{A}C$ | 2 | 1 | 1 | 6 |
| b) | $(A+B)(B+C)$ | 1 | 2 | 0 | 5 |
| c) | $A \oplus B \oplus C$ | - | - | - | 3 (XOR) |

### Respuestas 6.2 (Solo NAND)

**a) $F = AB + CD$**
$$F = \overline{\overline{AB} \cdot \overline{CD}}$$
NAND de (NAND(A,B), NAND(C,D))

**b) $F = A + BC$**
$$F = \overline{\overline{A} \cdot \overline{BC}}$$

**c) $F = (A + B)C$**
$$F = \overline{\overline{(A+B)C}} = \overline{\overline{A}\cdot\overline{B} + \overline{C}}$$

### Respuestas 6.3 (Solo NOR)

**a) $F = (A + B)(C + D)$**
$$F = \overline{\overline{A+B} + \overline{C+D}}$$
NOR de (NOR(A,B), NOR(C,D)) con inversión

**b) $F = AB + C$**
$$F = \overline{\overline{A}+\overline{B}} + C = \overline{\overline{\overline{\overline{A}+\overline{B}} + C}}$$

---

## Nivel 7: Problemas de Aplicación

### Respuestas 7.1 (Sistema de Alarma)

- **a) Expresión:** $F = PA + MOA$
- **b) Simplificada:** $F = A(P + MO)$
- **c) Circuito:** AND de M y O, OR con P, AND final con A

### Respuestas 7.2 (Votación Mayoría 4 bits)

$F = \sum m(7, 11, 13, 14, 15)$ → simplificando:

$$F = ABC + ABD + ACD + BCD$$

### Respuestas 7.3 (Comparador 2 bits)

- **G (A>B):** $G = A_1\overline{B_1} + A_0\overline{B_0}(A_1 \odot B_1)$
- **E (A=B):** $E = (A_1 \odot B_1)(A_0 \odot B_0)$
- **L (A<B):** $L = \overline{A_1}B_1 + \overline{A_0}B_0(A_1 \odot B_1)$

### Respuestas 7.4 (Detector Paridad Par)

$$F = A \oplus B \oplus C \oplus D$$

(F=1 cuando hay número impar de 1s, para paridad par usar $\overline{F}$)

---

## Problemas Integradores

### Respuestas 8.1

$F(A,B,C,D) = \sum m(0, 1, 2, 5, 8, 9, 10)$

- **a) SOP mínima:** $F = \overline{B}\overline{C} + \overline{A}\overline{B}D + A\overline{C}\overline{D}$
- **b) POS mínima:** Complementar y aplicar De Morgan
- **c) Solo NAND:** Doble negación de SOP
- **d) Solo NOR:** Doble negación de POS

### Respuestas 8.2 (MUX 4:1)

$$Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0I_1 + S_1\overline{S_0}I_2 + S_1S_0I_3$$

No se puede simplificar más (forma canónica del MUX).

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas rápidas para verificación
NOTA: Algunas simplificaciones pueden tener soluciones alternativas equivalentes
-->
