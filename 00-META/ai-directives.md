# Directrices IA (Reglamento tecnico)

Reglas concretas para que agentes de IA produzcan contenido consistente, seguro y renderizable.

## Formato general
- Idioma: espanol neutro; usar frases cortas y activas.
- Codificacion: ASCII siempre que sea viable; evitar caracteres invisibles.
- No incluir HTML incrustado; solo Markdown y LaTeX cuando sea necesario.

## LaTeX y tablas
- En tablas, envolver toda la expresion en $...$; evitar mezclar inline y display.
- Para valores absolutos usar \lvert x \rvert; para normas \lVert x \rVert.
- Vectores: usar \vec{v} o negritas mathbf{v}; evitar flechas ASCII.
- Conjuntos: \mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}.
- Operadores logicos: \land, \lor, \lnot; usar \oplus para XOR.
- No usar "|" desnudo para condicion en tablas; usar \mid.
- En fracciones dentro de tablas, preferir \tfrac para mantener altura compacta.

## Bloques de solucion
- Nivel 1: breve en prosa; declarar entradas, salidas y supuestos.
- Nivel 2: tabla con columnas "Dato/Resultado" y "Valor"; incluir formula final.
- Nivel 3: desarrollo paso a paso, con ecuaciones numeradas si es largo.

## Estilo de archivos
- Encabezado de metadatos al inicio cuando aplique (titulo, tags, nivel, prerequisitos).
- Nombres de archivos segun nomenclatura-estandar.md.
- Mantener consistencia de secciones: Intro, Teoria, Metodos, Problemas, Soluciones, Aplicaciones.

## Referencias y enlaces
- Usar rutas relativas; apuntar al glosario en GLOSSARY/ cuando el termino exista.
- No crear enlaces rotos: verificar con tools/validate_repo.py y scripts/check_links.py.

## Seguridad y revision
- No introducir dependencias externas en scripts sin validar licencia.
- Si una decision no esta cubierta por estas reglas, detenerse y consultar.
