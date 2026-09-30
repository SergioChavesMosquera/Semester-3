# Taller 1 – Álgebra Lineal, EXPLICADO DESDE CERO
UNAL · Prof. Leonardo A. Cano G.

Esta versión asume que no te acuerdas de nada. Cada ejercicio explica QUÉ es cada cosa, POR QUÉ se hace cada paso, y luego el procedimiento completo. Transcribe esto y luego repite el taller original con tus valores usando el mismo razonamiento.

---

# PARTE 0 — Conceptos base (defínelos así en tu cuaderno)

### ¿Qué es un vector?
Un vector es una "flecha" que representa una magnitud con dirección. En el espacio 3D lo escribimos como `v = (v1, v2, v3)`, donde cada número es cuánto avanza el vector en el eje x, y, z respectivamente. Ejemplo: `v=(2,1,-1)` significa "avanza 2 en x, 1 en y, retrocede 1 en z".

Un **punto** `(x0,y0,z0)` es una posición fija en el espacio. Un vector no tiene posición fija: solo tiene dirección y tamaño. Pero podemos "anclar" un vector a un punto para formar una recta (ver más abajo).

### ¿Qué es la norma de un vector?
La **norma** (o magnitud, o longitud) de un vector es qué tan "largo" es, es decir, la distancia desde el origen hasta la punta de la flecha. Se calcula con el Teorema de Pitágoras extendido a 3D:

`|v| = √(v1² + v2² + v3²)`

Ejemplo: si `v=(3,4,0)`, entonces `|v| = √(9+16+0) = √25 = 5`.

Un **vector unitario** es un vector de norma 1 (longitud 1). Para "unitarizar" cualquier vector, lo divides entre su propia norma: `û = v/|v|`. Esto no cambia la dirección, solo lo "encoge" o "estira" para que mida exactamente 1. Se usa mucho porque nos deja movernos "una unidad de distancia" en una dirección específica.

### ¿Qué es el producto punto (o producto escalar)?
Toma dos vectores y da como resultado UN NÚMERO (no un vector). Sirve principalmente para dos cosas: (1) saber el ángulo entre dos vectores, y (2) saber si dos vectores son perpendiculares.

`u·v = u1v1 + u2v2 + u3v3`

**Dato clave que vas a usar en casi todo el taller:** si `u·v = 0`, entonces u y v son PERPENDICULARES (forman 90°). Esto es la base de casi todos los ejercicios de "encuentre una recta dentro de un plano" o "encuentre un vector perpendicular a otro".

**Fórmula del ángulo entre vectores:**
`cosθ = (u·v) / (|u|·|v|)`

Esto sale de la definición geométrica del producto punto; no necesitas memorizar de dónde sale, solo usarla.

### ¿Qué es el producto cruz?
Toma dos vectores y da como resultado OTRO VECTOR (no un número), que tiene la característica de ser **perpendicular a los dos vectores originales al mismo tiempo**. Se usa cuando necesitas "generar" una dirección perpendicular a un plano, dado que conoces dos direcciones que están DENTRO de ese plano.

`u×v = (u2v3−u3v2,  u3v1−u1v3,  u1v2−u2v1)`

Truco para no confundirte con la fórmula (regla mnemotécnica): tapa la primera columna y cruza en X las que quedan (u2v3−u3v2), tapa la segunda columna y cruza en X invertido (u3v1−u1v3), tapa la tercera y cruza en X (u1v2−u2v1).

### ¿Qué es un plano y qué significa su ecuación?
Un plano es una "hoja" infinita y plana en el espacio 3D. Su ecuación se escribe:

`ax + by + cz = d`

El vector `n=(a,b,c)` (los coeficientes de x,y,z) se llama **vector normal** del plano: es un vector PERPENDICULAR a todo el plano (imagina un palillo de dientes clavado perpendicularmente en una hoja de papel — esa es la normal). Esto es clave: **conocer la normal es conocer "hacia dónde mira" el plano**.

