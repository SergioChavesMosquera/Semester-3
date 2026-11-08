# Matemáticas Discretas I — Teoría de Grafos (Introducción) 🕸️

### Clase 4 Nov · Libro: Bondy & Murty, Capítulo 1 · Matemática Estructural

**Leyenda:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Teorema/Propiedad · 🔵 Notación · 🩷 Ejemplo · 💜 Advertencia

> El quiz es una **revisión general introductoria** del Capítulo 1. Enfócate en definiciones, saber leer/dibujar un grafo, grados, matrices y el teorema del apretón de manos.

---

## 1. ¿Qué es un grafo? (idea intuitiva)

- Empezó con el juego: *"¿puedo dibujar esta figura sin levantar el lápiz y sin repetir líneas?"* — ese es el origen histórico de los grafos (puentes de Königsberg).
- 🟢 Un **grafo** es una estructura de **puntos conectados por líneas**.
  - **Vértices (nodos)** = los puntos. Se dibujan como •
  - **Aristas (edges)** = las líneas que unen dos vértices.
- 🔵 En código: librerías `NetworkX`, `igraph` (Python). Vértices = nodes, aristas = edges.

### Definición formal
- 🟢 Un grafo es una **tupla G = (V, E)**:
  - 🔵 **V** = conjunto de **vértices**.
  - 🔵 **E ⊆ V × V** = conjunto de **aristas** (pares de vértices).
- 🟡 Notación del profe: **V(G)** = vértices de G, **E(G)** = aristas de G.
- 💜 Como el grafo **no es dirigido**, la relación de aristas es **simétrica**: la arista {a,b} es la misma que {b,a}.

- 🩷 Ejemplo del profe: V = {a,b,c,d,e}, |V| = 5.
  E = { {a,b}, {a,c}, {a,e}, {a,d}, {b,c}, {c,d}, {c,e}, {d,e} }

---

## 2. Grafos "deformables" (isomorfismo intuitivo)

- 💜 Un grafo es **deformable**: puedo mover los vértices y estirar las aristas; **sigue siendo el mismo grafo** mientras no cambien las conexiones.
- 🩷 Dos dibujos que se ven distintos pueden ser "el mismo" grafo si conectan los mismos vértices igual.

### Isomorfismo (definición formal)
- 🟢 Sean G₁ = (V₁, E₁) y G₂ = (V₂, E₂). Un **isomorfismo** es una función **f: G₁ → G₂** tal que:
  - **f: V₁ → V₂** es una **biyección** (empareja vértices uno a uno).
  - 🟡 **Preserva adyacencia:** a~b en G₁ ⟺ f(a)~f(b) en G₂.
- 💜 En palabras: dos grafos son isomorfos si son "el mismo" reetiquetando los vértices.

---

## 3. Subgrafos

- 🟢 **G₂ = (V₂, E₂) es subgrafo de G₁ = (V₁, E₁)** si:
  - 🟡 **V₂ ⊆ V₁** (sus vértices son parte de los de G₁)
  - 🟡 **E₂ ⊆ E₁** (sus aristas son parte de las de G₁)
- 💜 OJO: no puede tener una arista cuyos extremos no estén en V₂. Una arista "colgando" o que use un vértice que no incluiste **NO es subgrafo válido**.

---

## 4. Vocabulario esencial (¡cae seguro en el quiz!) ⭐

| Término | Definición | 🩷 Ejemplo / Nota |
|---------|------------|-------------------|
| 🟢 **Adyacentes** | Dos **vértices** conectados por una arista | a adyacente a d si existe arista {a,d} |
| 🟢 **Incidentes** | Dos **aristas** que comparten un vértice común | — |
| 🟢 **Incidencia (vértice-arista)** | Un vértice y una arista son incidentes si el vértice es extremo de la arista | — |
| 🟢 **Bucle (loop)** | Arista de un vértice a **sí mismo** | se dibuja como un lazo ↺ |
| 🟢 **Aristas paralelas (múltiples)** | Dos aristas que conectan **el mismo par** de vértices | dos líneas entre a y b |
| 🟢 **Grafo simple** | Grafo **sin bucles ni aristas paralelas** | el caso "normal" |

- 💜 Distinción clave: **adyacente** es entre VÉRTICES; **incidente** es entre ARISTAS (o entre vértice y arista).

---

## 5. Grado de un vértice ⭐⭐

- 🟢 **Grado de v** = 🔵 **gr(v) = g(v) = d(v)** = número de aristas que **tocan** (inciden en) ese vértice.
- 💜 Un **bucle cuenta como 2** en el grado (toca al vértice por ambos extremos).

### Teorema del apretón de manos (Handshaking) — EL teorema del tema
- 🟠 🟡 **Σ gr(v) = 2·|E|**
  - "La suma de TODOS los grados es igual al doble del número de aristas."
- 🟠 **Demostración (del profe):** cada arista aporta exactamente **2** a la suma de grados (uno por cada extremo). Al sumar todos los grados, cada arista se cuenta 2 veces. ∎
- 🩷 Ejemplo del profe: grados 3,4,2,4,3 → suma = 16 = 2·8 → el grafo tiene 8 aristas. ✓

### Corolarios útiles (pueden caer)
- 🟠 La suma de los grados **siempre es par**.
- 🟠 El número de vértices de **grado impar** es siempre **par**.

