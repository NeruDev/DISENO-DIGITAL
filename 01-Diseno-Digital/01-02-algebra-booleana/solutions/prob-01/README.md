# Soluciones Detalladas: Álgebra Booleana (DD-02)

```
::METADATA::
tipo: indice-soluciones
tema: dd-02-algebra-booleana
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`DD-02-Respuestas.md`](../DD-02-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Simplificación con Teoremas

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Teoremas de Absorción | [DD-02-Sol-Problema-1.1.md](DD-02-Sol-Problema-1.1.md) | ⭐ |
| 1.2 | Teorema de De Morgan | [DD-02-Sol-Problema-1.2.md](DD-02-Sol-Problema-1.2.md) | ⭐ |
| 1.3 | Aplicación mixta | [DD-02-Sol-Problema-1.3.md](DD-02-Sol-Problema-1.3.md) | ⭐⭐ |

### Nivel 2: Formas Canónicas

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Suma de Productos (SOP) | [DD-02-Sol-Problema-2.1.md](DD-02-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Producto de Sumas (POS) | [DD-02-Sol-Problema-2.2.md](DD-02-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Conversión SOP ↔ POS | [DD-02-Sol-Problema-2.3.md](DD-02-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Mapas de Karnaugh

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | K-Map 2 variables | [DD-02-Sol-Problema-3.1.md](DD-02-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | K-Map 3 variables | [DD-02-Sol-Problema-3.2.md](DD-02-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | K-Map 4 variables | [DD-02-Sol-Problema-3.3.md](DD-02-Sol-Problema-3.3.md) | ⭐⭐⭐ |
| 3.4 | K-Map con "Don't Care" | [DD-02-Sol-Problema-3.4.md](DD-02-Sol-Problema-3.4.md) | ⭐⭐⭐ |

---

## Teoremas de Referencia Rápida

### Teoremas Básicos

| # | Teorema | Forma AND | Forma OR |
|---|---------|-----------|----------|
| 1 | Identidad | $A \cdot 1 = A$ | $A + 0 = A$ |
| 2 | Null | $A \cdot 0 = 0$ | $A + 1 = 1$ |
| 3 | Idempotente | $A \cdot A = A$ | $A + A = A$ |
| 4 | Complemento | $A \cdot \bar{A} = 0$ | $A + \bar{A} = 1$ |
| 5 | Involución | $\bar{\bar{A}} = A$ | - |

### Teoremas de De Morgan

$$\overline{A \cdot B} = \bar{A} + \bar{B}$$
$$\overline{A + B} = \bar{A} \cdot \bar{B}$$

### Teoremas de Absorción

$$A + AB = A$$
$$A(A + B) = A$$
$$A + \bar{A}B = A + B$$

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [DD-02-Respuestas.md](../DD-02-Respuestas.md) | [DD-02-Intro.md](../../DD-02-Intro.md) | [DD-02-Problemas.md](../../problems/DD-02-Problemas.md) |
