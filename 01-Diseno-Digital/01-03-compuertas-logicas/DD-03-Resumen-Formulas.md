<!--
::METADATA::
type: reference
topic_id: dd-03-compuertas-logicas
file_id: resumen-formulas-compuertas
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, compuertas, CI, referencia]
search_keywords: "resumen, compuertas, circuitos integrados, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-03-Intro.md)

---

# 📋 Cheatsheet: Compuertas Lógicas

## Símbolos y Tablas

### Compuertas Básicas

```
NOT      AND       OR        NAND      NOR
─[>o]─   ─┬─D─     ─┬─)─     ─┬─D○─    ─┬─)○─
         ─┘       ─┘         ─┘        ─┘

XOR      XNOR      Buffer    Tri-State
─┬═)─    ─┬═)○─    ─[>]─     ─[>]─
─┘       ─┘                    │EN
```

### Tablas de Verdad Rápidas

```
A B│AND OR NAND NOR XOR XNOR
───┼─────────────────────────
0 0│ 0  0   1   1   0   1
0 1│ 0  1   1   0   1   0
1 0│ 0  1   1   0   1   0
1 1│ 1  1   0   0   0   1
```

---

## Conversiones Universales

### Solo NAND

| Función | Implementación |
|---------|----------------|
| NOT A | A NAND A |
| A AND B | (A NAND B) NAND (A NAND B) |
| A OR B | (A NAND A) NAND (B NAND B) |

### Solo NOR

| Función | Implementación |
|---------|----------------|
| NOT A | A NOR A |
| A OR B | (A NOR B) NOR (A NOR B) |
| A AND B | (A NOR A) NOR (B NOR B) |

---

## Circuitos Integrados TTL

| CI | Función | Contenido |
|----|---------|-----------|
| **74LS00** | NAND | 4 × 2-in |
| **74LS02** | NOR | 4 × 2-in |
| **74LS04** | NOT | 6 × inv |
| **74LS08** | AND | 4 × 2-in |
| 74LS10 | NAND | 3 × 3-in |
| 74LS11 | AND | 3 × 3-in |
| 74LS20 | NAND | 2 × 4-in |
| 74LS27 | NOR | 3 × 3-in |
| 74LS30 | NAND | 1 × 8-in |
| **74LS32** | OR | 4 × 2-in |
| **74LS86** | XOR | 4 × 2-in |

---

## Niveles Lógicos

### TTL (5V)

| Parámetro | Valor |
|-----------|-------|
| $V_{IH}$ min | 2.0V |
| $V_{IL}$ max | 0.8V |
| $V_{OH}$ min | 2.4V |
| $V_{OL}$ max | 0.4V |

### CMOS (5V)

| Parámetro | Valor |
|-----------|-------|
| $V_{IH}$ min | 3.5V |
| $V_{IL}$ max | 1.5V |
| $V_{OH}$ min | 4.9V |
| $V_{OL}$ max | 0.1V |

---

## Parámetros Importantes

### Fan-Out

$$\text{Fan-out} = \min\left(\frac{I_{OH}}{I_{IH}}, \frac{I_{OL}}{I_{IL}}\right)$$

**Típico 74LS:** 20

### Margen de Ruido

$$NM_H = V_{OH(min)} - V_{IH(min)} = 0.4V$$
$$NM_L = V_{IL(max)} - V_{OL(max)} = 0.4V$$

### Retardo de Propagación

$$t_p = \frac{t_{pLH} + t_{pHL}}{2}$$

**Típico 74LS:** 10ns

---

## Familias Lógicas

| Familia | Velocidad | Consumo | Notas |
|---------|-----------|---------|-------|
| 74LS | Media | Medio | Estándar |
| 74HC | Alta | Bajo | CMOS |
| 74HCT | Alta | Bajo | CMOS compatible TTL |
| 74F | Muy Alta | Medio | Fast |
| 74ALS | Alta | Bajo | Advanced LS |

---

## Compatibilidad

| De → A | Directo | Solución |
|--------|---------|----------|
| TTL → CMOS | No | Pull-up 4.7kΩ |
| CMOS → TTL | Sí* | Verificar fan-out |
| HC → LS | Sí | - |
| HCT → LS | Sí | - |

---

## Reglas Prácticas

### ⚠️ Entradas No Conectadas

- **TTL:** Actúa como "1" (no recomendado)
- **CMOS:** ¡NUNCA dejar flotantes!

### Desacoplamiento

- Capacitor 0.1µF entre VCC y GND
- Uno por cada CI

### Cálculo de Retardo Total

$$t_{total} = \sum t_{p(compuertas\ en\ ruta\ crítica)}$$

---

## Expresiones Útiles

### SOP a NAND (2 niveles)

$$Y = AB + CD = \overline{\overline{AB} \cdot \overline{CD}}$$

### POS a NOR (2 niveles)

$$Y = (A+B)(C+D) = \overline{\overline{A+B} + \overline{C+D}}$$

---

## Pinout 74LS00 (NAND)

```
     ┌──U──┐
1A ──┤1  14├── VCC
1B ──┤2  13├── 4B
1Y ──┤3  12├── 4A
2A ──┤4  11├── 4Y
2B ──┤5  10├── 3B
2Y ──┤6   9├── 3A
GND ─┤7   8├── 3Y
     └─────┘
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño y laboratorio
-->
