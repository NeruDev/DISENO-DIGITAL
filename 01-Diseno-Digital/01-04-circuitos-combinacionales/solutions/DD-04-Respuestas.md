<!--
::METADATA::
type: solution
topic_id: dd-04-circuitos-combinacionales
file_id: respuestas-circuitos-combinacionales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, circuitos combinacionales"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-04-Problemas.md)

---

# Respuestas: Circuitos Combinacionales

## Nivel 1: Multiplexores

### Respuestas 1.1

**a)** $Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0I_1 + S_1\overline{S_0}I_2 + S_1S_0I_3$

**b)** Cuando $S_1S_0=10$: Y = $I_2$ = 1

**c)** Circuito: 2 NOT (para S̄₁, S̄₀), 4 AND de 3 entradas, 1 OR de 4 entradas

### Respuestas 1.2

**a)** $F = \sum m(1, 2, 5, 7)$

| AB | Minterms | Entrada |
|----|----------|---------|
| 00 | 0,1 | C |
| 01 | 2,3 | $\overline{C}$ |
| 10 | 4,5 | C |
| 11 | 6,7 | C |

**b)** $F = \sum m(0, 3, 4, 6)$: $I_0=\overline{C}$, $I_1=C$, $I_2=\overline{C}$, $I_3=\overline{C}$

**c)** XOR: $I_0=C$, $I_1=\overline{C}$, $I_2=\overline{C}$, $I_3=C$

### Respuestas 1.3

**a)** MUX 8:1 con A,B,C como selectores:
| ABC | F | Entrada |
|-----|---|---------|
| 000 | 1 | D=0→$\overline{D}$, D=1→1 | $\overline{D}+D=1$→**1** |

Entradas: $I_0=1, I_1=1, I_2=0, I_3=1, I_4=0, I_5=1, I_6=0, I_7=D$

**b)** Cascada: Usar A,B para dos MUX 4:1, C para MUX 2:1 final

---

## Nivel 2: Decodificadores

### Respuestas 2.1

**a)** Expresiones:
- $Y_0 = \overline{A}\overline{B}\overline{C}$
- $Y_1 = \overline{A}\overline{B}C$
- ...
- $Y_7 = ABC$

**b)** Entrada 101 (decimal 5) → $Y_5$ activa

**c)** Cuando $\overline{EN}=1$: todas las salidas inactivas

### Respuestas 2.2

**a)** $F = Y_0 + Y_2 + Y_6 + Y_7$

**b)** POS = complemento de minterms no listados: $F = Y_0 \cdot Y_2 \cdot Y_4 \cdot Y_6 \cdot Y_7$
(Usando salidas activas bajas)

**c)** $F_1 = Y_1 + Y_4 + Y_7$; $F_2 = Y_2 + Y_4 + Y_5$

### Respuestas 2.3

**Tabla de verdad:**
| $I_3$ | $I_2$ | $I_1$ | $I_0$ | $A_1$ | $A_0$ | V |
|-------|-------|-------|-------|-------|-------|---|
| 0 | 0 | 0 | 0 | X | X | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | X | 0 | 1 | 1 |
| 0 | 1 | X | X | 1 | 0 | 1 |
| 1 | X | X | X | 1 | 1 | 1 |

**Expresiones:**
- $A_1 = I_3 + I_2$
- $A_0 = I_3 + \overline{I_2}I_1$
- $V = I_3 + I_2 + I_1 + I_0$

---

## Nivel 3: Sumadores

### Respuestas 3.1

**a-b)**
| A | B | S | C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$S = A \oplus B$, $C = AB$

**c)** 1 XOR, 1 AND

**d)** Solo NAND: 5 NAND para XOR + 1 NAND para AND (invertido)

### Respuestas 3.2

**c)** $S = A \oplus B \oplus C_{in}$, $C_{out} = AB + C_{in}(A \oplus B)$

**d)** HA1: A,B → S1,C1; HA2: S1,Cin → S,C2; OR: C1,C2 → Cout

### Respuestas 3.3

**a)**
```
  1010
+ 0111
------
  Cin: 0110
------
 10001
```
Resultado: 10001 (con overflow de 4 bits)

**b)** Retardo máximo: 4 × 20ns = 80ns (peor caso: acarreo propaga por todas las etapas)

**c)** Overflow cuando $C_3 \oplus C_4$ (acarreos de bit 3 y salida difieren)

### Respuestas 3.4

**b)** M=0: Suma (B pasa directo, $C_0=0$)
     M=1: Resta (B invertido, $C_0=1$)

**c)** Overflow: $V = C_3 \oplus C_4$

---

## Nivel 4: Comparadores

### Respuestas 4.1

$$G = A\overline{B}$$
$$E = A \odot B = AB + \overline{A}\overline{B}$$
$$L = \overline{A}B$$

### Respuestas 4.2

