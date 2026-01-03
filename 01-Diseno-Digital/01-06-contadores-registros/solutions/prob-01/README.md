# Soluciones Detalladas: Contadores y Registros (DD-06)

```
::METADATA::
tipo: indice-soluciones
tema: dd-06-contadores-registros
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`DD-06-Respuestas.md`](../DD-06-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Contadores Síncronos

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Contador ascendente 3 bits | [DD-06-Sol-Problema-1.1.md](DD-06-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Contador descendente 3 bits | [DD-06-Sol-Problema-1.2.md](DD-06-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | Contador módulo N | [DD-06-Sol-Problema-1.3.md](DD-06-Sol-Problema-1.3.md) | ⭐⭐ |
| 1.4 | Contador up/down | [DD-06-Sol-Problema-1.4.md](DD-06-Sol-Problema-1.4.md) | ⭐⭐⭐ |

### Nivel 2: Contadores Asíncronos (Ripple)

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Contador ripple 4 bits | [DD-06-Sol-Problema-2.1.md](DD-06-Sol-Problema-2.1.md) | ⭐ |
| 2.2 | Análisis de timing ripple | [DD-06-Sol-Problema-2.2.md](DD-06-Sol-Problema-2.2.md) | ⭐⭐ |

### Nivel 3: Registros

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Registro PIPO 4 bits | [DD-06-Sol-Problema-3.1.md](DD-06-Sol-Problema-3.1.md) | ⭐ |
| 3.2 | Registro SISO | [DD-06-Sol-Problema-3.2.md](DD-06-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | Registro universal | [DD-06-Sol-Problema-3.3.md](DD-06-Sol-Problema-3.3.md) | ⭐⭐⭐ |
| 3.4 | LFSR y secuencias pseudo-aleatorias | [DD-06-Sol-Problema-3.4.md](DD-06-Sol-Problema-3.4.md) | ⭐⭐⭐ |

---

## Referencia de Contadores

### Tipos de Contadores

| Tipo | Características | Aplicación |
|------|-----------------|------------|
| Síncrono | Todos FF con mismo CLK | Alta velocidad |
| Asíncrono (Ripple) | CLK en cascada | Bajo costo |
| Ascendente | Cuenta 0→max | General |
| Descendente | Cuenta max→0 | Temporizadores |
| Módulo-N | Reinicia en N | Frecuencias específicas |
| BCD | Módulo-10 | Display decimal |
| Gray | 1 bit cambia | Encoders |
| Johnson | Anillo torcido | Generación de fases |

### Fórmulas Clave

**Módulo de contador:**
$$M = 2^n \text{ (binario completo)}$$

**Frecuencia de salida:**
$$f_{out} = \frac{f_{CLK}}{M}$$

**Retardo en ripple counter:**
$$t_{total} = n \cdot t_{pd}$$

---

## Referencia de Registros

### Tipos de Registros

| Tipo | Entrada | Salida | Uso |
|------|---------|--------|-----|
| PIPO | Paralela | Paralela | Almacenamiento |
| SISO | Serie | Serie | Línea de retardo |
| SIPO | Serie | Paralela | Serial→Paralelo |
| PISO | Paralela | Serie | Paralelo→Serial |
| Universal | Ambas | Ambas | Multipropósito |

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [DD-06-Respuestas.md](../DD-06-Respuestas.md) | [DD-06-Intro.md](../../DD-06-Intro.md) | [DD-06-Problemas.md](../../problems/DD-06-Problemas.md) |
