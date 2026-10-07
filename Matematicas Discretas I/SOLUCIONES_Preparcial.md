# ✅ SOLUCIONES — Preparcial "Lógica y Teoría de Conjuntos"

> Resueltas completas con justificación formal, como las pide el profe. Estudia primero intentándolas solo, luego compara.

---

## SECCIÓN 1 — Lógica y Conjuntos

### Punto 1. Demostrar que (p → (q → r)) → ((p → q) → (p → r)) es tautología

**Parte A — Tabla de verdad:**

| p | q | r | q→r | p→(q→r) | p→q | p→r | (p→q)→(p→r) | TOTAL |
|---|---|---|-----|---------|-----|-----|-------------|-------|
| V | V | V | V   | V       | V   | V   | V           | **V** |
| V | V | F | F   | F       | V   | F   | F           | **V** |
| V | F | V | V   | V       | F   | V   | V           | **V** |
| V | F | F | V   | V       | F   | F   | V           | **V** |
| F | V | V | V   | V       | V   | V   | V           | **V** |
| F | V | F | F   | V       | V   | V   | V           | **V** |
| F | F | V | V   | V       | V   | V   | V           | **V** |
| F | F | F | V   | V       | V   | V   | V           | **V** |

Como la columna TOTAL es **toda V**, la proposición es una **tautología**. ∎

**Parte B — Razonamiento informal:**
Supongamos, por contradicción, que la implicación es **falsa**. Entonces el antecedente p→(q→r) es V y el consecuente (p→q)→(p→r) es F.
- Que (p→q)→(p→r) sea F exige: p→q verdadera **y** p→r falsa.
- p→r falsa ⟹ p = V y r = F.
- p→q verdadera con p = V ⟹ q = V.
- p→(q→r) verdadera con p = V ⟹ q→r verdadera.
- Pero q = V y r = F ⟹ q→r es **F**. Contradicción. ⊥

Luego la proposición nunca es falsa ⟹ es tautología. ∎

---

### Punto 2a. ¿Es cierto que para todo A, A ⊆ 𝒫(𝒫(A))?

**FALSO.** Contraejemplo:
- Sea A = {1}.
- 𝒫(A) = {∅, {1}}.
- 𝒫(𝒫(A)) = { ∅, {∅}, {{1}}, {∅, {1}} }.
- Para que A ⊆ 𝒫(𝒫(A)) necesitaríamos 1 ∈ 𝒫(𝒫(A)). Pero los elementos de 𝒫(𝒫(A)) son conjuntos de subconjuntos de A, y 1 **no** es ninguno de ellos.
- ∴ 1 ∈ A pero 1 ∉ 𝒫(𝒫(A)), luego A ⊄ 𝒫(𝒫(A)). ∎

> 💡 Idea: los elementos de A son objetos; los de 𝒫(𝒫(A)) son conjuntos de conjuntos. Casi nunca coinciden.

---

### Punto 2b. ¿Es cierto que para todo A, 𝒫(A) ∈ 𝒫(𝒫(A))?

**VERDADERO.** Demostración:
- Por definición, 𝒫(A) ∈ 𝒫(𝒫(A)) ⟺ 𝒫(A) ⊆ 𝒫(A).
- Todo conjunto es subconjunto de sí mismo (reflexividad de ⊆): 𝒫(A) ⊆ 𝒫(A). ✓
- ∴ 𝒫(A) ∈ 𝒫(𝒫(A)) para todo A. ∎

> 💡 Contraste con 2a: cuidado con ∈ vs ⊆. Aquí preguntan si 𝒫(A) es ELEMENTO (y sí, porque es subconjunto de 𝒫(A)).

---

### Punto 3. Describir X = {6, 10, 14, 18, 22, ...} intensionalmente

**Patrón:** empieza en 6 y aumenta de 4 en 4 → términos de la forma 4n + 2.
- n = 1 → 6, n = 2 → 10, n = 3 → 14, ... ✓

**Respuesta:**
$$X = \{\, x \in \mathbb{N} : x = 4n + 2 \text{ para algún } n \in \mathbb{N},\, n \ge 1 \,\}$$

