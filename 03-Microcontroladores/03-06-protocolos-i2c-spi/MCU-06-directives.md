# Directivas — Protocolos I2C/SPI

<!--
::METADATA::
type: reference
topic_id: mcu-06-protocolos-i2c-spi
file_id: _directives
status: stable
audience: ai_context
-->

## Clasificación del Contenido

| Carpeta/Archivo | Archivo Principal | Descripción |
|-----------------|-------------------|-------------|
| `theory/` | `MCU-06-Teoria-I2C-SPI.md` | Teoría de protocolos I2C/SPI |
| `methods/` | `MCU-06-Metodos-I2C-SPI.md` | Implementación I2C/SPI |
| `problems/` | `MCU-06-Problemas.md` | Enunciados de problemas |
| `solutions/` | `MCU-06-Respuestas.md` | Soluciones desarrolladas |
| `applications/` | `APP-MCU-06-temp-i2c.md` | Sensor de temperatura I2C |
| `MCU-06-Intro.md` | — | Entrada principal del tema |
| `MCU-06-Resumen-Formulas.md` | — | Resumen de registros |
| `manifest.json` | — | Metadatos y configuración |

## Directivas para IA

- **Audiencia:** Estudiante universitario de microcontroladores
- **Formato de salida:** Markdown con código C y diagramas de comunicación
- **Notación:** Seguir `[00-META/notation-cheatsheet.md](../../00-META/notation-cheatsheet.md)`
- **Tareas permitidas:** explain_concept, generate_code, analyze_protocol, verify_solution, diagnostic_check
- **Hardware asumido:** PIC16F887 (MSSP) / AVR ATmega328P (TWI/SPI)
- **Nivel de dificultad:** Avanzado (3/3)

## Contexto del Tema

- **Prerrequisitos:** mcu-05-comunicacion-serial
- **Tags:** I2C, SPI, MSSP, TWI, maestro, esclavo, SCL, SDA, MOSI, MISO, SS
- **Propósito:** Implementar comunicación síncrona usando protocolos I2C y SPI
