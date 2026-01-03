<!--
::METADATA::
type: method
topic_id: dd-01-sistemas-numericos
file_id: metodos-conversiones
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [conversion, metodo, algoritmo, paso-a-paso]
search_keywords: "conversión, método, algoritmo, decimal a binario, binario a hexadecimal"
-->

> 🏠 **Navegación:** [← Teoría](../theory/DD-01-Teoria-SistemasNumericos.md) | [Problemas →](../problems/DD-01-Problemas.md)

---

# Métodos de Conversión entre Sistemas Numéricos

## Método 1: Decimal → Binario (Enteros)

### Algoritmo: Divisiones Sucesivas

**Pasos:**
1. Dividir el número decimal entre 2
2. Anotar el residuo (0 o 1)
3. Tomar el cociente y repetir desde el paso 1
4. Continuar hasta que el cociente sea 0
5. Leer los residuos de abajo hacia arriba

### Ejemplo Resuelto: Convertir $45_{(10)}$ a binario

```
45 ÷ 2 = 22  residuo 1  ← LSB
22 ÷ 2 = 11  residuo 0
11 ÷ 2 = 5   residuo 1
 5 ÷ 2 = 2   residuo 1
 2 ÷ 2 = 1   residuo 0
 1 ÷ 2 = 0   residuo 1  ← MSB
```

**Resultado:** $45_{(10)} = 101101_{(2)}$

---

## Método 2: Decimal → Binario (Fraccionarios)

### Algoritmo: Multiplicaciones Sucesivas

**Pasos:**
1. Multiplicar la parte fraccionaria por 2
2. Anotar la parte entera (0 o 1)
3. Tomar solo la parte fraccionaria del resultado
4. Repetir hasta obtener 0 o alcanzar la precisión deseada
5. Leer los enteros de arriba hacia abajo

### Ejemplo Resuelto: Convertir $0.625_{(10)}$ a binario

```
0.625 × 2 = 1.25  → 1  ← MSB (después del punto)
0.25  × 2 = 0.50  → 0
0.50  × 2 = 1.00  → 1  ← LSB
0.00  → FIN
```

**Resultado:** $0.625_{(10)} = 0.101_{(2)}$

---

## Método 3: Binario → Decimal

### Algoritmo: Suma de Potencias

**Pasos:**
1. Numerar las posiciones desde 0 (derecha) hasta n-1 (izquierda)
2. Multiplicar cada bit por $2^{posición}$
3. Sumar todos los productos

### Ejemplo Resuelto: Convertir $110101_{(2)}$ a decimal

| Posición | 5 | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|---|
| Bit | 1 | 1 | 0 | 1 | 0 | 1 |
| Potencia | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| Valor | 32 | 16 | 0 | 4 | 0 | 1 |

$$32 + 16 + 0 + 4 + 0 + 1 = 53$$

**Resultado:** $110101_{(2)} = 53_{(10)}$

---

## Método 4: Binario → Hexadecimal

### Algoritmo: Agrupación de 4 bits

**Pasos:**
1. Agrupar los bits de 4 en 4 desde la derecha (LSB)
2. Si faltan bits a la izquierda, completar con ceros
3. Convertir cada grupo usando la tabla de equivalencias

### Ejemplo Resuelto: Convertir $10110111_{(2)}$ a hexadecimal

```
1011 0111
 ↓    ↓
 B    7
```

**Resultado:** $10110111_{(2)} = \text{B7}_{(16)}$

---

## Método 5: Hexadecimal → Binario

### Algoritmo: Expansión de 4 bits

**Pasos:**
1. Tomar cada dígito hexadecimal
2. Convertir a su equivalente de 4 bits
3. Concatenar todos los grupos

### Ejemplo Resuelto: Convertir $\text{3F}_{(16)}$ a binario

```
 3    F
 ↓    ↓
0011 1111
```

**Resultado:** $\text{3F}_{(16)} = 00111111_{(2)}$

