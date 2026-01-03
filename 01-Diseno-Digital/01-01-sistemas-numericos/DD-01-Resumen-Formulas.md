<!--
::METADATA::
type: reference
topic_id: dd-01-sistemas-numericos
file_id: resumen-formulas-sistemas-numericos
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, formulas, resumen, referencia-rapida]
search_keywords: "resumen, fórmulas, cheatsheet, referencia rápida"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-01-Intro.md)

---

# 📋 Cheatsheet: Sistemas Numéricos

## Bases Numéricas

| Sistema | Base | Símbolos | Prefijo |
|---------|------|----------|---------|
| Binario | 2 | 0, 1 | `0b` |
| Octal | 8 | 0-7 | `0o` |
| Decimal | 10 | 0-9 | - |
| Hexadecimal | 16 | 0-9, A-F | `0x` |

---

## Tabla Hex-Bin-Oct

| Hex | Dec | Bin | Oct |
|-----|-----|-----|-----|
| 0 | 0 | 0000 | 0 |
| 1 | 1 | 0001 | 1 |
| 2 | 2 | 0010 | 2 |
| 3 | 3 | 0011 | 3 |
| 4 | 4 | 0100 | 4 |
| 5 | 5 | 0101 | 5 |
| 6 | 6 | 0110 | 6 |
| 7 | 7 | 0111 | 7 |
| 8 | 8 | 1000 | 10 |
| 9 | 9 | 1001 | 11 |
| A | 10 | 1010 | 12 |
| B | 11 | 1011 | 13 |
| C | 12 | 1100 | 14 |
| D | 13 | 1101 | 15 |
| E | 14 | 1110 | 16 |
| F | 15 | 1111 | 17 |

---

## Potencias de 2

| $2^n$ | Valor | Nombre |
|-------|-------|--------|
| $2^0$ | 1 | - |
| $2^1$ | 2 | - |
| $2^2$ | 4 | - |
| $2^3$ | 8 | - |
| $2^4$ | 16 | Nibble |
| $2^8$ | 256 | Byte |
| $2^{10}$ | 1024 | 1 Ki |
| $2^{16}$ | 65536 | 64 Ki |
| $2^{20}$ | 1048576 | 1 Mi |

---

## Fórmulas de Conversión

### Binario → Decimal
$$N_{(10)} = \sum_{i=0}^{n-1} b_i \cdot 2^i$$

### Decimal → Binario
Divisiones sucesivas por 2, leer residuos ↑

### Fracción Decimal → Binario
Multiplicaciones sucesivas por 2, leer enteros ↓

---

## Complemento a 2

### Obtener -N
$$-N = \overline{N} + 1$$

### Atajo
Desde LSB: copiar hasta primer 1, luego invertir

### Rangos (n bits)

| Tipo | Mínimo | Máximo |
|------|--------|--------|
| Sin signo | $0$ | $2^n - 1$ |
| C2 | $-2^{n-1}$ | $2^{n-1} - 1$ |

**8 bits:** Sin signo: 0-255 | C2: -128 a +127

---

## Códigos Especiales

### BCD
Cada dígito decimal → 4 bits
$$259 = 0010\ 0101\ 1001$$

### Gray
$$G_i = B_i \oplus B_{i+1}$$

| Bin | Gray |
|-----|------|
| 0000 | 0000 |
| 0001 | 0001 |
| 0010 | 0011 |
| 0011 | 0010 |

---

## Aritmética Binaria

### Suma
```
0+0=0  0+1=1  1+0=1  1+1=10
```

### Resta (usando C2)
$$A - B = A + \overline{B} + 1$$

### Overflow (C2)
- Positivo + Positivo = Negativo → ⚠️
- Negativo + Negativo = Positivo → ⚠️

---

## Terminología

| Término | Definición |
|---------|------------|
| **Bit** | Binary digit (0 o 1) |
| **Nibble** | 4 bits |
| **Byte** | 8 bits |
| **Word** | 16/32/64 bits |
| **MSB** | Bit más significativo |
| **LSB** | Bit menos significativo |

---

## Conversiones Rápidas

```
Bin → Hex: agrupar 4 bits desde LSB
Bin → Oct: agrupar 3 bits desde LSB
Hex → Bin: expandir cada dígito a 4 bits
Oct → Bin: expandir cada dígito a 3 bits
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante exámenes o resolución de problemas
-->
