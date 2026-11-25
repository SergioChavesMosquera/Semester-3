# Punto 11 — Diámetro de un grafo y su complemento

## Respuesta resumida

La proposición es **verdadera** y es un teorema clásico:

> Si un grafo simple $G$ tiene $\operatorname{diám}(G) \ge 4$, entonces su complemento $G^c$ cumple $\operatorname{diám}(G^c) \le 2$.

La idea clave cabe en dos renglones:

> **Idea clave.** Tomo dos vértices $u,v$ con $d_G(u,v)\ge 4$. Como están tan lejos en $G$, ningún vértice puede ser vecino (en $G$) de ambos a la vez; por eso, en el complemento $G^c$, el par $\{u,v\}$ "alcanza" a todo el mundo en un paso, y eso obliga a que cualquier par de vértices esté a distancia $\le 2$ en $G^c$.

El reporte verifica explícitamente que **no quedan huecos lógicos**, en particular el caso delicado *"$x$ cuelga de $u$ en $G^c$ y $y$ cuelga de $v$ en $G^c$"*: ese caso, cuando además $x,y$ son adyacentes en $G$, produce un camino $v\text{–}x\text{–}y\text{–}u$ de longitud $3$ en $G$, lo que contradice $d_G(u,v)\ge 4$. Por lo tanto no puede ocurrir, y el argumento cierra.

A continuación va la **demostración completa, lista para transcribir a mano**, seguida de la verificación de casos y de notas de rigor.

---

## Demostración (para transcribir al cuaderno)

### Definiciones usadas

- **Grafo simple $G=(V,E)$:** conjunto de vértices $V$ y aristas sin bucles ni aristas múltiples. Escribimos $xy\in E$ si $x$ e $y$ son adyacentes en $G$.
- **Complemento $G^c$:** mismo conjunto de vértices $V$; dos vértices distintos $x,y$ son adyacentes en $G^c$ **si y solo si** $xy\notin E$ (es decir, *no* son adyacentes en $G$).
- **Distancia $d_G(x,y)$:** longitud (número de aristas) del camino más corto entre $x$ e $y$ en $G$; si no existe camino, $d_G(x,y)=\infty$. Además $d_G(x,x)=0$.
- **Diámetro:** $\operatorname{diám}(G)=\max_{x,y\in V} d_G(x,y)$, el máximo tomado sobre todos los pares de vértices.
- Observación inmediata usada varias veces: $d_G(x,y)=1 \iff xy\in E$, y $d_G(x,y)\le 2 \iff$ ($x=y$, o $xy\in E$, o $x,y$ tienen un vecino común en $G$).

### Hipótesis

Supongamos que $\operatorname{diám}(G)\ge 4$. Por definición de diámetro como máximo, existen **dos vértices $u,v$** tales que
$$d_G(u,v)\ge 4 .$$
(En particular $d_G(u,v)$ es finita, así que ese máximo se alcanza en un par concreto $u\neq v$.)

Debemos probar que para **todo** par de vértices distintos $x,y\in V$ se cumple $d_{G^c}(x,y)\le 2$. Eso es exactamente $\operatorname{diám}(G^c)\le 2$.

---

### Paso 1 — Lema de los "vecinos comunes prohibidos"

**Lema 1.** Ningún vértice $z\in V$ puede ser adyacente en $G$ a $u$ y a $v$ al mismo tiempo.

**Prueba.** Supongamos, por contradicción, que existe $z$ con $zu\in E$ y $zv\in E$. Entonces $u\text{–}z\text{–}v$ es un camino en $G$ de longitud $2$, luego $d_G(u,v)\le 2$. Esto contradice $d_G(u,v)\ge 4$. $\qquad\blacksquare$