- Si tienes un punto `P0=(x0,y0,z0)` y sabes la normal `n=(a,b,c)`, el plano que pasa por P0 con esa normal es: `a(x−x0)+b(y−y0)+c(z−z0)=0`, que reordenando da `ax+by+cz = ax0+by0+cz0 = d`.
- Dos planos son PARALELOS si sus normales son paralelas (una es múltiplo de la otra, ej: `(2,-1,0)` y `(4,-2,0)`).
- El ÁNGULO entre dos planos es el mismo que el ángulo entre sus normales (usas la fórmula de ángulo entre vectores, pero con las normales).

### ¿Qué es una recta en el espacio y qué es un "vector director"?
Una recta se define con: (1) un punto por donde pasa, `P0=(x0,y0,z0)`, y (2) un **vector director** `v=(v1,v2,v3)` que indica hacia dónde avanza. La ecuación paramétrica es:

`(x,y,z) = P0 + t·v = (x0+t·v1, y0+t·v2, z0+t·v3)`

Aquí `t` es un parámetro (un número que "recorre" la recta: en t=0 estás en P0, en t=1 avanzaste una vez el vector v, etc.)

**¿Cuándo una recta está DENTRO de un plano?** Se necesitan dos condiciones:
1. El punto `P0` de la recta debe cumplir la ecuación del plano (estar sobre él).
2. El vector director `v` de la recta debe ser PERPENDICULAR a la normal del plano, es decir `v·n = 0` (esto significa que la recta "no se sale" del plano, se queda acostada dentro de él).

### ¿Qué significa "trayectoria" y la diferencia entre "cruzarse" y "chocar"?
Una trayectoria es una recta pero donde el parámetro `t` representa TIEMPO: `r(t) = P0 + (t−t0)·v` (en el instante `t0` el objeto está en el punto P0).

- **Se cruzan (intersectan):** sus caminos (las rectas) comparten un punto, pero cada objeto pasa por ahí en un momento distinto → no chocan.
- **Se estrellan (chocan):** ambos objetos están en el MISMO punto en el MISMO instante t.

### Fórmulas de distancia (las 3 que vas a necesitar)

**Distancia de un punto a un plano:**
`dist = |a·x0 + b·y0 + c·z0 − d| / |n|`
(evalúas el punto en la ecuación del plano, restas d, tomas valor absoluto, divides por la norma de la normal)

**Planos paralelos a distancia k de otro plano `ax+by+cz=d`:**
`ax+by+cz = d ± k·|n|`
(hay dos soluciones: una sumando, otra restando — por eso casi siempre piden "los dos planos")

**Distancia entre dos puntos:**
`dist = √((x2−x1)² + (y2−y1)² + (z2−z1)²)` — es la norma del vector que va de un punto al otro.

---

# PARTE 1 — Los 13 ejercicios, paso a paso

## Ejercicio 1
**Enunciado (con valores cambiados):** Encuentre los dos planos a una distancia 4 del plano `3x + y = 2`.

**Razonamiento:** "Planos a distancia k de otro plano" siempre son PARALELOS al original (si no fueran paralelos, la distancia entre ellos no sería constante en todos los puntos). Y como vimos arriba, planos paralelos a distancia k se obtienen con la fórmula `ax+by+cz = d ± k|n|`. Solo necesito identificar la normal del plano original y su norma.

**Paso 1 — Identificar la normal.**
El plano `3x+y=2` en realidad es `3x+1y+0z=2` (el coeficiente de z es 0 porque no aparece). Entonces `n=(3,1,0)`.

**Paso 2 — Calcular la norma de esa normal.**
`|n| = √(3²+1²+0²) = √(9+1) = √10`

**Paso 3 — Aplicar la fórmula de planos paralelos a distancia k=4.**
`3x+y = 2 ± 4·√10`

**Respuesta final:**
`3x+y = 2+4√10` y `3x+y = 2−4√10`

(Estos dos planos son paralelos al original, uno "más allá" y otro "más acá", ambos a exactamente 4 unidades de distancia.)

---

