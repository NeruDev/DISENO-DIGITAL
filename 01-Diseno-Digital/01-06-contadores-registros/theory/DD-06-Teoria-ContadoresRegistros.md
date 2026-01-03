<!--
::METADATA::
type: theory
topic_id: dd-06-contadores-registros
file_id: teoria-contadores-registros
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [contador, registro, desplazamiento, sincronico, asincronico]
search_keywords: "contadores, registros, desplazamiento, shift register, ripple counter"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-06-Intro.md) | [Métodos →](../methods/DD-06-Metodos-Contadores.md)

---

# Contadores y Registros

## 1. Contadores

### 1.1 Definición

Un **contador** es un circuito secuencial que sigue una secuencia de estados predeterminada, generalmente en respuesta a pulsos de reloj.

**Módulo:** Número de estados distintos antes de repetir.
$$\text{Módulo } N \Rightarrow \text{Cuenta } 0 \text{ a } N-1$$

### 1.2 Clasificación

| Criterio | Tipos |
|----------|-------|
| Sincronización | Síncrono / Asíncrono |
| Dirección | Ascendente / Descendente / Bidireccional |
| Módulo | Binario ($2^n$) / Década (10) / Arbitrario |

---

## 2. Contadores Asíncronos (Ripple)

### 2.1 Concepto

El reloj solo se aplica al primer flip-flop. Cada FF dispara al siguiente.

```
CLK ─┬─[T FF]─Q0─┬─[T FF]─Q1─┬─[T FF]─Q2
     │    T=1    │    T=1    │    T=1
     │           │           │
     └─ LSB      └─          └─ MSB
```

### 2.2 Contador Ascendente 4 bits

Usando flip-flops T (o JK con J=K=1):

```
CLK ──>CLK[FF0]─Q0──>CLK[FF1]─Q1──>CLK[FF2]─Q2──>CLK[FF3]─Q3
         │             │             │             │
         └─bit 0       └─bit 1       └─bit 2       └─bit 3
```

**Secuencia:** 0000 → 0001 → 0010 → ... → 1111 → 0000

### 2.3 Contador Descendente

Conectar $\overline{Q}$ al CLK del siguiente FF.

```
CLK ──>CLK[FF0]─Q̄0──>CLK[FF1]─Q̄1──>CLK[FF2]
```

**Secuencia:** 1111 → 1110 → 1101 → ... → 0000 → 1111

### 2.4 Retardo de Propagación

$$t_{total} = n \times t_{pd}$$

**Problema:** Glitches durante las transiciones. A mayor número de bits, peor.

### 2.5 CI Típico: 74LS93

- Contador binario de 4 bits
- Dividido en contador de 1 bit y contador de 3 bits
- Entradas de reset

---

## 3. Contadores Síncronos

### 3.1 Concepto

Todos los flip-flops comparten el mismo reloj. Transiciones simultáneas.

### 3.2 Contador Síncrono de 4 bits

```
        ┌───────────────────────────────────┐
        │       ┌───────────────────┐       │
        │       │       ┌───────┐   │       │
        │       │       │       │   │       │
CLK ────┼───────┼───────┼───────┼───┼───────┼───
        │       │       │       │   │       │
     [J FF0] [J FF1] [J FF2] [J FF3]│       │
        │       │       │       │   │       │
J0=1────┤       │       │       │   │       │
K0=1────┤       │       │       │   │       │
        │       │       │       │   │       │
   Q0 ──┴─[AND]─┼── J1 ─┘       │   │       │
                │       │       │   │       │
   Q0Q1 ────────┴─[AND]─┼── J2 ─┘   │       │
                        │           │       │
   Q0Q1Q2 ──────────────┴─[AND]─── J3 ──────┘
```

**Ecuaciones:**
- $J_0 = K_0 = 1$ (toggle siempre)
- $J_1 = K_1 = Q_0$
- $J_2 = K_2 = Q_0 Q_1$
- $J_3 = K_3 = Q_0 Q_1 Q_2$

### 3.3 Ventajas sobre Asíncrono

| Síncrono | Asíncrono |
|----------|-----------|
| Sin glitches | Glitches posibles |
| Más rápido para n grande | Más simple |
| Retardo = 1 × $t_{pd}$ | Retardo = n × $t_{pd}$ |

### 3.4 CI Típico: 74LS163

- Contador síncrono de 4 bits
- Carga paralela
- Enable (ENT, ENP)
- Clear síncrono
- Carry output (RCO)

---

## 4. Contadores de Módulo N

### 4.1 Método con Reset

Detectar estado N y resetear a 0.

**Ejemplo: Módulo 6 (0-5)**

```
Q2Q1Q0 = 110 (6) → RESET
```

Circuito: NAND(Q2, Q1) → CLR

**Problema:** Glitch momentáneo al estado 6.

### 4.2 Método con Carga

Usar carga paralela para cargar valor inicial.

**Ejemplo: Módulo 6 con 74LS163**

Cuando cuenta = 5, cargar 0 en el siguiente ciclo.

### 4.3 Diseño desde Cero (FSM)

Diseñar como máquina de estados con N estados.

---

## 5. Contadores BCD (Década)

### 5.1 Concepto

Cuenta de 0 a 9 (módulo 10).

**Secuencia:** 0000 → 0001 → ... → 1001 → 0000

### 5.2 CI Típico: 74LS90

- Contador de década
- Puede configurarse como ÷2 y ÷5
- Reset a 0 o a 9

