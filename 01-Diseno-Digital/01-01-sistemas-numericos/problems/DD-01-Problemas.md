<!--
::METADATA::
type: problem
topic_id: dd-01-sistemas-numericos
file_id: problemas-sistemas-numericos
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, conversion, binario, hexadecimal, complemento]
search_keywords: "ejercicios, problemas, conversión, práctica"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-01-Metodos-Conversiones.md) | [Respuestas →](../solutions/DD-01-Respuestas.md)

---

# Problemas: Sistemas Numéricos

## Nivel 1: Conversiones Básicas

### Problema 1.1
Convertir los siguientes números decimales a binario:
- a) $27$
- b) $64$
- c) $100$
- d) $255$

### Problema 1.2
Convertir los siguientes números binarios a decimal:
- a) $1010$
- b) $11011$
- c) $10000001$
- d) $11111111$

### Problema 1.3
Convertir los siguientes números binarios a hexadecimal:
- a) $10110011$
- b) $11110000$
- c) $01010101$
- d) $11111111$

### Problema 1.4
Convertir los siguientes números hexadecimales a binario:
- a) $\text{4A}$
- b) $\text{FF}$
- c) $\text{1C3}$
- d) $\text{BEEF}$

### Problema 1.5
Convertir los siguientes números binarios a octal:
- a) $110101$
- b) $11111111$
- c) $10000000$
- d) $101010101$

---

## Nivel 2: Conversiones con Fracciones

### Problema 2.1
Convertir a binario (hasta 4 bits fraccionarios):
- a) $0.5$
- b) $0.75$
- c) $0.125$
- d) $0.3$ (aproximar)

### Problema 2.2
Convertir a decimal:
- a) $101.11_{(2)}$
- b) $11.001_{(2)}$
- c) $\text{A.8}_{(16)}$
- d) $7.4_{(8)}$

### Problema 2.3
Convertir $25.625_{(10)}$ a:
- a) Binario
- b) Hexadecimal
- c) Octal

---

## Nivel 3: Números con Signo

### Problema 3.1
Representar los siguientes números en complemento a 2 usando 8 bits:
- a) $+45$
- b) $-45$
- c) $+127$
- d) $-128$
- e) $-1$

### Problema 3.2
¿Qué números decimales representan los siguientes valores en complemento a 2 (8 bits)?
- a) $01111111$
- b) $10000000$
- c) $11111111$
- d) $10000001$
- e) $11110000$

### Problema 3.3
¿Cuál es el rango de números que se pueden representar con:
- a) 4 bits sin signo
- b) 4 bits en complemento a 2
- c) 16 bits sin signo
- d) 16 bits en complemento a 2

---

## Nivel 4: Aritmética Binaria

### Problema 4.1
Realizar las siguientes sumas en binario (8 bits):
- a) $01100101 + 00011010$
- b) $11111111 + 00000001$
- c) $10101010 + 01010101$

### Problema 4.2
Realizar las siguientes restas usando complemento a 2 (8 bits):
- a) $50 - 25$
- b) $100 - 150$
- c) $-30 - 40$

### Problema 4.3
Verificar si hay overflow en las siguientes operaciones (complemento a 2, 8 bits):
- a) $100 + 50$
- b) $100 + 100$
- c) $-100 + (-50)$
- d) $-100 + (-100)$

---

## Nivel 5: Códigos Especiales

### Problema 5.1
Convertir a BCD:
- a) $47$
- b) $256$
- c) $1000$
- d) $9999$

### Problema 5.2
Convertir de BCD a decimal:
- a) $0001\ 0010\ 0011$
- b) $1001\ 0000\ 0101$
- c) $0110\ 0111\ 1000\ 1001$

### Problema 5.3
Convertir de binario a código Gray:
- a) $0000$
- b) $0111$
- c) $1010$
- d) $1111$

### Problema 5.4
Convertir de código Gray a binario:
- a) $0000$
- b) $0100$
- c) $1100$
- d) $1000$

---

## Nivel 6: Problemas de Aplicación

### Problema 6.1
Un microcontrolador tiene registros de 8 bits. Si se necesita almacenar el valor $-100$:
- a) ¿Cuál es su representación en complemento a 2?
- b) ¿Qué valor mostraría si se interpreta como número sin signo?

### Problema 6.2
Una dirección de memoria está dada como $\text{0x3FF}_{(16)}$. 
- a) ¿Cuál es su valor en decimal?
- b) ¿Cuántos bits se necesitan para direccionar esta memoria?

### Problema 6.3
Un convertidor analógico-digital (ADC) de 10 bits produce la salida $1100110011_{(2)}$. Si el rango de entrada es 0-5V:
- a) ¿Cuál es el valor digital en decimal?
- b) ¿Qué voltaje representa? (Usar: $V = \frac{Digital}{2^{10}-1} \times 5V$)

### Problema 6.4
Se transmiten datos seriales donde cada byte tiene el formato:
- 1 bit de inicio (siempre 0)
- 8 bits de datos
- 1 bit de paridad par
- 1 bit de stop (siempre 1)

Si se quiere enviar el carácter ASCII 'A' (valor $65_{(10)}$):
- a) Representar el byte de datos en binario
- b) Calcular el bit de paridad par
- c) Escribir la trama completa

---

## Problema Integrador

### Problema 7.1
Diseñar una tabla que muestre los números del 0 al 15 en:
- Decimal
- Binario (4 bits)
- Hexadecimal
- Octal
- BCD
- Código Gray

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios graduado por dificultad
RESPUESTAS: Ver archivo solutions/DD-01-Respuestas.md
DESARROLLOS: Ver carpeta solutions/prob-XX/ para soluciones detalladas
-->
