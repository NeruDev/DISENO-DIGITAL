<!--
::METADATA::
type: theory
topic_id: dd-03-compuertas-logicas
file_id: teoria-compuertas-logicas
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [compuertas, AND, OR, NOT, NAND, NOR, XOR, TTL, CMOS]
search_keywords: "compuertas lógicas, AND, OR, NOT, NAND, NOR, TTL, CMOS, circuito integrado"
-->

> 🏠 **Navegación:** [← Volver al Índice](../01-03-Intro.md) | [Métodos →](../methods/DD-03-Metodos-Analisis.md)

---

# Compuertas Lógicas

## 1. Introducción

Las **compuertas lógicas** son los bloques fundamentales de construcción de todos los circuitos digitales. Son dispositivos electrónicos que implementan funciones booleanas básicas.

---

## 2. Compuertas Básicas

### 2.1 Compuerta NOT (Inversor)

**Función:** $Y = \overline{A}$

**Símbolo:**
```
      ┌───┐
A ────┤   ├○──── Y
      └───┘
```

**Tabla de Verdad:**

| A | Y |
|---|---|
| 0 | 1 |
| 1 | 0 |

**Características:**
- 1 entrada, 1 salida
- CI típico: 74LS04 (6 inversores)

---

### 2.2 Compuerta AND

**Función:** $Y = A \cdot B$

**Símbolo:**
```
A ────┬───┐
      │   │
      │   ├──── Y
      │   │
B ────┴───┘
```

**Tabla de Verdad:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Características:**
- Salida es 1 solo si TODAS las entradas son 1
- CI típico: 74LS08 (4 AND de 2 entradas)
- También disponible: 74LS11 (3 AND de 3 entradas)

---

### 2.3 Compuerta OR

**Función:** $Y = A + B$

**Símbolo:**
```
A ────┬───╲
      │    ╲
      │     ╲──── Y
      │    ╱
B ────┴───╱
```

**Tabla de Verdad:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Características:**
- Salida es 1 si AL MENOS una entrada es 1
- CI típico: 74LS32 (4 OR de 2 entradas)

---

## 3. Compuertas Universales

### 3.1 Compuerta NAND

**Función:** $Y = \overline{A \cdot B}$

**Símbolo:**
```
A ────┬───┐
      │   │
      │   ├○──── Y
      │   │
B ────┴───┘
```

**Tabla de Verdad:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Características:**
- **Compuerta Universal:** Puede implementar cualquier función lógica
- CI típico: 74LS00 (4 NAND de 2 entradas)
- También: 74LS10 (3 NAND de 3 entradas), 74LS20 (2 NAND de 4 entradas)

**Equivalencias con NAND:**
```
NOT:  Y = A NAND A
AND:  Y = (A NAND B) NAND (A NAND B)
OR:   Y = (A NAND A) NAND (B NAND B)
```

---

### 3.2 Compuerta NOR

**Función:** $Y = \overline{A + B}$

**Símbolo:**
```
A ────┬───╲
      │    ╲
      │     ╲○──── Y
      │    ╱
B ────┴───╱
```

**Tabla de Verdad:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

**Características:**
- **Compuerta Universal:** Puede implementar cualquier función lógica
- CI típico: 74LS02 (4 NOR de 2 entradas)

**Equivalencias con NOR:**
```
NOT:  Y = A NOR A
OR:   Y = (A NOR B) NOR (A NOR B)
AND:  Y = (A NOR A) NOR (B NOR B)
```

---

## 4. Compuertas Especiales

### 4.1 Compuerta XOR (OR Exclusivo)

**Función:** $Y = A \oplus B = A\overline{B} + \overline{A}B$

**Símbolo:**
```
A ────┬───╲╲
      │    ╲╲
      │     ╲╲──── Y
      │    ╱╱
B ────┴───╱╱
```

**Tabla de Verdad:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Características:**
- Salida es 1 cuando las entradas son DIFERENTES
- Útil para: comparadores, sumadores, detectores de paridad
- CI típico: 74LS86 (4 XOR de 2 entradas)

---

### 4.2 Compuerta XNOR (Equivalencia)

**Función:** $Y = A \odot B = AB + \overline{A}\overline{B}$

**Símbolo:**
```
A ────┬───╲╲
      │    ╲╲
      │     ╲╲○──── Y
      │    ╱╱
B ────┴───╱╱
```

**Tabla de Verdad:**

| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Características:**
- Salida es 1 cuando las entradas son IGUALES
- Útil para: comparadores de igualdad
- CI típico: 74LS266 (4 XNOR de 2 entradas)

---

## 5. Buffer y Tri-State

### 5.1 Buffer

**Función:** $Y = A$

**Símbolo:**
```
      ┌───┐
A ────┤   ├──── Y
      └───┘
```

**Uso:**
- Amplificación de señal
- Regeneración de niveles lógicos
- Aislamiento de etapas
- CI típico: 74LS244 (8 buffers)

