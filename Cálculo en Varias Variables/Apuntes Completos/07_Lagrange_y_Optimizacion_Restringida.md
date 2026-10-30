# 07 · Optimización restringida: Lagrange, sustitución y región cerrada

> **Clases fuente:** 5 Oct (1er algoritmo: optimizar en región encerrada por una curva), 14 Oct (ejercicios), 19 Oct (multiplicadores de Lagrange). Sección **4.2 Marsden-Tromba**.
> **Idea en una línea:** cuando optimizas f pero estás **obligado a quedarte sobre una curva/frontera** g(x)=c, en el óptimo el gradiente de f es **paralelo** al de g: `∇f = λ∇g`. Ese es Lagrange. Alternativa: **parametrizar** la curva y reducir a Cálculo 1.

---

## 1. Dos situaciones distintas (no confundir)

| Situación | Qué pide | Método |
|-----------|----------|--------|
| **Optimización LIBRE** | máx/mín de f en todo ℝ² | ∇f=0 + Hessiano (apunte 06) |
| **Optimización RESTRINGIDA** | máx/mín de f **sujeto a** g(x,y)=c | Lagrange ó sustitución/parametrización |
| **Máx/mín ABSOLUTO en región cerrada** | máx/mín de f en un dominio acotado (interior + borde) | 1er algoritmo del profe (interior + frontera) |

---

## 2. Por qué funciona Lagrange (la derivación del profe, 19 Oct)

