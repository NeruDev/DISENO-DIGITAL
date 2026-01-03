<!--
::METADATA::
type: detailed_solution
topic_id: dd-07-memorias
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, memoria, ROM, decodificador]
-->

> 🏠 **Navegación:** [← Respuestas](../DD-07-Respuestas.md) | [Problema 1.2 →](./DD-07-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Diseñar una ROM de 8×4 bits que implemente la función BCD a 7-segmentos (dígitos 0-7 únicamente).

---

## Paso 1: Especificación de la ROM

### Parámetros
| Parámetro | Valor |
|-----------|-------|
| Direcciones | 8 ($2^3$) |
| Bits de dirección | 3 ($A_2 A_1 A_0$) |
| Ancho de palabra | 4 bits ($D_3 D_2 D_1 D_0$) |
| Capacidad total | 8 × 4 = 32 bits |

### Diagrama de bloques
```
         ┌─────────────┐
   A2 ───┤             ├─── D3
   A1 ───┤  ROM 8×4    ├─── D2
   A0 ───┤             ├─── D1
         │             ├─── D0
         └─────────────┘
```

---

## Paso 2: Display de 7 Segmentos

### Disposición de segmentos
```
      ─── a ───
     │         │
     f         b
     │         │
      ─── g ───
     │         │
     e         c
     │         │
      ─── d ───
```

### Codificación elegida
Para este problema, usamos solo 4 salidas para simplificar:
- $D_3$ = segmento a
- $D_2$ = segmento b
- $D_1$ = segmento c
- $D_0$ = segmento d

---

## Paso 3: Tabla de Contenido de la ROM

| Dirección | Dígito | a | b | c | d | $D_3D_2D_1D_0$ | Hex |
|:---------:|:------:|:-:|:-:|:-:|:-:|:--------------:|:---:|
| 000 | 0 | 1 | 1 | 1 | 1 | 1111 | F |
| 001 | 1 | 0 | 1 | 1 | 0 | 0110 | 6 |
| 010 | 2 | 1 | 1 | 0 | 1 | 1101 | D |
| 011 | 3 | 1 | 1 | 1 | 1 | 1111 | F |
| 100 | 4 | 0 | 1 | 1 | 0 | 0110 | 6 |
| 101 | 5 | 1 | 0 | 1 | 1 | 1011 | B |
| 110 | 6 | 1 | 0 | 1 | 1 | 1011 | B |
| 111 | 7 | 1 | 1 | 1 | 0 | 1110 | E |

---

## Paso 4: Implementación con Decoder + OR

### Arquitectura

```
         ┌───────────┐
   A2 ───┤           ├─ 0 ──┬──────┬──────┬──────┐
   A1 ───┤  DECODER  ├─ 1 ──┼──┬───┼──┬───┼──────┤
   A0 ───┤   3:8     ├─ 2 ──┤  │   │  │   │      │
         │           ├─ 3 ──┼──┼───┤  │   ├──────┤
         │           ├─ 4 ──│  ├───┼──┤   │      │
         │           ├─ 5 ──┤  │   ├──┤   ├──────┤
         │           ├─ 6 ──┤  │   ├──┤   ├──────┤
         │           ├─ 7 ──┤  ├───┤  │   │      │
         └───────────┘      │  │   │  │   │      │
                            │  │   │  │   │      │
                           ┌▼──▼┐ ┌▼──▼┐ ┌▼─────▼┐
                           │ OR │ │ OR │ │  OR   │
                           └──┬─┘ └──┬─┘ └───┬───┘
                              │      │       │
                             D3     D2      D1    D0
```

### Ecuaciones de cada salida

$$D_3 = \sum(0, 2, 3, 5, 6, 7) = m_0 + m_2 + m_3 + m_5 + m_6 + m_7$$
$$D_2 = \sum(0, 1, 2, 3, 4, 7) = m_0 + m_1 + m_2 + m_3 + m_4 + m_7$$
$$D_1 = \sum(0, 1, 3, 4, 5, 6, 7) = m_0 + m_1 + m_3 + m_4 + m_5 + m_6 + m_7$$
$$D_0 = \sum(0, 2, 3, 5, 6) = m_0 + m_2 + m_3 + m_5 + m_6$$

---

## Paso 5: Matriz de ROM (Fusibles)

La ROM se implementa como una matriz de diodos/transistores:

```
             D3   D2   D1   D0
             │    │    │    │
Línea 0 ─────●────●────●────●───  (0: 1111)
             │    │    │    │
Línea 1 ─────○────●────●────○───  (1: 0110)
             │    │    │    │
Línea 2 ─────●────●────○────●───  (2: 1101)
             │    │    │    │
Línea 3 ─────●────●────●────●───  (3: 1111)
             │    │    │    │
Línea 4 ─────○────●────●────○───  (4: 0110)
             │    │    │    │
Línea 5 ─────●────○────●────●───  (5: 1011)
             │    │    │    │
Línea 6 ─────●────○────●────●───  (6: 1011)
             │    │    │    │
Línea 7 ─────●────●────●────○───  (7: 1110)

● = Conexión (fusible intacto / diodo presente)
○ = Sin conexión (fusible quemado)
```

---

## Paso 6: Tipos de ROM Aplicables

| Tipo | Programación | Uso |
|------|--------------|-----|
| Mask ROM | Fábrica | Alto volumen |
| PROM | Una vez | Prototipos |
| EPROM | UV | Desarrollo |
| EEPROM | Eléctrica | Actualizable |
| Flash | Eléctrica (bloques) | Firmware |

---

## Paso 7: Verificación

### Prueba para dirección 101 (dígito 5)

1. **Entrada:** $A_2A_1A_0 = 101$
2. **Decodificador:** Activa línea 5
3. **Conexiones en línea 5:** D3=1, D2=0, D1=1, D0=1
4. **Salida:** 1011₂ = B₁₆

### Verificación visual del dígito 5:
```
  ─── a ───     ← D3=1 ✓
 │             
 f         
 │         
  ─── g ───     
             │
         c   ← D1=1 ✓
             │
  ─── d ───     ← D0=1 ✓
```
Corresponde correctamente al dígito 5.

---

## Resumen

| Característica | Valor |
|----------------|-------|
| Tamaño ROM | 8 × 4 bits |
| Bits de dirección | 3 |
| Bits de datos | 4 |
| Conexiones activas | 24 de 32 (75%) |
| Implementación | Decoder 3:8 + ORs |

---

## Conceptos Clave Aplicados

1. **ROM como tabla:** Cada dirección contiene un valor fijo
2. **Decodificador:** Selecciona una línea por dirección
3. **Matriz programable:** Define el contenido de la ROM
4. **Implementación de funciones:** ROM puede implementar cualquier función combinacional

---

## Extensión: ROM Completa para 7 Segmentos

Para display completo de 7 segmentos (dígitos 0-9):

| Tamaño requerido | 16 × 7 bits |
|------------------|-------------|
| Direcciones | 16 (4 bits BCD) |
| Salidas | 7 (a-g) |
| Don't cares | Direcciones 10-15 |

---

> 💡 **Tip:** Una ROM de $2^n \times m$ bits puede implementar **m funciones** de **n variables** simultáneamente.
