# Matemáticas Discretas I — Operaciones con Conjuntos: ∪, ∩, \, Complemento 🔧

### Clases 14 y 16 Sep · Matemática Estructural

**Leyenda:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Propiedad/Ley · 🔵 Notación · 🩷 Ejemplo · 💜 Advertencia

---

## 1. Unión e Intersección

- 🟢 **A ∪ B** = {x : x ∈ A **∨** x ∈ B}  — "en A o en B (o ambos)".
- 🟢 **A ∩ B** = {x : x ∈ A **∧** x ∈ B}  — "en A y en B a la vez".
- 🟢 **Disjuntos:** A y B son disjuntos ⟺ A ∩ B = ∅ (no comparten nada).

### Traducción lógica (la clave de las demostraciones)
- Toda operación de conjuntos se traduce a un conectivo lógico:
  - ∪ ↔ ∨ (o)
  - ∩ ↔ ∧ (y)
  - \ ↔ ∧ ¬ (y no)
  - ᶜ ↔ ¬ (no)
  - ⊆ ↔ → (implica)
  - = ↔ ↔ (sii)

---

## 2. Diferencia y Complemento

- 🟢 **A \ B** = {x : x ∈ A ∧ x ∉ B}  — "en A pero NO en B".
- 🟢 **Universo 𝒰:** conjunto de contexto que contiene todo lo relevante.
- 🟢 **Complemento Aᶜ** = 𝒰 \ A = {x ∈ 𝒰 : x ∉ A}  — "todo lo que NO está en A".
- 🟠 Propiedades del complemento:
  - 🟡 **A ∪ Aᶜ = 𝒰**
  - 🟡 **A ∩ Aᶜ = ∅**

### Identidad estrella (sale muchísimo)
- 🟡 **A \ B = A ∩ Bᶜ**  — "quitar B es intersecar con el complemento de B".
  - Demo: x ∈ A\B ⟺ x ∈ A ∧ x ∉ B ⟺ x ∈ A ∧ x ∈ Bᶜ ⟺ x ∈ A ∩ Bᶜ. □

---

## 3. Demostraciones formales (el método del profe)

🟠 **Estructura para probar igualdad X = Y:**
```
⊆) Sea x ∈ X ⟹ (traducir a lógica) ⟹ ... ⟹ x ∈ Y.
⊇) Sea x ∈ Y ⟹ ... ⟹ x ∈ X.
∴ X = Y.  □
```

### Ejemplo del profe: (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C)  [distributividad]
```
Sea x ∈ (A ∪ B) ∩ C
⟺ (x ∈ A ∨ x ∈ B) ∧ x ∈ C
⟺ (x ∈ A ∧ x ∈ C) ∨ (x ∈ B ∧ x ∈ C)   [distributiva lógica]
⟺ x ∈ (A ∩ C) ∨ x ∈ (B ∩ C)
⟺ x ∈ (A ∩ C) ∪ (B ∩ C).  □
```
- 💜 La demostración de conjuntos SE APOYA en las leyes lógicas (distributiva, De Morgan, etc.). Traduces a lógica, aplicas la ley, retraduces.

---

## 4. Identidades que salen en el preparcial

### (A ∪ B) \ B = A \ B  ✅ VERDADERA
```
Sea x ∈ (A∪B)\B
⟺ (x ∈ A ∨ x ∈ B) ∧ x ∉ B
⟺ (x ∈ A ∧ x ∉ B) ∨ (x ∈ B ∧ x ∉ B)   [distributiva]
⟺ (x ∈ A ∧ x ∉ B) ∨ FALSO              [x∈B ∧ x∉B es contradicción]
⟺ x ∈ A ∧ x ∉ B
⟺ x ∈ A\B.  □
```
- 💜 OJO con la variante del preparcial: **(A∪B) \ A = B \ A** — misma idea, cambiando B por A. Es VERDADERA por el mismo argumento (simétrico).

### (A∪B)\A = B\A — demostración
```
Sea x ∈ (A∪B)\A ⟺ (x∈A ∨ x∈B) ∧ x∉A
⟺ (x∈A ∧ x∉A) ∨ (x∈B ∧ x∉A)
⟺ FALSO ∨ (x∈B ∧ x∉A)
⟺ x∈B ∧ x∉A ⟺ x ∈ B\A.  □
```

### Leyes de De Morgan
- 🟡 **(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ**
- 🟡 **(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ**

### Otras identidades útiles
- 🟡 (A ∩ B) ∪ (A ∩ Bᶜ) = A
- 🟡 A ∪ B = ∅ ⟹ A = ∅ ∧ B = ∅
- 🟡 A ⊄ B ⟺ A \ B ≠ ∅  (hay algo en A que no está en B)

---

## 5. Monotonía de la unión/intersección
- 🟠 B ⊆ A ⟺ A ∪ B = A
- 🟠 B ⊆ A ⟺ A ∩ B = B

---

## Ideas clave para el parcial
1. Traduce la operación a lógica, aplica la ley lógica, retraduce. Ese es TODO el truco.
2. A\B = A∩Bᶜ es la reescritura más útil.
3. Para demostrar igualdad: ⊆ y ⊇ (o cadena de ⟺ si cada paso es reversible).
4. x ∈ B ∧ x ∉ B es una CONTRADICCIÓN (= FALSO), colapsa esa rama.
