# Directivas — Comunicación Serial

<!--
::METADATA::
type: reference
topic_id: mcu-05-comunicacion-serial
file_id: _directives
status: stable
audience: ai_context
-->

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `MCU-05-Teoria-UART.md` | Teoría de comunicación serial |
| `methods/` | `MCU-05-Metodos-UART.md` | Configuración de UART |
| `problems/` | `MCU-05-Problemas.md` | Enunciados de problemas |
| `solutions/` | `MCU-05-Respuestas.md` | Soluciones desarrolladas |
| `applications/` | `APP-MCU-05-uart-loopback.md` | Monitor serial con eco |
| `MCU-05-Intro.md` | — | Entrada principal del tema |
| `MCU-05-Resumen-Formulas.md` | — | Resumen de fórmulas |
| `manifest.json` | — | Metadatos y configuración |

## Directivas para IA

- **Audiencia:** Estudiante universitario de microcontroladores
- **Formato de salida:** Markdown con código C y cálculos de baud rate
- **Notación:** Seguir `[00-META/notation-cheatsheet.md](../../00-META/notation-cheatsheet.md)`
- **Tareas permitidas:** explain_concept, generate_code, calculate_baud, verify_solution, diagnostic_check
- **Hardware asumido:** PIC16F887 (EUSART) / AVR ATmega328P (USART)
- **Nivel de dificultad:** Intermedio (2/3)

## Contexto del Tema

- **Prerrequisitos:** mcu-04-adc-dac
- **Tags:** UART, EUSART, RS232, baud rate, TXSTA, RCSTA, SPBRG, serial
- **Propósito:** Implementar comunicación serial asíncrona (UART) entre dispositivos
