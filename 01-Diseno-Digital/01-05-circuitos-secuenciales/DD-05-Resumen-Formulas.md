<!--
::METADATA::
type: reference
topic_id: dd-05-circuitos-secuenciales
file_id: resumen-formulas-secuenciales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, formulas, secuenciales, flip-flop, FSM]
search_keywords: "resumen, fórmulas, circuitos secuenciales, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-05-Intro.md)

---

# 📋 Cheatsheet: Circuitos Secuenciales

## Latches

### Latch SR (NOR)
| S | R | Q+ |
|---|---|-----|
| 0 | 0 | Q |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | ❌ |

### Latch D
$$Q^+ = D$$ (cuando E=1)

---

## Flip-Flops

### Ecuaciones Características

| FF | Ecuación |
|----|----------|
| D | $Q^+ = D$ |
| JK | $Q^+ = J\overline{Q} + \overline{K}Q$ |
| T | $Q^+ = T \oplus Q$ |
| SR | $Q^+ = S + \overline{R}Q$ |

### Tablas de Excitación

**D:** $D = Q^+$

**JK:**
| Q→Q+ | J | K |
|------|---|---|
| 0→0 | 0 | X |
| 0→1 | 1 | X |
| 1→0 | X | 1 |
| 1→1 | X | 0 |

**T:** $T = Q \oplus Q^+$

---

## Conversiones

| De | A | Conexión |
|----|---|----------|
| JK | D | J=D, K=D̄ |
| D | T | D=T⊕Q |
| JK | T | J=K=T |

---

## Temporización

### Parámetros
- $t_{setup}$: D estable ANTES del flanco
- $t_{hold}$: D estable DESPUÉS del flanco
- $t_{CQ}$: Retardo CLK→Q

### Frecuencia Máxima
$$f_{max} = \frac{1}{t_{CQ} + t_{comb} + t_{setup}}$$

---

## FSM

### Tipos

| Moore | Mealy |
|-------|-------|
| Y = f(Q) | Y = f(Q,X) |
| Salida en estado | Salida en transición |
| Más estados | Menos estados |
| Sin glitches | Respuesta rápida |

### Número de FF
$$n_{FF} = \lceil \log_2(\text{estados}) \rceil$$

---

## Diseño FSM

### Pasos
1. Diagrama de estados
2. Tabla de estados
3. Asignación de códigos
4. Tabla de transición
5. Mapas K → Ecuaciones
6. Implementación

### Codificación One-Hot
Un FF por estado → n estados = n FF

---

## CIs Comunes

| CI | Descripción |
|----|-------------|
| 74LS74 | Dual D FF |
| 74LS76 | Dual JK FF |
| 74LS112 | Dual JK (neg edge) |
| 74LS175 | Quad D FF |
| 74LS273 | Octal D + CLR |

---

## Diagrama de Estados

```
      entrada/salida (Mealy)
           ↓
    ┌────────────┐
    │            │
    ▼   0/0      │
┌──────┐    ┌──────┐
│  S0  │───>│  S1  │
│  /0  │    │  /1  │
└──────┘    └──────┘
  ↑ salida Moore
```

---

## Detector de Secuencia

### "101" Moore
Estados: S0→S1→S2→S3(Z=1)

### Solapamiento
Volver a estado intermedio, no inicial.

---

## Verificación

✓ Estados alcanzables
✓ Sin estados trampa
✓ Reset definido
✓ Setup/hold OK
✓ Estados no usados

---

## Metaestabilidad

Ocurre cuando se viola $t_{setup}$ o $t_{hold}$.
Solución: sincronizadores de 2 etapas.

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño y exámenes
-->
