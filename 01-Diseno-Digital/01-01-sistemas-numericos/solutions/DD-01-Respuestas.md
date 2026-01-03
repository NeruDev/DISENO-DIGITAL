<!--
::METADATA::
type: solution
topic_id: dd-01-sistemas-numericos
file_id: respuestas-sistemas-numericos
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, resultados"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-01-Problemas.md) | [Soluciones Detalladas →](./prob-01/)

---

# Respuestas: Sistemas Numéricos

## Nivel 1: Conversiones Básicas

### Respuestas 1.1 (Decimal → Binario)
| | Decimal | Binario |
|--|---------|---------|
| a) | 27 | $11011$ |
| b) | 64 | $1000000$ |
| c) | 100 | $1100100$ |
| d) | 255 | $11111111$ |

### Respuestas 1.2 (Binario → Decimal)
| | Binario | Decimal |
|--|---------|---------|
| a) | 1010 | $10$ |
| b) | 11011 | $27$ |
| c) | 10000001 | $129$ |
| d) | 11111111 | $255$ |

### Respuestas 1.3 (Binario → Hexadecimal)
| | Binario | Hexadecimal |
|--|---------|-------------|
| a) | 10110011 | $\text{B3}$ |
| b) | 11110000 | $\text{F0}$ |
| c) | 01010101 | $\text{55}$ |
| d) | 11111111 | $\text{FF}$ |

### Respuestas 1.4 (Hexadecimal → Binario)
| | Hex | Binario |
|--|-----|---------|
| a) | 4A | $01001010$ |
| b) | FF | $11111111$ |
| c) | 1C3 | $000111000011$ |
| d) | BEEF | $1011111011101111$ |

### Respuestas 1.5 (Binario → Octal)
| | Binario | Octal |
|--|---------|-------|
| a) | 110101 | $65$ |
| b) | 11111111 | $377$ |
| c) | 10000000 | $200$ |
| d) | 101010101 | $525$ |

---

## Nivel 2: Conversiones con Fracciones

### Respuestas 2.1 (Decimal fraccionario → Binario)
| | Decimal | Binario |
|--|---------|---------|
| a) | 0.5 | $0.1$ |
| b) | 0.75 | $0.11$ |
| c) | 0.125 | $0.001$ |
| d) | 0.3 | $0.0100$ (aprox) |

### Respuestas 2.2 (Conversión a decimal)
| | Original | Decimal |
|--|----------|---------|
| a) | $101.11_{(2)}$ | $5.75$ |
| b) | $11.001_{(2)}$ | $3.125$ |
| c) | $\text{A.8}_{(16)}$ | $10.5$ |
| d) | $7.4_{(8)}$ | $7.5$ |

### Respuestas 2.3 ($25.625_{(10)}$)
| Sistema | Resultado |
|---------|-----------|
| a) Binario | $11001.101$ |
| b) Hexadecimal | $\text{19.A}$ |
| c) Octal | $31.5$ |

---

## Nivel 3: Números con Signo

### Respuestas 3.1 (Complemento a 2, 8 bits)
| | Decimal | Complemento a 2 |
|--|---------|-----------------|
| a) | +45 | $00101101$ |
| b) | -45 | $11010011$ |
| c) | +127 | $01111111$ |
| d) | -128 | $10000000$ |
| e) | -1 | $11111111$ |

### Respuestas 3.2 (C2 → Decimal)
| | Complemento a 2 | Decimal |
|--|-----------------|---------|
| a) | 01111111 | $+127$ |
| b) | 10000000 | $-128$ |
| c) | 11111111 | $-1$ |
| d) | 10000001 | $-127$ |
| e) | 11110000 | $-16$ |

### Respuestas 3.3 (Rangos)
| | Formato | Rango |
|--|---------|-------|
| a) | 4 bits sin signo | $0$ a $15$ |
| b) | 4 bits C2 | $-8$ a $+7$ |
| c) | 16 bits sin signo | $0$ a $65535$ |
| d) | 16 bits C2 | $-32768$ a $+32767$ |

---

## Nivel 4: Aritmética Binaria

### Respuestas 4.1 (Sumas)
| | Operación | Resultado |
|--|-----------|-----------|
| a) | 01100101 + 00011010 | $01111111$ (127) |
| b) | 11111111 + 00000001 | $00000000$ (overflow) |
| c) | 10101010 + 01010101 | $11111111$ (255) |

