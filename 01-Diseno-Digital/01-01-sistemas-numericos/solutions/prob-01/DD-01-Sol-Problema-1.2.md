<!--
::METADATA::
type: detailed_solution
topic_id: dd-01-sistemas-numericos
problem_id: 1.2
file_id: solucion-problema-1-2
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 1
tags: [solucion, conversion, binario-decimal, paso-a-paso]
-->

> 🏠 **Navegación:** [← Problema 1.1](./DD-01-Sol-Problema-1.1.md) | [Problema 1.3 →](./DD-01-Sol-Problema-1.3.md)

---

# Solución Detallada: Problema 1.2

## Enunciado
Convertir los siguientes números binarios a decimal:
- a) $1010$
- b) $11011$
- c) $10000001$
- d) $11111111$

---

## Método Utilizado: Notación Posicional

Cada bit tiene un peso según su posición: $b_n \cdot 2^n + ... + b_1 \cdot 2^1 + b_0 \cdot 2^0$

---

## a) Convertir $1010_{(2)}$ a decimal

### Paso 1: Identificar posiciones (de derecha a izquierda, empezando en 0)

| Posición | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|
| Bit | 1 | 0 | 1 | 0 |
| Peso | $2^3$ | $2^2$ | $2^1$ | $2^0$ |

### Paso 2: Calcular

$$1010_{(2)} = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0$$
$$= 1 \cdot 8 + 0 \cdot 4 + 1 \cdot 2 + 0 \cdot 1$$
$$= 8 + 0 + 2 + 0$$

### Resultado
$$1010_{(2)} = \boxed{10_{(10)}}$$

---

## b) Convertir $11011_{(2)}$ a decimal

### Paso 1: Identificar posiciones

| Posición | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|
| Bit | 1 | 1 | 0 | 1 | 1 |
| Peso | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |

### Paso 2: Calcular

$$11011_{(2)} = 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0$$
$$= 16 + 8 + 0 + 2 + 1$$

### Resultado
$$11011_{(2)} = \boxed{27_{(10)}}$$

---

## c) Convertir $10000001_{(2)}$ a decimal

### Paso 1: Identificar posiciones

| Posición | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|---|---|---|
| Bit | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Peso | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |

### Paso 2: Calcular (solo bits en 1)

$$10000001_{(2)} = 1 \cdot 2^7 + 1 \cdot 2^0$$
$$= 128 + 1$$

### Resultado
$$10000001_{(2)} = \boxed{129_{(10)}}$$

### Observación
Solo hay dos bits en 1, lo que simplifica mucho el cálculo.

---

## d) Convertir $11111111_{(2)}$ a decimal

### Método 1: Suma directa

| Posición | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|---|---|---|
| Bit | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Valor | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

$$11111111_{(2)} = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255$$

### Método 2: Fórmula para todos unos

Cuando todos los bits son 1:
$$\underbrace{111...1}_{n \text{ bits}} = 2^n - 1$$

Para 8 bits:
$$11111111_{(2)} = 2^8 - 1 = 256 - 1 = 255$$

### Resultado
$$11111111_{(2)} = \boxed{255_{(10)}}$$

---

## Resumen de Respuestas

| Binario | Decimal | Observación |
|---------|---------|-------------|
| 1010 | 10 | Patrón alterno |
| 11011 | 27 | - |
| 10000001 | 129 | Solo 2 bits en 1 |
| 11111111 | 255 | Máximo de 8 bits |

---

## Tabla de Potencias de 2 (Referencia)

| $2^0$ | $2^1$ | $2^2$ | $2^3$ | $2^4$ | $2^5$ | $2^6$ | $2^7$ | $2^8$ |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |

---

## Conceptos Clave Aplicados

1. **Notación posicional:** Cada posición tiene un peso de $2^n$
2. **Optimización:** Solo sumar donde hay bits en 1
3. **Fórmula especial:** $2^n - 1$ para números con todos bits en 1
4. **Rangos:** Con n bits se representan valores de 0 a $2^n - 1$

---

> 💡 **Tip:** Memorizar las potencias de 2 hasta $2^{10} = 1024$ acelera mucho los cálculos.
