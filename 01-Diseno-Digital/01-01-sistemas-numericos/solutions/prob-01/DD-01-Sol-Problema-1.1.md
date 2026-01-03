<!--
::METADATA::
type: detailed_solution
topic_id: dd-01-sistemas-numericos
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 1
tags: [solucion, conversion, decimal-binario, paso-a-paso]
-->

> 🏠 **Navegación:** [← Respuestas](../DD-01-Respuestas.md) | [Problema 1.2 →](./DD-01-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Convertir los siguientes números decimales a binario:
- a) $27$
- b) $64$
- c) $100$
- d) $255$

---

## Método Utilizado: División Sucesiva por 2

Para convertir un número decimal a binario, dividimos sucesivamente entre 2 y tomamos los residuos de abajo hacia arriba.

---

## a) Convertir $27_{(10)}$ a binario

### Paso 1: Divisiones sucesivas

| División | Cociente | Residuo |
|----------|----------|---------|
| $27 \div 2$ | 13 | **1** (LSB) |
| $13 \div 2$ | 6 | **1** |
| $6 \div 2$ | 3 | **0** |
| $3 \div 2$ | 1 | **1** |
| $1 \div 2$ | 0 | **1** (MSB) |

### Paso 2: Leer residuos de abajo hacia arriba

$$27_{(10)} = \boxed{11011_{(2)}}$$

### Verificación
$$1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0$$
$$= 16 + 8 + 0 + 2 + 1 = 27 \checkmark$$

---

## b) Convertir $64_{(10)}$ a binario

### Paso 1: Divisiones sucesivas

| División | Cociente | Residuo |
|----------|----------|---------|
| $64 \div 2$ | 32 | **0** (LSB) |
| $32 \div 2$ | 16 | **0** |
| $16 \div 2$ | 8 | **0** |
| $8 \div 2$ | 4 | **0** |
| $4 \div 2$ | 2 | **0** |
| $2 \div 2$ | 1 | **0** |
| $1 \div 2$ | 0 | **1** (MSB) |

### Paso 2: Resultado

$$64_{(10)} = \boxed{1000000_{(2)}}$$

### Observación
$64 = 2^6$, por lo que es un 1 seguido de 6 ceros.

### Verificación
$$1 \cdot 2^6 = 64 \checkmark$$

---

## c) Convertir $100_{(10)}$ a binario

### Paso 1: Divisiones sucesivas

| División | Cociente | Residuo |
|----------|----------|---------|
| $100 \div 2$ | 50 | **0** (LSB) |
| $50 \div 2$ | 25 | **0** |
| $25 \div 2$ | 12 | **1** |
| $12 \div 2$ | 6 | **0** |
| $6 \div 2$ | 3 | **0** |
| $3 \div 2$ | 1 | **1** |
| $1 \div 2$ | 0 | **1** (MSB) |

### Paso 2: Resultado

$$100_{(10)} = \boxed{1100100_{(2)}}$$

### Verificación
$$1 \cdot 2^6 + 1 \cdot 2^5 + 0 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0$$
$$= 64 + 32 + 0 + 0 + 4 + 0 + 0 = 100 \checkmark$$

---

## d) Convertir $255_{(10)}$ a binario

### Paso 1: Divisiones sucesivas

| División | Cociente | Residuo |
|----------|----------|---------|
| $255 \div 2$ | 127 | **1** (LSB) |
| $127 \div 2$ | 63 | **1** |
| $63 \div 2$ | 31 | **1** |
| $31 \div 2$ | 15 | **1** |
| $15 \div 2$ | 7 | **1** |
| $7 \div 2$ | 3 | **1** |
| $3 \div 2$ | 1 | **1** |
| $1 \div 2$ | 0 | **1** (MSB) |

### Paso 2: Resultado

$$255_{(10)} = \boxed{11111111_{(2)}}$$

### Observación
$255 = 2^8 - 1$, por lo que es el máximo valor representable con 8 bits (todos unos).

### Verificación
$$2^7 + 2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0 = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255 \checkmark$$

---

## Resumen de Respuestas

| Decimal | Binario | Bits |
|---------|---------|------|
| 27 | 11011 | 5 |
| 64 | 1000000 | 7 |
| 100 | 1100100 | 7 |
| 255 | 11111111 | 8 |

---

## Conceptos Clave Aplicados

1. **División sucesiva:** Método estándar para conversión decimal → binario
2. **LSB y MSB:** El primer residuo es el bit menos significativo
3. **Verificación:** Siempre convertir de vuelta para validar
4. **Patrones:** Potencias de 2 tienen patrón simple (1 seguido de ceros)

---

> 💡 **Tip:** Para números cercanos a potencias de 2, es útil identificar la potencia más cercana y sumar/restar.
