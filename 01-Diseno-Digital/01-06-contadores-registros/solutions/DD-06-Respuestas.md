<!--
::METADATA::
type: solution
topic_id: dd-06-contadores-registros
file_id: respuestas-contadores-registros
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, verificacion]
search_keywords: "respuestas, soluciones, contadores, registros"
-->

> 🏠 **Navegación:** [← Problemas](../problems/DD-06-Problemas.md)

---

# Respuestas: Contadores y Registros

## Nivel 1: Contadores Asíncronos

### Respuestas 1.1

**a)** Diagrama de tiempo:
- Q0 cambia cada CLK
- Q1 cambia cada 2 CLK
- Q2 cambia cada 4 CLK
- Q3 cambia cada 8 CLK

**b)** $f_{Q3} = \frac{1MHz}{16} = 62.5 kHz$

**c)** Retardo máximo = $4 \times 10ns = 40ns$

### Respuestas 1.2

**a)** 4 flip-flops ($\lceil \log_2 10 \rceil = 4$)

**b)** Estado 1010 (10) activa reset

**c)** Reset = Q3 · Q1 (NAND → R0)

### Respuestas 1.3

**a)** Retardo total = $3 \times 15ns = 45ns$

**b)** $f_{max} = \frac{1}{45ns} = 22.2 MHz$

**c)** Glitches en transiciones como 011→100, 111→000

---

## Nivel 2: Contadores Síncronos

### Respuestas 2.1

**a)** Tabla de transición:
| Q2Q1Q0 | Q2+Q1+Q0+ |
|--------|-----------|
| 000 | 001 |
| 001 | 010 |
| 010 | 011 |
| 011 | 100 |
| 100 | 101 |
| 101 | 110 |
| 110 | 111 |
| 111 | 000 |

**b)** Ecuaciones:
- $D_0 = \overline{Q_0}$
- $D_1 = Q_1 \oplus Q_0$
- $D_2 = Q_2 \oplus (Q_1 \cdot Q_0)$

### Respuestas 2.2

**d)** Estados no usados (6,7) deben ir a estado válido:
- Opción 1: Tratar como don't care
- Opción 2: Forzar transición a 0

### Respuestas 2.3

**a)** Síncrono requiere más compuertas (ANDs para enable)

**b)** Retardo: Síncrono = 1×tpd, Asíncrono = n×tpd

**c)** Frecuencia: Síncrono >> Asíncrono

---

## Nivel 3: Contadores con CI

### Respuestas 3.1

**a)** Módulo 12:
- Detectar Q3Q2 = 11 (cuando cuenta = 12)
- Aplicar LOAD con valor 0000

**b)** RCO (Terminal Count) indica cuenta = 15

### Respuestas 3.2

**a)** Dividir por 16: Conectar QA→CLKB, usar QB-QD

**b)** Dividir por 12: Reset cuando Q3Q2 = 11

**c)** 15 no es factorizable fácilmente en ÷2 × ÷n

### Respuestas 3.3

**a)** Módulo 10: Reset con BORROW cuando DOWN llega a -1 desde 0

**b)** CARRY = overflow arriba, BORROW = overflow abajo

**c)** Cascada: CARRY→UP del siguiente, BORROW→DOWN del siguiente

---

## Nivel 4: Contadores Especiales

### Respuestas 4.1

**b)** Secuencia anillo 4-bit: 1000→0100→0010→0001→1000

**c)** Inicialización: PRESET en FF0, CLEAR en FF1-FF3

### Respuestas 4.2

**a)** Secuencia Johnson 3-bit:
000→100→110→111→011→001→000

**b)** 6 estados válidos (2n)

**c)** Decodificación:
- 000: $\overline{Q_2} \cdot \overline{Q_0}$
- 100: $Q_0 \cdot \overline{Q_1}$
- etc.

### Respuestas 4.3

**c)** Es módulo 4 pero con secuencia no natural (pares)

---

## Nivel 5: Bidireccionales

### Respuestas 5.1

