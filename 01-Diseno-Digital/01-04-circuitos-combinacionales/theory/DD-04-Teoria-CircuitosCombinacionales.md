<!--
::METADATA::
type: theory
topic_id: dd-04-circuitos-combinacionales
file_id: teoria-circuitos-combinacionales
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [combinacional, multiplexor, decodificador, sumador, comparador, ALU]
search_keywords: "circuitos combinacionales, multiplexor, decodificador, codificador, sumador, comparador"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-04-Intro.md) | [Métodos →](../methods/DD-04-Metodos-Diseno.md)

---

# Circuitos Combinacionales

## 1. Introducción

Un **circuito combinacional** es aquel cuya salida depende únicamente de las entradas actuales, sin memoria de estados anteriores.

$$Y = f(X_1, X_2, \ldots, X_n)$$

**Características:**
- No tiene retroalimentación
- No tiene elementos de memoria
- La salida cambia cuando cambian las entradas

---

## 2. Multiplexores (MUX)

### 2.1 Definición

Un **multiplexor** selecciona una de varias entradas de datos y la envía a una única salida.

### 2.2 MUX 2:1

**Entradas:** $I_0$, $I_1$ (datos), $S$ (selector)
**Salida:** $Y$

$$Y = \overline{S}I_0 + SI_1$$

| S | Y |
|---|---|
| 0 | $I_0$ |
| 1 | $I_1$ |

### 2.3 MUX 4:1

**Entradas:** $I_0$, $I_1$, $I_2$, $I_3$, selectores $S_1S_0$

$$Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0I_1 + S_1\overline{S_0}I_2 + S_1S_0I_3$$

| $S_1$ | $S_0$ | Y |
|-------|-------|---|
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

**CI típico:** 74LS153 (dual MUX 4:1), 74LS151 (MUX 8:1)

### 2.4 Implementación de Funciones con MUX

Cualquier función de n variables puede implementarse con un MUX de $2^{n-1}$:1

**Ejemplo:** $F(A,B,C) = \sum m(1,2,4,7)$ con MUX 4:1

Usando A, B como selectores:
| AB | Minterms | $I$ |
|----|----------|-----|
| 00 | $m_0, m_1$ | C |
| 01 | $m_2, m_3$ | $\overline{C}$ |
| 10 | $m_4, m_5$ | $\overline{C}$ |
| 11 | $m_6, m_7$ | C |

---

## 3. Demultiplexores (DEMUX)

### 3.1 Definición

Un **demultiplexor** toma una entrada y la dirige a una de varias salidas según los selectores.

### 3.2 DEMUX 1:4

**Entrada:** D (dato), $S_1S_0$ (selectores)
**Salidas:** $Y_0, Y_1, Y_2, Y_3$

$$Y_i = D \cdot (\text{combinación de selectores para } i)$$

| $S_1$ | $S_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
|-------|-------|-------|-------|-------|-------|
| 0 | 0 | D | 0 | 0 | 0 |
| 0 | 1 | 0 | D | 0 | 0 |
| 1 | 0 | 0 | 0 | D | 0 |
| 1 | 1 | 0 | 0 | 0 | D |

---

## 4. Decodificadores

### 4.1 Definición

Un **decodificador** de n a $2^n$ activa exactamente una salida basándose en la combinación de entrada.

### 4.2 Decodificador 2:4

**Entradas:** $A_1, A_0$
**Salidas:** $Y_0, Y_1, Y_2, Y_3$ (activas en bajo o alto)

$$Y_0 = \overline{A_1}\overline{A_0}$$
$$Y_1 = \overline{A_1}A_0$$
$$Y_2 = A_1\overline{A_0}$$
$$Y_3 = A_1A_0$$

**CI típico:** 74LS139 (dual 2:4), 74LS138 (3:8)

### 4.3 Decodificador 3:8 (74LS138)

| $A_2$ | $A_1$ | $A_0$ | Salida Activa |
|-------|-------|-------|---------------|
| 0 | 0 | 0 | $\overline{Y_0}$ |
| 0 | 0 | 1 | $\overline{Y_1}$ |
| 0 | 1 | 0 | $\overline{Y_2}$ |
| ... | ... | ... | ... |
| 1 | 1 | 1 | $\overline{Y_7}$ |

### 4.4 Implementación de Funciones con Decodificadores

$$F = \sum m(i, j, k) = m_i + m_j + m_k$$

Usando decodificador + OR:
- Cada minterm es una salida del decodificador
- OR de las salidas correspondientes

---

## 5. Codificadores

### 5.1 Codificador Simple 4:2

