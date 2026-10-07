# 🎯 CHEAT-SHEET — Parcial 1 Matemáticas Discretas I (Matemática Estructural)

> Regla de oro: JUSTIFICA TODO. Si es verdadero → demostración formal. Si es falso → CONTRAEJEMPLO concreto.

---

## 1️⃣ LÓGICA
- p→q es FALSA solo cuando p=V, q=F. Todo lo demás V.
- Tautología: tabla de verdad toda V, o suponer falso y llegar a ⊥.
- p→q ≡ ¬p∨q. Contrapositiva: p→q ≡ ¬q→¬p.
- ¬(p→q) ≡ p∧¬q. ¬(p∧q) ≡ ¬p∨¬q (De Morgan).

## 2️⃣ CONJUNTOS — Definiciones
- A ⊆ B ⟺ ∀x: x∈A ⟹ x∈B. (Para demos: "sea x∈A, entonces... ⟹ x∈B.")
- A = B ⟺ A⊆B ∧ B⊆A. (Doble contención.)
- 𝒫(A) = {X : X ⊆ A}. |𝒫(A)| = 2^|A|. Siempre ∅ ∈ 𝒫(A) y A ∈ 𝒫(A).
- X ⊆ A ⟺ X ∈ 𝒫(A). ← LA conversión fundamental.

## 3️⃣ OPERACIONES
- A ∪ B: x∈A ∨ x∈B.     A ∩ B: x∈A ∧ x∈B.
- A \ B: x∈A ∧ x∉B.     Aᶜ: x ∈ 𝒰 ∧ x∉A.
- **A\B = A∩Bᶜ** — la reescritura reina.
- Demos = traducir a lógica → aplicar ley → retranducir.

### Identidades favoritas del profe
- (A∪B)\A = B\A.  (Lo que se une de B, al quitar A, queda lo puro de B.)
- A\B = A∩Bᶜ.
- De Morgan: (A∪B)ᶜ = Aᶜ∩Bᶜ ; (A∩B)ᶜ = Aᶜ∪Bᶜ.
- A⊆B ⟹ 𝒫(A) ⊆ 𝒫(B) (monotonía).

## 4️⃣ CONJUNTO POTENCIA — Trampas tipo parcial

### A ⊆ 𝒫(𝒫(A)) → ¿V o F?
- Para que A ⊆ 𝒫(𝒫(A)), necesito que cada x∈A sea también x∈𝒫(𝒫(A)), o sea x⊆𝒫(A).
- Si x es un "objeto común" (ej: un número), NO es un subconjunto de 𝒫(A).
- **FALSO en general.** Contraejemplo: A = {1}. 𝒫(A) = {∅, {1}}. 𝒫(𝒫(A)) = {∅, {∅}, {{1}}, {∅,{1}}}. 1 ∉ 𝒫(𝒫(A)). ✗

### 𝒫(A) ∈ 𝒫(𝒫(A)) → ¿V o F?
- 𝒫(A) ∈ 𝒫(𝒫(A)) ⟺ 𝒫(A) ⊆ 𝒫(A). ¡Siempre cierto! (Todo conjunto es subconjunto de sí mismo.)
- **VERDADERO.** ✅

### 𝒫(A∪B) ⊇ 𝒫(A) ∪ 𝒫(B) → ¿V o F?
- Sea X ∈ 𝒫(A) ∪ 𝒫(B) ⟹ X∈𝒫(A) ∨ X∈𝒫(B) ⟹ X⊆A ∨ X⊆B ⟹ X⊆A∪B ⟹ X∈𝒫(A∪B).
- **VERDADERO.** ✅

## 5️⃣ DESCRIBIR CONJUNTOS INTENSIONALMENTE
- Ver el patrón: {6, 10, 14, 18, 22, ...} → empiezan en 6, de 4 en 4.
- Fórmula: a_n = 6 + 4(n-1) = 4n + 2 (n ≥ 1) o equivalente 2(2n+1) para n ≥ 1.
- Alternativo: pares no múltiplos de 4 mayores que 4, o sea {x ∈ ℕ : x ≥ 6 ∧ x ≡ 2 (mod 4)}.
- También: {4n + 2 : n ∈ ℕ, n ≥ 1} o {2(2k+1) : k ∈ ℕ, k ≥ 1} si quieres ser elegante.

## 6️⃣ RELACIONES
- R ⊆ X×X. Propiedades: reflexiva, simétrica, antisimétrica, transitiva.
- Reflexiva: ∀a∈X: (a,a)∈R.
- Simétrica: (a,b)∈R ⟹ (b,a)∈R.
- Antisimétrica: (a,b)∈R ∧ (b,a)∈R ⟹ a=b.
- Transitiva: (a,b)∈R ∧ (b,c)∈R ⟹ (a,c)∈R.
- **R∪S reflexivas ⟹ R∪S reflexiva** (∀a: (a,a)∈R ⟹ (a,a)∈R∪S). ✅
- Eq. de equivalencia = Ref+Sim+Trans. Orden parcial = Ref+Antisim+Trans.

## 7️⃣ VERDADERO O FALSO — Trucos
- **V:** escribe una demostración formal ("sea x ∈ ...").
- **F:** da un CONTRAEJEMPLO numérico concreto.
- Truco: si crees que es falso, prueba con conjuntos chiquitos (A={1}, B={2}).
- Para ∃ (existe): basta exhibir UN ejemplo.
- Para ∀ (para todo): un solo contraejemplo rompe.
- "Existe X tal que..." → piensa en X = ∅ o X = 𝒰 como candidatos.

---

## ⚠️ ERRORES FRECUENTES
1. Confundir ∈ con ⊆. "3 ∈ {3}" ✅ pero "3 ⊆ {3}" ✗ (3 no es un conjunto).
2. Confundir ∅ con {∅}. |∅|=0, |{∅}|=1.
3. En V/F sobre 𝒫: antes de responder, EVALÚA con A concreto chiquito.
4. Olvidar que antisimétrica NO es lo contrario de simétrica. Pueden cumplirse ambas (ej: ≤ en {1}).
