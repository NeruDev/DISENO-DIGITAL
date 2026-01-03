# Soluciones Detalladas: Circuitos Secuenciales (DD-05)

```
::METADATA::
tipo: indice-soluciones
tema: dd-05-circuitos-secuenciales
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`DD-05-Respuestas.md`](../DD-05-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Flip-Flops Básicos

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Flip-Flop D análisis | [DD-05-Sol-Problema-1.1.md](DD-05-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Flip-Flop JK análisis | [DD-05-Sol-Problema-1.2.md](DD-05-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | Flip-Flop T análisis | [DD-05-Sol-Problema-1.3.md](DD-05-Sol-Problema-1.3.md) | ⭐⭐ |
| 1.4 | Conversión entre FF | [DD-05-Sol-Problema-1.4.md](DD-05-Sol-Problema-1.4.md) | ⭐⭐ |

### Nivel 2: Latches y Timing

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Latch SR análisis | [DD-05-Sol-Problema-2.1.md](DD-05-Sol-Problema-2.1.md) | ⭐ |
| 2.2 | Setup y Hold time | [DD-05-Sol-Problema-2.2.md](DD-05-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Metaestabilidad | [DD-05-Sol-Problema-2.3.md](DD-05-Sol-Problema-2.3.md) | ⭐⭐⭐ |

### Nivel 3: Circuitos Secuenciales Síncronos

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Detector de secuencia | [DD-05-Sol-Problema-3.1.md](DD-05-Sol-Problema-3.1.md) | ⭐⭐⭐ |
| 3.2 | Registro de desplazamiento | [DD-05-Sol-Problema-3.2.md](DD-05-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | Divisor de frecuencia | [DD-05-Sol-Problema-3.3.md](DD-05-Sol-Problema-3.3.md) | ⭐⭐ |

---

## Referencia de Flip-Flops

### Tablas Características

**Flip-Flop D:**
| D | Q⁺ |
|:-:|:--:|
| 0 | 0 |
| 1 | 1 |

$Q^+ = D$

**Flip-Flop JK:**
| J | K | Q⁺ |
|:-:|:-:|:--:|
| 0 | 0 | Q |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | Q̄ |

$Q^+ = J\bar{Q} + \bar{K}Q$

**Flip-Flop T:**
| T | Q⁺ |
|:-:|:--:|
| 0 | Q |
| 1 | Q̄ |

$Q^+ = T\bar{Q} + \bar{T}Q = T \oplus Q$

### Tablas de Excitación

**FF-D:**
| Q | Q⁺ | D |
|:-:|:--:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**FF-JK:**
| Q | Q⁺ | J | K |
|:-:|:--:|:-:|:-:|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

**FF-T:**
| Q | Q⁺ | T |
|:-:|:--:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [DD-05-Respuestas.md](../DD-05-Respuestas.md) | [DD-05-Intro.md](../../DD-05-Intro.md) | [DD-05-Problemas.md](../../problems/DD-05-Problemas.md) |
