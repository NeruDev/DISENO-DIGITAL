<!--
::METADATA::
type: solution
topic_id: dd-03-compuertas-logicas
file_id: respuestas-compuertas-logicas
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, compuertas lógicas"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-03-Problemas.md)

---

# Respuestas: Compuertas Lógicas

## Nivel 1: Tablas de Verdad

### Respuestas 1.1

**a) AND de 3 entradas:** Y=1 solo cuando A=B=C=1

**b) OR de 3 entradas:** Y=0 solo cuando A=B=C=0

**c) NAND de 3 entradas:** Y=0 solo cuando A=B=C=1

**d) NOR de 3 entradas:** Y=1 solo cuando A=B=C=0

### Respuestas 1.2

| | Compuerta | Entradas | Salida |
|--|-----------|----------|--------|
| a) | AND | A=1, B=0, C=1 | **0** |
| b) | OR | A=0, B=0, C=0 | **0** |
| c) | NAND | A=1, B=1 | **0** |
| d) | XOR | A=1, B=1 | **0** |
| e) | XNOR | A=0, B=1 | **0** |

---

## Nivel 2: Expresiones desde Circuitos

### Respuestas 2.1

| | Expresión |
|--|-----------|
| a) | $Y = \overline{A} \cdot B$ |
| b) | $Y = (A + B) \cdot C$ |
| c) | $Y = \overline{\overline{A} \cdot \overline{B}} = A + B$ (De Morgan) |
| d) | $Y = AB + CD$ |

### Respuestas 2.2

**a) Expresión:** $Y = \overline{A}B + A\overline{B}$

**b) Tabla de verdad:**
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**c) Simplificada:** $Y = A \oplus B$ (XOR)

---

## Nivel 3: Circuitos desde Expresiones

### Respuestas 3.1

**a) $Y = A\overline{B} + \overline{A}B$:** 2 NOT, 2 AND, 1 OR (o 1 XOR)

**b) $Y = (A + B)\overline{C}$:** 1 OR, 1 NOT, 1 AND

**c) $Y = \overline{A}BC + A\overline{B}C + AB\overline{C}$:** 3 NOT, 3 AND de 3 entradas, 1 OR de 3 entradas

**d) $Y = (A + B)(C + D)$:** 2 OR, 1 AND

### Respuestas 3.2

**a)** $Y = AB + AC + BC$ → Factorizar: No se simplifica más, pero se puede implementar con:
- 3 AND + 1 OR de 3 entradas

**b)** $Y = \overline{A}B + A\overline{B} + AB = A + B$
- 1 OR de 2 entradas

**c)** $Y = \overline{(\overline{A} + \overline{B})} = AB$ (De Morgan)
- 1 AND de 2 entradas

---

## Nivel 4: Implementación con NAND

### Respuestas 4.1

| Función | Implementación NAND |
|---------|---------------------|
| a) NOT | A NAND A |
| b) AND | (A NAND B) NAND (A NAND B) |
| c) OR | (A NAND A) NAND (B NAND B) |
| d) XOR | Ver diagrama completo* |

*XOR con NAND requiere 4 compuertas NAND

### Respuestas 4.2

**a) $Y = AB + CD$:** 3 NAND (2 para productos, 1 para suma)

**b) $Y = A + BC$:** 
$$Y = \overline{\overline{A} \cdot \overline{BC}}$$
4 NAND

**c) $Y = (A + B)C$:**
$$Y = \overline{\overline{(A+B)C}} = \overline{\overline{A}\overline{B} + \overline{C}}$$
4 NAND

**d) $Y = \overline{A}B + A\overline{B}$:** 4 NAND (estructura XOR)

### Respuestas 4.3

| | Expresión | NANDs necesarios |
|--|-----------|------------------|
| a) | $ABC$ | 3 (cascade AND) → 4 con solo 2-input |
| b) | $A + B + C$ | 4 (inversores + NAND) |
| c) | $AB + CD + EF$ | 4 (3 productos + 1 suma) |

---

## Nivel 5: Implementación con NOR

### Respuestas 5.1