**Consecuencia (reformulación en $G^c$).** Para **todo** vértice $z\in V$:
$$z \text{ no es adyacente en } G \text{ a } u, \quad\text{o}\quad z \text{ no es adyacente en } G \text{ a } v.$$
Traducido al complemento: **todo** vértice $z$ es adyacente en $G^c$ a $u$, o es adyacente en $G^c$ a $v$ (o a ambos). Diremos que $z$ es de **lado $u$** si $z u\notin E$ (equivalentemente, $z$ adyacente a $u$ en $G^c$, tomando $z\neq u$), y de **lado $v$** si $zv\notin E$. El Lema 1 dice: **cada vértice es de lado $u$ o de lado $v$** (posiblemente de ambos).

### Paso 2 — $u$ y $v$ son adyacentes en $G^c$

Como $d_G(u,v)\ge 4 > 1$, no puede ser $uv\in E$ (si lo fuera, $d_G(u,v)=1$). Por lo tanto $uv\notin E$, y por definición de complemento,
$$u \text{ y } v \text{ son adyacentes en } G^c, \qquad\text{es decir } d_{G^c}(u,v)=1 .$$
En el lenguaje del Paso 1: $u$ es de lado $v$ (pues $uv\notin E$) y $v$ es de lado $u$.

### Paso 3 — Afirmación principal: todo par está a distancia $\le 2$ en $G^c$

Sean $x,y\in V$ dos vértices **distintos** cualesquiera. Queremos $d_{G^c}(x,y)\le 2$. Distinguimos dos situaciones.

**Situación 1: $x$ e $y$ NO son adyacentes en $G$ (es decir $xy\notin E$).**
Entonces, por definición de complemento, $x$ e $y$ **sí** son adyacentes en $G^c$, luego
$$d_{G^c}(x,y)=1\le 2 .$$

**Situación 2: $x$ e $y$ SÍ son adyacentes en $G$ (es decir $xy\in E$).**
Entonces en $G^c$ **no** hay arista entre $x$ e $y$, así que $d_{G^c}(x,y)\neq 1$. Basta encontrar un **vecino común en $G^c$**, es decir, un vértice $z\notin\{x,y\}$ con $z$ adyacente en $G^c$ a $x$ y a $y$ (equivalentemente $zx\notin E$ y $zy\notin E$); eso dará el camino $x\text{–}z\text{–}y$ en $G^c$ y por tanto $d_{G^c}(x,y)\le 2$.

Afirmamos que **$u$ o $v$ sirve como ese vecino común**. Según el Paso 1, cada uno de $x$ e $y$ es de lado $u$ o de lado $v$. Analizamos todos los casos.

- **Caso A: $x$ e $y$ son ambos de lado $u$** (es decir $xu\notin E$ y $yu\notin E$).
  Si además $x\neq u$ e $y\neq u$, entonces $u\notin\{x,y\}$ y $u$ es adyacente en $G^c$ tanto a $x$ como a $y$; es el vecino común buscado y $d_{G^c}(x,y)\le 2$.
  Si uno de ellos es $u$, digamos $x=u$ (el caso $y=u$ es idéntico): como $xy\in E$, se tiene $uy\in E$, luego por el Lema 1 **no** puede ser $vy\in E$, es decir $vy\notin E$; y por el Paso 2 también $vu\notin E$, o sea $vx\notin E$. Entonces $v\notin\{x,y\}$ es adyacente en $G^c$ a $x=u$ y a $y$, y de nuevo $d_{G^c}(x,y)\le 2$.

- **Caso B: $x$ e $y$ son ambos de lado $v$** (es decir $xv\notin E$ y $yv\notin E$).
  Simétrico al Caso A intercambiando los papeles de $u$ y $v$: o bien $v$ es vecino común en $G^c$ de $x$ e $y$, o bien (si uno de ellos es $v$) $u$ lo es. En ambos sub-casos $d_{G^c}(x,y)\le 2$.

