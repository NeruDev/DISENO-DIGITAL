<!--
::METADATA::
type: method
topic_id: dd-03-compuertas-logicas
file_id: metodos-analisis-circuitos
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [analisis, circuito, expresion, diagrama]
search_keywords: "análisis de circuitos, obtener expresión, dibujar circuito"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-03-Teoria-CompuertasLogicas.md) | [Problemas →](../problems/DD-03-Problemas.md)

---

# Métodos de Análisis de Circuitos con Compuertas

## Método 1: Obtener Expresión desde Diagrama

### Algoritmo

**Pasos:**
1. Identificar las entradas (variables)
2. Comenzar desde las entradas hacia la salida
3. Escribir la expresión de cada compuerta intermedia
4. Combinar hasta obtener la expresión final
5. Simplificar si es necesario

### Ejemplo Resuelto

```
A ─────┬─────[AND]───┐
       │             │
B ─────┴─[NOT]──┐    [OR]──── Y
                │    │
C ──────────────┴────┘
```

**Paso 1:** Identificar entradas: A, B, C

**Paso 2:** Analizar por etapas:
- Salida NOT: $\overline{B}$
- Salida AND: $A \cdot B$
- Salida OR: $(A \cdot B) + (\overline{B}) + C$

**Paso 3:** Expresión final:
$$Y = AB + \overline{B} + C$$

**Paso 4:** Simplificar (opcional):
$$Y = AB + \overline{B} + C = A + \overline{B} + C$$

---

## Método 2: Dibujar Circuito desde Expresión

### Algoritmo

**Pasos:**
1. Identificar el operador principal (última operación)
2. Dibujar la compuerta de salida
3. Recursivamente dibujar las compuertas para cada operando
4. Conectar las entradas originales
5. Verificar la expresión resultante

### Reglas de Precedencia

1. Paréntesis (evaluar primero)
2. NOT (complemento)
3. AND (producto)
4. OR (suma)

### Ejemplo Resuelto

Dibujar: $Y = AB + \overline{C}D$

**Paso 1:** Operador principal = OR (hay una suma)

**Paso 2:** 
- Primer término: $AB$ (necesita AND)
- Segundo término: $\overline{C}D$ (necesita NOT y AND)

**Paso 3:** Circuito:
```
A ────┬────[AND]────┐
B ────┘             │
                    [OR]──── Y
C ────[NOT]─┬─[AND]─┘
D ──────────┘
```

---

## Método 3: Análisis por Tabla de Verdad

### Algoritmo

**Pasos:**
1. Listar todas las combinaciones de entrada ($2^n$ filas)
2. Para cada combinación, seguir el circuito
3. Determinar el valor de cada salida intermedia
4. Obtener el valor de la salida final
5. Si se requiere, obtener la expresión en minterms

### Ejemplo Resuelto

Circuito: $Y = (A + B) \cdot \overline{C}$

| A | B | C | A+B | $\overline{C}$ | Y |
|---|---|---|-----|----------------|---|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

**Expresión en minterms:** $Y = \sum m(2, 4, 6)$

---

## Método 4: Conversión a Solo NAND

### Algoritmo

**Pasos:**
1. Expresar la función en forma SOP (suma de productos)
2. Aplicar doble negación: $F = \overline{\overline{F}}$
3. Usar De Morgan para convertir a NANDs

### Fórmulas de Conversión

| Original | Con NAND |
|----------|----------|
| NOT A | A NAND A |
| A AND B | (A NAND B) NAND (A NAND B) |
| A OR B | (A NAND A) NAND (B NAND B) |

### Ejemplo Resuelto

Convertir: $Y = AB + CD$

**Paso 1:** Doble negación
$$Y = \overline{\overline{AB + CD}}$$

**Paso 2:** De Morgan interno
$$Y = \overline{\overline{AB} \cdot \overline{CD}}$$

**Paso 3:** Implementación
```
A ────┬────[NAND]────┐
B ────┘              │
                     [NAND]──── Y
C ────┬────[NAND]────┘
D ────┘
```

> **Regla práctica:** Para SOP de 2 niveles, se necesitan:
> - NANDs para cada término producto (nivel 1)
> - Una NAND para combinar (nivel 2)

---

## Método 5: Conversión a Solo NOR

### Algoritmo

**Pasos:**
1. Expresar la función en forma POS (producto de sumas)
2. Aplicar doble negación
3. Usar De Morgan para convertir a NORs

### Fórmulas de Conversión

| Original | Con NOR |
|----------|---------|
| NOT A | A NOR A |
| A OR B | (A NOR B) NOR (A NOR B) |
| A AND B | (A NOR A) NOR (B NOR B) |

### Ejemplo Resuelto

Convertir: $Y = (A + B)(C + D)$

**Paso 1:** Doble negación
$$Y = \overline{\overline{(A + B)(C + D)}}$$

**Paso 2:** De Morgan interno
$$Y = \overline{\overline{A + B} + \overline{C + D}}$$

**Paso 3:** Implementación
```
A ────┬────[NOR]────┐
B ────┘             │
                    [NOR]──── Y
C ────┬────[NOR]────┘
D ────┘
```

---

## Método 6: Verificación de Equivalencia

### Algoritmo

**Pasos:**
1. Construir tabla de verdad para ambas expresiones
2. Comparar columna por columna
3. Si todas las filas coinciden, son equivalentes

### Método Algebraico

Simplificar ambas expresiones hasta obtener la misma forma.

### Ejemplo

Verificar: $AB + \overline{A}B = B$

| A | B | AB | $\overline{A}$B | AB + $\overline{A}$B | B |
|---|---|----|----|------|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 |

**Resultado:** Son equivalentes ✓

---

## Método 7: Análisis de Tiempos

### Cálculo de Retardo Total

**Pasos:**
1. Identificar la ruta crítica (camino más largo)
2. Sumar los retardos de cada compuerta en la ruta
3. Considerar $t_{pLH}$ y $t_{pHL}$ por separado

### Ejemplo

```
     [NOT]─────[AND]────┐
A ────┘                 │
                        [OR]──── Y
B ─────────────[AND]────┘
C ─────────────┘
```

**Ruta crítica:** A → NOT → AND → OR

**Retardo total:** $t_p = t_{NOT} + t_{AND} + t_{OR}$

Si cada compuerta tiene $t_p = 10ns$:
$$t_{total} = 10 + 10 + 10 = 30ns$$

---

## Método 8: Cálculo de Fan-Out

### Algoritmo

**Pasos:**
1. Para cada salida, contar cuántas entradas alimenta
2. Verificar que no exceda el fan-out máximo del CI
3. Si excede, agregar buffers

### Ejemplo

Si 74LS00 tiene fan-out = 10 y una salida alimenta 12 entradas:
- **Problema:** Excede fan-out
- **Solución:** Usar buffer o dividir la carga

---

## Resumen de Conversiones

| De | A | Método |
|----|---|--------|
| Diagrama | Expresión | Seguir de entrada a salida |
| Expresión | Diagrama | Identificar operador principal |
| Expresión | Tabla | Evaluar todas combinaciones |
| Tabla | Expresión | Minterms donde F=1 |
| SOP | Solo NAND | Doble negación + De Morgan |
| POS | Solo NOR | Doble negación + De Morgan |

---

<!-- IA_CONTEXT
USO: Referencia para análisis y diseño de circuitos con compuertas
NIVEL: Básico a Intermedio (1-2/3)
HERRAMIENTAS: LogiSim, Digital, Proteus para simulación
-->
