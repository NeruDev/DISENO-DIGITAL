<!--
::METADATA::
type: detailed_solution
topic_id: dd-03-compuertas-logicas
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 1
tags: [solucion, compuertas, tabla-verdad, circuito]
-->

> 🏠 **Navegación:** [← Respuestas](../DD-03-Respuestas.md) | [Problema 1.2 →](./DD-03-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Completar la tabla de verdad y dibujar el circuito para la función:
$$F = (A \cdot B) + C$$

---

## Paso 1: Identificar Variables y Operaciones

| Elemento | Descripción |
|----------|-------------|
| Variables | A, B, C (3 entradas → $2^3 = 8$ filas) |
| Operaciones | AND ($A \cdot B$), luego OR ($+ C$) |

---

## Paso 2: Tabla de Verdad Completa

| A | B | C | A·B | F = (A·B)+C |
|---|---|---|:---:|:-----------:|
| 0 | 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | 0 | **1** |
| 0 | 1 | 0 | 0 | **0** |
| 0 | 1 | 1 | 0 | **1** |
| 1 | 0 | 0 | 0 | **0** |
| 1 | 0 | 1 | 0 | **1** |
| 1 | 1 | 0 | 1 | **1** |
| 1 | 1 | 1 | 1 | **1** |

---

## Paso 3: Análisis del Comportamiento

La salida F es **1** cuando:
- $C = 1$ (independiente de A y B), **Ó**
- $A = 1$ Y $B = 1$ (independiente de C)

### Mintérminos (donde F = 1)
$$F = \Sigma m(1, 3, 5, 6, 7)$$
$$F = \bar{A}\bar{B}C + \bar{A}BC + A\bar{B}C + AB\bar{C} + ABC$$

### Simplificación
$$F = C(\bar{A}\bar{B} + \bar{A}B + A\bar{B} + AB) + AB\bar{C}$$
$$F = C + AB \quad \text{(verificado)}$$

---

## Paso 4: Circuito Lógico

```
          ┌─────┐
    A ────┤     │
          │ AND ├───┐
    B ────┤     │   │   ┌─────┐
          └─────┘   └───┤     │
                        │ OR  ├──── F
    C ──────────────────┤     │
                        └─────┘
```

### Descripción del circuito:
1. **Compuerta AND** de 2 entradas: recibe A y B
2. **Compuerta OR** de 2 entradas: recibe la salida del AND y C

---

## Paso 5: Análisis de Compuertas Necesarias

| Compuerta | Cantidad | Entradas |
|-----------|:--------:|:--------:|
| AND | 1 | 2 |
| OR | 1 | 2 |
| **Total** | **2** | - |

---

## Verificación con Valores

### Caso 1: A=1, B=1, C=0
$$F = (1 \cdot 1) + 0 = 1 + 0 = 1 \checkmark$$

### Caso 2: A=1, B=0, C=1
$$F = (1 \cdot 0) + 1 = 0 + 1 = 1 \checkmark$$

### Caso 3: A=0, B=0, C=0
$$F = (0 \cdot 0) + 0 = 0 + 0 = 0 \checkmark$$

---

## Implementación con Solo NAND

Usando De Morgan: $F = (AB) + C = \overline{\overline{AB} \cdot \bar{C}}$

```
          ┌──────┐
    A ────┤      │
          │ NAND ├───┐
    B ────┤      │   │   ┌──────┐
          └──────┘   ├───┤      │
                     │   │ NAND ├──── F
    C ──┬────────────│───┤      │
        │            │   └──────┘
        │  ┌──────┐  │
        └──┤ NAND ├──┘
           │(INV) │
           └──────┘
```

Requiere: 3 compuertas NAND

---

## Conceptos Clave Aplicados

1. **Precedencia:** AND se evalúa antes que OR
2. **Tabla de verdad:** Método sistemático de $2^n$ combinaciones
3. **Universalidad NAND:** Cualquier función puede implementarse solo con NAND
4. **Mintérminos:** Forma canónica SOP desde la tabla de verdad

---

## Resumen

| Propiedad | Valor |
|-----------|-------|
| Número de unos | 5 |
| Número de ceros | 3 |
| Mintérminos | $\Sigma m(1,3,5,6,7)$ |
| Maxtérminos | $\Pi M(0,2,4)$ |
| Expresión mínima | $F = C + AB$ |

---

> 💡 **Tip:** Cuando una variable aparece complementada y sin complementar en todos los mintérminos, esa variable puede "absorberse" (como C en este caso).