- **Caso C (el caso delicado): $x$ es SÓLO de lado $u$ e $y$ es SÓLO de lado $v$** (o viceversa). Es decir, $x$ no es de lado $v$ e $y$ no es de lado $u$:
  $$xv\in E \quad\text{y}\quad yu\in E .$$
  (En palabras del enunciado: *$x$ cuelga de $u$ en $G^c$ y $y$ cuelga de $v$ en $G^c$*, pero $x$ está pegado a $v$ en $G$ e $y$ está pegado a $u$ en $G$.)
  **Afirmamos que este caso es imposible bajo la hipótesis de la Situación 2.** En efecto, en la Situación 2 tenemos $xy\in E$. Junto con $xv\in E$ y $yu\in E$, formamos el camino en $G$
  $$v \;\text{–}\; x \;\text{–}\; y \;\text{–}\; u ,$$
  que tiene longitud $3$. Por tanto $d_G(u,v)\le 3$, lo que contradice $d_G(u,v)\ge 4$. La contradicción muestra que el Caso C no puede presentarse: **siempre** estamos en el Caso A o en el Caso B.

Como los Casos A y B son los únicos posibles y en ambos obtuvimos un vecino común en $G^c$, concluimos $d_{G^c}(x,y)\le 2$ también en la Situación 2.

### Paso 4 — Conclusión

En ambas situaciones (Situación 1 y Situación 2), y por tanto para **todo** par de vértices distintos $x,y\in V$, hemos probado
$$d_{G^c}(x,y)\le 2 .$$
En consecuencia $\operatorname{diám}(G^c)=\max_{x,y} d_{G^c}(x,y)\le 2$. En particular $G^c$ es conexo (toda pareja está a distancia finita). Esto es justo lo que se pedía: $\operatorname{diám}(G)\ge 4 \implies \operatorname{diám}(G^c)\le 2$. $\qquad\blacksquare$

---

## Verificación de que no quedan huecos lógicos

1. **Existencia del par $u,v$.** El diámetro es un máximo sobre pares; $\operatorname{diám}(G)\ge 4$ garantiza que existe un par concreto $u\neq v$ con $d_G(u,v)\ge 4$. No hace falta suponer que ese valor sea finito: lo único que usa la demostración es que **no** hay camino de longitud $\le 3$ entre $u$ y $v$, y eso es cierto tanto si $d_G(u,v)$ es un número $\ge 4$ como si es $\infty$. (Ver la nota de rigor sobre grafos desconexos más abajo.)

2. **Cobertura total de pares $x,y$.** La disyunción "Situación 1 ($xy\notin E$) / Situación 2 ($xy\in E$)" es exhaustiva y excluyente para cualquier par de vértices **distintos**. No hay un tercer caso.

3. **El caso explícitamente señalado en el enunciado** —"$x$ adyacente a $u$ en $G^c$ e $y$ adyacente a $v$ en $G^c$"— está tratado así: ese enunciado dice $xu\notin E$ y $yv\notin E$ (ambos de su respectivo lado). Eso NO basta para un problema; el subcaso realmente problemático es cuando *además* $xv\in E$ y $yu\in E$ (Caso C). Ahí se demuestra que, **si** $x,y$ son adyacentes en $G$, aparece el camino $v\text{–}x\text{–}y\text{–}u$ de longitud $3$ y se contradice la hipótesis. Si en cambio $x,y$ **no** son adyacentes en $G$, estamos en la Situación 1 y $d_{G^c}(x,y)=1$ sin más. Por tanto el caso "peligroso" nunca rompe el resultado.

4. **Los Casos A, B, C agotan la Situación 2.** Por el Lema 1 cada vértice es de lado $u$ o de lado $v$. Clasificando $x$ e $y$ según de qué lado(s) son:
   - si ambos comparten el lado $u$ → Caso A;
   - si ambos comparten el lado $v$ → Caso B;
   - si no comparten ningún lado, entonces uno es de lado $u$ pero no $v$ y el otro de lado $v$ pero no $u$ → Caso C (imposible en Situación 2).
   Un vértice que sea de ambos lados cae automáticamente en A y en B, así que siempre hay lado compartido salvo en C. La clasificación es completa.