| Función | Implementación NOR |
|---------|-------------------|
| a) NOT | A NOR A |
| b) AND | (A NOR A) NOR (B NOR B) |
| c) OR | (A NOR B) NOR (A NOR B) |
| d) NAND | Ver implementación completa* |

### Respuestas 5.2

**a) $Y = (A + B)(C + D)$:** 3 NOR (estructura directa para POS)

**b) $Y = AB + C$:** 5 NOR

**c) $Y = A(B + C)$:** 4 NOR

---

## Nivel 6: Análisis de Tiempos

### Respuestas 6.1

**a)** Ruta: NOT → AND → OR
$$t_{total} = 3 \times 10ns = 30ns$$

**b)** Ruta crítica: C/D → OR → AND → AND
$$t_{total} = 3 \times 10ns = 30ns$$

### Respuestas 6.2

**a)** Máximo niveles: $\lfloor 25/8 \rfloor = 3$ niveles

**b)** $Y = AB + CD + EF$ tiene 2 niveles (AND-OR), cumple con $2 \times 8 = 16ns < 25ns$ ✓

---

## Nivel 7: Fan-Out

### Respuestas 7.1

$$\text{Fan-out}_L = \frac{8mA}{0.4mA} = 20$$
$$\text{Fan-out}_H = \frac{400\mu A}{20\mu A} = 20$$

**Fan-out = 20**

### Respuestas 7.2

Con fan-out = 20 y necesidad de 25 entradas:

**Solución:** Usar un buffer (74LS244) o dividir la carga entre 2 salidas.

---

## Nivel 8: Compatibilidad

### Respuestas 8.1

| | Conexión | ¿Compatible? |
|--|----------|--------------|
| a) | 74LS00 → CD4011 | **No** (TTL $V_{OH}$ < CMOS $V_{IH}$) |
| b) | CD4011 → 74LS00 | **Sí** (niveles CMOS cubren TTL) |
| c) | 74HC00 → 74LS00 | **Sí** (HC compatible con TTL) |

### Respuestas 8.2

**Para (a):** Resistencia pull-up de 4.7kΩ a VCC

---

## Nivel 9: Aplicaciones

### Respuestas 9.1 (Detector Paridad)

**a)** $P = A \oplus B \oplus C \oplus D$

**b)** 3 compuertas XOR (en cascada o árbol)

### Respuestas 9.2 (Control Motor)

**a)** $M = P \cdot \overline{T} \cdot (B + A)$

**b)** Circuito: 1 NOT, 1 OR, 2 AND

**c)** Solo NAND: 5 compuertas NAND

### Respuestas 9.3 (Votación)

**a)** Tabla: Y=1 para (0,1,1), (1,0,1), (1,1,0), (1,1,1)

**b)** $Y = AB + AC + BC$

**c)** 3 AND + 1 OR de 3 entradas

**d)** Solo NAND: 4 NAND de 2 entradas

---

## Nivel 10: Problemas Integradores

### Respuestas 10.1

**a)** $Y = \overline{\overline{AB} \cdot \overline{AC}}$

**b)** Por De Morgan: $Y = AB + AC = A(B + C)$

**c)** Función: AND-OR / Selector

**d)** Tabla: Y=1 cuando A=1 Y (B=1 O C=1)

### Respuestas 10.2 (Comparador 1 bit)

$$G = A\overline{B}$$
$$E = \overline{A \oplus B} = AB + \overline{A}\overline{B}$$
$$L = \overline{A}B$$

**Mínimo:** 2 NOT, 2 AND para G y L, 1 XNOR para E

### Respuestas 10.3 (Sistema Alarma)

**a)** $Y = A(P + V) + ANM$

**b)** $Y = A(P + V + NM)$

**c)** Usando 74LS00:
- 2 NAND como inversores (para P+V)
- 1 NAND para P+V
- 1 NAND para NM
- 1 NAND para OR final
- 1 NAND para AND con A

**d)** 1 CI 74LS00 (4 NAND) + parcial de otro = **2 CI**

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas rápidas para verificación
NOTA: Pueden existir implementaciones alternativas igualmente válidas
-->
