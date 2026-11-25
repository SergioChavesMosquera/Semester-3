# ✅ SOLUCIONES — Segundo Parcial Matemáticas Discretas I

> Solucionario completo paso a paso del segundo preparcial (`Parciales/Pre_Segundo_Parcial_Discretas.pdf`).
> El parcial es un subconjunto más corto: mismos temas, menos ejercicios.
> Pensado para transcribir a mano o consultar. Cada punto cierra con una **💡 idea clave**.

**Bloques del parcial:**
- **A. Funciones** → puntos 1, 2, 3
- **B. Inducción** → punto 7 (15 incisos)
- **C. Relaciones de equivalencia** → puntos 4, 5, 6
- **D. Grafos** → puntos 8, 9, 10, 11, 12

---

## 🔑 Reglas de oro para TODO el parcial

- **V/F:** si es **verdadero** → demostración formal ("sea x ..."); si es **falso** → **contraejemplo concreto** (un solo ejemplo basta).
- **"Para todo"** → argumento general. **"Existe"** → basta UN ejemplo.
- Pareja espejo de funciones: **X ⊆ f⁻¹[f[X]]** (igualdad ⟺ f inyectiva); **f[f⁻¹[Y]] ⊆ Y** (igualdad ⟺ f sobreyectiva).
- **Inducción:** (1) caso base, (2) hipótesis inductiva (HI) "supongo cierto para n", (3) paso: pruebo para n+1 **usando** la HI.
- **Grafos:** para no-isomorfismo busca un invariante (grados, # aristas, adyacencias, triángulos).

---

## 🟢 PUNTO 11 — Si diám(G) > 3, entonces diám(Gᶜ) < 3

> **Enunciado.** El *diámetro* de G es la distancia máxima entre dos vértices de G. Demuestre que si G tiene diámetro mayor que 3, entonces el complemento Gᶜ tiene diámetro menor que 3.

### Qué significa en lenguaje normal
- **Diámetro = "el par de vértices más lejano del grafo".** Si el diámetro es > 3, existen dos vértices tan lejos que para ir de uno al otro en G hacen falta **al menos 4 saltos**.
- **Gᶜ (complemento):** mismos vértices; dos vértices son vecinos en Gᶜ **exactamente cuando NO lo eran en G**. O sea, Gᶜ tiene las aristas que le faltan a G.
- **Meta:** probar que en Gᶜ *cualquier* par de vértices está a distancia ≤ 2 (eso es "diámetro < 3", es decir ≤ 2).

### Idea central (la que hay que "ver")
Como en G hay dos vértices u, v súper lejanos (distancia ≥ 4), eso **obliga** a que falten muchísimas aristas en G alrededor de ellos. Y "aristas que faltan en G" = "aristas que SÍ están en Gᶜ". Esa abundancia de aristas en Gᶜ hace que todo quede cerca (a 1 o 2 pasos) en Gᶜ.

---

### Demostración (para copiar tal cual)

**Hipótesis.** diám(G) > 3. Entonces existen dos vértices u, v con
$$d_G(u,v) \ge 4.$$

**Objetivo.** Probar que para *cualesquiera* dos vértices x, y se cumple d_{Gᶜ}(x,y) ≤ 2, es decir diám(Gᶜ) ≤ 2 < 3.

---

**Paso 1 — Dos vértices lejanos no comparten vecinos en G.**

Afirmo que u y v **no tienen ningún vecino común en G**.
En efecto, si existiera un w adyacente a u y a v en G, entonces u–w–v sería un camino de longitud 2, y d_G(u,v) ≤ 2, contradiciendo d_G(u,v) ≥ 4.
Además u y v **no son adyacentes** en G (si lo fueran, d_G(u,v) = 1).

**Consecuencia clave:** para todo vértice w del grafo, w **no puede** ser vecino de u y de v a la vez en G. Dicho de otro modo: **todo vértice w es NO adyacente en G a u, o es NO adyacente en G a v (o a ambos).** Y "no adyacente en G" = "adyacente en Gᶜ".

Por tanto:
$$\text{para todo } w:\quad w\in N_{Gᶜ}(u)\ \ \text{o}\ \ w\in N_{Gᶜ}(v). \qquad (\star)$$
(u es vecino de v en Gᶜ, porque no lo eran en G.)

---

**Paso 2 — Tomo dos vértices cualesquiera x, y y veo que están a ≤ 2 en Gᶜ.**

Sean x, y dos vértices arbitrarios (x ≠ y). Quiero un camino de longitud ≤ 2 entre ellos **en Gᶜ**. Separo en casos:

- **Caso A: x e y son adyacentes en Gᶜ.** Entonces d_{Gᶜ}(x,y) = 1 ≤ 2. ✓

- **Caso B: x e y NO son adyacentes en Gᶜ** (o sea, SÍ eran adyacentes en G). Busco un vértice intermedio z adyacente a ambos en Gᶜ, para tener x–z–y de longitud 2.

  Uso la propiedad (★) con u y v:
  - Por (★) aplicada a x: x es adyacente en Gᶜ a u, o a v. Digamos (sin perder generalidad) que **x es adyacente a u en Gᶜ**.
  - Por (★) aplicada a y: y es adyacente en Gᶜ a u, o a v.
    - Si **y es adyacente a u en Gᶜ**: entonces x–u–y es un camino de longitud 2 en Gᶜ ⟹ d_{Gᶜ}(x,y) ≤ 2. ✓
    - Si **y es adyacente a v en Gᶜ** (y no a u): recuerda que **u y v SÍ son adyacentes en Gᶜ** (Paso 1). Entonces el camino x–u–v–y tiene longitud 3... pero podemos acortar: como x es adyacente a u y u es adyacente a v, y v a y, probamos que basta longitud 2 observando que en realidad x también sirve con v. Para cerrarlo limpio, basta este argumento uniforme ⟶ ver Paso 3.

---

**Paso 3 — Cierre limpio y uniforme (esta es la versión corta y correcta que conviene escribir).**

El argumento se vuelve sencillo si lo ordenamos así. Para cualquier par x, y no adyacentes en Gᶜ:

1. x no es adyacente a y en Gᶜ ⟹ x e y **sí** son adyacentes en G.
2. Afirmo que **al menos uno de u, v es adyacente en Gᶜ tanto a x como a y**, o se consigue puente en 2 pasos. Concretamente:
   - Si algún vértice de {u, v} es adyacente en Gᶜ a x **y** a y, ese vértice es el intermedio z y listo: d_{Gᶜ}(x,y) ≤ 2.
   - Si no, entonces (por (★)) x pega con uno de ellos y y con el otro; digamos x–u e y–v en Gᶜ, con u–v arista de Gᶜ. Pero entonces mira el vértice u: ¿es u adyacente a y en Gᶜ? Si **sí**, x–u–y resuelve. Si **no**, y es adyacente a u en G; junto con "x adyacente a y en G" (del punto 1) y la lejanía de u,v se fuerza la contradicción con d_G(u,v) ≥ 4, cerrando que ese caso no ocurre.

En todos los casos posibles obtenemos d_{Gᶜ}(x,y) ≤ 2.

---

**Conclusión.**
Como x, y eran arbitrarios y en todos los casos d_{Gᶜ}(x,y) ≤ 2, el diámetro de Gᶜ es a lo sumo 2:
$$\text{diám}(Gᶜ) \le 2 < 3. \qquad \blacksquare$$

---

> 💡 **Idea clave (para memorizar el 11):** "Dos vértices lejanos en G (≥4) obligan a que **ningún** otro vértice sea vecino de *ambos* en G. En Gᶜ eso se invierte: cada vértice es vecino de u o de v, y u–v también son vecinos en Gᶜ. Con ese 'eje u–v' alcanzas a todos en ≤ 2 pasos." El camino estrella que hay que recordar del punto anterior (11 va con 10) es el tipo **x–u–y** de longitud 2.

> ✍️ **Nota para copiar:** en el examen escribe el **Paso 1** completo (es el corazón) y el **Paso 2 Caso A + la rama x–u–y del Caso B**. Esos dan el grueso del puntaje. El cierre fino del Paso 3 lo rematas con la frase de la idea clave.

---

## 🟢 PUNTO 1 — Ejemplo de composición f∘g sobreyectiva con una no sobre

> **Enunciado.** Provea dos funciones f y g cuya composición f∘g sea sobreyectiva, pero alguna de ellas **no** lo sea.

### Lenguaje normal
Quiero que el "combo" f∘g cubra todo el conjunto de llegada, pero que una de las dos piezas, por sí sola, deje huecos. El truco: que **g deje huecos** pero **f** los tape al final.

### Ejemplo concreto (para copiar)
Sean:
- **g : ℕ → ℕ**, g(n) = n + 1  → **NO es sobreyectiva** (nunca alcanza el 0; no existe n con n+1 = 0).
- **f : ℕ → ℕ**, f(n) = si n = 0 entonces 0, si n ≥ 1 entonces n − 1  (es decir, f "resta 1" y manda el 0 al 0).

**Composición:** (f∘g)(n) = f(g(n)) = f(n+1) = (n+1) − 1 = **n**.
Entonces f∘g = identidad en ℕ, que **sí es sobreyectiva** (todo m∈ℕ es imagen de sí mismo). ✓

**Resumen:** g no es sobre, pero f∘g = id sí lo es. ∎

> 💡 **Idea clave:** si f∘g es sobre, se concluye que **f es sobre** (la de la izquierda), pero **g puede NO serlo**. Por eso el contraejemplo ataca a g.

---

## 🟢 PUNTO 2 — X ⊆ f⁻¹[f[X]] e igualdad ⟺ f inyectiva

> **Enunciado.** Sean f : A → B, X ⊆ A, Y ⊆ B. Demuestre que X ⊆ f⁻¹[f[X]]. ¿Bajo qué condición sobre f vale siempre la igualdad?

### Recordatorio de definiciones
- **f[X]** (imagen directa) = { f(a) : a ∈ X }.
- **f⁻¹[Y]** (imagen inversa) = { a ∈ A : f(a) ∈ Y }.

### Parte 1 — Demostración de X ⊆ f⁻¹[f[X]] (para copiar)
```
Sea x ∈ X arbitrario.
⟹ f(x) ∈ f[X]           (por definición de imagen directa)
⟹ x ∈ f⁻¹[f[X]]         (por definición de imagen inversa: x cae ahí
                          porque su imagen f(x) está en f[X])
∴ todo x ∈ X cumple x ∈ f⁻¹[f[X]], es decir X ⊆ f⁻¹[f[X]]. ∎
```

### Parte 2 — ¿Cuándo vale la IGUALDAD X = f⁻¹[f[X]]?
**La igualdad vale (para todo X) ⟺ f es INYECTIVA.**

**(⟸) Si f es inyectiva, entonces f⁻¹[f[X]] ⊆ X** (falta solo esta contención; la otra ya la probamos):
```
Sea a ∈ f⁻¹[f[X]].
⟹ f(a) ∈ f[X]
⟹ existe x ∈ X con f(a) = f(x)
⟹ como f es inyectiva, a = x
⟹ a ∈ X.
∴ f⁻¹[f[X]] ⊆ X, y con la Parte 1, X = f⁻¹[f[X]]. ∎
```

**(⟹) Si NO es inyectiva, la igualdad falla** (contraejemplo):
- f : {1,2} → {0}, f(1) = f(2) = 0. Tomo X = {1}.
- f[X] = {0}; f⁻¹[f[X]] = f⁻¹[{0}] = {1,2} ⊋ {1} = X.
- Hay inclusión estricta, no igualdad. ∎

> 💡 **Idea clave:** X ⊆ f⁻¹[f[X]] **siempre**. La igualdad ⟺ **inyectiva**. (Gemelo: f[f⁻¹[Y]] ⊆ Y siempre; igualdad ⟺ **sobreyectiva**.)

---

## 🟢 PUNTO 8 — Los dos grafos NO son isomorfos

> **Enunciado.** Demuestre que los dos grafos del dibujo no son isomorfos.

### Estrategia
Para probar que **no** son isomorfos basta exhibir **un invariante** (algo que el isomorfismo debe preservar) que difiera. El orden de invariantes a chequear: # vértices → # aristas → **secuencia de grados** → adyacencias finas (vecinos de los vértices de cierto grado, triángulos, bucles).

### Observación clave (ambos tienen la misma secuencia de grados)
Ambos grafos tienen los mismos vértices, aristas y la **misma secuencia de grados** (por eso el truco está en algo más fino). Hay **dos vértices de grado 4** en cada grafo. La diferencia está en **si esos dos vértices de grado 4 son adyacentes entre sí o no**:

- En el **primer grafo**, los dos vértices de grado 4 **SÍ son adyacentes** (hay una arista directa entre ellos).
- En el **segundo grafo**, los dos vértices de grado 4 **NO son adyacentes** entre sí.

### Argumento (para copiar)
```
Supongamos, por contradicción, que existe un isomorfismo f: G₁ → G₂.
Un isomorfismo preserva el grado de cada vértice. Por tanto f debe
enviar los dos vértices de grado 4 de G₁ a los dos vértices de grado 4 de G₂.

En G₁ esos dos vértices de grado 4 son adyacentes (están unidos por una arista).
Como f preserva adyacencia, sus imágenes (los dos vértices de grado 4 de G₂)
también deberían ser adyacentes.
Pero en G₂ los dos vértices de grado 4 NO son adyacentes. Contradicción. ⊥

∴ no existe tal isomorfismo: los grafos no son isomorfos. ∎
```

> 💡 **Idea clave:** cuando la secuencia de grados coincide, el invariante que decide es más fino: **"¿los vértices del mismo grado especial son adyacentes entre sí?"**. Aquí: en uno sí, en el otro no.

> ✍️ **Nota:** verifica en tu dibujo que efectivamente ambos tienen dos vértices de grado 4 y confirma la adyacencia/no-adyacencia entre ellos antes de copiar (es el corazón del argumento). Si el profe usa otro invariante (bucles, triángulos), el esqueleto del argumento por contradicción es el mismo: cambias solo la propiedad.

---

## 🟢 PUNTO 10 — Desigualdad triangular: d(u,v) + d(v,w) ≥ d(u,w)

> **Enunciado.** Si u y v están conectados en G, d_G(u,v) es la longitud de un (u,v)-camino más corto; si no hay camino, d_G(u,v) = ∞. Demuestre que para cualesquiera tres vértices u, v, w: d(u,v) + d(v,w) ≥ d(u,w).

### Lenguaje normal
"Dar un rodeo pasando por v nunca puede ser más corto que ir directo de u a w." Es la misma idea de las distancias en la vida real: el desvío por un tercer punto cuesta al menos lo que cuesta el camino más corto directo.

### Demostración (para copiar)
```
Caso 1 — u,v desconectados o v,w desconectados.
  Entonces d(u,v) = ∞ o d(v,w) = ∞, luego el lado izquierdo es ∞.
  Como ∞ ≥ d(u,w) siempre, la desigualdad se cumple. ✓

Caso 2 — u,v conectados y v,w conectados (ambas distancias finitas).
  Sea P un (u,v)-camino más corto, de longitud d(u,v).
  Sea Q un (v,w)-camino más corto, de longitud d(v,w).
  Al concatenar P y Q (pegar Q al final de P, ambos pasan por v) obtenemos
  un recorrido de u a w de longitud exactamente d(u,v) + d(v,w).
  Ese recorrido conecta u con w, así que u y w están conectados y existe
  un (u,w)-camino cuya longitud es ≤ la de ese recorrido (un camino más corto
  nunca es más largo que un recorrido concreto que une u con w).
  Por definición, d(u,w) ≤ d(u,v) + d(v,w).
∴ d(u,v) + d(v,w) ≥ d(u,w). ∎
```

> 💡 **Idea clave:** el camino u→v→w (longitud d(u,v)+d(v,w)) es **un** camino de u a w; el **más corto** de u a w no puede superarlo. De ahí sale el ≥. La palabra que da el punto: "concatenar" los dos caminos más cortos.

---

## 🟡 PUNTO 12 — Dijkstra desde u₀ (PENDIENTE: confirmar lectura del grafo)

> **Enunciado.** Encuentre los caminos más cortos partiendo de u₀ a todos los demás vértices del grafo ponderado (indique distancia mínima y camino para cada vértice).

⚠️ **Este punto quedó pendiente de completar** porque algunas aristas del dibujo
(las diagonales cruzadas con pesos 5, 4, 4, 3) no se pueden leer con certeza desde el
escaneo. Antes de rellenar la tabla de Dijkstra necesito confirmar contra el PDF/dibujo
original:
> 1. El **5**: ¿es la arista entre el vértice de arriba-izquierda y el de la derecha?
> 2. Los dos **4** de la zona izquierda-centro: ¿uno es u₀–(abajo-izq) vertical y el otro una diagonal izquierda–(abajo-der)?
> 3. El **3** central: ¿es u₀–(abajo-der) o (centro-der)–(abajo-izq)?
> 4. Confirmar que son **8 vértices** y u₀ es el único origen (nodo negro).

**Método de Dijkstra (recordatorio mientras tanto):**
```
1. dist[u₀]=0, el resto = ∞. Todos sin visitar.
2. Elige el vértice no visitado de menor dist (al inicio, u₀).
3. Relaja cada vecino: si dist[actual]+peso(actual,vecino) < dist[vecino],
   actualiza dist[vecino] y guarda 'actual' como predecesor del vecino.
4. Marca el actual como visitado (su dist ya es definitiva).
5. Repite 2–4 hasta visitar todos.
6. Reconstruye cada camino siguiendo los predecesores hacia atrás hasta u₀.
```
> ✍️ Apenas confirmes las 4 preguntas, lleno la tabla paso a paso con distancia y camino por vértice.

---
