<!--
::METADATA::
type: method
topic_id: dd-02-algebra-booleana
file_id: metodos-simplificacion
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [simplificacion, karnaugh, algebra, metodo]
search_keywords: "simplificación, Karnaugh, método algebraico, minimización"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-02-Teoria-AlgebraBooleana.md) | [Problemas →](../problems/DD-02-Problemas.md)

---

# Métodos de Simplificación Booleana

## Método 1: Simplificación Algebraica

### Algoritmo General

**Pasos:**
1. Escribir la expresión original
2. Aplicar teoremas booleanos para reducir términos
3. Buscar factores comunes
4. Aplicar De Morgan cuando sea conveniente
5. Verificar que no se pueda simplificar más

### Teoremas Más Útiles para Simplificación

| Teorema | Aplicación |
|---------|------------|
| $A + AB = A$ | Absorción |
| $A + \overline{A}B = A + B$ | Absorción extendida |
| $A \cdot \overline{A} = 0$ | Eliminar términos |
| $A + A = A$ | Idempotencia |
| $AB + A\overline{B} = A$ | Combinación |

### Ejemplo Resuelto 1

Simplificar: $F = ABC + AB\overline{C} + A\overline{B}C$

```
Paso 1: Agrupar términos con factores comunes
F = AB(C + C̄) + AB̄C

Paso 2: Aplicar A + Ā = 1
F = AB(1) + AB̄C
F = AB + AB̄C

Paso 3: Factorizar A
F = A(B + B̄C)

Paso 4: Aplicar A + ĀB = A + B
F = A(B + C)
```

**Resultado:** $F = A(B + C) = AB + AC$

### Ejemplo Resuelto 2

Simplificar: $F = \overline{A}B + A\overline{B} + AB$

```
Paso 1: Identificar patrón
Notar que ĀB + AB = B(Ā + A) = B

Paso 2: Reorganizar
F = (ĀB + AB) + AB̄
F = B + AB̄

Paso 3: Aplicar absorción extendida (A + ĀB = A + B)
F = B + A (usando B + AB̄ = B + A)
```

**Resultado:** $F = A + B$

---

## Método 2: Mapas de Karnaugh (2 Variables)

### Estructura del Mapa

```
        B=0   B=1
      ┌─────┬─────┐
A=0   │ m₀  │ m₁  │
      ├─────┼─────┤
A=1   │ m₂  │ m₃  │
      └─────┴─────┘
```

### Algoritmo

**Pasos:**
1. Dibujar el mapa K de 2×2
2. Colocar 1s en las celdas correspondientes a los minterms
3. Agrupar 1s adyacentes en potencias de 2 (1, 2, 4)
4. Cada grupo genera un término producto
5. Los grupos deben ser lo más grandes posible

### Ejemplo: $F = \sum m(0, 2, 3)$

```
        B=0   B=1
      ┌─────┬─────┐
A=0   │  1  │  0  │  ← grupo vertical: B̄
      ├─────┼─────┤
A=1   │  1  │  1  │  ← grupo horizontal: A
      └─────┴─────┘
```

**Resultado:** $F = A + \overline{B}$

---

## Método 3: Mapas de Karnaugh (3 Variables)

### Estructura del Mapa

```
          BC
        00   01   11   10
      ┌─────┬─────┬─────┬─────┐
A=0   │ m₀  │ m₁  │ m₃  │ m₂  │
      ├─────┼─────┼─────┼─────┤
A=1   │ m₄  │ m₅  │ m₇  │ m₆  │
      └─────┴─────┴─────┴─────┘
```

> ⚠️ **Nota:** El orden de columnas es 00, 01, 11, 10 (código Gray)

### Reglas de Agrupación

1. Grupos de 1, 2, 4, 8 celdas (potencias de 2)
2. Solo celdas adyacentes (horizontal, vertical)
3. **Los bordes son adyacentes** (wrap-around)
4. Cada 1 debe pertenecer a al menos un grupo
5. Grupos más grandes = expresión más simple
6. Se permite solapamiento de grupos

### Ejemplo: $F(A,B,C) = \sum m(0, 2, 4, 5, 6)$

```
          BC
        00   01   11   10
      ┌─────┬─────┬─────┬─────┐
A=0   │  1  │  0  │  0  │  1  │
      ├─────┼─────┼─────┼─────┤
A=1   │  1  │  1  │  0  │  1  │
      └─────┴─────┴─────┴─────┘

Grupos:
- Columna 00: m₀, m₄ → B̄C̄
- Columna 10: m₂, m₆ → BC̄
- m₄, m₅: AB̄
```