---

## Método 6: Binario → Octal

### Algoritmo: Agrupación de 3 bits

**Pasos:**
1. Agrupar los bits de 3 en 3 desde la derecha (LSB)
2. Si faltan bits a la izquierda, completar con ceros
3. Convertir cada grupo (0-7)

### Ejemplo Resuelto: Convertir $10110111_{(2)}$ a octal

```
010 110 111
 ↓   ↓   ↓
 2   6   7
```

**Resultado:** $10110111_{(2)} = 267_{(8)}$

---

## Método 7: Obtener Complemento a 2

### Algoritmo

**Pasos:**
1. Escribir el número en binario con n bits
2. Invertir todos los bits (complemento a 1)
3. Sumar 1 al resultado

### Ejemplo Resuelto: Obtener $-25$ en complemento a 2 (8 bits)

```
Paso 1: +25 = 00011001
Paso 2: Invertir → 11100110
Paso 3: Sumar 1 → 11100111
```

**Resultado:** $-25_{(10)} = 11100111_{(C2, 8 bits)}$

### Método Alternativo (Atajo)

1. Recorrer el número de derecha a izquierda
2. Copiar todos los bits hasta encontrar el primer 1 (inclusive)
3. Invertir todos los bits restantes

```
+25 = 00011001
            ↑ primer 1 desde la derecha
      11100111  (copiar hasta el 1, invertir el resto)
```

---

## Método 8: Conversión BCD

### Decimal → BCD

**Pasos:**
1. Tomar cada dígito decimal por separado
2. Convertir cada dígito a 4 bits

### Ejemplo: $259_{(10)}$ a BCD

```
2    5    9
↓    ↓    ↓
0010 0101 1001
```

**Resultado:** $259_{(10)} = 0010\ 0101\ 1001_{(BCD)}$

### BCD → Decimal

**Pasos:**
1. Agrupar de 4 en 4 bits
2. Convertir cada grupo a dígito decimal (debe ser 0-9)

---

## Método 9: Binario → Gray

### Algoritmo

$$G_n = B_n$$
$$G_i = B_{i+1} \oplus B_i \quad \text{para } i < n$$

### Ejemplo: Convertir $1011_{(2)}$ a Gray

```
B:  1  0  1  1
    ↓  
G₃= 1
G₂= 1⊕0 = 1
G₁= 0⊕1 = 1
G₀= 1⊕1 = 0
```

**Resultado:** $1011_{(Binario)} = 1110_{(Gray)}$

---

## Método 10: Gray → Binario

### Algoritmo

$$B_n = G_n$$
$$B_i = B_{i+1} \oplus G_i \quad \text{para } i < n$$

### Ejemplo: Convertir $1110_{(Gray)}$ a binario

```
G:  1  1  1  0
    ↓
B₃= 1
B₂= 1⊕1 = 0
B₁= 0⊕1 = 1
B₀= 1⊕0 = 1
```

**Resultado:** $1110_{(Gray)} = 1011_{(Binario)}$

---

## Tabla de Referencia Rápida

| Conversión | Método | Clave |
|------------|--------|-------|
| Dec → Bin | Divisiones sucesivas | ÷2, leer residuos ↑ |
| Bin → Dec | Suma de potencias | $\sum b_i \cdot 2^i$ |
| Bin → Hex | Grupos de 4 bits | Desde LSB |
| Bin → Oct | Grupos de 3 bits | Desde LSB |
| Hex → Bin | Expandir 4 bits | Por dígito |
| Oct → Bin | Expandir 3 bits | Por dígito |
| +N → -N (C2) | Invertir + 1 | O atajo desde LSB |

---

<!-- IA_CONTEXT
USO: Documento de referencia para resolver conversiones paso a paso
NIVEL: Básico (1/3)
CUANDO_USAR: Cuando el estudiante necesite un algoritmo claro para conversiones
-->