## Ejercicio 2
**Enunciado:** Encuentre una recta paralela al plano `x+2y−z=3` y a una distancia 5 del mismo.

**Razonamiento:** Una recta es "paralela a un plano" si vive completamente en un plano paralelo al dado. Entonces el truco es: primero encuentro el plano paralelo a distancia 5 (igual que en el ejercicio 1), y luego dentro de ESE plano elijo cualquier recta (un punto + un vector director perpendicular a la normal).

**Paso 1 — Normal y su norma.**
`n=(1,2,-1)`, `|n| = √(1+4+1) = √6`

**Paso 2 — Plano paralelo a distancia 5** (tomo el signo +, cualquiera de los dos sirve):
`x+2y−z = 3+5√6`

**Paso 3 — Encontrar un punto dentro de ese plano nuevo.**
La forma más fácil es fijar dos variables en 0 y despejar la tercera. Hago `y=0, z=0`:
`x = 3+5√6` → el punto es `P0=(3+5√6, 0, 0)`

**Paso 4 — Encontrar un vector director `v` que esté "acostado" en ese plano.**
Recuerda: `v` debe cumplir `v·n=0`. Pruebo con `v=(2,-1,0)` y verifico:
`v·n = 2(1)+(-1)(2)+0(-1) = 2-2+0 = 0` ✓ (funciona)

*¿Cómo se me ocurrió (2,-1,0)? Truco rápido: si la normal es `(a,b,c)`, un vector perpendicular fácil de encontrar es `(b,-a,0)` (intercambias los dos primeros números y le pones un signo negativo a uno). Aquí `n=(1,2,-1)` → `(2,-1,0)`. Siempre verifica con el producto punto que dé 0.*

**Respuesta final:**
`(x,y,z) = (3+5√6, 0, 0) + t(2,-1,0)`

---

## Ejercicio 3
**Enunciado:** Encuentre una recta paralela al vector `(2,1,-1)` y a una distancia 3 del punto `(0,2,-3)`.

**Razonamiento:** Aquí NO me dan un plano ni un punto de la recta — me dan un vector director y quieren que la recta pase "cerca" de un punto dado, a exactamente 3 unidades. Hay infinitas rectas que cumplen esto (puedo rotar alrededor del punto), así que construyo UNA: parto del punto dado, me desplazo 3 unidades en cualquier dirección PERPENDICULAR al vector director (para que la distancia mínima entre el punto y la recta sea justo esas 3 unidades), y ese es el punto de anclaje de mi recta.

**Paso 1 — Encontrar un vector `w` perpendicular a `v=(2,1,-1)`.**
Uso el mismo truco: intercambio y cambio signo de dos componentes, dejando la tercera en 0. Pruebo `w=(1,-2,0)`:
`w·v = 1(2)+(-2)(1)+0(-1) = 2-2+0 = 0` ✓

**Paso 2 — Convertir `w` en vector unitario (longitud 1), para poder "caminar" exactamente 3 unidades con él.**
`|w| = √(1+4+0) = √5`
`ŵ = w/|w| = (1/√5, -2/√5, 0)`

**Paso 3 — Desde el punto dado `Q=(0,2,-3)`, avanzo 3 unidades en la dirección `ŵ` para obtener el punto de anclaje `P0` de mi recta.**
`P0 = Q + 3·ŵ = (0,2,-3) + 3(1/√5, -2/√5, 0) = (3/√5, 2-6/√5, -3)`

*¿Por qué esto garantiza distancia 3? Porque me moví en línea recta, perpendicularmente al vector director, una distancia de exactamente 3 (3 veces un vector de longitud 1 = longitud 3). Y la distancia mínima de un punto a una recta se mide justamente de forma perpendicular.*

**Respuesta final:**
`(x,y,z) = (3/√5, 2-6/√5, -3) + t(2,1,-1)`

---

## Ejercicio 4
**Enunciado:** Encuentre los dos vectores unitarios que forman un ángulo de `π/3` (60°) con el vector `(3,4)`.

