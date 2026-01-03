<!--
::METADATA::
type: problem
topic_id: dd-04-circuitos-combinacionales
file_id: problemas-circuitos-combinacionales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, combinacionales, multiplexor, sumador, decodificador]
search_keywords: "ejercicios, problemas, circuitos combinacionales"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-04-Metodos-Diseno.md) | [Respuestas →](../solutions/DD-04-Respuestas.md)

---

# Problemas: Circuitos Combinacionales

## Nivel 1: Multiplexores

### Problema 1.1
Para un MUX 4:1 con selectores $S_1S_0$ y entradas $I_0, I_1, I_2, I_3$:
- a) Escribir la expresión booleana de la salida Y
- b) Si $I_0=1$, $I_1=0$, $I_2=1$, $I_3=0$, ¿cuál es Y cuando $S_1S_0=10$?
- c) Dibujar el circuito interno usando compuertas básicas

### Problema 1.2
Implementar las siguientes funciones usando MUX 4:1 con A,B como selectores:
- a) $F(A,B,C) = \sum m(1, 2, 5, 7)$
- b) $F(A,B,C) = \sum m(0, 3, 4, 6)$
- c) $F(A,B,C) = A \oplus B \oplus C$

### Problema 1.3
Implementar $F(A,B,C,D) = \sum m(0, 1, 3, 5, 7, 8, 9, 15)$ usando:
- a) Un MUX 8:1
- b) Dos MUX 4:1 y un MUX 2:1

---

## Nivel 2: Decodificadores y Codificadores

### Problema 2.1
Para un decodificador 3:8:
- a) Escribir las expresiones para todas las salidas
- b) ¿Qué salida está activa cuando la entrada es 101?
- c) Si tiene enable activo bajo, ¿qué pasa cuando $\overline{EN}=1$?

### Problema 2.2
Implementar las siguientes funciones usando decodificador 3:8 y compuertas OR:
- a) $F(A,B,C) = \sum m(0, 2, 6, 7)$
- b) $F(A,B,C) = \prod M(1, 3, 5)$
- c) $F_1 = \sum m(1, 4, 7)$ y $F_2 = \sum m(2, 4, 5)$ simultáneamente

### Problema 2.3
Diseñar un codificador de prioridad 4:2:
- a) Tabla de verdad (mayor prioridad = entrada más significativa)
- b) Expresiones para las salidas
- c) Agregar salida de "entrada válida"

---

## Nivel 3: Sumadores

### Problema 3.1
Diseñar un Half Adder:
- a) Tabla de verdad
- b) Expresiones para S y C
- c) Circuito con compuertas básicas
- d) Circuito usando solo NAND

### Problema 3.2
Diseñar un Full Adder:
- a) Tabla de verdad completa
- b) Mapas de Karnaugh para S y $C_{out}$
- c) Expresiones simplificadas
- d) Implementar usando 2 Half Adders y 1 OR

### Problema 3.3
Para un sumador de 4 bits (ripple carry):
- a) Calcular $1010 + 0111$ mostrando todos los acarreos
- b) ¿Cuál es el retardo máximo si cada FA tiene $t_p = 20ns$?
- c) Detectar overflow para números con signo

### Problema 3.4
Diseñar un sumador/restador de 4 bits:
- a) Diagrama de bloques
- b) Función de la señal de control M
- c) ¿Cómo se detecta overflow?

---

## Nivel 4: Comparadores

### Problema 4.1
Diseñar un comparador de 1 bit:
- a) Tabla de verdad para G, E, L
- b) Expresiones booleanas
- c) Circuito con compuertas

### Problema 4.2
Para el 74LS85 (comparador 4 bits):
- a) Explicar el uso de las entradas de cascada
- b) Diseñar un comparador de 8 bits usando dos 74LS85
- c) ¿Cuál es el retardo total?

### Problema 4.3
Diseñar un circuito que compare dos números de 2 bits (A₁A₀ vs B₁B₀) sin usar CI comparadores:
- a) Obtener las expresiones para A>B, A=B, A<B
- b) Simplificar usando mapas K
- c) Implementar el circuito

---

## Nivel 5: Convertidores de Código

