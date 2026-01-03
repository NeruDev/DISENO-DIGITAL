<!--
::METADATA::
type: problem
topic_id: dd-07-memorias
file_id: problemas-memorias
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, memorias, ROM, RAM]
search_keywords: "ejercicios, problemas, memorias, ROM, RAM"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-07-Metodos-Memorias.md) | [Respuestas →](../solutions/DD-07-Respuestas.md)

---

# Problemas: Memorias

## Nivel 1: Conceptos Básicos

### Problema 1.1
Calcular para cada memoria:
- a) 2716 (2K × 8): ¿Cuántas líneas de dirección? ¿Capacidad en bits?
- b) 6264 (8K × 8): ¿Cuántas ubicaciones? ¿Capacidad en KB?
- c) 27C256: ¿Qué significa el 256?

### Problema 1.2
Una memoria tiene 14 líneas de dirección y palabra de 16 bits:
- a) ¿Cuántas ubicaciones?
- b) ¿Capacidad total en bits?
- c) ¿Capacidad en KB?

### Problema 1.3
Clasificar las siguientes memorias:
- a) ROM, PROM, EPROM, EEPROM, Flash
- b) SRAM, DRAM
- c) ¿Cuáles son volátiles?

---

## Nivel 2: Estructura Interna

### Problema 2.1
Para una ROM de 16 × 4:
- a) ¿Cuántas líneas de dirección?
- b) ¿Cuántas líneas de datos?
- c) Dibujar diagrama de bloques

### Problema 2.2
Explicar la diferencia entre:
- a) Celda SRAM vs celda DRAM
- b) ¿Por qué DRAM necesita refresh?
- c) ¿Cuál es más rápida y por qué?

### Problema 2.3
Para la memoria 2716 (2K × 8):
- a) Dibujar pinout simplificado
- b) ¿Qué hace cada pin de control?
- c) Describir ciclo de lectura

---

## Nivel 3: Expansión de Memoria

### Problema 3.1
Diseñar una memoria de 4K × 8 usando chips de 1K × 8:
- a) ¿Cuántos chips necesarios?
- b) Diagrama de conexiones
- c) Tabla de decodificación

### Problema 3.2
Diseñar una memoria de 1K × 16 usando chips de 1K × 4:
- a) ¿Cuántos chips necesarios?
- b) Diagrama de conexiones
- c) ¿Cómo se conectan los buses?

### Problema 3.3
Diseñar una memoria de 8K × 16 usando chips de 2K × 8:
- a) Calcular chips necesarios (expansión combinada)
- b) Diagrama de bloques
- c) Lógica de decodificación

---

## Nivel 4: Decodificación de Direcciones

### Problema 4.1
Un sistema tiene espacio de direcciones de 64K (16 bits):
- RAM: 0000-7FFF (32K)
- ROM: 8000-FFFF (32K)

- a) ¿Qué bit determina RAM vs ROM?
- b) Diseñar decodificador simple
- c) Verificar rangos

### Problema 4.2
Diseñar decodificación para:
- RAM: 0000-3FFF (16K)
- I/O: 4000-5FFF (8K)
- ROM: 8000-FFFF (32K)

- a) ¿Qué bits decodificar?
- b) Ecuaciones de selección
- c) ¿Hay espacio sin usar?

### Problema 4.3
Con un 74LS138 (decodificador 3:8), diseñar selección para 8 memorias de 8K × 8 en un espacio de 64K.

---

## Nivel 5: ROM como Circuito Combinacional

### Problema 5.1
Implementar con ROM la función:
$$F(A,B,C) = \sum m(1,2,4,7)$$

- a) Tamaño mínimo de ROM
- b) Contenido de la ROM
- c) Comparar con implementación con compuertas

### Problema 5.2
Implementar un convertidor BCD a 7 segmentos usando ROM:
- a) Tamaño de ROM necesario
- b) Tabla de programación
- c) Diagrama de conexiones

### Problema 5.3
Implementar un multiplicador de 4×4 bits usando ROM:
- a) ¿Cuántas entradas y salidas?
- b) Tamaño de ROM
- c) ¿Es práctico? Alternativas

---

## Nivel 6: SRAM