**Razonamiento:** Quiero "girar" el vector dado 60° hacia un lado y 60° hacia el otro lado. Para girar un vector en el plano 2D un ángulo θ, existe la fórmula de rotación (esto sale de trigonometría, la das por hecha):

`vector rotado = (x·cosθ − y·senθ,  x·senθ + y·cosθ)`

**Paso 1 — Convertir `(3,4)` en vector unitario** (porque quiero que la respuesta sea unitaria; si giro un vector, su longitud no cambia, así que si parto de uno unitario, el resultado también será unitario).
`|(3,4)| = √(9+16) = 5`
`û = (3/5, 4/5)`

**Paso 2 — Aplicar la fórmula de rotación con θ=60°.** Recuerda `cos60°=1/2`, `sen60°=√3/2`.

Rotación de +60°:
`x' = (3/5)(1/2) − (4/5)(√3/2) = 3/10 − 4√3/10 = (3−4√3)/10`
`y' = (3/5)(√3/2) + (4/5)(1/2) = 3√3/10 + 4/10 = (4+3√3)/10`

Rotación de −60° (mismo procedimiento pero con `cos(−60°)=1/2`, `sen(−60°)=−√3/2`):
`x'' = (3/5)(1/2) − (4/5)(−√3/2) = 3/10+4√3/10 = (3+4√3)/10`
`y'' = (3/5)(−√3/2) + (4/5)(1/2) = −3√3/10+4/10 = (4−3√3)/10`

**Respuesta final:**
`v1 = ((3−4√3)/10, (4+3√3)/10)` y `v2 = ((3+4√3)/10, (4−3√3)/10)`

---

## Ejercicio 5
**Enunciado:** Encuentre dos planos que formen un ángulo de `π/4` (45°) con el plano `2x−y=3`.

**Razonamiento:** El ángulo entre dos planos = el ángulo entre sus normales (repaso de la Parte 0). Entonces este ejercicio es IDÉNTICO al ejercicio 4, pero en vez de rotar un vector cualquiera, rotamos la NORMAL del plano. Como la normal `n=(2,-1,0)` no tiene componente en z, la rotación se puede hacer directamente en el plano XY, igual que en el ejercicio 4.

**Paso 1 — Rotar `(2,-1)` por +45°** (`cos45°=sen45°=√2/2`):
`x' = 2(√2/2) − (-1)(√2/2) = √2 + √2/2 = 3√2/2`
`y' = 2(√2/2) + (-1)(√2/2) = √2 − √2/2 = √2/2`
Esto da el vector `(3√2/2, √2/2)`, que simplificando (dividiendo entre `√2/2`) es proporcional a `(3,1)`.

**Paso 2 — Rotar `(2,-1)` por −45°:**
`x'' = 2(√2/2) + (-1)(√2/2) = √2/2`
`y'' = -2(√2/2) + (-1)(√2/2) = -3√2/2`
Proporcional a `(1,-3)`.

**Paso 3 — Verificación (opcional pero recomendable):**
`cosθ = ((2)(3)+(-1)(1)+0) / (√5·√10) = 5/√50 = 5/(5√2) = 1/√2 = √2/2` → efectivamente θ=45° ✓

**Paso 4 — Escribir los planos con esas normales.**
El valor de `d` (el número del lado derecho) es libre — no afecta el ángulo, solo desplaza el plano. Elegimos d=0 por simplicidad.

**Respuesta final:**
`3x+y=0` y `x−3y=0`

---

## Ejercicio 6
**Enunciado:** Encuentre dos trayectorias con velocidades `(1,2,-1)` y `(3,-1,2)` que se intersecten en el punto `(2,0,1)` pero NO se estrellen.

**Razonamiento:** "Se intersectan pero no se estrellan" significa que ambos caminos pasan por el mismo punto, pero en tiempos diferentes. La forma más fácil: hago que la trayectoria 1 pase por el punto en `t=0`, y la trayectoria 2 pase por el mismo punto en un tiempo distinto, por ejemplo `t=1`.

