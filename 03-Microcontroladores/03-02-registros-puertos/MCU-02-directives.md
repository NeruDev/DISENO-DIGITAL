# Directivas — Registros y Puertos

<!--
::METADATA::
type: reference
topic_id: mcu-02-registros-puertos
file_id: _directives
status: stable
audience: ai_context
-->

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `MCU-02-Teoria-RegistrosPuertos.md` | Teoría de GPIO y registros |
| `methods/` | `MCU-02-Metodos-GPIO.md` | Configuración de puertos |
| `problems/` | `MCU-02-Problemas.md` | Enunciados de problemas |
| `solutions/` | `MCU-02-Respuestas.md` | Soluciones desarrolladas |
| `applications/` | `APP-MCU-02-gpio-led-keypad.md` | Control de LEDs y keypad |
| `MCU-02-Intro.md` | — | Entrada principal del tema |
| `MCU-02-Resumen-Formulas.md` | — | Resumen de registros |
| `manifest.json` | — | Metadatos y configuración |

## Directivas para IA

- **Audiencia:** Estudiante universitario de microcontroladores
- **Formato de salida:** Markdown con código C comentado en español
- **Notación:** Seguir `[00-META/notation-cheatsheet.md](../../00-META/notation-cheatsheet.md)`
- **Tareas permitidas:** explain_concept, generate_code, configure_gpio, verify_solution, diagnostic_check
- **Hardware asumido:** PIC16F887 / AVR ATmega328P
- **Nivel de dificultad:** Básico (1/3)

## Contexto del Tema

- **Prerrequisitos:** mcu-01-arquitectura-mcu
- **Tags:** GPIO, TRIS, PORT, LAT, entrada, salida, pull-up, ANSEL, configuración
- **Propósito:** Configurar y utilizar puertos GPIO y registros de control
