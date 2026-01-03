<!--
::METADATA::
type: theory
topic_id: dd-01-sistemas-numericos
file_id: teoria-sistemas-numericos
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [binario, octal, hexadecimal, decimal, conversion, complemento]
search_keywords: "sistemas numéricos, binario, conversión, base, hexadecimal, octal, complemento a 2"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-01-Intro.md) | [Métodos →](../methods/DD-01-Metodos-Conversiones.md)

---

# Sistemas Numéricos

## 1. Introducción

Los **sistemas numéricos** son conjuntos de símbolos y reglas que permiten representar cantidades. En diseño digital, trabajamos principalmente con cuatro sistemas:

| Sistema | Base | Símbolos | Prefijo/Sufijo |
|---------|------|----------|----------------|
| Binario | 2 | 0, 1 | `0b` o `b` |
| Octal | 8 | 0-7 | `0o` o `o` |
| Decimal | 10 | 0-9 | (ninguno) |
| Hexadecimal | 16 | 0-9, A-F | `0x` o `h` |

---

## 2. Sistema Binario (Base 2)

El sistema binario es la base de toda la electrónica digital. Cada dígito se llama **bit** (binary digit).

### 2.1 Notación Posicional

$$N_{(2)} = \sum_{i=0}^{n-1} b_i \cdot 2^i$$

Donde $b_i$ es el bit en la posición $i$.

### 2.2 Ejemplo

El número binario $1101_{(2)}$:

$$1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 8 + 4 + 0 + 1 = 13_{(10)}$$

### 2.3 Terminología

- **MSB** (Most Significant Bit): Bit más significativo (izquierda)
- **LSB** (Least Significant Bit): Bit menos significativo (derecha)
- **Nibble**: Grupo de 4 bits
- **Byte**: Grupo de 8 bits
- **Word**: Grupo de 16, 32 o 64 bits (según arquitectura)

---

## 3. Sistema Octal (Base 8)

Utiliza dígitos del 0 al 7. Cada dígito octal equivale a **3 bits**.

### 3.1 Tabla de Equivalencias

| Octal | Binario |
|-------|---------|
| 0 | 000 |
| 1 | 001 |
| 2 | 010 |
| 3 | 011 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |

### 3.2 Ejemplo

$$347_{(8)} = 011\ 100\ 111_{(2)} = 231_{(10)}$$

---

## 4. Sistema Hexadecimal (Base 16)

Utiliza dígitos 0-9 y letras A-F. Cada dígito hexadecimal equivale a **4 bits** (un nibble).

### 4.1 Tabla de Equivalencias

| Hex | Decimal | Binario |
|-----|---------|---------|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| A | 10 | 1010 |
| B | 11 | 1011 |
| C | 12 | 1100 |
| D | 13 | 1101 |
| E | 14 | 1110 |
| F | 15 | 1111 |

### 4.2 Ejemplo

$$\text{2AF}_{(16)} = 0010\ 1010\ 1111_{(2)} = 687_{(10)}$$

---

## 5. Conversiones Entre Bases

### 5.1 Decimal a Binario

**Método de divisiones sucesivas:** Dividir entre 2 repetidamente y tomar los residuos en orden inverso.

**Ejemplo:** $25_{(10)}$ a binario

| División | Cociente | Residuo |
|----------|----------|---------|
| 25 ÷ 2 | 12 | 1 (LSB) |
| 12 ÷ 2 | 6 | 0 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 (MSB) |

**Resultado:** $25_{(10)} = 11001_{(2)}$

### 5.2 Binario a Decimal

Sumar las potencias de 2 correspondientes a los bits en 1.

### 5.3 Binario ↔ Hexadecimal

Agrupar bits de 4 en 4 desde el LSB y convertir cada grupo.

**Ejemplo:** $10110111_{(2)} = 1011\ 0111 = \text{B7}_{(16)}$

### 5.4 Binario ↔ Octal

Agrupar bits de 3 en 3 desde el LSB y convertir cada grupo.

**Ejemplo:** $10110111_{(2)} = 010\ 110\ 111 = 267_{(8)}$

---

## 6. Números con Signo

### 6.1 Magnitud con Signo

El MSB indica el signo: 0 = positivo, 1 = negativo.

- **Ventaja:** Fácil de entender
- **Desventaja:** Dos representaciones del cero (+0 y -0)

### 6.2 Complemento a 1

Para obtener el negativo: invertir todos los bits.

$$-N = \overline{N}$$

**Ejemplo (4 bits):**
- $+5 = 0101$
- $-5 = 1010$

### 6.3 Complemento a 2

Para obtener el negativo: invertir bits y sumar 1.

$$-N = \overline{N} + 1$$

**Ejemplo (4 bits):**
- $+5 = 0101$
- $-5 = 1010 + 1 = 1011$

### 6.4 Rango de Representación (n bits)

| Formato | Rango |
|---------|-------|
| Sin signo | $0$ a $2^n - 1$ |
| Complemento a 2 | $-2^{n-1}$ a $2^{n-1} - 1$ |

**Para 8 bits:**
- Sin signo: 0 a 255
- Complemento a 2: -128 a +127

---

## 7. Códigos Binarios Especiales

### 7.1 BCD (Binary Coded Decimal)

Cada dígito decimal se codifica con 4 bits.

$$259_{(10)} = 0010\ 0101\ 1001_{(BCD)}$$

### 7.2 Código Gray

Código donde valores adyacentes difieren en un solo bit.

| Decimal | Binario | Gray |
|---------|---------|------|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |

**Conversión Binario → Gray:**
$$G_i = B_i \oplus B_{i+1}$$

---

## 8. Aritmética Binaria

### 8.1 Suma Binaria

| A | B | Suma | Acarreo |
|---|---|------|---------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

### 8.2 Resta Binaria (usando Complemento a 2)

$$A - B = A + (-B) = A + \overline{B} + 1$$

---

## Referencias

- Mano, M. M. (2013). *Digital Design*. Pearson.
- Tocci, R. J. (2017). *Digital Systems: Principles and Applications*. Pearson.

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: Ninguno
CONEXIONES: Este tema es fundamento para álgebra booleana y todos los circuitos digitales
ERRORES_COMUNES: Confundir complemento a 1 con complemento a 2; olvidar el acarreo en sumas
-->