**Paso 1 — Trayectoria 1, que pase por `(2,0,1)` en `t=0`.**
Fórmula: `r(t) = P0 + (t−t0)·v`. Aquí `t0=0`, `P0=(2,0,1)`, `v=(1,2,-1)`:
`r1(t) = (2,0,1) + t(1,2,-1)`

**Paso 2 — Trayectoria 2, que pase por el MISMO punto pero en `t=1` (no en t=0).**
`r2(t) = (2,0,1) + (t−1)(3,-1,2)`

**Comprobación:** en `t=0`, `r1(0)=(2,0,1)` (está ahí). En `t=1`, `r2(1)=(2,0,1)` (está ahí, pero un instante después). Como nunca coinciden en el mismo t en ese punto, no chocan, solo se cruzan.

---

## Ejercicio 7
**Enunciado:** Encuentre dos trayectorias con velocidades `(2,-1,1)` y `(1,3,-2)` que SÍ se estrellen en el punto `(0,2,-1)`, en el tiempo `t=3`.

**Razonamiento:** Ahora es al revés del ejercicio 6: quiero que ambas pasen por el mismo punto en el MISMO instante `t=3`. Uso la misma fórmula pero con `t0=3` para ambas.

**Paso 1 — Trayectoria 1:**
`r1(t) = (0,2,-1) + (t−3)(2,-1,1)`

**Paso 2 — Trayectoria 2:**
`r2(t) = (0,2,-1) + (t−3)(1,3,-2)`

**Comprobación:** en `t=3`, el factor `(t-3)=0` para ambas, entonces `r1(3)=r2(3)=(0,2,-1)` → mismo punto, mismo instante → chocan.

---

## Ejercicio 8
**Enunciado:** Encuentre una recta con vector velocidad `(2,1,-1)` que se estrelle con el plano `x+2y-z=4` en el tiempo `t=2`.

**Razonamiento:** "Chocar con un plano en t=2" significa que en ese instante, la posición de la recta debe caer exactamente SOBRE el plano. Entonces: (1) elijo cualquier punto Q que esté en el plano, y (2) armo la trayectoria para que llegue justo a Q cuando t=2.

**Paso 1 — Encontrar un punto Q del plano** `x+2y-z=4`. Fijo `y=0, z=0`:
`x=4` → `Q=(4,0,0)`. Verifico: `4+2(0)-0=4` ✓

**Paso 2 — Construir la recta para que en `t=2` esté en Q.**
`r(t) = Q + (t−2)·v = (4,0,0) + (t-2)(2,1,-1)`

**Comprobación:** en `t=2`, el factor `(t-2)=0`, entonces `r(2)=(4,0,0)=Q`, que está en el plano ✓

**Respuesta final:**
`r(t) = (4+2(t-2), t-2, -(t-2))`

---

## Ejercicio 9
**Enunciado:** Encuentre dos rectas con vectores directores NO paralelos, ambas dentro del plano `x+2y-z=3`.

**Razonamiento:** Recuerda de la Parte 0: una recta está "dentro" de un plano si (1) su punto de anclaje cumple la ecuación del plano, y (2) su vector director es perpendicular a la normal (`v·n=0`). Necesito dos vectores `v1`, `v2` que cumplan `v·n=0`, pero que NO sean múltiplos entre sí (para que las rectas no sean paralelas).

**Paso 1 — Normal:** `n=(1,2,-1)`

**Paso 2 — Primer vector director** usando el truco de intercambiar/cambiar signo: `v1=(2,-1,0)`.
Verifico: `2(1)+(-1)(2)+0(-1) = 2-2 = 0` ✓

**Paso 3 — Segundo vector director, DIFERENTE del primero.** Pruebo `v2=(1,0,1)`.
Verifico: `1(1)+0(2)+1(-1) = 1-1 = 0` ✓ y no es múltiplo de `v1` (uno tiene ceros en posiciones distintas) → no son paralelos.

**Paso 4 — Un punto común dentro del plano** (fijo `y=0,z=0`): `x=3` → `P0=(3,0,0)`

**Respuesta final:**
`L1: (3,0,0)+t(2,-1,0)` y `L2: (3,0,0)+s(1,0,1)`

