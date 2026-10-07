# Matemáticas Discretas I — Conjuntos: Definición, Pertenencia, Subconjuntos, Igualdad y 𝒫(A) 🧱

### Clase 07 Sep · Matemática Estructural

**Leyenda:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Propiedad/Ley · 🔵 Notación · 🩷 Ejemplo · 💜 Advertencia

---

## 1. ¿Qué es un conjunto?

- 🟢 Un **conjunto** es una colección de objetos definida sin ambigüedad.
- 🔵 **x ∈ A** = "x pertenece al conjunto A" (es uno de sus objetos).
- 🔵 **x ∉ A** = "x no pertenece a A".
- 💜 Un conjunto NO tiene orden ni repeticiones: {1, 2, 3} = {3, 1, 2} = {1, 1, 2, 3}.

### Notación
- **Extensión (listar):** A = {1, 2, 3, 7} — listo todos los elementos.
- **Comprensión (propiedad):** A = {x ∈ ℕ : p(x)} — describo qué propiedad cumplen.
- 🔵 **Conjuntos famosos:** ℕ = {0, 1, 2, 3, ...}, ℤ = {..., -2, -1, 0, 1, 2, ...}, ℝ = los reales.

---

## 2. Subconjuntos (⊆)

- 🟢 **A ⊆ B** (A es subconjunto de B) ⟺ 🟡 **∀x: x ∈ A ⟹ x ∈ B**
  - "Todos los elementos de A son también elementos de B."
- 💜 **NO confundir ∈ con ⊆:**
  - ∈ = "es ELEMENTO de" (un objeto individual pertenece a un conjunto)
  - ⊆ = "está CONTENIDO en" (todos los elementos de uno están en el otro)
  - 🩷 Si A = {1, 2}, entonces 1 ∈ A, pero {1} ⊆ A. Y {1} ∈ 𝒫(A), no {1} ∈ A.

### Demostrar A ⊆ B (estructura estándar)
```
Sea x ∈ A (arbitrario).
... (cadena de implicaciones) ...
⟹ x ∈ B.
∴ A ⊆ B.  □
```
- 🩷 Ejemplo del profe: A = {2n : n ∈ ℕ}, B = {m : m ∈ ℕ, m es par}. Mostrar A ⊆ B.
  - Sea x ∈ A ⟹ ∃n ∈ ℕ tal que x = 2n ⟹ x es par ⟹ x ∈ B. □

---

## 3. Igualdad de conjuntos (=)

- 🟢 **A = B** ⟺ 🟡 **A ⊆ B ∧ B ⊆ A**
  - "Tienen exactamente los mismos elementos."
- 🟠 Para demostrar A = B, hay que hacer las DOS contenciones (ida y vuelta).
- 💜 Alternativa (Extensionalidad): A = B ⟺ ∀x (x ∈ A ⟺ x ∈ B).

---

## 4. Conjunto Potencia 𝒫(A) ⭐

- 🟢 **𝒫(A)** = {todos los subconjuntos de A} = {X : X ⊆ A}.
- 🔵 **Mismos nombres (TODOS son 𝒫(A)):** "conjunto potencia de A" = "**Partes de A**" = P(A) = 2^A. El profe la llama "Partes de A". La letra 𝒫 es justamente de "Partes".
- 🟡 Si |A| = n, entonces **|𝒫(A)| = 2ⁿ**.

### Ejemplo paso a paso
- 🩷 A = {a, b, c}, |A| = 3, entonces |𝒫(A)| = 2³ = 8.
- Subconjuntos de tamaño 0: {∅}  → 1
- Subconjuntos de tamaño 1: {a}, {b}, {c}  → 3
- Subconjuntos de tamaño 2: {a,b}, {a,c}, {b,c}  → 3
- Subconjuntos de tamaño 3: {a,b,c}  → 1
- 𝒫(A) = {∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}}

### Propiedades fundamentales
- 🟠 **∅ ∈ 𝒫(A)** siempre. Porque ∅ ⊆ A para todo A (vacuamente cierto).
- 🟠 **A ∈ 𝒫(A)** siempre. Porque A ⊆ A.
- 🟠 **𝒫(A) ≠ ∅** siempre (al menos tiene a ∅).

### Relación ⊆ vs ∈ con 𝒫
- 🟡 **X ⊆ A ⟺ X ∈ 𝒫(A)**
  - "Ser subconjunto de A" es lo mismo que "ser elemento del conjunto potencia de A".
- 💜 Entonces preguntar "¿A ⊆ 𝒫(𝒫(A))?" es preguntar "¿todo elemento de A es un elemento de 𝒫(𝒫(A)), es decir, un subconjunto de 𝒫(A)?"

---

## 5. 𝒫 anidado — La trampa del parcial

- 🩷 A = {a, 1}:
  - 𝒫(A) = {∅, {a}, {1}, {a,1}}
  - A ⊆ 𝒫(A)? Necesitaría a ∈ 𝒫(A) y 1 ∈ 𝒫(A). Pero a NO es un subconjunto de A (a es un elemento, no un conjunto). **FALSO en general**.

- 💜 La diferencia clave: los ELEMENTOS de A son objetos; los ELEMENTOS de 𝒫(A) son CONJUNTOS. Para que A ⊆ 𝒫(A), cada elemento de A tendría que ser un subconjunto de A — eso casi nunca pasa.

---

## Ideas clave para el parcial
1. Para demostrar A ⊆ B: tomar x ∈ A arbitrario y llegar a x ∈ B.
2. Para demostrar A = B: demostrar ⊆ y ⊇.
3. X ⊆ A ⟺ X ∈ 𝒫(A) — esto convierte preguntas de "⊆" en preguntas de "∈" y viceversa.
4. |𝒫(A)| = 2^|A|. Siempre ∅ ∈ 𝒫(A) y A ∈ 𝒫(A).