### Problema 6.1
Para la SRAM 6116 (2K × 8):
- a) Diagrama de tiempos para lectura
- b) Diagrama de tiempos para escritura
- c) ¿Qué pasa si WE y OE están activos simultáneamente?

### Problema 6.2
Diseñar interfaz entre 6264 (8K × 8) y un bus de 16 bits de datos:
- a) ¿Cuántos chips?
- b) Conexiones de control
- c) Manejo de bytes vs palabras

### Problema 6.3
Calcular si una SRAM de 70ns es compatible con un MPU de 8 MHz:
- a) Tiempo de ciclo del MPU
- b) Tiempo disponible para memoria
- c) ¿Necesita estados de espera?

---

## Nivel 7: DRAM

### Problema 7.1
Explicar el multiplexado de direcciones en DRAM:
- a) ¿Por qué se usa?
- b) Secuencia de señales RAS y CAS
- c) Ventajas y desventajas

### Problema 7.2
Una DRAM de 1M × 1 requiere refresh cada 64ms:
- a) ¿Cuántas filas tiene?
- b) ¿Cuántos ciclos de refresh por segundo?
- c) Tiempo promedio entre refreshes

### Problema 7.3
Comparar organización de DRAM:
- 1M × 1 (1 bit por chip)
- 256K × 4 (4 bits por chip)

Para sistema de 1MB:
- a) Chips necesarios
- b) Pines de direcciones
- c) ¿Cuál es mejor?

---

## Nivel 8: EEPROM y Flash

### Problema 8.1
Para una EEPROM 28C64 (8K × 8):
- a) Tiempo de escritura típico por byte
- b) ¿Cuánto tiempo para escribir 1K?
- c) Ciclos de escritura garantizados

### Problema 8.2
Comparar EEPROM vs Flash:
- a) Unidad mínima de borrado
- b) Velocidad de escritura
- c) Aplicaciones típicas de cada una

### Problema 8.3
Diseñar sistema de almacenamiento de configuración con EEPROM I²C (24LC256):
- a) Señales necesarias
- b) Protocolo de escritura
- c) ¿Cómo verificar escritura exitosa?

---

## Nivel 9: Diseño de Sistema de Memoria

### Problema 9.1
Diseñar sistema de memoria para microcontrolador:
- 16K ROM para programa
- 4K RAM para datos
- 256 bytes EEPROM para configuración

- a) Mapa de memoria propuesto
- b) Chips a usar
- c) Decodificación completa

### Problema 9.2
Un sistema embebido necesita:
- Boot loader: 4K (no modificable)
- Firmware: 28K (actualizable)
- Variables: 8K (volátil)
- Config: 512B (no volátil)

- a) Tipos de memoria para cada sección
- b) Mapa de memoria
- c) Consideraciones de diseño

### Problema 9.3
Calcular ancho de banda de memoria:
- Bus de datos: 32 bits
- Frecuencia: 100 MHz
- Eficiencia: 60%

- a) Ancho de banda teórico
- b) Ancho de banda real
- c) ¿Suficiente para video 1080p?

---

## Nivel 10: Problemas Avanzados

### Problema 10.1
Diseñar un sistema de memoria con:
- Espacio total: 1MB
- RAM: 512KB (SRAM de 128K × 8)
- ROM: 256KB (EPROM de 64K × 8)
- I/O: 64KB

- a) Número de chips de cada tipo
- b) Mapa de memoria detallado
- c) Circuito de decodificación completo

### Problema 10.2
Implementar una memoria caché simple de mapeo directo:
- Cache: 1KB
- Bloque: 16 bytes
- Dirección: 16 bits

- a) ¿Cuántos bloques?
- b) Bits de tag, índice, offset
- c) Diagrama de bloques

### Problema 10.3
Analizar jerarquía de memoria:
- L1 Cache: 32KB, 1ns
- L2 Cache: 256KB, 4ns
- RAM: 4GB, 50ns
- SSD: 256GB, 100µs

Con tasa de aciertos L1=95%, L2=80%:
- a) Tiempo promedio de acceso
- b) ¿Qué pasa si L1 hit rate baja a 90%?
- c) Impacto en rendimiento

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios para memorias semiconductoras
RESPUESTAS: Ver archivo solutions/DD-07-Respuestas.md
HERRAMIENTAS: LogiSim, Proteus, simuladores de memoria
-->
