# 🧪 SIMULACRO tipo Parcial 1 — Matemáticas Discretas I

> Intenta cada punto SOLO primero. Cronométrate (~5 min por punto). Luego baja a las soluciones.
> Mismo estilo del preparcial: tautologías, conjuntos, 𝒫, operaciones, V/F con justificación.

---

## ENUNCIADOS

### Punto 1 — Lógica
Demuestre con tabla de verdad que la siguiente proposición es tautología:
$$((p \land q) \to r) \to (p \to (q \to r))$$

### Punto 2 — Conjuntos y potencia (V o F con justificación)
a) Para todo conjunto A, ∅ ∈ 𝒫(A).
b) Para todo conjunto A, {A} ⊆ 𝒫(A).
c) Si A ⊆ B entonces 𝒫(A) ⊆ 𝒫(B).

### Punto 3 — Describir intensionalmente
Sea Y = {3, 7, 11, 15, 19, ...}. Describa Y como {x ∈ ℕ : p(x)}.

### Punto 4 — Operaciones (demuestre la igualdad)
Demuestre que A \ (B ∪ C) = (A \ B) ∩ (A \ C).

### Punto 5 — V o F con justificación
a) Para todo A, B: si A ∪ B = A ∩ B entonces A = B.
b) Si R es simétrica y S es simétrica sobre X, entonces R ∪ S es simétrica.
c) (A \ B) ∪ B = A.

---
---
---

## SOLUCIONES (no mires hasta intentar)

### Punto 1 — Tabla de verdad

| p | q | r | p∧q | (p∧q)→r | q→r | p→(q→r) | TOTAL |
|---|---|---|-----|---------|-----|---------|-------|
| V | V | V | V   | V       | V   | V       | **V** |
| V | V | F | V   | F       | F   | F       | **V** |
| V | F | V | F   | V       | V   | V       | **V** |
| V | F | F | F   | V       | V   | V       | **V** |
| F | V | V | F   | V       | V   | V       | **V** |
| F | V | F | F   | V       | F   | V       | **V** |
| F | F | V | F   | V       | V   | V       | **V** |
| F | F | F | F   | V       | V   | V       | **V** |

Columna TOTAL toda V ⟹ **tautología**. ∎
(De hecho esto es la "exportación/importación": (p∧q)→r ≡ p→(q→r). Son equivalentes.)

### Punto 2
**a) VERDADERO.** ∅ ⊆ A para todo A (vacuamente), y X⊆A ⟺ X∈𝒫(A). Luego ∅ ∈ 𝒫(A). ∎

**b) VERDADERO.** {A} ⊆ 𝒫(A) ⟺ todo elemento de {A} está en 𝒫(A). El único elemento de {A} es A, y A ∈ 𝒫(A) porque A ⊆ A. ∎
> ⚠️ No confundir con "A ⊆ 𝒫(A)", que es falso en general. Aquí es {A} (el conjunto cuyo único elemento es A).

**c) VERDADERO.** Sea X ∈ 𝒫(A) ⟹ X⊆A ⟹ (transitividad con A⊆B) X⊆B ⟹ X∈𝒫(B). ∴ 𝒫(A)⊆𝒫(B). ∎

### Punto 3
Patrón: empieza en 3, salta de 4 en 4 → 4n + 3 (o 4n − 1).
$$Y = \{\, x \in \mathbb{N} : x = 4n + 3,\ n \in \mathbb{N} \,\} = \{4n+3 : n \in \mathbb{N}\}$$
Equivalente: {x ∈ ℕ : x ≡ 3 (mod 4)}.

### Punto 4 — A \ (B∪C) = (A\B) ∩ (A\C)
```
Sea x ∈ A\(B∪C)
⟺ x∈A ∧ x∉(B∪C)
⟺ x∈A ∧ ¬(x∈B ∨ x∈C)
⟺ x∈A ∧ (x∉B ∧ x∉C)          [De Morgan]
⟺ (x∈A ∧ x∉B) ∧ (x∈A ∧ x∉C)  [idempotencia de x∈A + reordenar]
⟺ x∈(A\B) ∧ x∈(A\C)
⟺ x ∈ (A\B)∩(A\C). ∎
```

### Punto 5
**a) VERDADERO.** Si A∪B = A∩B:
- Siempre A ⊆ A∪B = A∩B ⊆ B, luego A⊆B.
- Siempre B ⊆ A∪B = A∩B ⊆ A, luego B⊆A.
- ∴ A = B. ∎

**b) VERDADERO.** Sea (a,b) ∈ R∪S ⟹ (a,b)∈R ∨ (a,b)∈S.
- Si (a,b)∈R, por simetría de R, (b,a)∈R ⟹ (b,a)∈R∪S.
- Si (a,b)∈S, por simetría de S, (b,a)∈S ⟹ (b,a)∈R∪S.
- En ambos casos (b,a)∈R∪S. ∴ R∪S simétrica. ∎
> 💡 Simetría SÍ se preserva bajo unión. (Transitividad NO — ojo con esa trampa.)

**c) FALSO.** Contraejemplo: A = {1}, B = {2}.
- A\B = {1}, (A\B)∪B = {1,2} ≠ {1} = A. ✗
> 💡 (A\B)∪B = A∪B, no A. Solo sería A si B ⊆ A.

---

## 📋 Respuestas rápidas
| Punto | Respuesta |
|-------|-----------|
| 1 | Tautología ✅ |
| 2a | V (∅⊆A) |
| 2b | V ({A} tiene a A, y A∈𝒫(A)) |
| 2c | V (monotonía de 𝒫) |
| 3 | Y = {4n+3 : n∈ℕ} |
| 4 | De Morgan + distributiva |
| 5a | V (A⊆B y B⊆A) |
| 5b | V (simetría se preserva) |
| 5c | **F** (contraejemplo A={1},B={2}) |