---

## Ejercicio 10
**Enunciado:** Encuentre dos puntos DENTRO del plano `x+3y-2z=4` cuya distancia entre ellos sea 3.

**Razonamiento:** Tomo un punto cualquiera del plano, y me "desplazo" desde ahí una distancia de 3 unidades, pero MOVIÉNDOME EN UNA DIRECCIÓN QUE NO ME SAQUE DEL PLANO (es decir, una dirección perpendicular a la normal). Así el punto de llegada también estará en el plano.

**Paso 1 — Un punto A del plano** (`y=0,z=0`): `x=4` → `A=(4,0,0)`

**Paso 2 — Una dirección `v` dentro del plano** (`v·n=0`, con `n=(1,3,-2)`): pruebo `v=(3,-1,0)`:
`3(1)+(-1)(3)+0(-2) = 3-3=0` ✓

**Paso 3 — Unitarizar v** para poder desplazarme exactamente 3 unidades:
`|v|=√(9+1)=√10` → `v̂=(3/√10, -1/√10, 0)`

**Paso 4 — Calcular el segundo punto B:**
`B = A + 3·v̂ = (4+9/√10, -3/√10, 0)`

**Respuesta final:**
`A=(4,0,0)`, `B=(4+9/√10, -3/√10, 0)`, con `|AB|=3` garantizado por construcción.

---

## Ejercicio 11
**Enunciado:** Encuentre dos planos cuya intersección sea exactamente la recta `(x,y,z)=(1,0,-2)+t(2,-1,3)`.

**Razonamiento:** Cuando dos planos se cruzan, su intersección es una recta. Para que esa recta sea justo la que me dan, necesito que: (1) AMBOS planos contengan el punto `(1,0,-2)`, y (2) las normales de ambos planos sean perpendiculares al vector director `v=(2,-1,3)` (porque la recta debe "acostarse" dentro de cada plano, igual que en ejercicios anteriores).

**Paso 1 — Buscar una primera normal `n1` perpendicular a `v=(2,-1,3)`.**
Pruebo `n1=(1,2,0)`: `2(1)+(-1)(2)+3(0) = 2-2=0` ✓

**Paso 2 — Construir el plano 1** usando el punto `(1,0,-2)`:
`n1·(x,y,z) = n1·(1,0,-2)` → `1x+2y+0z = 1(1)+2(0)+0(-2) = 1`
→ **Plano 1: `x+2y=1`**

**Paso 3 — Buscar una segunda normal `n2`, diferente de n1, también perpendicular a v.**
Pruebo `n2=(3,0,-2)`: `2(3)+(-1)(0)+3(-2) = 6-6=0` ✓

**Paso 4 — Construir el plano 2:**
`3x+0y-2z = 3(1)+0(0)-2(-2) = 3+4=7`
→ **Plano 2: `3x-2z=7`**

**Paso 5 — Verificación (para estar seguro que la intersección es correcta):**
El producto cruz de las dos normales debe dar un vector paralelo al director de la recta:
`n1×n2 = (2·(-2)-0·0, 0·3-1·(-2), 1·0-2·3) = (-4,2,-6)`
Y en efecto `(-4,2,-6) = -2·(2,-1,3)` → es paralelo a `v` ✓ (confirma que está bien)

---

## Ejercicio 12
**Enunciado:** Muestre que el producto cruz NO es asociativo (es decir, que `(a×b)×c ≠ a×(b×c)` en general).

**Razonamiento:** Para "demostrar que algo NO se cumple siempre", basta con dar UN solo ejemplo (contraejemplo) donde falle. No hace falta una demostración general.

**Elijo tres vectores sencillos:** `a=(1,0,0)`, `b=(1,1,0)`, `c=(0,1,1)`

**Paso 1 — Calcular `a×b`:**
`a×b = (0·0-0·1, 0·1-1·0, 1·1-0·1) = (0,0,1)`

**Paso 2 — Calcular `(a×b)×c`:**
`(0,0,1)×(0,1,1) = (0·1-1·1, 1·0-0·1, 0·1-0·0) = (-1,0,0)`

