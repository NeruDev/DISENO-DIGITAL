<!--
::METADATA::
type: reference
topic_id: dd-04-circuitos-combinacionales
file_id: resumen-formulas-combinacionales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, formulas, combinacionales, referencia]
search_keywords: "resumen, fórmulas, circuitos combinacionales, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-04-Intro.md)

---

# 📋 Cheatsheet: Circuitos Combinacionales

## Multiplexor (MUX)

### MUX 2:1
$$Y = \overline{S}I_0 + SI_1$$

### MUX 4:1
$$Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0I_1 + S_1\overline{S_0}I_2 + S_1S_0I_3$$

### Implementar Función con MUX

Para $F(n\ variables)$ usar MUX $2^{n-1}$:1
- n-1 variables como selectores
- 1 variable (o 0,1,$\overline{V}$,V) como entradas

---

## Decodificador

### Decodificador n:2ⁿ

Cada salida = un minterm

$$Y_i = m_i$$

### Implementar Función con DEC

$$F = \sum m(i,j,k) \rightarrow F = Y_i + Y_j + Y_k$$

---

## Sumadores

### Half Adder
$$S = A \oplus B$$
$$C = AB$$

### Full Adder
$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = AB + C_{in}(A \oplus B)$$

### Sumador/Restador
$$A - B = A + \overline{B} + 1$$

---

## Comparador

### 1 bit
$$G = A\overline{B}$$
$$E = A \odot B$$
$$L = \overline{A}B$$

### n bits (cascada)
$$G_i = A_i\overline{B_i} + E_{i+1} \cdot G_{i+1}$$

---

## CIs Comunes

| CI | Función |
|----|---------|
| 74LS151 | MUX 8:1 |
| 74LS153 | Dual MUX 4:1 |
| 74LS138 | DEC 3:8 |
| 74LS139 | Dual DEC 2:4 |
| 74LS283 | Sumador 4 bits |
| 74LS85 | Comparador 4 bits |
| 74LS181 | ALU 4 bits |
| 74LS47 | BCD a 7-seg |

---

## Conversiones de Código

### Gray ↔ Binario

**Bin → Gray:**
$$G_i = B_i \oplus B_{i+1}$$

**Gray → Bin:**
$$B_i = B_{i+1} \oplus G_i$$

---

## Paridad

### Generador Par
$$P = D_0 \oplus D_1 \oplus D_2 \oplus D_3$$

### Verificador
Error = $D_0 \oplus D_1 \oplus \cdots \oplus P \neq 0$

---

## Display 7 Segmentos

```
    a
   ───
f │   │ b
   ─g─
e │   │ c
   ───
    d
```

| Dígito | Segmentos |
|--------|-----------|
| 0 | a,b,c,d,e,f |
| 1 | b,c |
| 2 | a,b,d,e,g |
| 3 | a,b,c,d,g |
| 4 | b,c,f,g |
| 5 | a,c,d,f,g |
| 6 | a,c,d,e,f,g |
| 7 | a,b,c |
| 8 | todos |
| 9 | a,b,c,d,f,g |

---

## Retardos

### Ripple Carry Adder
$$t_{total} = n \times t_{FA}$$

### Carry Look-Ahead
$$t_{total} = t_{PG} + t_{CLA} + t_{sum}$$

---

## Detección Overflow (C2)

$$V = C_{n-1} \oplus C_n$$

Overflow cuando los acarreos del bit MSB difieren.

---

## Fórmulas ALU

### Zero Flag
$$Z = \overline{F_{n-1} + F_{n-2} + \cdots + F_0}$$

### Negative Flag
$$N = F_{n-1}$$

### Carry Flag
$$C = C_{out}$$

---

## Proceso de Diseño

1. Especificación → Entradas/Salidas
2. Tabla de Verdad
3. Minterms / Maxterms
4. Simplificación (K-map)
5. Implementación
6. Verificación

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño y exámenes
-->
