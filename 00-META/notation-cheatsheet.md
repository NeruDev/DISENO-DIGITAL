# Notation cheatsheet

Referencia rapida de simbolos y estilos usados en el repositorio.

## Conjuntos y constantes
- Naturales: \(\mathbb{N}\), Enteros: \(\mathbb{Z}\), Racionales: \(\mathbb{Q}\), Reales: \(\mathbb{R}\), Complejos: \(\mathbb{C}\).
- Conjunto vacio: \(\varnothing\). Cardinalidad: \(\lvert A \rvert\).
- Intervalos: abierto \((a,b)\), cerrado \([a,b]\), semiabierto \([a,b)\).

## Vectores y matrices
- Vector columna: \(\mathbf{v} = [v_1, v_2, \dots, v_n]^T\).
- Norma: \(\lVert x \rVert_2\); valor absoluto: \(\lvert x \rvert\).
- Matriz identidad: \(I_n\); transpuesta: \(A^T\); inversa: \(A^{-1}\).

## Logica booleana
- AND: \(\land\), OR: \(\lor\), NOT: \(\lnot\), XOR: \(\oplus\).
- Implicacion: \(\Rightarrow\); bicondicional: \(\Leftrightarrow\).
- Tabla de verdad: usar 0/1 o F/V de forma consistente por archivo.

## Circuitos y senales
- Puertas logicas: AND (\(\cdot\)), OR (+), NOT (\(\overline{x}\) o \(x'\)).
- Funciones en forma canonicamente expresadas: SOP (suma de productos), POS (producto de sumas).
- Cronogramas: usar ejes t horizontales y niveles logicos 0/1 claros; incluir etiquetas de flanco.

## Probabilidad y estadistica
- Esperanza: \(\mathbb{E}[X]\); varianza: \(\mathrm{Var}(X)\); probabilidad: \(\mathbb{P}(A)\).
- Distribuciones: Bernoulli \(\mathrm{Bern}(p)\), Binomial \(\mathrm{Bin}(n,p)\), Normal \(\mathcal{N}(\mu,\sigma^2)\).

## Derivacion y limites
- Derivada: \(f'(x)\) o \(\frac{df}{dx}\); parcial: \(\frac{\partial f}{\partial x}\).
- Limite: \(\lim_{x \to a} f(x)\); infinito: \(\infty\).

## Estilo en tablas LaTeX
- Usar \tfrac en fracciones pequenas y \dfrac en ecuaciones display.
- Para condicionales en probabilidades usar \mid: \(\mathbb{P}(A \mid B)\).
- Evitar simbolos ASCII crudos dentro de celdas; preferir comandos LaTeX.
