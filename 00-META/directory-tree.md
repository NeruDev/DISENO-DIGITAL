<!--
::METADATA::
type: reference
topic_id: meta-directory-tree
file_id: directory-tree
status: stable
audience: both
last_updated: 2026-01-08
-->

# Árbol de Directorios Esperado

Mapa de referencia para ubicar cada archivo en el repositorio.

## Nivel 0: Raíz

```
DISEÑO-DIGITAL-GITHUB/
├── README.md                         # Portada del repositorio
├── WIKI_INDEX.md                     # Tabla de contenidos maestra
├── glossary.md                       # Diccionario centralizado
├── Guía de Arquitectura.md           # Documentación técnica
├── AUDITORIA_ESTADO_REPO.md          # Reporte de salud (auto-generado)
├── Plantilla de Arquitectura...md    # Referencia de arquitectura
│
├── 00-META/                          # Centro de control
├── 01-Diseno-Digital/                # Módulo DD (prefijo: DD)
├── 02-Diseno-Digital-con-VHDL/       # Módulo VHDL (prefijo: VHDL)
├── 03-Microcontroladores/            # Módulo MCU (prefijo: MCU)
├── GLOSSARY/                         # Glosario expandido
├── WIKI/                             # Documentación complementaria
└── ci/                               # Workflows CI/CD
```

## Carpeta 00-META/ (Centro de Control)

```
00-META/
├── 🤖 DIRECTIVAS PARA IA
│   ├── ia-contract.md                # LEY SUPREMA - Reglas fundamentales
│   └── ai-directives.md              # Reglas técnicas complementarias
│
├── 📏 ESTÁNDARES Y NORMAS
│   ├── nomenclatura-estandar.md      # Convenciones de nombrado
│   ├── notation-cheatsheet.md        # Símbolos y notación estándar
│   └── bibliografia-general.md       # Fuentes académicas autorizadas
│
├── 🔍 HERRAMIENTAS DE AUDITORÍA
│   ├── audit-file-list.md            # Lista de archivos obligatorios
│   ├── audit-table-issues.md         # Registro de problemas
│   ├── directory-tree.md             # Este archivo
│   └── repo-tests.md                 # Pruebas de integridad
│
├── 🎓 RECURSOS PARA USUARIOS
│   ├── study-guide.md                # Guía de navegación
│   ├── prompts-for-students.md       # Prompts prediseñados para IA
│   └── plantilla-respuestas.md       # Modelo para soluciones
│
├── 📄 templates/                     # Plantillas reutilizables
│   ├── directives.template.md
│   ├── manifest.template.json
│   └── metadata-header.template.md
│
└── 🔧 tools/                         # Scripts de automatización
    ├── validate_repo.py              # Auditor de estructura
    ├── link_knowledge_base.py        # Auto-vinculador al glosario
    ├── fix_manifests_and_names.py    # Corrector de manifests
    ├── check_tables.py               # Validador de tablas Markdown
    ├── check_links.py                # Verificador de enlaces
    └── validate_metadata.py          # Validador de bloques ::METADATA::
```

## Estructura de Módulo (Nivel 1)

```
XX-[Nombre-Modulo]/
├── 00-Index.md                       # Índice del módulo
├── XX-01-[subtema]/                  # Subtemas...
├── XX-02-[subtema]/
└── XX-NN-[subtema]/
```

## Estructura de Subtema (Nivel 2)

```
XX-NN-[nombre-subtema]/
├── 📋 CONFIGURACIÓN
│   ├── manifest.json                 # Metadatos del subtema
│   └── [PREFIX]-NN-directives.md     # Instrucciones específicas
│
├── 📚 CONTENIDO PRINCIPAL
│   ├── [PREFIX]-NN-Intro.md          # Punto de entrada
│   └── [PREFIX]-NN-Resumen-Formulas.md  # Cheatsheet
│
├── 📖 CARPETAS SEMÁNTICAS
│   ├── theory/                       # Desarrollo teórico
│   │   └── [PREFIX]-NN-Teoria-*.md
│   ├── methods/                      # Procedimientos
│   │   └── [PREFIX]-NN-Metodos-*.md
│   ├── problems/                     # Ejercicios
│   │   └── [PREFIX]-NN-Problemas.md
│   └── solutions/                    # Respuestas
│       ├── [PREFIX]-NN-Respuestas.md           # Nivel 1
│       ├── [PREFIX]-NN-Soluciones-Desarrolladas.md  # Nivel 2
│       └── prob-XX/                            # Nivel 3
│
├── 📁 RECURSOS
│   ├── applications/                 # Casos de uso reales
│   ├── media/                        # Recursos visuales
│   │   └── generated/                # Auto-generados
│   └── diagnostic/                   # Evaluaciones (opcional)
│
└── 🔓 SANDBOX
    └── Notas/                        # Zona libre sin validación
        └── README.md                 # Directiva de excepción
```

## Ejemplo: Diseño Digital

```
01-Diseno-Digital/
├── 00-Index.md
├── 01-01-sistemas-numericos/
│   ├── manifest.json
│   ├── DD-01-directives.md
│   ├── DD-01-Intro.md
│   ├── DD-01-Resumen-Formulas.md
│   ├── theory/
│   │   └── DD-01-Teoria-SistemasNumericos.md
│   ├── methods/
│   │   └── DD-01-Metodos-Conversiones.md
│   ├── problems/
│   │   └── DD-01-Problemas.md
│   ├── solutions/
│   │   ├── DD-01-Respuestas.md
│   │   └── prob-01/
│   ├── applications/
│   └── media/
├── 01-02-algebra-booleana/
├── 01-03-compuertas-logicas/
├── 01-04-circuitos-combinacionales/
├── 01-05-circuitos-secuenciales/
├── 01-06-contadores-registros/
└── 01-07-memorias/
```

---

> 📝 **Última actualización:** 2026-01-08  
> Usar este árbol como referencia para validar nuevas contribuciones y ubicar archivos faltantes.
