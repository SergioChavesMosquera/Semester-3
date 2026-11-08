# 🎯 CHEAT-SHEET — Quiz Grafos (Capítulo 1, Bondy-Murty)

> Quiz introductorio / revisión general. Enfócate en definiciones, grados, matrices y apretón de manos.

---

## 1️⃣ QUÉ ES UN GRAFO
- **G = (V, E)**: V = vértices (puntos •), E ⊆ V×V = aristas (líneas).
- No dirigido ⟹ relación **simétrica** ({a,b} = {b,a}).
- Notación: **V(G)** vértices, **E(G)** aristas. |V| = # vértices, |E| = # aristas.
- "Deformable": puedo mover vértices; sigue siendo el mismo grafo si no cambian las conexiones.

## 2️⃣ VOCABULARIO (lo que más cae)
- **Adyacentes** = dos VÉRTICES unidos por una arista.
- **Incidentes** = dos ARISTAS que comparten un vértice (o vértice-arista que se tocan).
- **Bucle (loop)** = arista de un vértice a sí mismo ↺.
- **Paralelas (múltiples)** = dos aristas entre el mismo par de vértices.
- **Grafo simple** = SIN bucles NI paralelas.
- ⚠️ Adyacente = vértices. Incidente = aristas. No los confundas.

## 3️⃣ GRADO ⭐
- **gr(v) = g(v) = d(v)** = # de aristas que tocan v.
- **Un bucle cuenta 2** en el grado.
- 🟡 **Σ gr(v) = 2·|E|** ← APRETÓN DE MANOS (handshaking). Memorízalo.
  - Prueba: cada arista aporta 2 grados (uno por extremo).
- Corolarios: la suma de grados es PAR; el # de vértices con grado IMPAR es PAR.
- **k-regular** = todos los vértices tienen grado k. (Pentágono = 2-regular.)

## 4️⃣ MATRIZ DE ADYACENCIA (vértices × vértices)
- Cuadrada n×n. Entrada (i,j) = # aristas entre i y j.
- **Diagonal = 0** (si no hay bucles).
- **Simétrica** (porque no es dirigido).
- **Suma de la fila i = grado del vértice i**. ← truco para verificar.

## 5️⃣ MATRIZ DE INCIDENCIA (vértices × aristas)
- Tamaño (n vértices) × (m aristas). Entrada (v,e) = 1 si v es extremo de e, 0 si no.
- Cada columna tiene exactamente dos 1 (los dos extremos de la arista).

## 6️⃣ SUBGRAFO
- G₂ subgrafo de G₁ ⟺ V₂ ⊆ V₁ **y** E₂ ⊆ E₁.
- ⚠️ No vale una arista cuyo extremo no esté en V₂.

## 7️⃣ ISOMORFISMO (idea)
- Dos grafos son isomorfos si son "el mismo" reetiquetando vértices.
- f: V₁→V₂ biyección que **preserva adyacencia**: a~b ⟺ f(a)~f(b).

---

## ⚠️ ERRORES FRECUENTES
1. Confundir adyacente (vértices) con incidente (aristas).
2. Olvidar que el bucle suma 2 al grado.
3. En la matriz de adyacencia: olvidar que es simétrica / diagonal 0.
4. Decir Σgrados = |E| en vez de **2|E|**.
5. Armar un "subgrafo" con una arista que usa un vértice no incluido.

## ✅ MÉTODO PARA EJERCICIOS TÍPICOS
- **"Calcula los grados"**: cuenta aristas que tocan cada vértice (bucle = 2).
- **"¿Cuántas aristas?"**: suma los grados y divide entre 2.
- **"Escribe la matriz de adyacencia"**: n×n, pon 1 donde hay arista, verifica simetría y que la suma de fila = grado.
- **"¿Son isomorfos?"**: compara # vértices, # aristas y la secuencia de grados (si difieren, NO son isomorfos).