Formas equivalentes aceptables:
- X = {4n + 2 : n ∈ ℕ, n ≥ 1}
- X = {x ∈ ℕ : x ≥ 6 ∧ x ≡ 2 (mod 4)}  (pares que dejan residuo 2 al dividir por 4, desde 6)
- X = {2(2k + 1) : k ∈ ℕ, k ≥ 1}  (el doble de un impar ≥ 3)

> 💡 Verifica siempre con los primeros 2-3 términos antes de entregar.

---

## SECCIÓN 2 — Verdadero o Falso (con justificación)

### 1. "Existe un conjunto X tal que, si X ∩ B = X ∩ C, entonces B = C."

**VERDADERO.** Basta EXHIBIR un X que lo cumpla (el enunciado dice "existe").
- Tomo **X = 𝒰** (el universo), o cualquier conjunto que contenga a B y C.
- Entonces X ∩ B = B y X ∩ C = C.
- Si X ∩ B = X ∩ C ⟹ B = C. ✓
- ∴ existe tal X. ∎

> 💡 Clave: el enunciado pide EXISTENCIA, no "para todo X". Con un solo X que funcione, es verdadero. (Si fuera "para todo X" sería FALSO: con X=∅, ∅∩B = ∅∩C siempre, pero B≠C.)

---

### 2. 𝒫(A ∪ B) ⊇ 𝒫(A) ∪ 𝒫(B)

**VERDADERO.** Demostración:
```
Sea X ∈ 𝒫(A) ∪ 𝒫(B).
⟹ X ∈ 𝒫(A)  ∨  X ∈ 𝒫(B)
⟹ X ⊆ A     ∨  X ⊆ B
En cualquier caso, X ⊆ A ∪ B  (porque A ⊆ A∪B y B ⊆ A∪B).
⟹ X ∈ 𝒫(A ∪ B).
∴ 𝒫(A) ∪ 𝒫(B) ⊆ 𝒫(A ∪ B), es decir 𝒫(A∪B) ⊇ 𝒫(A) ∪ 𝒫(B). ∎
```

> 💡 El recíproco (⊆) es FALSO: con A={1}, B={2}, el conjunto {1,2} ∈ 𝒫(A∪B) pero {1,2} ∉ 𝒫(A)∪𝒫(B). Por eso solo vale ⊇, no =.

---

### 3. (A ∪ B) \ A = B \ A

**VERDADERO.** Demostración (doble contención o cadena de ⟺):
```
Sea x ∈ (A∪B)\A
⟺ x ∈ (A∪B)  ∧  x ∉ A
⟺ (x∈A ∨ x∈B)  ∧  x∉A
⟺ (x∈A ∧ x∉A)  ∨  (x∈B ∧ x∉A)      [distributiva]
⟺ FALSO        ∨  (x∈B ∧ x∉A)      [x∈A ∧ x∉A es contradicción]
⟺ x∈B ∧ x∉A
⟺ x ∈ B\A.
∴ (A∪B)\A = B\A. ∎
```

> 💡 El truco: al unir A y B y luego quitar A, lo que queda es exactamente "lo de B que no estaba en A".

---

### 4. "Si R y S son reflexivas sobre X, entonces R ∪ S también lo es."

**VERDADERO.** Demostración:
```
R reflexiva sobre X ⟹ ∀a ∈ X: (a,a) ∈ R.
Sea a ∈ X arbitrario. Entonces (a,a) ∈ R.
Por definición de unión, (a,a) ∈ R ⟹ (a,a) ∈ R ∪ S.
∴ ∀a ∈ X: (a,a) ∈ R ∪ S ⟹ R ∪ S es reflexiva sobre X. ∎
```

> 💡 Con que UNA de las dos sea reflexiva ya basta para la unión. No necesitas usar S.

---

## 📋 Resumen de respuestas

| Punto | Respuesta |
|-------|-----------|
| 1 (lógica) | Tautología ✅ (tabla + informal) |
| 2a | **FALSO** (contraejemplo A={1}) |
| 2b | **VERDADERO** (𝒫(A)⊆𝒫(A)) |
| 3 | X = {4n+2 : n∈ℕ, n≥1} |
| V/F 1 | **VERDADERO** (X=𝒰) |
| V/F 2 | **VERDADERO** (demostración ⊇) |
| V/F 3 | **VERDADERO** (distributiva) |
| V/F 4 | **VERDADERO** (reflexividad bajo ∪) |