**Resultado:** $F = \overline{B}\overline{C} + B\overline{C} + A\overline{B} = \overline{C} + A\overline{B}$

---

## Método 4: Mapas de Karnaugh (4 Variables)

### Estructura del Mapa

```
            CD
          00   01   11   10
        ┌─────┬─────┬─────┬─────┐
AB=00   │ m₀  │ m₁  │ m₃  │ m₂  │
        ├─────┼─────┼─────┼─────┤
AB=01   │ m₄  │ m₅  │ m₇  │ m₆  │
        ├─────┼─────┼─────┼─────┤
AB=11   │ m₁₂ │ m₁₃ │ m₁₅ │ m₁₄ │
        ├─────┼─────┼─────┼─────┤
AB=10   │ m₈  │ m₉  │ m₁₁ │ m₁₀ │
        └─────┴─────┴─────┴─────┘
```

### Adyacencias Especiales

- Fila superior ↔ Fila inferior (wrap vertical)
- Columna izquierda ↔ Columna derecha (wrap horizontal)
- Esquinas opuestas pueden formar grupo de 4

### Ejemplo: $F(A,B,C,D) = \sum m(0, 2, 5, 7, 8, 10, 13, 15)$

```
            CD
          00   01   11   10
        ┌─────┬─────┬─────┬─────┐
AB=00   │  1  │  0  │  0  │  1  │
        ├─────┼─────┼─────┼─────┤
AB=01   │  0  │  1  │  1  │  0  │
        ├─────┼─────┼─────┼─────┤
AB=11   │  0  │  1  │  1  │  0  │
        ├─────┼─────┼─────┼─────┤
AB=10   │  1  │  0  │  0  │  1  │
        └─────┴─────┴─────┴─────┘

Grupos:
- 4 esquinas (m₀, m₂, m₈, m₁₀): B̄D̄
- Centro (m₅, m₇, m₁₃, m₁₅): BD
```

**Resultado:** $F = \overline{B}\overline{D} + BD$

---

## Método 5: Condiciones "Don't Care"

### ¿Qué son?

Son combinaciones de entrada que:
- Nunca ocurren en la práctica, o
- Su salida no importa

Se marcan con **X** o **d** en el mapa K.

### Regla

Usar los "don't care" como 1 o 0 según convenga para hacer grupos más grandes.

### Ejemplo: BCD a 7 segmentos (detectar números > 4)

Los valores 10-15 no son BCD válidos → don't care

```
            CD
          00   01   11   10
        ┌─────┬─────┬─────┬─────┐
AB=00   │  0  │  0  │  0  │  0  │
        ├─────┼─────┼─────┼─────┤
AB=01   │  0  │  1  │  1  │  1  │
        ├─────┼─────┼─────┼─────┤
AB=11   │  X  │  X  │  X  │  X  │
        ├─────┼─────┼─────┼─────┤
AB=10   │  1  │  1  │  X  │  X  │
        └─────┴─────┴─────┴─────┘

Usando don't cares:
- Grupo vertical columnas 01,11: D
- Grupo inferior: A
```

**Resultado:** $F = A + D$ (en lugar de expresión más compleja)

---

## Método 6: Obtener POS desde Mapa K

### Algoritmo

1. Agrupar los **0s** en lugar de los 1s
2. Escribir la expresión complementada
3. Aplicar De Morgan para obtener POS

### Ejemplo

Si el mapa da $\overline{F} = \overline{A}C + B\overline{C}$

Entonces:
$$F = \overline{\overline{A}C + B\overline{C}} = (A + \overline{C})(\overline{B} + C)$$

---

## Tabla Resumen: Tamaño de Grupos

| Tamaño Grupo | Variables Eliminadas | Término Resultante |
|--------------|---------------------|-------------------|
| 1 | 0 | Minterm completo |
| 2 | 1 | n-1 variables |
| 4 | 2 | n-2 variables |
| 8 | 3 | n-3 variables |
| 16 | 4 | Constante 1 |

---

## Verificación de Resultados

### Método de Verificación

1. Expandir la expresión simplificada a minterms
2. Comparar con la lista original de minterms
3. Usar tabla de verdad para casos pequeños

### Ejemplo

Original: $F = \sum m(1, 3, 5, 7)$
Simplificada: $F = C$

Verificación: $C = 1$ cuando minterm es impar → ✓

---

<!-- IA_CONTEXT
USO: Referencia para simplificación de funciones booleanas
NIVEL: Básico a Intermedio (1-2/3)
HERRAMIENTAS: Se puede usar software como LogiSim o Digital para verificar
-->
