# 🔧 Aplicación: Reloj Digital con Display 7-Segmentos

```
::METADATA::
tipo: aplicacion
tema: DD-06-contadores-registros
dificultad: avanzada
objetivo: Diseñar reloj digital con horas:minutos:segundos
::END::
```

## 📋 Descripción del Proyecto

Diseñar un reloj digital completo utilizando contadores en cascada y displays de 7 segmentos.

## 🎯 Objetivos de Aprendizaje

- Diseñar contadores BCD y módulo-N
- Implementar cascada de contadores
- Crear decodificadores BCD a 7-segmentos
- Manejar multiplexación de displays

## 📝 Especificaciones

### Entradas
| Señal | Descripción |
|-------|-------------|
| `CLK_1HZ` | Reloj de 1 Hz |
| `RST` | Reset a 00:00:00 |
| `SET_HR` | Incrementar horas |
| `SET_MIN` | Incrementar minutos |
| `MODE` | 12H/24H |

### Salidas
| Señal | Descripción |
|-------|-------------|
| `SEG[6:0]` | Segmentos (a-g) |
| `AN[5:0]` | Ánodos (selección display) |
| `AM_PM` | Indicador AM/PM (modo 12H) |

## 🔍 Arquitectura de Contadores

```
                    CADENA DE CONTADORES
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐     │
│  │SEC_U   │    │SEC_D   │    │MIN_U   │    │MIN_D   │     │
│  │ MOD-10 │TC─▶│ MOD-6  │TC─▶│ MOD-10 │TC─▶│ MOD-6  │TC──┐│
│  └────────┘    └────────┘    └────────┘    └────────┘    ││
│       ▲                                                   ││
│       │                                                   ││
│    CLK_1HZ                                                ││
│                                                           ▼│
│  ┌────────┐    ┌────────────────────────────────────────┐ ││
│  │HR_D    │    │            HORAS                       │ ││
│  │MOD-2/3 │◀TC─│  HR_U (MOD-10 o MOD-4 según HR_D)     │◀┘│
│  └────────┘    └────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘

TC = Terminal Count (carry out)

Segundos: 00-59 (MOD-60 = MOD-10 × MOD-6)
Minutos:  00-59 (MOD-60 = MOD-10 × MOD-6)
Horas:    00-23 (24H) o 01-12 (12H)
```

## 📐 Contador MOD-10 (BCD)

```
        ┌────────────────────────────────┐
        │         CONTADOR BCD           │
CLK ───▶│  ┌───┐ ┌───┐ ┌───┐ ┌───┐     │
        │  │Q3 │ │Q2 │ │Q1 │ │Q0 │     │
RST ───▶│  └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘     │
        │    │     │     │     │        │
        │    └─────┴─────┴─────┘        │
        │              │                │
        │     ┌────────▼────────┐       │
        │     │  NEXT STATE     │       │
        │     │  (Reset @ 10)   │──TC──▶│
        │     └─────────────────┘       │
        └────────────────────────────────┘

Secuencia: 0→1→2→3→4→5→6→7→8→9→0...
TC = (Q3·Q0) = (Q == 9)
Reset cuando Q == 10 (1010)
```

## 🔧 Decodificador BCD a 7-Segmentos

```
Dígito    a b c d e f g    Hex
  0       1 1 1 1 1 1 0    7E
  1       0 1 1 0 0 0 0    30
  2       1 1 0 1 1 0 1    6D
  3       1 1 1 1 0 0 1    79
  4       0 1 1 0 0 1 1    33
  5       1 0 1 1 0 1 1    5B
  6       1 0 1 1 1 1 1    5F
  7       1 1 1 0 0 0 0    70
  8       1 1 1 1 1 1 1    7F
  9       1 1 1 1 0 1 1    7B

       ──a──
      │     │
      f     b
      │     │
       ──g──
      │     │
      e     c
      │     │
       ──d──
```

## 🛠️ Multiplexación de Displays

```
CLK_MUX (~1kHz)     ┌─────────────────────────────────────┐
       │            │                                     │
       ▼            │   MULTIPLEXOR DE 6 DISPLAYS        │
┌──────────┐        │                                     │
│ CONTADOR │        │  AN[5:0] = 6'b111110 → Display 0   │
│  MOD-6   │───────▶│  AN[5:0] = 6'b111101 → Display 1   │
│          │        │  AN[5:0] = 6'b111011 → Display 2   │
└──────────┘        │  AN[5:0] = 6'b110111 → Display 3   │
                    │  AN[5:0] = 6'b101111 → Display 4   │
SEG[6:0] ◀──────────│  AN[5:0] = 6'b011111 → Display 5   │
                    │                                     │
                    └─────────────────────────────────────┘

Rotación rápida crea ilusión de 6 displays simultáneos
```

## 📊 Ajuste de Horas (24H)

```
if (HR_D == 2 && HR_U == 3 && TC_minutos)
    HR_D <= 0; HR_U <= 0;  // 23:59:59 → 00:00:00
else if (TC_minutos)
    if (HR_U == 9)
        HR_U <= 0; HR_D <= HR_D + 1;
    else
        HR_U <= HR_U + 1;
```

## ✅ Criterios de Éxito

- [ ] Cuenta correcta 00:00:00 a 23:59:59
- [ ] Cambio suave de día (23:59:59 → 00:00:00)
- [ ] Ajuste manual de horas/minutos
- [ ] Modo 12H/24H seleccionable
- [ ] Sin parpadeo visible en displays

## 📚 Recursos Relacionados

- [DD-06-Intro.md](../DD-06-Intro.md)
- [GLOSSARY: contador](../../../GLOSSARY/README.md#contador)
- [GLOSSARY: registro](../../../GLOSSARY/README.md#registro)

---

> 💡 **Tip**: Usar contadores BCD simplifica la decodificación a 7-segmentos
