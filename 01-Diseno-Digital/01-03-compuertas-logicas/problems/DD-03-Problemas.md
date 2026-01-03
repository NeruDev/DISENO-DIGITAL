<!--
::METADATA::
type: problem
topic_id: dd-03-compuertas-logicas
file_id: problemas-compuertas-logicas
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, compuertas, circuitos, analisis]
search_keywords: "ejercicios, problemas, compuertas lógicas, circuitos"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-03-Metodos-Analisis.md) | [Respuestas →](../solutions/DD-03-Respuestas.md)

---

# Problemas: Compuertas Lógicas

## Nivel 1: Tablas de Verdad de Compuertas

### Problema 1.1
Completar las tablas de verdad para las siguientes compuertas:

**a) AND de 3 entradas:**
| A | B | C | Y = ABC |
|---|---|---|---------|
| 0 | 0 | 0 | ? |
| 0 | 0 | 1 | ? |
| ... | ... | ... | ... |

**b) OR de 3 entradas:**
| A | B | C | Y = A+B+C |
|---|---|---|-----------|
| 0 | 0 | 0 | ? |
| ... | ... | ... | ... |

**c) NAND de 3 entradas**

**d) NOR de 3 entradas**

### Problema 1.2
Determinar la salida Y para las siguientes entradas:
- a) AND: A=1, B=0, C=1
- b) OR: A=0, B=0, C=0
- c) NAND: A=1, B=1
- d) XOR: A=1, B=1
- e) XNOR: A=0, B=1

---

## Nivel 2: Obtener Expresiones desde Circuitos

### Problema 2.1
Obtener la expresión booleana para cada circuito:

**a)**
```
A ────[NOT]────┬────[AND]──── Y
               │
B ─────────────┘
```

**b)**
```
A ────┬────[OR]────┬────[AND]──── Y
      │            │
B ────┘            │
                   │
C ─────────────────┘
```

**c)**
```
A ────[NOT]────┬────[NAND]──── Y
               │
B ────[NOT]────┘
```

**d)**
```
A ────┬────[AND]────┐
B ────┘             │
                    [OR]──── Y
C ────┬────[AND]────┘
D ────┘
```

### Problema 2.2
Para el siguiente circuito, obtener:
- a) La expresión booleana
- b) La tabla de verdad
- c) La expresión simplificada

```
A ────[NOT]───┬────[AND]────┐
              │             │
B ────────────┘             [OR]──── Y
                            │
A ────────────┬────[AND]────┘
              │
B ────[NOT]───┘
```

---

## Nivel 3: Dibujar Circuitos desde Expresiones

### Problema 3.1
Dibujar el circuito con compuertas básicas (AND, OR, NOT):
- a) $Y = A\overline{B} + \overline{A}B$
- b) $Y = (A + B)\overline{C}$
- c) $Y = \overline{A}BC + A\overline{B}C + AB\overline{C}$
- d) $Y = (A + B)(C + D)$

### Problema 3.2
Dibujar el circuito optimizado (mínimo número de compuertas):
- a) $Y = AB + AC + BC$
- b) $Y = \overline{A}B + A\overline{B} + AB$
- c) $Y = \overline{(\overline{A} + \overline{B})}$

---

## Nivel 4: Implementación con NAND

### Problema 4.1
Implementar usando SOLO compuertas NAND:
- a) NOT
- b) AND
- c) OR
- d) XOR (2 entradas)

### Problema 4.2
Convertir los siguientes circuitos a solo NAND:
- a) $Y = AB + CD$
- b) $Y = A + BC$
- c) $Y = (A + B)C$
- d) $Y = \overline{A}B + A\overline{B}$

### Problema 4.3
¿Cuántas compuertas NAND de 2 entradas se necesitan para implementar?
- a) $Y = ABC$
- b) $Y = A + B + C$
- c) $Y = AB + CD + EF$

---

## Nivel 5: Implementación con NOR

### Problema 5.1
Implementar usando SOLO compuertas NOR:
- a) NOT
- b) AND
- c) OR
- d) NAND