Recordando del parcial 1: si g: ℝⁿ→ℝ es diferenciable, entonces **∇g(p) es perpendicular (⊥) a la curva/superficie de nivel g⁻¹(c)**.
(Demostración: si α(t) vive en el nivel, g(α(t))=c constante → derivando, ∇g·α'=0 → ∇g ⊥ al tangente.)

Ahora, el truco: si x₀ es un **máx o mín de f restringido a la curva** S=g⁻¹(c), y parametrizamos la curva con α (α(0)=x₀), entonces f∘α tiene un máx/mín en t=0, así que su derivada se anula:
```
(f∘α)'(0) = ∇f(x₀) · α'(0) = 0
```
Esto dice que **∇f(x₀) ⊥ al tangente de la curva**. Pero **∇g(x₀) TAMBIÉN es ⊥ al tangente**. Dos vectores perpendiculares a la misma recta tangente (en el plano) son **paralelos**, así que existe un escalar λ con:

```
┌─────────────────────────┐
│   ∇f(x₀) = λ ∇g(x₀)      │   ← ecuación de Lagrange
└─────────────────────────┘
```

`λ` es el **multiplicador de Lagrange**.

---

## 3. MÉTODO Lagrange (paso a paso)

Para optimizar **f(x,y)** sujeto a **g(x,y) = c**:

1. Plantear el sistema:
   - ∂f/∂x = λ ∂g/∂x
   - ∂f/∂y = λ ∂g/∂y
   - g(x,y) = c  (la restricción)
2. Resolver el sistema (3 ecuaciones, incógnitas x, y, λ).
3. Evaluar f en cada punto candidato → el mayor es el máx, el menor el mín.

> **Varias restricciones:** si hay g₁=0 y g₂=0 (como en el ejemplo del profe con cilindro ∩ plano), entonces ∇f = λ₁∇g₁ + λ₂∇g₂.

---

## 4. MÉTODO sustitución / parametrización (la alternativa del profe)

El profe **insiste en resolver de las dos formas** para verificar. La alternativa a Lagrange:

1. **Parametrizar** la curva restricción con una variable t (ej: una circunferencia → (cos t, sen t)).
2. **Sustituir** en f → queda h(t) = f(curva), una función de UNA variable.
3. **Cálculo 1:** h'(t)=0 → puntos críticos de t → evaluar.

> **Ejemplo del profe (19 Oct):** optimizar f(x,y,z)=x+y+z sujeto a g₁=x²+y²−2=0 (cilindro) y g₂=x+z−1=0 (plano). La intersección es una curva que parametriza como
> α(θ) = (√2 cosθ, √2 senθ, 1−√2 cosθ).
> Sustituye: f(α(θ)) = √2 cosθ + √2 senθ + (1−√2 cosθ) = **1 + √2 senθ**.
> Esto se maximiza en θ=π/2 y se minimiza en θ=3π/2. ✅ (Mucho más simple que el sistema de Lagrange con dos λ.)

---

## 5. EL "PRIMER ALGORITMO" del profe (máx/mín ABSOLUTO en región cerrada)

> Esto es el **tema estrella del 5 Oct** y cae en el modelo (P6: máx/mín en un triángulo). Es el análogo multivariable del "evaluar en los extremos [a,b]" de Cálculo 1.

En Cálculo 1, para f:[a,b]→ℝ continua: (1) hallar puntos críticos del interior, (2) evaluar f en a y b, (3) comparar. El máx y mín absolutos están entre esos candidatos (Teorema de Weierstrass: f continua en cerrado y acotado SÍ alcanza máx y mín).

**Versión del profe para f: región D ⊂ ℝ² acotada por una curva cerrada:**

1. **Interior:** encontrar los puntos críticos de f en el interior (∇f=0).
2. **Frontera:** **parametrizar la frontera** (la curva que encierra D) con γ, y optimizar **f∘γ** (una variable) → esto da los candidatos del borde. Para un polígono (triángulo, rectángulo), parametrizar lado por lado y revisar también los **vértices**.
3. **Comparar:** evaluar f en TODOS los candidatos (interior + frontera) → el mayor es el máx absoluto, el menor el mín absoluto.

> Clave del profe: la frontera se maneja **parametrizando** y reduciendo a Cálculo 1 (igual que la sustitución). No hace falta Lagrange para el borde si sabes parametrizarlo.

---

## 6. EJEMPLO RESUELTO 1 — Lagrange (sabor parcial: caja)

**Una caja de dimensiones l, a, h cumple l + 2a + 2h = 120. Maximizar el volumen V = l·a·h.** (Modelo P4 del Parcial 2.)

**Vía Lagrange:** f = l a h, restricción g = l + 2a + 2h = 120.
∇f = (ah, lh, la), ∇g = (1, 2, 2).
Sistema:
- ah = λ·1
- lh = λ·2
- la = λ·2

De la 2ª y 3ª: lh = la → h = a (si l≠0). De la 1ª y 2ª: ah=λ, lh=2λ → lh = 2ah → l = 2a.
Restricción: l+2a+2h = 2a+2a+2a = 6a = 120 → **a=20, h=20, l=40**.
Volumen máx = 40·20·20 = **16000**. ✅

> **Verificación por sustitución** (lo que pide el profe): despejar l=120−2a−2h, V=(120−2a−2h)·a·h, y optimizar con ∂V/∂a=0, ∂V/∂h=0 → mismo resultado. (Nota: esta caja da "cubo con dos lados dobles"; compara con el ejercicio 21 del Marsden donde la caja óptima ES un cubo.)

---

## 7. EJEMPLO RESUELTO 2 — región cerrada (sabor parcial: triángulo)

**Hallar máx y mín absolutos de f(x,y) = x + y en el triángulo de vértices (0,0), (2,0), (0,2).**

**Paso 1 — interior:** ∇f = (1,1) ≠ (0,0) nunca → **no hay críticos en el interior**. El óptimo está en la frontera.

**Paso 2 — frontera (3 lados):**
- Lado y=0, x∈[0,2]: f=x → va de 0 a 2.
- Lado x=0, y∈[0,2]: f=y → va de 0 a 2.
- Lado x+y=2 (hipotenusa): f=x+y=2 constante → vale 2 en todo el lado.

**Paso 3 — comparar (incluyendo vértices):**
f(0,0)=0, f(2,0)=2, f(0,2)=2, y todo el lado x+y=2 vale 2.
**Mínimo absoluto = 0 en (0,0); máximo absoluto = 2 (en toda la hipotenusa).** ✅

> Justificación del profe: "f es continua y el triángulo es cerrado y acotado, por Weierstrass alcanza máx y mín; comparando interior y frontera..."

---

## 8. ¿Cuándo uso cuál? (guía rápida)
- Restricción es una **ecuación g=c** y me piden máx/mín sobre ella → **Lagrange** (o parametrizar si la curva es fácil).
- La curva restricción se **parametriza fácil** (círculo, elipse, recta) → **sustitución** (más rápido, menos álgebra).
- Me dan una **región cerrada** (disco, triángulo, rectángulo) y piden máx/mín absolutos → **1er algoritmo**: interior (∇f=0) + frontera (parametrizar) + vértices.
- El profe pide "de dos formas" → haz Lagrange Y sustitución, deben coincidir.

---

## 9. Errores típicos (trampas)
- **Olvidar la frontera** en región cerrada: el óptimo casi siempre está en el borde.
- **Olvidar los vértices** del polígono al comparar.
- **No incluir la ecuación de restricción** en el sistema de Lagrange (son 3 ecuaciones, no 2).
- **Dividir por cero** al despejar en Lagrange: si asumes l≠0, verifica aparte el caso l=0.
- **No justificar con Weierstrass** que el máx/mín existen.
- Olvidar que con **dos restricciones** es ∇f = λ₁∇g₁ + λ₂∇g₂.

---

## 10. Checklist mental
- [ ] ¿Identifiqué si es libre, restringida (g=c) o región cerrada?
- [ ] Lagrange: ¿planteé las 3 ecuaciones (incluida la restricción)?
- [ ] ¿Verifiqué por el segundo método (sustitución) como pide el profe?
- [ ] Región cerrada: ¿interior + frontera (parametrizada) + vértices?
- [ ] ¿Evalué f en todos los candidatos y comparé?
- [ ] ¿Justifiqué (Weierstrass / teorema de Lagrange)?
