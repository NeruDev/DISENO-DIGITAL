# Soluciones Detalladas: Compuertas Lógicas (DD-03)

```
::METADATA::
tipo: indice-soluciones
tema: dd-03-compuertas-logicas
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`DD-03-Respuestas.md`](../DD-03-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Tablas de Verdad Básicas

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | AND + OR combinado | [DD-03-Sol-Problema-1.1.md](DD-03-Sol-Problema-1.1.md) | ⭐ |
| 1.2 | NOT + AND + OR | [DD-03-Sol-Problema-1.2.md](DD-03-Sol-Problema-1.2.md) | ⭐ |
| 1.3 | XOR y XNOR | [DD-03-Sol-Problema-1.3.md](DD-03-Sol-Problema-1.3.md) | ⭐ |

### Nivel 2: Análisis de Circuitos

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Obtener expresión de circuito | [DD-03-Sol-Problema-2.1.md](DD-03-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Circuito multinivel | [DD-03-Sol-Problema-2.2.md](DD-03-Sol-Problema-2.2.md) | ⭐⭐ |

### Nivel 3: Universalidad y Diseño

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Solo con NAND | [DD-03-Sol-Problema-3.1.md](DD-03-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | Solo con NOR | [DD-03-Sol-Problema-3.2.md](DD-03-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | Diseño desde especificación | [DD-03-Sol-Problema-3.3.md](DD-03-Sol-Problema-3.3.md) | ⭐⭐⭐ |

---

## Referencia de Compuertas

### Símbolos y Tablas

| Compuerta | Símbolo | Ecuación | Salida=1 cuando |
|-----------|---------|----------|-----------------|
| AND | & | $Y = A \cdot B$ | Ambas entradas = 1 |
| OR | ≥1 | $Y = A + B$ | Al menos una = 1 |
| NOT | 1 | $Y = \bar{A}$ | Entrada = 0 |
| NAND | &̅ | $Y = \overline{A \cdot B}$ | Al menos una = 0 |
| NOR | ≥̅1 | $Y = \overline{A + B}$ | Ambas = 0 |
| XOR | =1 | $Y = A \oplus B$ | Entradas diferentes |
| XNOR | =̅1 | $Y = \overline{A \oplus B}$ | Entradas iguales |

### Equivalencias Importantes

| Original | Con NAND | Con NOR |
|----------|----------|---------|
| NOT A | $\overline{A \cdot A}$ | $\overline{A + A}$ |
| A AND B | $\overline{\overline{AB} \cdot \overline{AB}}$ | $\overline{\bar{A} + \bar{B}}$ |
| A OR B | $\overline{\bar{A} \cdot \bar{B}}$ | $\overline{\overline{A+B} + \overline{A+B}}$ |

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [DD-03-Respuestas.md](../DD-03-Respuestas.md) | [DD-03-Intro.md](../../DD-03-Intro.md) | [DD-03-Problemas.md](../../problems/DD-03-Problemas.md) |
