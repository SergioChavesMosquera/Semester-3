# Matemáticas Discretas I — Cardinalidad, Vacío, COIP y Operaciones Generalizadas 🔢

### Clases 09 y 21 Sep · Matemática Estructural

**Leyenda:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Propiedad/Ley · 🔵 Notación · 🩷 Ejemplo · 💜 Advertencia

---

## 1. El conjunto vacío (∅)

- 🟢 **∅ = { }** = el conjunto sin elementos.
- 🟠 **∅ ⊆ A** para todo conjunto A.
  - Demo: "Sea x ∈ ∅ ⟹ x ∈ A" es vacuamente cierto (nunca hay un x ∈ ∅ que verificar). □
- 🟠 **El vacío es único.** Si ∅₁ y ∅₂ son ambos vacíos, entonces ∅₁ ⊆ ∅₂ y ∅₂ ⊆ ∅₁, luego ∅₁ = ∅₂. □
- 💜 **∅ ≠ {∅}**. El primero tiene 0 elementos; el segundo tiene 1 elemento (que es ∅). |∅| = 0, |{∅}| = 1.

---

## 2. La relación ⊆ es un orden parcial (COIP)

🟠 **⊆ es un "Conjunto Parcialmente Ordenado"** porque cumple:
- (i) **Reflexiva:** A ⊆ A
- (ii) **Antisimétrica:** A ⊆ B ∧ B ⊆ A ⟹ A = B  (¡esto es la Extensionalidad!)
- (iii) **Transitiva:** A ⊆ B ∧ B ⊆ C ⟹ A ⊆ C

- 💜 Es orden PARCIAL (no total) porque hay conjuntos incomparables: {a} y {b} no cumplen ni {a}⊆{b} ni {b}⊆{a}.

---

## 3. Cardinalidad (tamaño)

- 🔵 **|A|** = número de elementos de A.
- 🟢 Dos conjuntos tienen la misma cardinalidad si existe una biyección entre ellos.
- 🟠 Jerarquía de infinitos:
  - |ℕ| = |ℤ| = |ℚ| = ℵ₀ (numerable / contable)
  - 🟡 **|ℕ| < |ℝ|** — ℝ NO es numerable (argumento diagonal de Cantor con el 0.698...).
  - 🟡 **|A| < |𝒫(A)|** siempre (Teorema de Cantor). Por eso |ℕ| < |𝒫(ℕ)| < |𝒫(𝒫(ℕ))| < ...

### Teorema de Cantor (idea)
- No existe función sobreyectiva de A en 𝒫(A). Por eso 𝒫(A) siempre es "estrictamente más grande".

---

## 4. Propiedades de 𝒫 (del teorema de la clase)

Sea A un conjunto:
- (i) **∅ ∈ 𝒫(A)** — porque ∅ ⊆ A.
- (ii) **A ∈ 𝒫(A)** — porque A ⊆ A.
- (iii) **𝒫(A) ≠ ∅**.
- (iv) 🟡 **A ⊆ B ⟹ 𝒫(A) ⊆ 𝒫(B)** (monotonía).
  - Demo: Sea X ∈ 𝒫(A) ⟹ X ⊆ A ⟹ (por transitividad con A⊆B) X ⊆ B ⟹ X ∈ 𝒫(B). □
- (v) 🟡 **A = B ⟺ 𝒫(A) = 𝒫(B)**.

---

## 5. Unión e Intersección Generalizadas ⭐

Cuando 𝒜 es un "conjunto de conjuntos" (una familia):

- 🟢 **⋃𝒜** = {p : ∃ b ∈ 𝒜, p ∈ b}  — "los elementos que están en ALGÚN miembro de la familia".
- 🟢 **⋂𝒜** = {p : ∀ b ∈ 𝒜, p ∈ b}  — "los elementos que están en TODOS los miembros".

### Ejemplo del profe
- 🩷 𝒜 = { {1,3,5}, {1,4,8}, {1,9,10} }
  - ⋃𝒜 = {1, 3, 4, 5, 8, 9, 10}  (todo lo que aparece en alguno)
  - ⋂𝒜 = {1}  (lo único que está en los tres)

### Familias indexadas
- 🔵 𝒜 = {Aᵢ : i ∈ I} se escribe más cómodo como **⋃_{i∈I} Aᵢ** y **⋂_{i∈I} Aᵢ**.
- 🩷 Ejemplo: Aᵢ = [0, 1/i] para i ∈ ℕ⁺:
  - ⋃ Aᵢ = (0, 1]  (unión de todos los intervalitos)
  - ⋂ Aᵢ = {0}... (ojo: depende de si incluye 0; en la clase ⋂ Aᵢ = {0})

### Teoremas de generalizadas
- 🟠 **A ⊆ B ⟹ ⋃A ⊆ ⋃B**
- 🟠 **A ⊆ B ⟹ ⋂B ⊆ ⋂A**  (¡se invierte!)
- 🟠 Si a ∈ A ⟹ a ⊆ ⋃A  (cada miembro está contenido en la unión)
- 🟠 Si ∀a ∈ A se tiene a ⊆ C ⟹ ⋃A ⊆ C  (la unión es la "cota superior más pequeña")

---

## Ideas clave para el parcial
1. ∅ ⊆ A siempre (vacuamente). ∅ ≠ {∅}.
2. ⊆ es orden parcial: reflexiva + antisimétrica + transitiva.
3. A ⊆ B ⟹ 𝒫(A) ⊆ 𝒫(B). Y A ⊆ B ⟹ 𝒫(A) ∪ 𝒫(B) ⊆ 𝒫(A∪B) (relevante para el preparcial).
4. ⋃ usa ∃ (algún), ⋂ usa ∀ (todos).
5. |A| < |𝒫(A)| siempre (Cantor).
