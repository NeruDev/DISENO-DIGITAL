# Contrato IA (Constitucion)

Este documento define el marco operativo para agentes de IA que trabajen en este repositorio. Prioriza consistencia, trazabilidad y seguridad semantica.

## Alcance y objetivos
- Garantizar que el repositorio crezca de forma coherente y verificable.
- Permitir a las IAs asistir en redaccion, validacion, generacion de problemas y soluciones.
- Preservar la fidelidad matematica: no inventar notacion ni resultados.

## Roles y tareas permitidas
- Explicar conceptos con referencias a archivos existentes.
- Generar problemas y soluciones en el sistema de niveles (1, 2, 3) descrito abajo.
- Redactar resumos, glosarios y enlaces cruzados hacia GLOSSARY/ y WIKI/.
- Proponer mejoras de estructura, nomenclatura y metadatos.

## Tareas prohibidas
- Introducir notacion no estandar o ambiguas.
- Modificar resultados matematicos sin justificacion o evidencia.
- Borrar contexto existente (metadatos, manifiestos) salvo orden explicita.
- Insertar dependencias externas sin consenso.

## Sistema de niveles para problemas y soluciones
- Nivel 1 (Esqueleto): planteamiento, variables, supuestos, salida esperada en texto breve.
- Nivel 2 (Respuesta rapida): tabla con resultados clave, formula final y pasos minimos; sin desarrollo largo.
- Nivel 3 (Desarrollo completo): demostraciones, diagramas y pasos detallados; puede incluir latex extenso.

## Estructura global esperada
- Cada tema incluye Intro, Teoria, Metodos, Problemas, Soluciones, Aplicaciones y media asociada.
- Todo subtema mantiene un manifest.json con metadatos obligatorios.
- Archivos siguen la nomenclatura definida en nomenclatura-estandar.md.

## Interaccion con humanos
- Siempre citar rutas de archivo relativas al repositorio.
- Preguntar antes de alterar contenido sensible o borrar material.
- Responder en el idioma del archivo destino (por defecto espanol neutro).

## Interaccion con herramientas
- Ejecutar validaciones locales antes de confirmar cambios (ver repo-tests.md).
- Mantener scripts y plantillas en 00-META sincronizados con el arbol de contenidos.

## Estilo y consistencia
- Usar ASCII por defecto; latex solo donde aporte claridad.
- En tablas LaTeX, preferir \lvert ... \rvert en lugar de |; nunca mezclar $ y \( en la misma celda.
- Referenciar definiciones con enlaces internos al glosario cuando existan terminos ambiguos.

## Salvaguardas
- Ante falta de contexto, detenerse y pedir instrucciones.
- Documentar supuestos y fuentes al generar contenido nuevo.
- Conservar versionado: no sobrescribir plantillas ni manifiestos sin respaldo.
