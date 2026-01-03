<!--
::METADATA::
type: detailed_solution
topic_id: dd-05-circuitos-secuenciales
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, flip-flop, secuencial, tabla-caracteristica]
-->

> 🏠 **Navegación:** [← Respuestas](../DD-05-Respuestas.md) | [Problema 1.2 →](./DD-05-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Dado un flip-flop D, completar la tabla de estado y dibujar el diagrama de tiempos para la secuencia de entrada D = {1, 0, 1, 1, 0}.

---

## Paso 1: Características del Flip-Flop D

| Propiedad | Valor |
|-----------|-------|
| Ecuación característica | $Q^+ = D$ |
| Activación | Flanco positivo de CLK |
| Función | La salida copia la entrada en cada flanco |

### Tabla Característica

| D | $Q^+$ (siguiente estado) |
|:-:|:------------------------:|
| 0 | 0 |
| 1 | 1 |

---

## Paso 2: Análisis de la Secuencia

Asumimos estado inicial $Q_0 = 0$

| Ciclo | n | D | Q (actual) | Q⁺ (siguiente) |
|:-----:|:-:|:-:|:----------:|:--------------:|
| 1 | 0 | 1 | 0 | **1** |
| 2 | 1 | 0 | 1 | **0** |
| 3 | 2 | 1 | 0 | **1** |
| 4 | 3 | 1 | 1 | **1** |
| 5 | 4 | 0 | 1 | **0** |

### Secuencia de salida Q:
$$Q = \{0 \rightarrow 1 \rightarrow 0 \rightarrow 1 \rightarrow 1 \rightarrow 0\}$$

---

## Paso 3: Diagrama de Tiempos

```
        │    │    │    │    │    │
CLK  ___┌────┐____┌────┐____┌────┐____┌────┐____┌────┐____
        │    │    │    │    │    │    │    │    │    │
        └────┘    └────┘    └────┘    └────┘    └────┘

         n=0      n=1      n=2      n=3      n=4
        ────────────────────────────────────────────────
D    ___┌─────────┐         ┌──────────────────┐
        │         │         │                  │
        │    1    │    0    │    1    │    1   │    0
        └─────────┘─────────└─────────┴────────┘─────────

        ────────────────────────────────────────────────
Q    ───┐         ┌─────────┐         ┌──────────────┐
        │         │         │         │              │
   0    │    1    │    0    │    1    │       1      │   0
        └─────────┘─────────└─────────┴──────────────┴───
        ↑         ↑         ↑         ↑              ↑
        Flanco    Flanco    Flanco    Flanco         Flanco
```

---

## Paso 4: Análisis del Comportamiento

### Observaciones:

1. **Ciclo 1 (n=0):** D=1, Q pasa de 0 a 1 en el flanco
2. **Ciclo 2 (n=1):** D=0, Q pasa de 1 a 0 en el flanco
3. **Ciclo 3 (n=2):** D=1, Q pasa de 0 a 1 en el flanco
4. **Ciclo 4 (n=3):** D=1, Q permanece en 1 (sin cambio)
5. **Ciclo 5 (n=4):** D=0, Q pasa de 1 a 0 en el flanco

### Patrón identificado:
- Q sigue a D con un retardo de 1 ciclo de reloj
- La salida solo cambia en los flancos positivos de CLK

---

## Paso 5: Timing Detallado

| Parámetro | Símbolo | Descripción |
|-----------|---------|-------------|
| Setup time | $t_{su}$ | D debe ser estable antes del flanco |
| Hold time | $t_h$ | D debe mantenerse después del flanco |
| Clock-to-Q | $t_{CQ}$ | Retardo desde flanco hasta Q válido |

```
         tsu    th
         ←──→ ←──→
D    ────────────────
              │
CLK  _________↑______
                 │
              tCQ│
                 ↓
Q    ────────────────
```

---

## Paso 6: Verificación

### Método: Ecuación característica
Para cada ciclo, verificar $Q^+ = D$:

| n | D | Q actual | $Q^+ = D$ | Verificado |
|:-:|:-:|:--------:|:---------:|:----------:|
| 0 | 1 | 0 | 1 | ✓ |
| 1 | 0 | 1 | 0 | ✓ |
| 2 | 1 | 0 | 1 | ✓ |
| 3 | 1 | 1 | 1 | ✓ |
| 4 | 0 | 1 | 0 | ✓ |

---

## Paso 7: Implementación del FF-D con NAND

```
         ┌─────┐
    D ───┤NAND1├───┬───┐
         └──┬──┘   │   │
            │      │   │   ┌─────┐
CLK ────────┼──────┼───┼───┤     │
            │      │   │   │NAND3├───── Q
            │   ┌──┴───┴───┤     │
            │   │          └─────┘
            │   │
         ┌──┴───┤          ┌─────┐
         │NAND2 │      ┌───┤     │
         └──┬───┘      │   │NAND4├───── Q̄
            │          │   │     │
            └──────────┴───┤     │
                           └─────┘
```

---

## Conceptos Clave Aplicados

1. **Elemento de memoria:** El FF-D almacena 1 bit de información
2. **Sincronismo:** Los cambios ocurren solo con el reloj
3. **Retardo inherente:** Q siempre está un ciclo "atrás" de D
4. **Requisitos temporales:** Setup y hold deben respetarse

---

## Resumen

| Propiedad | Valor |
|-----------|-------|
| Entrada D | {1, 0, 1, 1, 0} |
| Salida Q | {0→1→0→1→1→0} |
| Cambios de estado | 4 transiciones |
| Estado final | Q = 0 |

---

## Aplicaciones del FF-D

1. **Registros:** Almacenamiento de datos de n bits
2. **Sincronización:** Eliminar metaestabilidad
3. **Retardo:** Crear delays de 1 ciclo de reloj
4. **División de frecuencia:** Con retroalimentación $D = \bar{Q}$

---

> 💡 **Tip:** El FF-D es el más utilizado en diseño digital por su comportamiento predecible: "lo que entra por D, sale por Q en el siguiente flanco".
