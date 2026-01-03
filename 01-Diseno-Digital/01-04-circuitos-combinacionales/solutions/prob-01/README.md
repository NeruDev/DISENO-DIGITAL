# Soluciones Detalladas: Circuitos Combinacionales (DD-04)

```
::METADATA::
tipo: indice-soluciones
tema: dd-04-circuitos-combinacionales
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`DD-04-Respuestas.md`](../DD-04-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Multiplexores y Demultiplexores

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Diseño MUX 4:1 | [DD-04-Sol-Problema-1.1.md](DD-04-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Diseño DEMUX 1:4 | [DD-04-Sol-Problema-1.2.md](DD-04-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | MUX en cascada | [DD-04-Sol-Problema-1.3.md](DD-04-Sol-Problema-1.3.md) | ⭐⭐ |

### Nivel 2: Decodificadores y Codificadores

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Decodificador 2:4 | [DD-04-Sol-Problema-2.1.md](DD-04-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Decodificador BCD a 7-seg | [DD-04-Sol-Problema-2.2.md](DD-04-Sol-Problema-2.2.md) | ⭐⭐⭐ |
| 2.3 | Codificador de prioridad | [DD-04-Sol-Problema-2.3.md](DD-04-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Sumadores y Comparadores

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Medio sumador | [DD-04-Sol-Problema-3.1.md](DD-04-Sol-Problema-3.1.md) | ⭐ |
| 3.2 | Sumador completo | [DD-04-Sol-Problema-3.2.md](DD-04-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | Sumador 4 bits ripple-carry | [DD-04-Sol-Problema-3.3.md](DD-04-Sol-Problema-3.3.md) | ⭐⭐ |
| 3.4 | Comparador de magnitud | [DD-04-Sol-Problema-3.4.md](DD-04-Sol-Problema-3.4.md) | ⭐⭐⭐ |

---

## Bloques Combinacionales de Referencia

### Resumen de Componentes

| Componente | Entradas | Salidas | Función |
|------------|:--------:|:-------:|---------|
| MUX 2ⁿ:1 | 2ⁿ datos + n select | 1 | Selecciona 1 de 2ⁿ |
| DEMUX 1:2ⁿ | 1 dato + n select | 2ⁿ | Distribuye a 1 de 2ⁿ |
| Decoder n:2ⁿ | n | 2ⁿ | Activa 1 de 2ⁿ |
| Encoder 2ⁿ:n | 2ⁿ | n | Codifica posición activa |
| Half Adder | 2 | 2 (S, C) | Suma sin carry-in |
| Full Adder | 3 | 2 (S, Cout) | Suma con carry-in |

### Ecuaciones Clave

**Medio Sumador:**
- $S = A \oplus B$
- $C = A \cdot B$

**Sumador Completo:**
- $S = A \oplus B \oplus C_{in}$
- $C_{out} = AB + C_{in}(A \oplus B)$

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [DD-04-Respuestas.md](../DD-04-Respuestas.md) | [DD-04-Intro.md](../../DD-04-Intro.md) | [DD-04-Problemas.md](../../problems/DD-04-Problemas.md) |