### 5.2 Buffer Tri-State

**Función:** $Y = A$ cuando $EN = 1$, alta impedancia cuando $EN = 0$

**Símbolo:**
```
       EN
        │
      ┌─┴─┐
A ────┤   ├──── Y
      └───┘
```

**Estados:**

| EN | A | Y |
|----|---|---|
| 0 | X | Z (alta impedancia) |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Uso:**
- Conexión a buses compartidos
- CI típico: 74LS244, 74LS245

---

## 6. Familias Lógicas

### 6.1 TTL (Transistor-Transistor Logic)

| Subfamilia | Prefijo | Velocidad | Consumo |
|------------|---------|-----------|---------|
| Estándar | 74xx | Media | Alto |
| Low Power | 74Lxx | Baja | Bajo |
| Schottky | 74Sxx | Alta | Alto |
| Low Power Schottky | 74LSxx | Media-Alta | Medio |
| Advanced Low Power Schottky | 74ALSxx | Alta | Bajo |
| Fast | 74Fxx | Muy Alta | Medio |

**Niveles Lógicos TTL:**
| Parámetro | Mín | Máx |
|-----------|-----|-----|
| $V_{IH}$ (entrada alta) | 2.0V | 5.0V |
| $V_{IL}$ (entrada baja) | 0V | 0.8V |
| $V_{OH}$ (salida alta) | 2.4V | - |
| $V_{OL}$ (salida baja) | - | 0.4V |

### 6.2 CMOS (Complementary Metal-Oxide Semiconductor)

| Subfamilia | Prefijo | Características |
|------------|---------|-----------------|
| Serie 4000 | CD4xxx | Bajo consumo, lento |
| HC | 74HCxx | Alta velocidad CMOS |
| HCT | 74HCTxx | Compatible TTL |
| AC | 74ACxx | Avanzado CMOS |
| ACT | 74ACTxx | Avanzado compatible TTL |

**Niveles Lógicos CMOS (5V):**
| Parámetro | Mín | Máx |
|-----------|-----|-----|
| $V_{IH}$ | 3.5V | 5.0V |
| $V_{IL}$ | 0V | 1.5V |
| $V_{OH}$ | 4.9V | - |
| $V_{OL}$ | - | 0.1V |

---

## 7. Parámetros Importantes

### 7.1 Tiempos de Propagación

- **$t_{pLH}$:** Retardo de bajo a alto
- **$t_{pHL}$:** Retardo de alto a bajo
- **$t_p$:** Promedio de ambos

### 7.2 Fan-Out

Número máximo de entradas que puede manejar una salida.

**Cálculo:**
$$\text{Fan-out} = \min\left(\frac{I_{OH}}{I_{IH}}, \frac{I_{OL}}{I_{IL}}\right)$$

### 7.3 Fan-In

Número de entradas de una compuerta. Afecta la carga sobre la etapa anterior.

### 7.4 Margen de Ruido

$$NM_H = V_{OH(min)} - V_{IH(min)}$$
$$NM_L = V_{IL(max)} - V_{OL(max)}$$

---

## 8. Circuitos Integrados Comunes

| CI | Función | Contenido |
|----|---------|-----------|
| 74LS00 | NAND | 4 × 2 entradas |
| 74LS02 | NOR | 4 × 2 entradas |
| 74LS04 | NOT | 6 inversores |
| 74LS08 | AND | 4 × 2 entradas |
| 74LS10 | NAND | 3 × 3 entradas |
| 74LS11 | AND | 3 × 3 entradas |
| 74LS20 | NAND | 2 × 4 entradas |
| 74LS21 | AND | 2 × 4 entradas |
| 74LS27 | NOR | 3 × 3 entradas |
| 74LS30 | NAND | 1 × 8 entradas |
| 74LS32 | OR | 4 × 2 entradas |
| 74LS86 | XOR | 4 × 2 entradas |

---

## 9. Consideraciones Prácticas

### 9.1 Entradas No Utilizadas

- **TTL:** Dejar flotantes actúa como "1" (no recomendado)
- **CMOS:** **NUNCA** dejar flotantes (riesgo de daño)
- **Solución:** Conectar a VCC o GND según función

### 9.2 Desacoplamiento

- Usar capacitores de 0.1µF entre VCC y GND
- Uno por cada CI, lo más cerca posible

### 9.3 Compatibilidad TTL-CMOS

| De | A | Solución |
|----|---|----------|
| TTL | CMOS | Pull-up 4.7kΩ |
| CMOS | TTL | Directa (verificar fan-out) |

---

## Referencias

- Texas Instruments. TTL Logic Data Book.
- Tocci, R. J. (2017). *Digital Systems*. Pearson.

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: 01-02 Álgebra Booleana
CONEXIONES: Base para circuitos combinacionales y secuenciales
ERRORES_COMUNES: Entradas CMOS flotantes, incompatibilidad de familias
-->