**c)** Con JK:
- $J_0 = K_0 = 1$
- $J_1 = K_1 = (DIR \cdot Q_0) + (\overline{DIR} \cdot \overline{Q_0})$
- $J_2 = K_2 = (DIR \cdot Q_1 \cdot Q_0) + (\overline{DIR} \cdot \overline{Q_1} \cdot \overline{Q_0})$

### Respuestas 5.2

Secuencia especial: Solo cambia 1 bit a la vez
UP: 000→001→011→111→000
DOWN: 111→011→001→000→111

### Respuestas 5.3

**a)** Cargar valor 5 (0101)

**b)** Detectar cuando Q = 12 (1100)

---

## Nivel 6: Registros de Desplazamiento

### Respuestas 6.1

**a)** Si entrada = 1011 (MSB primero):
Después de 4 CLK: Q3Q2Q1Q0 = 1011

**c)** 8 ciclos para un byte

### Respuestas 6.2

**b)** A y B se combinan con AND → permite gating de entrada

**c)** Señal "dato listo": Usar contador de 8 bits, pulso cuando llega a 8

### Respuestas 6.3

**b)** Secuencia: LOAD→8 pulsos de SHIFT

**c)** 9 ciclos totales (1 load + 8 shift)

---

## Nivel 7: Registros Bidireccionales

### Respuestas 7.1

**c)** ×2: Shift Left (0→entrada)
    ÷2: Shift Right (descartar LSB)

### Respuestas 7.2

Usar MUX 4:1 para cada D del FF:
- Entrada 0: Q actual (hold)
- Entrada 1: Q anterior (shift R)
- Entrada 2: Q siguiente (shift L)
- Entrada 3: Dato paralelo

### Respuestas 7.3

Configurar: S1=1, S0=0 (shift left), SL=Q3 (retroalimentación)

---

## Nivel 8: Divisores de Frecuencia

### Respuestas 8.1

**a)** 10 MHz → 1 MHz: ÷10 (contador década)

**b)** 10 MHz → 100 kHz: ÷100 (dos contadores década)

**c)** 10 MHz → 1 Hz: ÷10,000,000 (7 contadores década)

### Respuestas 8.2

**a)** 32768 = $2^{15}$, perfecto para división binaria

**b)** 15 flip-flops en cascada (contador binario de 15 bits)

**c)** Exactamente 15 flip-flops

### Respuestas 8.3

**a)** Factor = 1000000/60 ≈ 16667 (no exacto)

**b)** Alternativa: ÷16666 o ÷16667 alternando

---

## Nivel 9: Aplicaciones

### Respuestas 9.1

**Estructura:**
- Segundos: Contador BCD 0-59 (dos dígitos)
- Minutos: Contador BCD 0-59 (dos dígitos)
- Horas: Contador 0-23

**Cascada:**
- RCO de segundos → Enable de minutos
- RCO de minutos → Enable de horas

### Respuestas 9.2

**Diseño:**
1. Contador de n bits (según rango)
2. Compuerta para ventana de 1 segundo
3. Al fin de ventana, latch el valor y reset

### Respuestas 9.3

**Diseño PWM:**
- Contador de 8 bits (256 pasos)
- Comparador: Contador < Duty → Salida = 1
- Frecuencia: 1kHz × 256 = 256 kHz de reloj

---

## Nivel 10: Integradores

### Respuestas 10.1 (Transmisor Serial)

**Componentes:**
- Registro 10 bits (Start + 8 datos + Stop)
- Contador 0-9 para bits
- FSM: IDLE → TRANSMITTING → IDLE

**Timing para 9600 baud:**
- Período de bit = 1/9600 = 104.17 µs
- Divisor desde reloj principal

### Respuestas 10.2 (Contador con Display)

**Estructura:**
- 4 contadores BCD en cascada
- Decodificadores BCD a 7 segmentos
- Latch entre contador y display
- Reset asíncrono global

### Respuestas 10.3 (Secuenciador)

**Estructura:**
- Contador de anillo de 8 bits
- Selector: Manual (botón) / Auto (clock)
- Modo: Bit para cíclico vs single-shot
- 8 salidas, una activa a la vez

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para verificación de ejercicios
NOTA: Pueden existir soluciones alternativas válidas
-->
