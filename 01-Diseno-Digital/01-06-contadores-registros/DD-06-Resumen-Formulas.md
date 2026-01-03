<!--
::METADATA::
type: reference
topic_id: dd-06-contadores-registros
file_id: resumen-formulas-contadores
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, formulas, contadores, registros]
search_keywords: "resumen, fórmulas, contadores, registros, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-06-Intro.md)

---

# 📋 Cheatsheet: Contadores y Registros

## Contadores: Fórmulas Básicas

### Número de Flip-Flops
$$n = \lceil \log_2 N \rceil$$
donde N = módulo (número de estados)

### División de Frecuencia
$$f_{out} = \frac{f_{in}}{N}$$

### Retardo Asíncrono
$$t_{total} = n \times t_{pd}$$

---

## Tipos de Contadores

| Tipo | Características |
|------|-----------------|
| Asíncrono | CLK solo a FF0, simple, glitches |
| Síncrono | CLK a todos, sin glitches, más rápido |
| Anillo | n FF → n estados, un 1 circula |
| Johnson | n FF → 2n estados, retroalimentación invertida |

---

## Contador Síncrono: Ecuaciones

**Con Flip-Flops T:**
- $T_0 = 1$ (toggle siempre)
- $T_n = \prod_{i=0}^{n-1} Q_i$ (toggle cuando todos anteriores = 1)

**Con Flip-Flops JK:**
- $J_n = K_n = \prod_{i=0}^{n-1} Q_i$

---

## CIs de Contadores

| CI | Tipo | Características |
|----|------|-----------------|
| 74LS90 | Década | ÷2 × ÷5 |
| 74LS93 | Binario | 4-bit async |
| 74LS160 | Década | Sync, load |
| 74LS163 | Binario | Sync, load, enable |
| 74LS193 | Up/Down | Sync, load |

---

## Módulo N (No $2^n$)

### Método Reset
Detectar N → Reset a 0

### Método Load
Detectar N-1 → Cargar 0

---

## Registros de Desplazamiento

| Tipo | Entrada | Salida |
|------|---------|--------|
| SISO | Serial | Serial |
| SIPO | Serial | Paralelo |
| PISO | Paralelo | Serial |
| PIPO | Paralelo | Paralelo |

---

## 74LS194: Modos

| S1 | S0 | Modo |
|----|----|------|
| 0 | 0 | Hold |
| 0 | 1 | Shift Right |
| 1 | 0 | Shift Left |
| 1 | 1 | Load |

---

## CIs de Registros

| CI | Tipo | Bits |
|----|------|------|
| 74LS164 | SIPO | 8 |
| 74LS165 | PISO | 8 |
| 74LS194 | Universal | 4 |
| 74LS299 | Universal | 8 |

---

## Aplicaciones Comunes

| Aplicación | Componente |
|------------|------------|
| Divisor frecuencia | Contador |
| Reloj digital | Contadores BCD cascada |
| UART | PISO + SIPO |
| ×2, ÷2 | Shift L, Shift R |
| Secuenciador | Anillo/Johnson |

---

## Contador de Anillo

**Módulo = n** (n flip-flops)

Secuencia 4-bit:
```
1000 → 0100 → 0010 → 0001 → 1000
```

---

## Contador Johnson

**Módulo = 2n** (n flip-flops)

Secuencia 3-bit:
```
000 → 100 → 110 → 111 → 011 → 001 → 000
```

**Decodificación:** 2 compuertas por estado

---

## Cascada de Contadores

```
CLK → [CNT0]─RCO→[CNT1]─RCO→[CNT2]
         ↓        ↓         ↓
      Unidades  Decenas  Centenas
```

---

## Conversión Serial-Paralelo

**Recibir n bits:**
- n ciclos de CLK
- Bit n-1 (primero) → posición LSB o MSB según diseño

---

## Divisores Comunes

| Entrada | Salida | Divisor |
|---------|--------|---------|
| 1 MHz | 1 kHz | ÷1000 |
| 32.768 kHz | 1 Hz | ÷32768 ($2^{15}$) |
| 10 MHz | 1 Hz | ÷10M |

---

## Errores Comunes

❌ Ignorar glitches en asíncronos
❌ No manejar estados no usados
❌ Olvidar inicialización
❌ Confundir SIPO vs PISO
❌ Cascada incorrecta (RCO→ENT)

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño y exámenes
-->
