# Directivas — ADC y DAC

<!--
::METADATA::
type: reference
topic_id: mcu-04-adc-dac
file_id: _directives
status: stable
audience: ai_context
-->

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `MCU-04-Teoria-ADC.md` | Teoría de conversión A/D y D/A |
| `methods/` | `MCU-04-Metodos-ADC.md` | Configuración del ADC |
| `problems/` | `MCU-04-Problemas.md` | Enunciados de problemas |
| `solutions/` | `MCU-04-Respuestas.md` | Soluciones desarrolladas |
| `applications/` | `APP-MCU-04-sensor-lm35.md` | Termómetro con LM35 |
| `MCU-04-Intro.md` | — | Entrada principal del tema |
| `MCU-04-Resumen-Formulas.md` | — | Resumen de fórmulas |
| `manifest.json` | — | Metadatos y configuración |

## Directivas para IA

- **Audiencia:** Estudiante universitario de microcontroladores
- **Formato de salida:** Markdown con código C y fórmulas de conversión
- **Notación:** Seguir `[00-META/notation-cheatsheet.md](../../00-META/notation-cheatsheet.md)`
- **Tareas permitidas:** explain_concept, generate_code, calculate_conversion, verify_solution, diagnostic_check
- **Hardware asumido:** PIC16F887 / AVR ATmega328P (ADC 10 bits)
- **Nivel de dificultad:** Intermedio (2/3)

## Contexto del Tema

- **Prerrequisitos:** mcu-03-timers-interrupciones
- **Tags:** ADC, DAC, ADCON0, ADCON1, resolución, Vref, conversión, sensor analógico
- **Propósito:** Utilizar conversores analógico-digital y digital-analógico
