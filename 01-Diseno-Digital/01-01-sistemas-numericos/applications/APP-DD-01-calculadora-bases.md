# 🔧 Aplicación: Calculadora de Conversión de Bases

```
::METADATA::
tipo: aplicacion
tema: DD-01-sistemas-numericos
dificultad: intermedia
objetivo: Diseñar un circuito que convierta entre sistemas numéricos
::END::
```

## 📋 Descripción del Proyecto

Diseñar un sistema digital que permita convertir números entre diferentes bases numéricas (binario, decimal, hexadecimal).

## 🎯 Objetivos de Aprendizaje

- Aplicar conversiones entre sistemas numéricos
- Implementar algoritmos de división sucesiva en hardware
- Diseñar interfaz de entrada/salida para números

## 📝 Especificaciones

### Entradas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `num_in` | 8 bits | Número a convertir |
| `base_src` | 2 bits | Base origen (00=bin, 01=dec, 10=hex) |
| `base_dst` | 2 bits | Base destino |
| `convert` | 1 bit | Señal de inicio |

### Salidas
| Señal | Ancho | Descripción |
|-------|-------|-------------|
| `digit_out` | 4×4 bits | 4 dígitos del resultado |
| `ready` | 1 bit | Conversión completada |

## 🔍 Algoritmo

```
Conversión general:
1. Si base_src ≠ binario:
   - Convertir entrada a binario (valor interno)
2. Si base_dst ≠ binario:
   - Convertir valor interno a base destino
3. Mostrar resultado en display
```

### Ejemplo: Decimal 25 → Hexadecimal

```
25₁₀ = 16 + 9 = 16 + 8 + 1 = 11001₂ = 19₁₆
```

## 📐 Diagrama de Bloques

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   INPUT     │────▶│  BINARIO    │────▶│   OUTPUT    │
│   DECODER   │     │  INTERNO    │     │   ENCODER   │
└─────────────┘     └─────────────┘     └─────────────┘
     ▲                                        │
     │           ┌─────────────┐              │
     └───────────│   CONTROL   │◀─────────────┘
                 │    FSM      │
                 └─────────────┘
```

## 🛠️ Componentes Necesarios

1. **Decodificador de entrada**: Interpreta según base origen
2. **Registro interno**: Almacena valor binario de 8 bits
3. **Divisor iterativo**: Para conversión a bases no binarias
4. **Multiplexor de salida**: Selecciona dígitos
5. **FSM de control**: Coordina la conversión

## ✅ Criterios de Éxito

- [ ] Conversión correcta entre todas las combinaciones de bases
- [ ] Tiempo de conversión < 10 ciclos de reloj
- [ ] Manejo de overflow (números > 255)
- [ ] Indicación clara de finalización

## 📚 Recursos Relacionados

- [DD-01-Intro.md](../DD-01-Intro.md)
- [DD-01-Resumen-Formulas.md](../DD-01-Resumen-Formulas.md)
- [Problemas de práctica](../problems/)

---

> 💡 **Tip**: Usa una tabla de look-up para conversiones BCD-7seg
