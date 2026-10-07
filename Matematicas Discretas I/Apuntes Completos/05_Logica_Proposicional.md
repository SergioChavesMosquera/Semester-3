# Matemáticas Discretas I — Lógica Proposicional (Tablas de Verdad y Tautologías) 🧠

### Base para el preparcial · Matemática Estructural

**Leyenda:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Ley · 🔵 Notación · 🩷 Ejemplo · 💜 Advertencia

---

## 1. Conectivos y sus tablas de verdad

| p | q | ¬p | p∧q | p∨q | p→q | p↔q |
|---|---|----|----|----|----|----|
| V | V | F  | V  | V  | V  | V  |
| V | F | F  | F  | V  | F  | F  |
| F | V | V  | F  | V  | V  | F  |
| F | F | V  | F  | F  | V  | V  |

- 💜 **La implicación p→q solo es FALSA cuando p es V y q es F.** "Verdadero implica falso" es lo único prohibido.
- 🔵 p→q se lee "si p entonces q". Equivale a 🟡 **¬p ∨ q**.

---

## 2. Tautología

- 🟢 Una **tautología** es una proposición que es VERDADERA en TODAS las combinaciones de valores de verdad (toda la última columna V).
- 🟢 **Contradicción:** falsa en todas (toda F).
- 🟢 **Contingencia:** a veces V, a veces F.

### Cómo demostrar que algo es tautología
1. **Tabla de verdad:** construir todas las filas y verificar que la columna final sea toda V.
2. **Razonamiento informal:** suponer que es FALSA y llegar a una contradicción.

---

## 3. Leyes lógicas importantes (equivalencias)

- 🟠 **Doble negación:** ¬¬p ≡ p
- 🟠 **De Morgan:** ¬(p∧q) ≡ ¬p∨¬q ; ¬(p∨q) ≡ ¬p∧¬q
- 🟠 **Distributiva:** p∧(q∨r) ≡ (p∧q)∨(p∧r) ; p∨(q∧r) ≡ (p∨q)∧(p∨r)
- 🟠 **Contrapositiva:** p→q ≡ ¬q→¬p
- 🟠 **Implicación como ∨:** p→q ≡ ¬p∨q
- 🟠 **Negación de implicación:** ¬(p→q) ≡ p∧¬q

---

## 4. El ejercicio estrella del preparcial

**Demostrar que (p → (q → r)) → ((p → q) → (p → r)) es tautología.**

### Método A: Tabla de verdad (8 filas, 3 variables)
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

➡️ Columna TOTAL toda V ⟹ **es tautología**. ✅

### Método B: Razonamiento informal (suponer falso)
```
Supongo que TODA la implicación es FALSA.
Para que (A) → (B) sea F, necesito:
  (A) p→(q→r)  es V ... (1)
  (B) (p→q)→(p→r)  es F ... (2)

De (2) falsa: (p→q) es V ...(3) y (p→r) es F ...(4).
De (4) p→r falsa: p es V ...(5) y r es F ...(6).
De (3) p→q verdadera y p=V (5): entonces q es V ...(7).
De (1) p→(q→r) verdadera y p=V (5): entonces q→r es V ...(8).
Pero q=V (7) y r=F (6) ⟹ q→r es F. Contradice (8). ⊥

∴ No puede ser falsa ⟹ es tautología.  □
```

---

## Ideas clave para el parcial
1. p→q es FALSA solo cuando p=V, q=F. Memorízalo.
2. Tautología = toda la última columna V.
3. Método informal: supón falso y busca contradicción (más rápido que la tabla si hay muchas variables).
4. p→q ≡ ¬p∨q es la reescritura más útil.
