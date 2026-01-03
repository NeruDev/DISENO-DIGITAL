# 🔧 Aplicación: Semáforo con Controlador FSM

```
::METADATA::
tipo: aplicacion
tema: DD-05-circuitos-secuenciales
dificultad: intermedia
objetivo: Diseñar máquina de estados para control de semáforo
::END::
```

## 📋 Descripción del Proyecto

Diseñar un controlador de semáforo de intersección utilizando una máquina de estados finitos (FSM).

## 🎯 Objetivos de Aprendizaje

- Diseñar máquinas de estados (Moore/Mealy)
- Implementar flip-flops para almacenamiento de estado
- Generar temporización con contadores

## 📝 Especificaciones

### Entradas
| Señal | Descripción |
|-------|-------------|
| `CLK` | Reloj del sistema (1 Hz) |
| `RST` | Reset asíncrono |
| `SENSOR_N` | Sensor vehículos Norte-Sur |
| `SENSOR_E` | Sensor vehículos Este-Oeste |
| `EMERGENCY` | Señal de emergencia |

### Salidas
| Señal | Descripción |
|-------|-------------|
| `NS_R, NS_Y, NS_G` | Semáforo Norte-Sur |
| `EW_R, EW_Y, EW_G` | Semáforo Este-Oeste |
| `WALK_NS, WALK_EW` | Señal peatonal |

## 🔍 Diagrama de Estados

```
                    ┌──────────────┐
                    │              │
        ┌──────────▶│   NS_GREEN   │◀──────────┐
        │           │   (30 seg)   │           │
        │           └──────┬───────┘           │
        │                  │ timeout           │
        │                  ▼                   │
        │           ┌──────────────┐           │
        │           │  NS_YELLOW   │           │
        │           │   (5 seg)    │           │
        │           └──────┬───────┘           │
        │                  │ timeout           │
        │                  ▼                   │
        │           ┌──────────────┐           │
    timeout         │   ALL_RED    │       timeout
        │           │   (2 seg)    │           │
        │           └──────┬───────┘           │
        │                  │ timeout           │
        │                  ▼                   │
        │           ┌──────────────┐           │
        │           │  EW_GREEN    │           │
        │           │   (30 seg)   │           │
        │           └──────┬───────┘           │
        │                  │ timeout           │
        │                  ▼                   │
        │           ┌──────────────┐           │
        │           │  EW_YELLOW   │           │
        │           │   (5 seg)    │           │
        │           └──────┬───────┘           │
        │                  │ timeout           │
        │                  ▼                   │
        │           ┌──────────────┐           │
        └───────────│   ALL_RED    │───────────┘
                    │   (2 seg)    │
                    └──────────────┘
```

### Estados con Sensores (Modo Inteligente)

```
Si SENSOR_N = 0 y estado actual = NS_GREEN:
    → Reducir tiempo a mínimo (10 seg)

Si EMERGENCY = 1:
    → Ir a estado EMERGENCY_MODE (todos rojos)
```

## 📐 Codificación de Estados

| Estado | Q2 Q1 Q0 | NS | EW | Tiempo |
|--------|:--------:|:--:|:--:|:------:|
| NS_GREEN | 000 | 🟢 | 🔴 | 30s |
| NS_YELLOW | 001 | 🟡 | 🔴 | 5s |
| ALL_RED_1 | 010 | 🔴 | 🔴 | 2s |
| EW_GREEN | 011 | 🔴 | 🟢 | 30s |
| EW_YELLOW | 100 | 🔴 | 🟡 | 5s |
| ALL_RED_2 | 101 | 🔴 | 🔴 | 2s |
| EMERGENCY | 110 | 🔴 | 🔴 | ∞ |

## 🔧 Lógica de Salidas (Moore)

```
NS_G = ~Q2 & ~Q1 & ~Q0           // Estado 000
NS_Y = ~Q2 & ~Q1 &  Q0           // Estado 001
NS_R = Q2 | Q1                    // Estados 010-110

EW_G = ~Q2 &  Q1 &  Q0           // Estado 011
EW_Y =  Q2 & ~Q1 & ~Q0           // Estado 100
EW_R = ~Q1 | ~Q0 | Q2            // Resto
```

## 🛠️ Implementación con Flip-Flops

### Diagrama de Bloque

```
         ┌─────────────────────────────────────────┐
         │               FSM CONTROLLER            │
         │                                         │
CLK ────▶│  ┌─────┐    ┌─────┐    ┌─────┐        │
         │  │ FF  │    │ FF  │    │ FF  │        │
RST ────▶│  │ Q2  │    │ Q1  │    │ Q0  │        │
         │  └──┬──┘    └──┬──┘    └──┬──┘        │
         │     │          │          │            │
         │     └──────────┼──────────┘            │
         │                │                       │
         │     ┌──────────▼──────────┐            │
         │     │   NEXT STATE LOGIC  │◀── TIMEOUT │
         │     │   + OUTPUT LOGIC    │            │
         │     └──────────┬──────────┘            │
         │                │                       │
         └────────────────┼───────────────────────┘
                          │
                          ▼
              NS_R, NS_Y, NS_G, EW_R, EW_Y, EW_G
```

### Contador de Tiempo

```
// Contador descendente de 6 bits (máx 63 segundos)
TIMEOUT = (COUNTER == 0)

En cada CLK:
    if (COUNTER > 0)
        COUNTER <= COUNTER - 1
    else
        COUNTER <= LOAD_VALUE[estado_actual]
```

## ✅ Criterios de Éxito

- [ ] Secuencia correcta de estados
- [ ] Tiempos configurables por estado
- [ ] Respuesta inmediata a EMERGENCY
- [ ] Modo inteligente con sensores funcional
- [ ] Reset asíncrono lleva a estado seguro

## 📚 Recursos Relacionados

- [DD-05-Intro.md](../DD-05-Intro.md)
- [GLOSSARY: fsm](../../../GLOSSARY/README.md#fsm)
- [GLOSSARY: flip-flop](../../../GLOSSARY/README.md#flip-flop)
- [VHDL-06 Máquinas de Estados](../../../02-Diseno-Digital-con-VHDL/02-06-maquinas-estados/)

---

> 💡 **Tip**: Usar codificación one-hot para FSMs grandes reduce lógica combinacional
