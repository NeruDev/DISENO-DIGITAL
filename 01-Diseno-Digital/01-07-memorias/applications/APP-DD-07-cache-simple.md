# 🔧 Aplicación: Sistema de Caché Simple

```
::METADATA::
tipo: aplicacion
tema: DD-07-memorias
dificultad: avanzada
objetivo: Diseñar memoria caché de mapeo directo
::END::
```

## 📋 Descripción del Proyecto

Diseñar una memoria caché de mapeo directo que actúe como intermediaria entre CPU y memoria principal.

## 🎯 Objetivos de Aprendizaje

- Comprender organización de memorias
- Implementar lógica de hit/miss
- Diseñar controlador de caché
- Manejar política de escritura

## 📝 Especificaciones

### Parámetros del Sistema
| Parámetro | Valor |
|-----------|-------|
| Dirección CPU | 16 bits |
| Palabra | 8 bits |
| Tamaño caché | 256 bytes |
| Tamaño bloque | 4 bytes |
| Líneas caché | 64 |

### Entradas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `ADDR` | 16 bits | Dirección de memoria |
| `DATA_IN` | 8 bits | Dato a escribir |
| `RD` | 1 bit | Lectura |
| `WR` | 1 bit | Escritura |
| `CLK` | 1 bit | Reloj |

### Salidas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `DATA_OUT` | 8 bits | Dato leído |
| `HIT` | 1 bit | Acierto de caché |
| `MISS` | 1 bit | Fallo de caché |
| `READY` | 1 bit | Operación completada |

## 🔍 Estructura de Dirección

```
Dirección de 16 bits:
┌────────────────┬──────────────┬────────────┐
│     TAG        │    INDEX     │   OFFSET   │
│   (8 bits)     │  (6 bits)    │  (2 bits)  │
└────────────────┴──────────────┴────────────┘
    15...8           7...2          1...0

TAG:    Identifica bloque en memoria principal
INDEX:  Selecciona línea en caché (64 líneas)
OFFSET: Selecciona byte dentro del bloque (4 bytes)
```

## 📐 Estructura de Línea de Caché

```
┌───────┬─────────┬──────────────────────────────────┐
│ VALID │   TAG   │            DATA BLOCK            │
│(1 bit)│(8 bits) │           (32 bits)              │
└───────┴─────────┴──────────────────────────────────┘
                  │ Byte 0 │ Byte 1 │ Byte 2 │ Byte 3 │
```

### Organización de Caché (64 líneas)

```
       CACHE MEMORY ARRAY
┌─────────────────────────────────────────────┐
│ Line │ V │   TAG    │    DATA BLOCK         │
├──────┼───┼──────────┼───────────────────────┤
│  0   │ 1 │ 0xAB     │ D0 D1 D2 D3           │
│  1   │ 0 │ 0x00     │ -- -- -- --           │
│  2   │ 1 │ 0x12     │ D0 D1 D2 D3           │
│ ...  │   │          │                       │
│  63  │ 1 │ 0x55     │ D0 D1 D2 D3           │
└─────────────────────────────────────────────┘
```

## 🔧 Lógica de Hit/Miss

```
// Descomposición de dirección
TAG_ADDR   = ADDR[15:8]
INDEX      = ADDR[7:2]
OFFSET     = ADDR[1:0]

// Lectura de línea de caché
cache_line = CACHE[INDEX]
valid_bit  = cache_line.VALID
stored_tag = cache_line.TAG

// Comparación
HIT  = valid_bit & (stored_tag == TAG_ADDR)
MISS = ~HIT

// Selección de byte
DATA_OUT = cache_line.DATA[OFFSET]
```

## 📊 Diagrama de Flujo

```
           ┌─────────────┐
           │   REQUEST   │
           │  (RD o WR)  │
           └──────┬──────┘
                  │
                  ▼
         ┌────────────────┐
         │ Leer línea de  │
         │ caché [INDEX]  │
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ ¿TAG coincide  │
         │  Y VALID=1?    │
         └────────┬───────┘
                  │
         ┌────────┴────────┐
         │                 │
         ▼                 ▼
    ┌─────────┐      ┌─────────┐
    │   HIT   │      │  MISS   │
    └────┬────┘      └────┬────┘
         │                │
         ▼                ▼
    ┌─────────┐      ┌─────────────┐
    │ Retornar│      │Cargar bloque│
    │  dato   │      │desde memoria│
    └─────────┘      │  principal  │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │Actualizar   │
                     │línea caché  │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │ Retornar    │
                     │   dato      │
                     └─────────────┘
```

## 🛠️ Implementación de Componentes

### Memoria de Tags (64 × 8 bits)

```
// RAM síncrona para tags
TAG_MEM: array [0..63] of std_logic_vector(7 downto 0)

// Lectura
stored_tag <= TAG_MEM(to_integer(unsigned(INDEX)));

// Escritura (en miss)
TAG_MEM(to_integer(unsigned(INDEX))) <= TAG_ADDR;
```

### Memoria de Datos (64 × 32 bits)

```
// RAM síncrona para bloques de datos
DATA_MEM: array [0..63] of std_logic_vector(31 downto 0)

// Lectura con selección de byte
block <= DATA_MEM(to_integer(unsigned(INDEX)));
case OFFSET is
    when "00" => DATA_OUT <= block(7 downto 0);
    when "01" => DATA_OUT <= block(15 downto 8);
    when "10" => DATA_OUT <= block(23 downto 16);
    when "11" => DATA_OUT <= block(31 downto 24);
end case;
```

### Registro de Valid Bits (64 × 1 bit)

```
// Registro con reset
VALID_REG: std_logic_vector(63 downto 0) := (others => '0');

-- En reset: todas las líneas inválidas
-- En miss: VALID_REG(INDEX) <= '1';
```

## ✅ Criterios de Éxito

- [ ] Hit rate > 80% con accesos localizados
- [ ] Latencia de hit: 1 ciclo
- [ ] Latencia de miss: N ciclos (carga de bloque)
- [ ] Política write-through funcional
- [ ] Reset inicializa todos los valid bits a 0

## 📚 Recursos Relacionados

- [DD-07-Intro.md](../DD-07-Intro.md)
- [GLOSSARY: ram](../../../GLOSSARY/README.md#ram)
- [GLOSSARY: sram](../../../GLOSSARY/README.md#sram)
- [MCU-01 Arquitectura](../../../03-Microcontroladores/03-01-arquitectura-mcu/)

---

> 💡 **Tip**: El mapeo directo es simple pero puede tener conflictos; considerar set-associative para mejor rendimiento