### Grafo k-regular
- 🟢 Un grafo es **k-regular** si **TODOS** los vértices tienen el mismo grado k.
- 🩷 Ejemplo del profe: un pentágono (ciclo de 5 vértices) es **2-regular** (cada vértice tiene grado 2).

---

## 6. Representaciones matriciales

### Matriz de Adyacencia (vértices × vértices)
- 🟢 Matriz cuadrada **n×n** (n = # vértices). La entrada (i,j) = **número de aristas** entre el vértice i y el j.
- 🟠 Propiedades (para grafo simple no dirigido):
  - 🟡 **Diagonal de ceros** → porque no hay bucles.
  - 🟡 **Simétrica** → porque el grafo no es dirigido (si i~j entonces j~i).
  - 🟡 La **suma de la fila i = grado del vértice i**.
- 🩷 Ejemplo del profe (vértices a,b,c,d,e):
  ```
      a b c d e     grado
  a [ 0 1 0 1 1 ]    3
  b [ 1 0 1 1 1 ]    4
  c [ 0 1 0 1 0 ]    2
  d [ 1 1 1 0 1 ]    4
  e [ 1 1 0 1 0 ]    3
  ```
- 💜 Dato cultural (no suele caer): si elevas la matriz al cuadrado (P²), obtienes caminos de longitud 2. Base del algoritmo **PageRank** de Google.

### Matriz de Incidencia (vértices × aristas)
- 🟢 Matriz **(n vértices) × (m aristas)**. La entrada (v, e) = **1 si el vértice v es extremo de la arista e**, 0 si no.
- 💜 Cada columna (arista) tiene exactamente **dos 1** (los dos extremos de esa arista) — salvo bucles.

---

## 7. Próximas secciones del capítulo (contexto, menos probable en quiz introductorio)

- **1.6 Caminos y conexión:** un **camino** es una secuencia de vértices conectados por aristas. Un grafo es **conexo** si hay camino entre cualquier par de vértices.
- **1.7 Ciclos:** camino que empieza y termina en el mismo vértice sin repetir aristas.
- **1.8 Camino más corto** (algoritmo de Dijkstra) — avanzado.
- **1.9 Lema de Sperner** — avanzado.

---

## Ideas clave para el quiz
1. Grafo = (V, E). Vértices y aristas. No dirigido ⟹ simétrico.
2. Vocabulario: adyacente (vértices), incidente (aristas), bucle, paralelas, simple.
3. **grado = # aristas que tocan el vértice** (bucle cuenta 2).
4. **Σ grados = 2|E|** (apretón de manos). Número de vértices de grado impar es par.
5. Matriz de adyacencia: diagonal 0, simétrica, suma de fila = grado.
6. k-regular = todos los vértices con grado k.
7. Subgrafo: V₂⊆V₁ y E₂⊆E₁ (aristas solo entre vértices incluidos).

---

## 🎯 Banco de afirmaciones Verdadero/Falso (estilo quiz)

> Los quices del profe suelen ser V/F sobre teoría clave. Lee cada afirmación, decide V o F, y verifica. Estas son las "trampas" típicas del capítulo.

| # | Afirmación | ¿V o F? | Por qué |
|---|-----------|---------|---------|
| 1 | En un grafo no dirigido, la matriz de adyacencia es simétrica. | **V** | si i~j entonces j~i |
| 2 | La suma de todos los grados de un grafo es igual al número de aristas. | **F** | es **2·\|E\|**, no \|E\| |
| 3 | Un bucle aporta 1 al grado del vértice. | **F** | aporta **2** |
| 4 | En un grafo simple no hay bucles ni aristas paralelas. | **V** | es la definición de simple |
| 5 | Dos aristas son adyacentes si comparten un vértice. | **F** (término) | eso es **incidentes**; adyacente es entre vértices |
| 6 | El número de vértices de grado impar siempre es par. | **V** | corolario del apretón de manos |
| 7 | Todo grafo k-regular tiene todos sus vértices con grado k. | **V** | es la definición |
| 8 | Si dos grafos tienen distinto número de aristas, no pueden ser isomorfos. | **V** | el isomorfismo preserva # de aristas |
| 9 | La diagonal de la matriz de adyacencia de un grafo sin bucles es toda ceros. | **V** | no hay arista de un vértice a sí mismo |
| 10 | Un subgrafo puede tener una arista cuyos extremos no estén en su conjunto de vértices. | **F** | E₂⊆E₁ y los extremos deben estar en V₂ |
| 11 | En la matriz de incidencia, cada columna (arista simple) tiene exactamente dos 1. | **V** | los dos extremos de la arista |
| 12 | Dos grafos isomorfos deben tener la misma secuencia de grados. | **V** | el isomorfismo preserva grados |
| 13 | La suma de los grados de cualquier grafo es siempre par. | **V** | es 2\|E\|, múltiplo de 2 |
| 14 | Si dos grafos tienen la misma secuencia de grados, entonces son isomorfos. | **F** | es necesario pero NO suficiente |
| 15 | En un grafo dirigido la relación de aristas es simétrica. | **F** | solo el NO dirigido es simétrico |

> 💜 Trampa estrella: #14. "Misma secuencia de grados" es **condición necesaria pero no suficiente** para isomorfismo. Si te lo preguntan al revés (distinto # de aristas/grados ⟹ no isomorfos), eso SÍ es verdadero.