**Paso 3 — Calcular `b×c`:**
`b×c = (1,1,0)×(0,1,1) = (1·1-0·1, 0·0-1·1, 1·1-1·0) = (1,-1,1)`

**Paso 4 — Calcular `a×(b×c)`:**
`(1,0,0)×(1,-1,1) = (0·1-0·(-1), 0·1-1·1, 1·(-1)-0·1) = (0,-1,-1)`

**Conclusión:**
`(a×b)×c = (-1,0,0)` mientras que `a×(b×c) = (0,-1,-1)`. Son DIFERENTES → queda demostrado que el producto cruz no es asociativo.

---

## Ejercicio 13
**Enunciado:** Sea el plano `Π: x+y-2z=3`. El punto `P=(3,0,0)` está en Π (verifícalo: `3+0-0=3` ✓). Encuentre un punto `Q` en Π que esté a distancia 4 de P.

**Razonamiento:** Idéntico al ejercicio 10: me muevo desde P una distancia de 4, en una dirección que no me saque del plano (perpendicular a la normal).

**Paso 1 — Normal del plano:** `n=(1,1,-2)`

**Paso 2 — Vector `w` perpendicular a n (dentro del plano):** pruebo `w=(1,-1,0)`:
`1(1)+(-1)(1)+0(-2) = 1-1=0` ✓

**Paso 3 — Unitarizar w:**
`|w|=√(1+1+0)=√2` → `ŵ=(1/√2, -1/√2, 0)`

**Paso 4 — Calcular Q, desplazándome 4 unidades desde P:**
`Q = P + 4ŵ = (3+4/√2, -4/√2, 0) = (3+2√2, -2√2, 0)`

**Comprobación:** `Q` en el plano: `(3+2√2)+(-2√2)-2(0) = 3` ✓ (efectivamente sigue en Π)

**Respuesta final:**
`Q = (3+2√2, -2√2, 0)`

---

# PARTE 2 — Hoja de ruta del curso (Cálculo en Varias Variables, código 1000006)

## Dónde estás ahora
Solo viste la clase del 31 de agosto (superficies cuádricas, inicio de funciones escalares) + 1 clase más sin apuntes. El taller de arriba en realidad es REPASO de prerrequisitos (álgebra lineal: vectores, planos, rectas) que el profe puso porque vas a usarlo constantemente durante todo el semestre.

## Prioridad inmediata (antes de la próxima clase)
1. Vectores en R³ y sus operaciones (todo lo de la Parte 0 de este documento)
2. Ecuación de planos y rectas, y cómo saber si algo está "dentro" de un plano
3. Las 3 fórmulas de distancia
4. Repasar integración básica de una variable (sustitución, por partes) — la vas a necesitar pronto para integrales dobles y triples

## Orden en que verás los temas (según el programa oficial)
1. Superficies cuádricas y de revolución ← estás aquí
2. Funciones escalares de varias variables, curvas y superficies de nivel
3. Límites y continuidad
4. Derivadas parciales (primer orden y superior)
5. Diferencial, plano tangente, recta normal
6. Derivada direccional, gradiente
7. Regla de la cadena, derivada implícita
8. Máximos, mínimos, puntos de silla
9. Multiplicadores de Lagrange
10. Integrales dobles (iteradas, cambio de orden, coordenadas polares)
11. Integrales triples (cilíndricas, esféricas)
12. Campos vectoriales, curvas parametrizadas, vector tangente/normal, curvatura
13. Integral de línea, campos conservativos, Teorema de Green
14. Superficies parametrizadas, integral de superficie
15. Divergencia, rotacional, Teorema de Gauss, Teorema de Stokes

## Evaluación
2 parciales (25% c/u) + final acumulativo (30%) + participación (20%, por cuartil de desempeño en clase). No dejes acumular temas: cada parcial pesa mucho.

## Libro de referencia
Marsden-Tromba, Cálculo Vectorial (el mismo que ya subiste).