**b)** Conectar: $(G,E,L)_{out}$ del chip MSB → $(G,E,L)_{in}$ del chip LSB
      Inicializar chip MSB: $G_{in}=0, E_{in}=1, L_{in}=0$

**c)** Retardo: 2 × $t_p$ del comparador

### Respuestas 4.3

**a)**
- $A>B$: $G = A_1\overline{B_1} + (A_1 \odot B_1)A_0\overline{B_0}$
- $A=B$: $E = (A_1 \odot B_1)(A_0 \odot B_0)$
- $A<B$: $L = \overline{A_1}B_1 + (A_1 \odot B_1)\overline{A_0}B_0$

---

## Nivel 5: Convertidores

### Respuestas 5.1

BCD + 3 = Excess-3

| BCD | E-3 |
|-----|-----|
| 0000 | 0011 |
| 0001 | 0100 |
| ... | ... |
| 1001 | 1100 |

Usar sumador de 4 bits con B = 0011

### Respuestas 5.2

$$B_3 = G_3$$
$$B_2 = B_3 \oplus G_2$$
$$B_1 = B_2 \oplus G_1$$
$$B_0 = B_1 \oplus G_0$$

Retardo: 3 × $t_{XOR}$ (cascada)

### Respuestas 5.3 (segmento 'a')

$a = A + C + BD + \overline{B}\overline{D}$

(Con don't cares para 10-15)

---

## Nivel 6: Paridad

### Respuestas 6.1

$$P = D_0 \oplus D_1 \oplus D_2 \oplus D_3$$

3 XOR en cascada (o árbol de 2 niveles)

### Respuestas 6.2

**a)** Error cuando $D_0 \oplus D_1 \oplus D_2 \oplus D_3 \oplus P = 1$

**c)** Solo detecta errores impares, no puede corregir

---

## Nivel 7: ALU

### Respuestas 7.1

```
sel=00: F = A AND B
sel=01: F = A OR B
sel=10: F = A + B + Cin (suma)
sel=11: F = A + B̄ + 1 (resta, Cin=1)
```

Usar MUX 4:1 para seleccionar operación

### Respuestas 7.2

**c)**
- Overflow: $V = C_3 \oplus C_4$
- Zero: $Z = \overline{F_3 + F_2 + F_1 + F_0}$ (NOR de todas las salidas)

---

## Nivel 8: Aplicaciones

### Respuestas 8.1 (Semáforo)

| $S_1S_0$ | VNS | ANS | RNS | VEW | AEW | REW |
|----------|-----|-----|-----|-----|-----|-----|
| 00 | 1 | 0 | 0 | 0 | 0 | 1 |
| 01 | 0 | 1 | 0 | 0 | 0 | 1 |
| 10 | 0 | 0 | 1 | 1 | 0 | 0 |
| 11 | 0 | 0 | 1 | 0 | 1 | 0 |

Implementar con decodificador 2:4 y lógica combinacional

### Respuestas 8.2 (Dado)

```
LEDs:  1 2 3
       4 5 6
       7 8 9

Valor 1: LED 5
Valor 2: LEDs 3,7
Valor 3: LEDs 3,5,7
Valor 4: LEDs 1,3,7,9
Valor 5: LEDs 1,3,5,7,9
Valor 6: LEDs 1,2,3,7,8,9
```

### Respuestas 8.3 (Detector 5-10)

$F = \overline{A_3}A_2 + A_3\overline{A_2}\overline{A_1}$ 

(Simplificado con Karnaugh)

---

## Nivel 9: Integradores

### Respuestas 9.1 (Multiplicador 2×2)

$$P = A_1A_0 \times B_1B_0$$

- $P_0 = A_0B_0$
- $P_1 = A_1B_0 \oplus A_0B_1$
- $P_2 = A_1B_1 \oplus C_1$ (donde $C_1$ es acarreo de $P_1$)
- $P_3 = C_2$

### Respuestas 9.2 (Binario a BCD)

Para 4 bits (0-15):
- Decenas = 1 cuando entrada ≥ 10
- $D = A_3A_2 + A_3A_1$ (10-15)
- Unidades = entrada - 10 si D=1, sino entrada

### Respuestas 9.3 (Votación)

$Y = P \cdot M_3 + M_5$

Donde $M_3$ = al menos 3 votos, $M_5$ = unanimidad (5 votos)

---

## Nivel 10: Análisis

### Respuestas 10.1

$F = A\overline{B} + CD$

### Respuestas 10.2

| A | B | C | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

$Y = \overline{A}B + \overline{A}C + A\overline{C}B$

Simplificado: $Y = \overline{A}(B + C) + AB\overline{C}$

Función: Selector condicional basado en A

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para verificación de ejercicios combinacionales
NOTA: Algunas implementaciones tienen soluciones alternativas válidas
-->
