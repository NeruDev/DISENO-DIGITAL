# 🔧 Aplicación: Simplificador de Funciones Booleanas

```
::METADATA::
tipo: aplicacion
tema: DD-02-algebra-booleana
dificultad: intermedia
objetivo: Implementar algoritmo de simplificación usando mapas K
::END::
```

## 📋 Descripción del Proyecto

Sistema que recibe una función booleana en forma canónica y devuelve la expresión mínima utilizando el método del mapa de Karnaugh.

## 🎯 Objetivos de Aprendizaje

- Aplicar teoremas del álgebra booleana
- Implementar detección de adyacencias
- Generar mintérminos y maxtérminos

## 📝 Especificaciones

### Entradas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `truth_table` | 16 bits | Tabla de verdad (4 variables) |
| `mode` | 1 bit | 0=SOP, 1=POS |
| `start` | 1 bit | Iniciar simplificación |

### Salidas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `sop_terms` | 8×4 bits | Términos producto resultantes |
| `num_terms` | 3 bits | Cantidad de términos |
| `done` | 1 bit | Simplificación completada |

## 🔍 Algoritmo del Mapa K

```
Para mapa de 4 variables (A,B,C,D):

     CD
     00  01  11  10
    ┌───┬───┬───┬───┐
 00 │ 0 │ 1 │ 3 │ 2 │  AB
    ├───┼───┼───┼───┤
 01 │ 4 │ 5 │ 7 │ 6 │
    ├───┼───┼───┼───┤
 11 │12 │13 │15 │14 │
    ├───┼───┼───┼───┤
 10 │ 8 │ 9 │11 │10 │
    └───┴───┴───┴───┘

Grupos válidos: 1, 2, 4, 8, 16 celdas adyacentes
```

### Ejemplo: F(A,B,C,D) = Σm(0,1,2,8,9,10)

```
Tabla de verdad: 1110_0000_1110_0000

Mapa K:
     00  01  11  10
    ┌───┬───┬───┬───┐
 00 │ 1 │ 1 │ 0 │ 1 │  ← Grupo B'D'
    ├───┼───┼───┼───┤
 01 │ 0 │ 0 │ 0 │ 0 │
    ├───┼───┼───┼───┤
 11 │ 0 │ 0 │ 0 │ 0 │
    ├───┼───┼───┼───┤
 10 │ 1 │ 1 │ 0 │ 1 │  ← Grupo B'D'
    └───┴───┴───┴───┘

Resultado: F = B'D' + A'B'C'
```

## 📐 Diagrama de Bloques

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   TABLA     │────▶│   MAPA K    │────▶│  EXTRACTOR  │
│   VERDAD    │     │   4x4       │     │   GRUPOS    │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
                    ┌─────────────┐           ▼
                    │  GENERADOR  │◀──────────┘
                    │   SOP/POS   │
                    └─────────────┘
```

## 🛠️ Componentes Necesarios

1. **Memoria de tabla**: 16 bits para almacenar f(A,B,C,D)
2. **Detector de adyacencias**: Identifica grupos válidos
3. **Selector de grupos óptimos**: Algoritmo greedy
4. **Generador de términos**: Convierte grupos a expresión

## ✅ Criterios de Éxito

- [ ] Simplificación correcta para todas las funciones de 4 variables
- [ ] Generación de forma SOP y POS
- [ ] Manejo de don't cares (X)
- [ ] Expresión mínima garantizada

## 📚 Recursos Relacionados

- [DD-02-Intro.md](../DD-02-Intro.md)
- [Teoremas Booleanos](../theory/)
- [GLOSSARY: karnaugh](../../../GLOSSARY/README.md#karnaugh)

---

> 💡 **Tip**: Los grupos deben ser potencias de 2 y pueden envolver los bordes del mapa
