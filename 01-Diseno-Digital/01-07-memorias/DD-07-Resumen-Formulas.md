<!--
::METADATA::
type: reference
topic_id: dd-07-memorias
file_id: resumen-formulas-memorias
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, formulas, memorias, RAM, ROM]
search_keywords: "resumen, fórmulas, memorias, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./01-07-Intro.md)

---

# 📋 Cheatsheet: Memorias

## Fórmulas Básicas

### Capacidad
$$\text{Ubicaciones} = 2^n$$
$$\text{Capacidad (bits)} = 2^n \times m$$

donde n = líneas de dirección, m = bits por palabra

### Notación
- 1K = 1024 = $2^{10}$
- 1M = $2^{20}$
- 1G = $2^{30}$

---

## Tipos de Memoria

| Tipo | Volátil | R/W | Uso |
|------|---------|-----|-----|
| SRAM | Sí | R/W | Cache |
| DRAM | Sí | R/W | RAM principal |
| ROM | No | R | Firmware fijo |
| PROM | No | R (1 prog) | Prototipos |
| EPROM | No | R (reprog UV) | Desarrollo |
| EEPROM | No | R/W | Config |
| Flash | No | R/W | Almacenamiento |

---

## Señales de Control

### SRAM Típica
| Pin | Función |
|-----|---------|
| $\overline{CS}$ | Chip Select |
| $\overline{OE}$ | Output Enable |
| $\overline{WE}$ | Write Enable |

### Ciclo Lectura
$$\overline{CS} = 0, \overline{OE} = 0, \overline{WE} = 1$$

### Ciclo Escritura
$$\overline{CS} = 0, \overline{OE} = 1, \overline{WE} = 0$$

---

## CIs Comunes

### ROM/EPROM
| CI | Capacidad |
|----|-----------|
| 2716 | 2K × 8 |
| 2732 | 4K × 8 |
| 2764 | 8K × 8 |
| 27128 | 16K × 8 |
| 27256 | 32K × 8 |

### SRAM
| CI | Capacidad |
|----|-----------|
| 6116 | 2K × 8 |
| 6264 | 8K × 8 |
| 62256 | 32K × 8 |

---

## Expansión

### Más ubicaciones (palabras)
- Usar decodificador para CS
- Buses de datos en paralelo

### Más bits (palabra ancha)
- Direcciones en paralelo
- Cada chip maneja grupo de bits

### Chips necesarios
$$\text{Total} = \frac{\text{Direcciones necesarias}}{\text{Direcciones por chip}} \times \frac{\text{Bits palabra}}{\text{Bits por chip}}$$

---

## Decodificación

### Fórmula Rango
$$\text{Rango} = \frac{2^{\text{bits totales}}}{2^{\text{bits decodificados}}}$$

### Ejemplo 64K → 4 bloques
- 16 bits totales
- 2 bits superiores decodificados
- Bloques de 16K cada uno

---

## DRAM

### Refresh
- Típico: cada 64ms para todo el chip
- Ciclos = número de filas

### Multiplexado
```
RAS → Fila
CAS → Columna
```

Reduce pines a la mitad

---

## Tiempos

### Acceso
- $t_{AA}$: Address to output
- $t_{OE}$: OE to output
- $t_{WC}$: Write cycle

### Compatibilidad MPU
$$t_{mem} < t_{ciclo} - t_{setup}$$

---

## ROM como Lógica

ROM $2^n \times m$ implementa:
- m funciones
- de n variables
- Sin minimización

---

## Mapa de Memoria

```
┌─────────┐ FFFF
│   ROM   │
├─────────┤ 8000
│   I/O   │
├─────────┤ 4000
│   RAM   │
└─────────┘ 0000
```

---

## Comparativa Rápida

| Parámetro | SRAM | DRAM | Flash |
|-----------|------|------|-------|
| Velocidad | Alta | Media | Baja |
| Densidad | Baja | Alta | Alta |
| Costo/bit | Alto | Bajo | Bajo |
| Refresh | No | Sí | No |

---

## Errores Comunes

❌ Confundir bits y bytes
❌ Olvidar que 1K = 1024
❌ WE y OE activos juntos
❌ No considerar refresh DRAM
❌ Solapamiento en decodificación

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño y exámenes
-->
