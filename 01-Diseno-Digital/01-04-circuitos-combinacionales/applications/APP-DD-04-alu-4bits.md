# 🔧 Aplicación: Calculadora ALU de 4 bits

```
::METADATA::
tipo: aplicacion
tema: DD-04-circuitos-combinacionales
dificultad: avanzada
objetivo: Diseñar una ALU completa con operaciones aritméticas y lógicas
::END::
```

## 📋 Descripción del Proyecto

Diseñar una Unidad Aritmético-Lógica (ALU) de 4 bits capaz de realizar múltiples operaciones seleccionables.

## 🎯 Objetivos de Aprendizaje

- Integrar sumadores, comparadores y multiplexores
- Diseñar circuitos combinacionales complejos
- Implementar selección de operaciones

## 📝 Especificaciones

### Entradas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `A` | 4 bits | Operando A |
| `B` | 4 bits | Operando B |
| `OP` | 3 bits | Selector de operación |
| `Cin` | 1 bit | Carry de entrada |

### Salidas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `Y` | 4 bits | Resultado |
| `Cout` | 1 bit | Carry de salida |
| `Z` | 1 bit | Flag Zero (Y=0) |
| `N` | 1 bit | Flag Negativo (Y[3]=1) |
| `V` | 1 bit | Flag Overflow |

### Operaciones Soportadas

| OP[2:0] | Operación | Descripción |
|:-------:|-----------|-------------|
| 000 | ADD | Y = A + B |
| 001 | SUB | Y = A - B |
| 010 | AND | Y = A & B |
| 011 | OR | Y = A \| B |
| 100 | XOR | Y = A ⊕ B |
| 101 | NOT | Y = ~A |
| 110 | SHL | Y = A << 1 |
| 111 | SHR | Y = A >> 1 |

## 📐 Diagrama de Bloques

```
        ┌─────────────────────────────────────────┐
        │                  ALU                    │
        │                                         │
A[3:0]──┼──┬─[SUMADOR]──────────┐                │
        │  │                    │                │
        │  ├─[RESTADOR]─────────┤                │
        │  │                    │                │
        │  ├─[AND]──────────────┤                │
        │  │                    ├──[MUX 8:1]──Y[3:0]
        │  ├─[OR]───────────────┤       ▲        │
        │  │                    │       │        │
        │  ├─[XOR]──────────────┤    OP[2:0]     │
        │  │                    │                │
        │  ├─[NOT]──────────────┤                │
        │  │                    │                │
        │  ├─[SHL]──────────────┤                │
        │  │                    │                │
B[3:0]──┼──┴─[SHR]──────────────┘                │
        │                                         │
        │  ┌──────────────────────────────────┐  │
        │  │         FLAGS GENERATOR          │  │
        │  │   Z = (Y == 0)                   │  │
        │  │   N = Y[3]                       │  │
        │  │   V = overflow_detect            │  │
        │  │   Cout = carry_out               │  │
        │  └──────────────────────────────────┘  │
        └─────────────────────────────────────────┘
```

## 🔍 Diseño de Componentes

### Sumador de 4 bits (Ripple Carry)

```
      A[0] B[0]   A[1] B[1]   A[2] B[2]   A[3] B[3]
        │   │       │   │       │   │       │   │
        ▼   ▼       ▼   ▼       ▼   ▼       ▼   ▼
      ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
Cin──▶│  FA  │─C─▶│  FA  │─C─▶│  FA  │─C─▶│  FA  │──▶Cout
      └───┬──┘    └───┬──┘    └───┬──┘    └───┬──┘
          │           │           │           │
          ▼           ▼           ▼           ▼
         S[0]        S[1]        S[2]        S[3]
```

### Detector de Overflow

```
// Overflow en suma/resta con signo
V = (A[3] & B[3] & ~S[3]) | (~A[3] & ~B[3] & S[3])  // Para suma
V = (A[3] & ~B[3] & ~S[3]) | (~A[3] & B[3] & S[3])  // Para resta
```

### Detector de Zero

```
Z = ~(Y[3] | Y[2] | Y[1] | Y[0])
  = ~Y[3] & ~Y[2] & ~Y[1] & ~Y[0]
```

## 🛠️ Lista de Componentes

| Componente | Cantidad | Función |
|------------|:--------:|---------|
| Full Adder | 4 | Sumador/Restador |
| MUX 8:1 | 4 | Selector operación |
| AND-2 | 4 | Operación AND |
| OR-2 | 4 | Operación OR |
| XOR-2 | 8 | Operación XOR + Resta |
| NOT | 4 | Operación NOT |
| NOR-4 | 1 | Flag Zero |

## ✅ Criterios de Éxito

- [ ] Todas las operaciones funcionan correctamente
- [ ] Flags se generan apropiadamente
- [ ] Propagación de carry correcta
- [ ] Overflow detectado en operaciones con signo

## 📚 Recursos Relacionados

- [DD-04-Intro.md](../DD-04-Intro.md)
- [Sumadores](../theory/)
- [GLOSSARY: sumador](../../../GLOSSARY/README.md#sumador)
- [GLOSSARY: mux](../../../GLOSSARY/README.md#mux)

---

> 💡 **Tip**: La resta se implementa como A + (~B) + 1 (complemento a 2)
