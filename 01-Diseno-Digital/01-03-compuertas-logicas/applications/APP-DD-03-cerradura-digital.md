# 🔧 Aplicación: Cerradura de Combinación Digital

```
::METADATA::
tipo: aplicacion
tema: DD-03-compuertas-logicas
dificultad: basica
objetivo: Diseñar circuito de seguridad con compuertas lógicas
::END::
```

## 📋 Descripción del Proyecto

Diseñar una cerradura digital que solo se abra cuando se ingrese la combinación correcta de 4 interruptores.

## 🎯 Objetivos de Aprendizaje

- Aplicar compuertas AND, OR, NOT
- Diseñar circuitos combinacionales básicos
- Implementar lógica de comparación

## 📝 Especificaciones

### Entradas
| Señal | Descripción |
|-------|-------------|
| `SW[3:0]` | 4 interruptores de entrada |
| `KEY[3:0]` | 4 bits de código secreto (hardcoded) |

### Salidas
| Señal | Descripción |
|-------|-------------|
| `UNLOCK` | 1 si combinación correcta |
| `ERROR` | 1 si combinación incorrecta |
| `LED[3:0]` | Indicadores de coincidencia por bit |

## 🔍 Análisis de Diseño

### Tabla de Verdad (para código 1010)

| SW3 | SW2 | SW1 | SW0 | UNLOCK | ERROR |
|:---:|:---:|:---:|:---:|:------:|:-----:|
| 1 | 0 | 1 | 0 | **1** | 0 |
| otros | | | | 0 | **1** |

### Ecuaciones Booleanas

```
Para código KEY = 1010:

LED[3] = SW[3] XNOR KEY[3] = SW[3] XNOR 1 = SW[3]
LED[2] = SW[2] XNOR KEY[2] = SW[2] XNOR 0 = SW[2]'
LED[1] = SW[1] XNOR KEY[1] = SW[1] XNOR 1 = SW[1]
LED[0] = SW[0] XNOR KEY[0] = SW[0] XNOR 0 = SW[0]'

UNLOCK = LED[3] · LED[2] · LED[1] · LED[0]
ERROR  = UNLOCK'
```

## 📐 Diagrama de Circuito

```
SW[3] ──┬────[XNOR]──┬── LED[3]
        │     │      │
KEY[3] ─┘     │      │
              │      │
SW[2] ──┬────[XNOR]──┼── LED[2]
        │     │      │
KEY[2] ─┘     │      │
              │      │
SW[1] ──┬────[XNOR]──┼── LED[1]
        │     │      │
KEY[1] ─┘     │      │
              │      │
SW[0] ──┬────[XNOR]──┼── LED[0]
        │     │      │
KEY[0] ─┘     │      │
              │      │
              └──[AND4]── UNLOCK
                   │
                  [NOT]── ERROR
```

## 🛠️ Implementación con Compuertas Básicas

### XNOR usando AND, OR, NOT

```
A XNOR B = (A·B) + (A'·B')

       A ────┬───[AND]───┐
             │           │
       B ────┘           │
                        [OR]─── Y
       A'────┬───[AND]───┘
             │
       B'────┘
```

### Lista de Componentes

| Componente | Cantidad | Uso |
|------------|:--------:|-----|
| NOT (74LS04) | 4 | Inversores |
| AND-2 (74LS08) | 8 | Comparadores |
| OR-2 (74LS32) | 4 | XNOR |
| AND-4 (74LS21) | 1 | Verificación final |

## ✅ Criterios de Éxito

- [ ] Solo UNLOCK=1 con combinación correcta
- [ ] LEDs indican coincidencia parcial
- [ ] Respuesta instantánea (sin retardo de propagación visible)
- [ ] Código modificable (usando jumpers o DIP switches)

## 🔄 Extensiones Sugeridas

1. **Contador de intentos**: Bloquear después de 3 errores
2. **Temporizador**: Agregar timeout entre intentos
3. **Alarma**: Activar si ERROR persiste >10 segundos

## 📚 Recursos Relacionados

- [DD-03-Intro.md](../DD-03-Intro.md)
- [Compuertas Básicas](../theory/)
- [GLOSSARY: xnor](../../../GLOSSARY/README.md#xnor)

---

> 💡 **Tip**: El XNOR es un comparador de igualdad de 1 bit