5. **El vecino común es distinto de $x$ e $y$.** En los Casos A y B se verificó explícitamente el sub-caso en que $u$ (o $v$) coincide con $x$ o $y$, usando el otro vértice ($v$ o $u$) como testigo. Así el vecino común $z$ siempre satisface $z\notin\{x,y\}$, condición necesaria para que $x\text{–}z\text{–}y$ sea un camino de longitud $2$.

6. **No se usan resultados avanzados.** Solo se emplearon: definición de adyacencia, de complemento, de distancia/diámetro, la caracterización $d\le 2$ por vecino común, y razonamiento directo y por contradicción. Nivel de primer curso de matemáticas discretas.

---

## Notas de rigor y variantes

- **Versión fina confirmada.** El enunciado es la forma afilada del teorema. Existe también la versión más débil y conocida: *si $\operatorname{diám}(G)\ge 3$ entonces $\operatorname{diám}(G^c)\le 3$*. El salto a $\ge 4 \Rightarrow \le 2$ es correcto y es exactamente lo que pide el punto. (Ambas son clásicas; la demostración anterior es autocontenida y no las asume.)

- **Grafos desconexos / diámetro infinito.** Si $G$ es desconexo, hay pares con $d_G=\infty$, luego $\operatorname{diám}(G)=\infty\ge 4$. La demostración sigue funcionando: solo se necesita un par $u,v$ con $d_G(u,v)\ge 4$, y el único uso de esa hipótesis es "no existe camino de longitud $\le 3$ entre $u$ y $v$", lo cual es cierto incluso si $d_G(u,v)=\infty$ (están en componentes distintas o muy lejos). El Lema 1 y el Caso C se apoyan únicamente en que no hay caminos cortos $u\!-\!v$, así que el argumento es válido palabra por palabra. Para un estudiante, basta decir "tomo $u,v$ con $d_G(u,v)\ge 4$" sin preocuparse de si es finito o infinito.

- **Por qué falla en diámetro $3$.** El contraejemplo típico (camino $P_4$: $a\!-\!b\!-\!c\!-\!d$, con $\operatorname{diám}=3$) tiene complemento con diámetro $> 2$, lo que muestra que la cota $\ge 4$ en la hipótesis no se puede relajar a $\ge 3$ si se quiere la conclusión $\le 2$. Esto confirma que la versión "afilada" necesita exactamente $\ge 4$. (No es parte de la demostración pedida, pero sirve para no caer en la tentación de probar algo falso.)

- **Simetría del argumento.** Los Casos A y B son uno el reflejo del otro bajo el intercambio $u\leftrightarrow v$; en el cuaderno se puede escribir A en detalle y decir "B es análogo intercambiando $u$ y $v$", ahorrando espacio sin perder rigor.

---

## Conclusión y recomendación de transcripción

- **La proposición es cierta** y la demostración de arriba es correcta, completa y de nivel adecuado.
- **Qué copiar al cuaderno (orden sugerido):** (1) definiciones mínimas; (2) "Sea $d_G(u,v)\ge 4$"; (3) **Lema 1** con su prueba de una línea; (4) Paso 2 ($uv$ adyacentes en $G^c$); (5) Paso 3 con las dos situaciones y, dentro de la Situación 2, los Casos A/B/C (escribir A con detalle, B "análogo", y C como la contradicción del camino de longitud $3$); (6) conclusión $\operatorname{diám}(G^c)\le 2$.
- **El renglón de "idea clave"** se puede poner como encabezado para recordar la intuición en el parcial: *dos vértices muy lejanos en $G$ no tienen vecino común en $G$, así que en $G^c$ el par $\{u,v\}$ domina todo el grafo a distancia $\le 2$.*
- El punto más fácil de olvidar al escribir a mano es el **Caso C** (el camino $v\text{–}x\text{–}y\text{–}u$ de longitud $3$). Es el corazón del argumento; conviene marcarlo.