**Entradas:** $I_0, I_1, I_2, I_3$ (solo una activa)
**Salidas:** $A_1, A_0$ (código binario)

| Entrada Activa | $A_1$ | $A_0$ |
|----------------|-------|-------|
| $I_0$ | 0 | 0 |
| $I_1$ | 0 | 1 |
| $I_2$ | 1 | 0 |
| $I_3$ | 1 | 1 |

### 5.2 Codificador de Prioridad

Cuando múltiples entradas están activas, codifica la de mayor prioridad.

**CI típico:** 74LS148 (8:3 con prioridad)

---

## 6. Sumadores

### 6.1 Half Adder (Medio Sumador)

Suma 2 bits sin considerar acarreo de entrada.

**Entradas:** A, B
**Salidas:** S (suma), C (acarreo)

$$S = A \oplus B$$
$$C = AB$$

| A | B | S | C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

### 6.2 Full Adder (Sumador Completo)

Suma 2 bits más acarreo de entrada.

**Entradas:** A, B, $C_{in}$
**Salidas:** S, $C_{out}$

$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = AB + C_{in}(A \oplus B)$$

| A | B | $C_{in}$ | S | $C_{out}$ |
|---|---|----------|---|-----------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

### 6.3 Sumador de 4 bits (Ripple Carry)

Conectar 4 Full Adders en cascada.

**CI típico:** 74LS283 (sumador 4 bits)

### 6.4 Sumador/Restador

Para restar: $A - B = A + \overline{B} + 1$

Usar XOR controlado por señal SUB:
- SUB=0: Suma normal
- SUB=1: Invierte B y $C_{in}=1$

---

## 7. Comparadores

### 7.1 Comparador de 1 bit

**Salidas:**
$$G = A\overline{B} \quad \text{(A > B)}$$
$$E = \overline{A \oplus B} = AB + \overline{A}\overline{B} \quad \text{(A = B)}$$
$$L = \overline{A}B \quad \text{(A < B)}$$

### 7.2 Comparador de 4 bits (74LS85)

Compara dos números de 4 bits con entradas de cascada.

**Entradas:** $A_3A_2A_1A_0$, $B_3B_2B_1B_0$, $G_{in}$, $E_{in}$, $L_{in}$
**Salidas:** $G_{out}$, $E_{out}$, $L_{out}$

---

## 8. Unidad Aritmético-Lógica (ALU)

### 8.1 Definición

La **ALU** realiza operaciones aritméticas y lógicas seleccionadas por un código de operación.

### 8.2 74LS181 (ALU de 4 bits)

| S3 | S2 | S1 | S0 | M=1 (Lógica) | M=0 (Aritmética) |
|----|----|----|----|--------------| -----------------|
| 0 | 0 | 0 | 0 | $\overline{A}$ | A |
| 0 | 0 | 0 | 1 | $\overline{A+B}$ | A + B |
| ... | ... | ... | ... | ... | ... |
| 1 | 0 | 0 | 1 | $A \oplus B$ | A + B + Cin |

### 8.3 Operaciones Típicas

- Suma, resta
- AND, OR, XOR, NOT
- Incremento, decremento
- Comparación

---

## 9. Generadores/Detectores de Paridad

### 9.1 Paridad Par

El bit de paridad hace que el número total de 1s sea par.

$$P = D_0 \oplus D_1 \oplus D_2 \oplus D_3$$

### 9.2 CI Típico

74LS280: Generador/Verificador de paridad de 9 bits

---

## 10. Circuitos de Aplicación

### 10.1 Display 7 Segmentos

**Decodificador BCD a 7 segmentos:** 74LS47 (ánodo común), 74LS48 (cátodo común)

```
    a
   ───
f │   │ b
   ─g─
e │   │ c
   ───
    d
```

### 10.2 Convertidor de Código

Transforma un código binario en otro (BCD a Excess-3, Gray a Binario, etc.)

---

## 11. Análisis de Hazards

### 11.1 Hazard Estático

Glitch momentáneo en la salida cuando debería permanecer constante.

**Solución:** Agregar términos redundantes.

### 11.2 Hazard Dinámico

Múltiples transiciones cuando debería haber una sola.

**Solución:** Diseño cuidadoso de tiempos.

---

## Referencias

- Mano, M. M. (2013). *Digital Design*. Pearson.
- Wakerly, J. F. (2006). *Digital Design: Principles and Practices*. Pearson.

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 01-03 Compuertas Lógicas
CONEXIONES: Base para diseño de procesadores y sistemas digitales
ERRORES_COMUNES: Confundir MUX con DEMUX, olvidar acarreo en sumadores
-->
