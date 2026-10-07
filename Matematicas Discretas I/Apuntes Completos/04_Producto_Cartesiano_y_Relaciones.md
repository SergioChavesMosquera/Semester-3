# Matemáticas Discretas I — Producto Cartesiano y Relaciones 🔗

### Clases 23, 28 y 30 Sep · Matemática Estructural

**Leyenda:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Propiedad/Ley · 🔵 Notación · 🩷 Ejemplo · 💜 Advertencia

---

## 1. Producto cartesiano (A × B)

- 🟢 **A × B** = {(a, b) : a ∈ A, b ∈ B}  — todos los pares ordenados.
- 🟡 **|A × B| = |A| · |B|**.
- 💜 **PAR ORDENADO:** (a, b) ≠ (b, a) en general. El orden importa.
- 🟠 **Teorema:** (a, b) = (a', b') ⟺ a = a' ∧ b = b'.

### Definición formal de par ordenado (Kuratowski)
- 🔵 **(a, b) := {{a}, {a, b}}**  — así el orden queda codificado en la estructura.

### Casos especiales
- 🩷 ℝ² = ℝ × ℝ = el plano. Un punto (x, y).
- 🟠 **A × ∅ = ∅**  (no hay segundos elementos, no hay pares).
- n-tuplas: A₁ × A₂ × A₃ = (A₁ × A₂) × A₃.

---

## 2. Relaciones

- 🟢 Una **relación R de A en B** es un subconjunto de A × B: **R ⊆ A × B**.
  - Relaciona elementos de A con elementos de B.
- 🔵 Se escribe **aRb** o **(a,b) ∈ R** indistintamente.
- 🩷 R = "es padre de" = {(p, q) : p es padre de q}.
- 💜 Una relación puede ser sobre el mismo conjunto: R ⊆ A × A.

### Dominio e Imagen
- 🟢 **Dom(R)** = {x : ∃y, (x,y) ∈ R}  — primeras coordenadas que aparecen.
- 🟢 **Im(R)** = {y : ∃x, (x,y) ∈ R}  — segundas coordenadas que aparecen.
- 🩷 R = {(x,y) ∈ ℝ² : y² = x}. Dom(R) = ℝ⁺ (x≥0), Im(R) = ℝ.

### Relación inversa
- 🟢 **R⁻¹** = {(y, x) : (x, y) ∈ R}  — se voltean los pares.
- 🩷 Si R = "es padre de", entonces R⁻¹ = "es hijo de".
- 🟠 Si R = "es hermano de", entonces R⁻¹ = R (es simétrica).

### Imagen directa e inversa de un conjunto
- 🟢 **R[A]** = {y : ∃x ∈ A, (x,y) ∈ R}  — a dónde van los elementos de A.
- 🟢 **R⁻¹[A]** = imagen de A bajo la inversa.
- 🟠 Teorema: A ⊆ Dom(R) ⟹ A ⊆ R⁻¹[R[A]]. (No siempre con igualdad.)

---

## 3. Propiedades de relaciones (R ⊆ X × X) ⭐⭐⭐

Sea R una relación **sobre un conjunto X** (R ⊆ X × X):

| Propiedad | Definición | Idea |
|-----------|------------|------|
| 🟢 **Reflexiva** | ∀a ∈ X: (a, a) ∈ R | todo elemento se relaciona consigo mismo |
| 🟢 **Simétrica** | (a, b) ∈ R ⟹ (b, a) ∈ R | si a~b entonces b~a |
| 🟢 **Antisimétrica** | (a,b) ∈ R ∧ (b,a) ∈ R ⟹ a = b | solo "va y viene" si son iguales |
| 🟢 **Transitiva** | (a,b) ∈ R ∧ (b,c) ∈ R ⟹ (a,c) ∈ R | encadena |

### Ejemplos clave
- 🩷 "≤" sobre ℝ: reflexiva ✅, antisimétrica ✅ (a≤b ∧ b≤a ⟹ a=b), transitiva ✅. (NO simétrica.)
- 🩷 "ser hermano de": simétrica ✅, NO reflexiva (uno no es su propio hermano), transitiva ✅.
- 🩷 "<" (estricto): NO reflexiva, NO simétrica, antisimétrica (vacuamente ✅), transitiva ✅.
- 🩷 ⊆ sobre 𝒫(X): reflexiva, antisimétrica, transitiva → es orden parcial.
- 🩷 "divide a" sobre ℕ: reflexiva, antisimétrica, transitiva → orden parcial.

### Órdenes y equivalencias
- 🟢 **Relación de equivalencia:** reflexiva + simétrica + transitiva (ej: "ser igual", "misma clase de congruencia").
- 🟢 **Orden parcial:** reflexiva + antisimétrica + transitiva (ej: ≤, ⊆, "divide a").

---

## 4. Pregunta del preparcial: R ∪ S reflexivas ✅ VERDADERA

**"Si R y S son reflexivas sobre X, entonces R ∪ S también lo es."**
```
R reflexiva ⟹ ∀a ∈ X: (a,a) ∈ R.
Entonces (a,a) ∈ R ⟹ (a,a) ∈ R ∪ S  (por definición de unión).
∴ ∀a ∈ X: (a,a) ∈ R ∪ S ⟹ R ∪ S es reflexiva.  □
```
- 💜 Basta con que UNA sea reflexiva para que la unión lo sea. ¡Con R ya alcanza!
- 💜 OJO: la simetría y transitividad NO se preservan tan fácil bajo unión (ahí sí hay que pensar).

---

## 5. Funciones (relación especial)

- 🟢 Una **función f: A → B** es una relación R ⊆ A × B tal que cada x ∈ A tiene EXACTAMENTE un y ∈ B con (x,y) ∈ R.
  - (i) Totalidad: todo x ∈ A tiene imagen.
  - (ii) Unicidad: esa imagen es única.
- 💜 En una gráfica, "pasa la prueba de la recta vertical".

---

## Ideas clave para el parcial
1. R ⊆ A×B. aRb ⟺ (a,b) ∈ R.
2. Las 4 propiedades: reflexiva (∀a: aRa), simétrica (aRb⟹bRa), antisimétrica (aRb∧bRa⟹a=b), transitiva.
3. Para "¿R∪S preserva la propiedad?": escribe la definición y verifica con la def. de unión.
4. Reflexividad SÍ se preserva bajo unión. Simetría/transitividad hay que verificar caso a caso.
5. Orden parcial = R+Antisim+Trans. Equivalencia = R+Sim+Trans.