### Problema 5.1
Diseñar un convertidor BCD a Excess-3:
- a) Tabla de verdad
- b) Mapas de Karnaugh para cada salida
- c) Expresiones simplificadas

### Problema 5.2
Diseñar un convertidor de código Gray de 4 bits a Binario:
- a) Expresiones de conversión
- b) Circuito con XOR
- c) Retardo de propagación

### Problema 5.3
Diseñar un convertidor BCD a 7 segmentos (para dígitos 0-9):
- a) Tabla de verdad para cada segmento
- b) Mapas K con don't cares (10-15)
- c) Expresiones simplificadas para segmentos a, b, c

---

## Nivel 6: Generadores de Paridad

### Problema 6.1
Diseñar un generador de paridad par para 4 bits:
- a) Tabla de verdad
- b) Expresión usando XOR
- c) Circuito

### Problema 6.2
Diseñar un verificador de paridad para 5 bits (4 datos + 1 paridad):
- a) ¿Cuándo indica error?
- b) Implementación
- c) ¿Puede corregir errores?

---

## Nivel 7: ALU

### Problema 7.1
Diseñar una ALU de 1 bit que realice:
- AND (sel=00)
- OR (sel=01)
- Suma (sel=10)
- Resta (sel=11)

Incluir entrada de acarreo y salida de acarreo.

### Problema 7.2
Expandir la ALU del problema anterior a 4 bits:
- a) Diagrama de bloques
- b) ¿Cómo se conectan los acarreos?
- c) Agregar detección de overflow y zero

---

## Nivel 8: Aplicaciones

### Problema 8.1: Controlador de Semáforo Simplificado
Diseñar un circuito que controle las luces de un semáforo con 4 estados:
- Estado 0: Verde N-S, Rojo E-W
- Estado 1: Amarillo N-S, Rojo E-W
- Estado 2: Rojo N-S, Verde E-W
- Estado 3: Rojo N-S, Amarillo E-W

Entradas: 2 bits de estado (S₁S₀)
Salidas: VNS, ANS, RNS, VEW, AEW, REW

### Problema 8.2: Display de Dado Electrónico
Diseñar un circuito que muestre un dado en 7 LEDs:
```
● ● ●
● ● ●
● ● ●
```
Entradas: 3 bits (valores 1-6)
Determinar qué LEDs encender para cada valor.

### Problema 8.3: Detector de Rango
Diseñar un circuito que detecte si un número de 4 bits está en el rango 5-10 (inclusive).
- a) Tabla de verdad
- b) Expresión simplificada
- c) Implementación con comparadores

---

## Nivel 9: Problemas Integradores

### Problema 9.1
Diseñar un multiplicador de 2 bits × 2 bits:
- a) Tabla de verdad (entradas: A₁A₀, B₁B₀; salidas: P₃P₂P₁P₀)
- b) Mapas K para cada salida
- c) Circuito usando AND y sumadores

### Problema 9.2
Diseñar un circuito que convierta un número binario de 4 bits a dos dígitos BCD:
- Entrada: 0000 a 1111 (0 a 15)
- Salidas: Decenas (0 o 1), Unidades (0-9)

### Problema 9.3
Diseñar un circuito de votación con 5 entradas que active la salida cuando:
- Al menos 3 votos a favor, Y
- El presidente (entrada P) vote a favor O haya unanimidad

---

## Nivel 10: Análisis de Circuitos

### Problema 10.1
Analizar el siguiente circuito y determinar su función:
```
A ────┬────[AND]────┐
      │             │
B ────┼─[NOT]─[AND]─┼────[OR]── F
      │       │     │
      └───────┘     │
C ────────────[AND]─┘
D ────────────┘
```

### Problema 10.2
Dado el siguiente circuito con MUX 4:1:
- $S_1 = A$, $S_0 = B$
- $I_0 = C$, $I_1 = 1$, $I_2 = 0$, $I_3 = \overline{C}$

Determinar:
- a) Tabla de verdad
- b) Expresión booleana simplificada
- c) ¿Qué función implementa?

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios para circuitos combinacionales
RESPUESTAS: Ver archivo solutions/DD-04-Respuestas.md
HERRAMIENTAS: LogiSim, Digital, Quartus Prime
-->