### Respuestas 4.2 (Restas en C2)
| | Operación | Resultado | Decimal |
|--|-----------|-----------|---------|
| a) | 50 - 25 | $00011001$ | $25$ |
| b) | 100 - 150 | $11001110$ | $-50$ |
| c) | -30 - 40 | $10111010$ | $-70$ |

### Respuestas 4.3 (Detección de Overflow)
| | Operación | ¿Overflow? | Explicación |
|--|-----------|------------|-------------|
| a) | 100 + 50 | No | $150 < 127$? Sí → **Overflow** |
| b) | 100 + 100 | **Sí** | $200 > 127$ |
| c) | -100 + (-50) | **Sí** | $-150 < -128$ |
| d) | -100 + (-100) | **Sí** | $-200 < -128$ |

**Corrección 4.3a:** Sí hay overflow porque $150 > 127$

---

## Nivel 5: Códigos Especiales

### Respuestas 5.1 (Decimal → BCD)
| | Decimal | BCD |
|--|---------|-----|
| a) | 47 | $0100\ 0111$ |
| b) | 256 | $0010\ 0101\ 0110$ |
| c) | 1000 | $0001\ 0000\ 0000\ 0000$ |
| d) | 9999 | $1001\ 1001\ 1001\ 1001$ |

### Respuestas 5.2 (BCD → Decimal)
| | BCD | Decimal |
|--|-----|---------|
| a) | 0001 0010 0011 | $123$ |
| b) | 1001 0000 0101 | $905$ |
| c) | 0110 0111 1000 1001 | $6789$ |

### Respuestas 5.3 (Binario → Gray)
| | Binario | Gray |
|--|---------|------|
| a) | 0000 | $0000$ |
| b) | 0111 | $0100$ |
| c) | 1010 | $1111$ |
| d) | 1111 | $1000$ |

### Respuestas 5.4 (Gray → Binario)
| | Gray | Binario |
|--|------|---------|
| a) | 0000 | $0000$ |
| b) | 0100 | $0111$ |
| c) | 1100 | $1000$ |
| d) | 1000 | $1111$ |

---

## Nivel 6: Problemas de Aplicación

### Respuestas 6.1
- a) $-100$ en C2 (8 bits): $10011100$
- b) Como sin signo: $156$

### Respuestas 6.2
- a) $\text{0x3FF} = 1023_{(10)}$
- b) Se necesitan **10 bits** ($2^{10} = 1024$)

### Respuestas 6.3
- a) $1100110011_{(2)} = 819_{(10)}$
- b) $V = \frac{819}{1023} \times 5V = 4.00V$

### Respuestas 6.4
- a) 'A' = $65_{(10)} = 01000001_{(2)}$
- b) Paridad par: hay 2 unos → bit de paridad = $0$
- c) Trama: $0\ 01000001\ 0\ 1$ = `0 01000001 0 1`

---

## Problema Integrador

### Respuesta 7.1

| Dec | Binario | Hex | Octal | BCD | Gray |
|-----|---------|-----|-------|-----|------|
| 0 | 0000 | 0 | 0 | 0000 | 0000 |
| 1 | 0001 | 1 | 1 | 0001 | 0001 |
| 2 | 0010 | 2 | 2 | 0010 | 0011 |
| 3 | 0011 | 3 | 3 | 0011 | 0010 |
| 4 | 0100 | 4 | 4 | 0100 | 0110 |
| 5 | 0101 | 5 | 5 | 0101 | 0111 |
| 6 | 0110 | 6 | 6 | 0110 | 0101 |
| 7 | 0111 | 7 | 7 | 0111 | 0100 |
| 8 | 1000 | 8 | 10 | 1000 | 1100 |
| 9 | 1001 | 9 | 11 | 1001 | 1101 |
| 10 | 1010 | A | 12 | 0001 0000 | 1111 |
| 11 | 1011 | B | 13 | 0001 0001 | 1110 |
| 12 | 1100 | C | 14 | 0001 0010 | 1010 |
| 13 | 1101 | D | 15 | 0001 0011 | 1011 |
| 14 | 1110 | E | 16 | 0001 0100 | 1001 |
| 15 | 1111 | F | 17 | 0001 0101 | 1000 |

---

> 📘 **Nota:** Para ver el desarrollo paso a paso de problemas específicos, consulta la carpeta `solutions/prob-XX/`

<!-- IA_CONTEXT
PROPÓSITO: Respuestas rápidas para verificación
PARA_DESARROLLO_COMPLETO: Consultar carpeta solutions/prob-XX/
-->