### 5.3 Contadores en Cascada

Para contar más de 9, conectar varios contadores BCD:

```
CLK ─>[BCD 0-9]─RCO─>[BCD 0-9]─RCO─>[BCD 0-9]
       unidades     decenas       centenas
```

---

## 6. Contadores Up/Down

### 6.1 Control de Dirección

Entrada UP/DOWN controla la dirección de conteo.

```
UP=1: Cuenta ascendente
UP=0: Cuenta descendente
```

### 6.2 Implementación

```
J = (UP · Q_{n-1}) + (DOWN · Q̄_{n-1})
```

### 6.3 CI Típico: 74LS193

- Contador binario de 4 bits
- Entradas separadas UP y DOWN
- Carga paralela
- Salidas BORROW y CARRY

---

## 7. Contadores en Anillo

### 7.1 Contador de Anillo Simple

Solo un 1 circula por el registro.

**4 bits:** 1000 → 0100 → 0010 → 0001 → 1000

```
      ┌──────────────────────────────────┐
      │                                  │
      └──D[FF0]──Q0──D[FF1]──Q1──D[FF2]──Q2──D[FF3]──Q3
              CLK ────────────────────────────────────
```

**Módulo = n** (número de flip-flops)

### 7.2 Contador Johnson (Anillo Torcido)

El complemento de la última salida se retroalimenta.

**4 bits:** 0000 → 1000 → 1100 → 1110 → 1111 → 0111 → 0011 → 0001 → 0000

**Módulo = 2n**

### 7.3 Decodificación

| Anillo | Johnson |
|--------|---------|
| Una compuerta por estado | Dos entradas por estado |
| n FF para n estados | n FF para 2n estados |

---

## 8. Registros de Desplazamiento

### 8.1 Definición

Circuito que mueve bits de posición con cada pulso de reloj.

### 8.2 Tipos

| Tipo | Descripción |
|------|-------------|
| SISO | Serial In, Serial Out |
| SIPO | Serial In, Parallel Out |
| PISO | Parallel In, Serial Out |
| PIPO | Parallel In, Parallel Out |

### 8.3 SISO (Serial In, Serial Out)

```
SER_IN ──D[FF0]──D[FF1]──D[FF2]──D[FF3]── SER_OUT
              CLK ───────────────────────
```

**Aplicación:** Línea de retardo de n ciclos.

### 8.4 SIPO (Serial In, Parallel Out)

```
SER_IN ──D[FF0]──D[FF1]──D[FF2]──D[FF3]
            │       │       │       │
            Q0      Q1      Q2      Q3
```

**Aplicación:** Conversión serial a paralelo.

### 8.5 PISO (Parallel In, Serial Out)

```
D0  D1  D2  D3  (Carga paralela)
│   │   │   │
[FF0]──[FF1]──[FF2]──[FF3]── SER_OUT
```

**Aplicación:** Conversión paralelo a serial.

### 8.6 Bidireccional

Puede desplazar a izquierda o derecha según señal de control.

---

## 9. Circuitos Integrados de Registros

### 9.1 74LS164 (SIPO)

- 8 bits
- Entrada serial (2 ANDed)
- Clear asíncrono
- Salidas paralelas

### 9.2 74LS165 (PISO)

- 8 bits
- Carga paralela
- Entrada serial
- Salida serial (Q7, Q̄7)

### 9.3 74LS194 (Universal)

- 4 bits
- Bidireccional
- Modos: Hold, Shift Left, Shift Right, Load
- Entradas S0, S1 controlan modo

| S1 | S0 | Modo |
|----|----|------|
| 0 | 0 | Hold |
| 0 | 1 | Shift Right |
| 1 | 0 | Shift Left |
| 1 | 1 | Parallel Load |

### 9.4 74LS299 (8-bit Universal)

- 8 bits
- Bidireccional
- Tri-state outputs

---

## 10. Aplicaciones

### 10.1 Divisor de Frecuencia

Contador de n bits divide frecuencia por $2^n$.

$$f_{out} = \frac{f_{CLK}}{2^n}$$

### 10.2 Generador de Secuencias

Usar registro de desplazamiento con retroalimentación (LFSR).

### 10.3 Conversión Serial-Paralelo

Comunicaciones: recibir bits seriales, salida en paralelo.

### 10.4 Multiplicación/División por 2

- Shift Left = × 2
- Shift Right = ÷ 2

---

## 11. Tabla Resumen de CIs

| CI | Tipo | Descripción |
|----|------|-------------|
| 74LS90 | Contador | Década (÷2 × ÷5) |
| 74LS93 | Contador | Binario 4 bits asíncrono |
| 74LS160 | Contador | Década síncrono |
| 74LS163 | Contador | Binario 4 bits síncrono |
| 74LS193 | Contador | Up/Down binario |
| 74LS164 | Registro | 8-bit SIPO |
| 74LS165 | Registro | 8-bit PISO |
| 74LS194 | Registro | 4-bit universal |
| 74LS299 | Registro | 8-bit universal |

---

## Referencias

- Mano, M. M. (2013). *Digital Design*. Pearson.
- Tocci, R. J. (2011). *Digital Systems*. Pearson.

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 01-05 Circuitos Secuenciales
CONEXIONES: Base para diseño de procesadores, comunicaciones, temporizadores
ERRORES_COMUNES: Glitches en asíncronos, desbordamiento no manejado, inicialización
-->
