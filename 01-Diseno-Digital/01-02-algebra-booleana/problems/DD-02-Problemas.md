<!--
::METADATA::
type: problem
topic_id: dd-02-algebra-booleana
file_id: problemas-algebra-booleana
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, simplificacion, karnaugh, teoremas]
search_keywords: "ejercicios, problemas, álgebra booleana, Karnaugh"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-02-Metodos-Simplificacion.md) | [Respuestas →](../solutions/DD-02-Respuestas.md)

---

# Problemas: Álgebra Booleana

## Nivel 1: Tablas de Verdad

### Problema 1.1
Construir la tabla de verdad para las siguientes expresiones:
- a) $F = AB + \overline{A}C$
- b) $F = (A + B)(A + C)$
- c) $F = A \oplus B$
- d) $F = \overline{A + B}$

### Problema 1.2
Dada la siguiente tabla de verdad, obtener:
- a) La expresión en suma de productos (SOP)
- b) La expresión en producto de sumas (POS)
- c) La notación de minterms y maxterms

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

---

## Nivel 2: Aplicación de Teoremas

### Problema 2.1
Demostrar algebraicamente los siguientes teoremas:
- a) $A + AB = A$
- b) $A + \overline{A}B = A + B$
- c) $(A + B)(A + C) = A + BC$
- d) $AB + \overline{A}C + BC = AB + \overline{A}C$ (Consenso)

### Problema 2.2
Simplificar usando teoremas algebraicos:
- a) $F = A\overline{B} + AB$
- b) $F = \overline{A}B + A\overline{B} + AB$
- c) $F = ABC + AB\overline{C} + A\overline{B}C + A\overline{B}\overline{C}$
- d) $F = (A + B)(\overline{A} + B)(A + \overline{B})$

### Problema 2.3
Aplicar las leyes de De Morgan para obtener el complemento de:
- a) $F = AB + CD$
- b) $F = (A + B)(C + D)$
- c) $F = A\overline{B} + \overline{A}B$
- d) $F = \overline{A}BC + A\overline{B}C + AB\overline{C}$

---

## Nivel 3: Mapas de Karnaugh (2-3 Variables)

### Problema 3.1
Simplificar usando mapas de Karnaugh (2 variables):
- a) $F(A,B) = \sum m(0, 1, 2)$
- b) $F(A,B) = \sum m(1, 3)$
- c) $F(A,B) = \sum m(0, 3)$

### Problema 3.2
Simplificar usando mapas de Karnaugh (3 variables):
- a) $F(A,B,C) = \sum m(0, 2, 4, 6)$
- b) $F(A,B,C) = \sum m(1, 3, 5, 7)$
- c) $F(A,B,C) = \sum m(0, 1, 2, 3, 7)$
- d) $F(A,B,C) = \sum m(2, 3, 4, 5)$

### Problema 3.3
Simplificar y obtener SOP y POS:
- a) $F(A,B,C) = \sum m(0, 1, 6, 7)$
- b) $F(A,B,C) = \sum m(1, 2, 5, 6)$

---

## Nivel 4: Mapas de Karnaugh (4 Variables)

### Problema 4.1
Simplificar usando mapas de Karnaugh (4 variables):
- a) $F(A,B,C,D) = \sum m(0, 1, 2, 3, 4, 5, 6, 7)$
- b) $F(A,B,C,D) = \sum m(0, 2, 8, 10)$
- c) $F(A,B,C,D) = \sum m(1, 3, 5, 7, 9, 11, 13, 15)$
- d) $F(A,B,C,D) = \sum m(0, 4, 8, 12, 1, 5, 9, 13)$

### Problema 4.2
Simplificar las siguientes funciones:
- a) $F(A,B,C,D) = \sum m(0, 1, 4, 5, 6, 7, 8, 9, 14, 15)$
- b) $F(A,B,C,D) = \sum m(2, 3, 6, 7, 10, 11, 12, 13)$
- c) $F(A,B,C,D) = \sum m(0, 2, 3, 5, 7, 8, 10, 11, 13, 15)$

---

## Nivel 5: Condiciones Don't Care

### Problema 5.1
Simplificar con don't cares:
- a) $F(A,B,C) = \sum m(1, 2, 5) + d(0, 3)$
- b) $F(A,B,C) = \sum m(0, 4, 6) + d(2, 7)$

### Problema 5.2
Un display BCD de 7 segmentos necesita encender el segmento "a" (superior) para los dígitos 0, 2, 3, 5, 6, 7, 8, 9. Diseñar la función con don't cares para combinaciones 10-15.

### Problema 5.3
$F(A,B,C,D) = \sum m(1, 3, 5, 7, 9) + d(6, 12, 13)$

Simplificar y comparar el resultado con y sin usar don't cares.

---

## Nivel 6: Implementación con Compuertas

### Problema 6.1
Para las siguientes funciones simplificadas, determinar:
- Número de compuertas necesarias
- Tipo de compuertas
- Número total de entradas

- a) $F = AB + \overline{A}C$
- b) $F = (A + B)(B + C)$
- c) $F = A \oplus B \oplus C$

### Problema 6.2
Convertir las siguientes expresiones para implementar usando solo compuertas NAND:
- a) $F = AB + CD$
- b) $F = A + BC$
- c) $F = (A + B)C$

### Problema 6.3
Convertir las siguientes expresiones para implementar usando solo compuertas NOR:
- a) $F = (A + B)(C + D)$
- b) $F = AB + C$

---

## Nivel 7: Problemas de Aplicación

### Problema 7.1: Sistema de Alarma
Un sistema de alarma debe activarse (F=1) cuando:
- La puerta está abierta (P=1) Y el sistema está armado (A=1), O
- Se detecta movimiento (M=1) Y está oscuro (O=1) Y el sistema está armado (A=1)

a) Escribir la expresión booleana
b) Simplificar
c) Dibujar el circuito

### Problema 7.2: Votación Mayoría
Diseñar un circuito que produzca salida 1 cuando la mayoría de 4 interruptores (A, B, C, D) están en posición 1.

a) Construir la tabla de verdad
b) Obtener la función en minterms
c) Simplificar usando mapa de Karnaugh

### Problema 7.3: Comparador
Diseñar un circuito que compare dos números de 2 bits (A₁A₀ y B₁B₀) y produzca:
- G = 1 cuando A > B
- E = 1 cuando A = B
- L = 1 cuando A < B

### Problema 7.4: Detector de Paridad
Diseñar un circuito que detecte si un número de 4 bits tiene un número par de unos (paridad par).

---

## Problemas Integradores

### Problema 8.1
Dada la función $F(A,B,C,D) = \sum m(0, 1, 2, 5, 8, 9, 10)$:
- a) Simplificar usando mapa K
- b) Obtener la expresión POS mínima
- c) Implementar usando solo NAND
- d) Implementar usando solo NOR

### Problema 8.2
Para un multiplexor 4:1 con entradas de selección S₁S₀ y entradas de datos I₀, I₁, I₂, I₃:
- a) Escribir la tabla de verdad
- b) Obtener la expresión booleana
- c) Simplificar (si es posible)

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios graduado por dificultad
RESPUESTAS: Ver archivo solutions/DD-02-Respuestas.md
HERRAMIENTAS: Usar LogiSim o Digital para verificar circuitos
-->