### Problema 5.2
Convertir los siguientes circuitos a solo NOR:
- a) $Y = (A + B)(C + D)$
- b) $Y = AB + C$
- c) $Y = A(B + C)$

---

## Nivel 6: Análisis de Tiempos

### Problema 6.1
Para un circuito donde cada compuerta tiene $t_p = 10ns$, calcular el retardo máximo:

**a)**
```
A ────[NOT]────[AND]────[OR]──── Y
```

**b)**
```
A ────[AND]────┐
B ────┘        │
               [AND]──── Y
C ────[OR]─────┘
D ────┘
```

### Problema 6.2
Si un sistema requiere que la salida esté lista en máximo 25ns y cada compuerta tiene $t_p = 8ns$:
- a) ¿Cuál es el número máximo de niveles de compuertas?
- b) Rediseñar $Y = AB + CD + EF$ para cumplir el requisito

---

## Nivel 7: Fan-Out y Carga

### Problema 7.1
Una salida de 74LS00 (NAND) tiene:
- $I_{OL} = 8mA$
- $I_{OH} = -400\mu A$

Las entradas de 74LS00 requieren:
- $I_{IL} = 0.4mA$
- $I_{IH} = 20\mu A$

Calcular el fan-out máximo.

### Problema 7.2
Si una señal debe alimentar 25 entradas de 74LS00, ¿qué solución propones?

---

## Nivel 8: Compatibilidad de Familias

### Problema 8.1
Determinar si se puede conectar directamente:
- a) Salida 74LS00 → Entrada CD4011 (CMOS 5V)
- b) Salida CD4011 → Entrada 74LS00
- c) Salida 74HC00 → Entrada 74LS00

### Problema 8.2
¿Qué componente adicional se necesita para cada caso incompatible del problema anterior?

---

## Nivel 9: Circuitos de Aplicación

### Problema 9.1: Detector de Paridad
Diseñar un circuito que detecte si un número de 4 bits tiene paridad par (número par de 1s).
- a) Usando compuertas XOR
- b) ¿Cuántas compuertas XOR se necesitan?

### Problema 9.2: Control de Motor
Un motor debe encenderse (M=1) cuando:
- El interruptor principal está ON (P=1), Y
- El sensor de temperatura está OK (T=0), Y
- (El botón de marcha está presionado (B=1) O el modo automático está activo (A=1))

- a) Obtener la expresión booleana
- b) Dibujar el circuito
- c) Implementar solo con NAND

### Problema 9.3: Sistema de Votación
Diseñar un circuito para 3 jueces (A, B, C) donde la decisión es favorable si al menos 2 jueces votan a favor.
- a) Tabla de verdad
- b) Expresión simplificada
- c) Circuito con compuertas básicas
- d) Circuito solo con NAND

---

## Nivel 10: Problemas Integradores

### Problema 10.1
Dado el circuito:
```
A ────[NAND]───┬────[NAND]──── Y
B ────┘        │
               │
A ────[NAND]───┘
C ────┘
```

- a) Obtener la expresión booleana
- b) Simplificar algebraicamente
- c) ¿Qué función reconoces?
- d) Construir la tabla de verdad

### Problema 10.2
Diseñar un comparador de 1 bit (A vs B) que produzca tres salidas:
- G = 1 cuando A > B
- E = 1 cuando A = B
- L = 1 cuando A < B

Implementar con el mínimo número de compuertas.

### Problema 10.3
Un sistema de alarma tiene las siguientes condiciones:
- Sensores: Puerta (P), Ventana (V), Movimiento (M)
- Controles: Armado (A), Modo Noche (N)

La alarma (Y) debe activarse cuando:
- Sistema armado Y (puerta O ventana abiertas), O
- Sistema armado Y modo noche Y movimiento detectado

- a) Expresión booleana
- b) Simplificar
- c) Implementar con CI 74LS00 (NAND)
- d) ¿Cuántos CI se necesitan?

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios graduado por dificultad
RESPUESTAS: Ver archivo solutions/DD-03-Respuestas.md
HERRAMIENTAS: LogiSim, Digital, Tinkercad para simulación
-->
