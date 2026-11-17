# 📱 Guía de bolsillo — ejercicios para el bus (mar 17)

> Para hacer en el celular/papel sin computador. Cada tema trae: **mini-recordatorio del procedimiento** + **ejercicios** + **respuestas al final** (no mires hasta terminar). Intenta de memoria primero; si te atascas, relee el recordatorio.

---

## ⚡ RECORDATORIOS DE PROCEDIMIENTO (léelos antes de arrancar)

### TEMA 1 — Optimización libre (Hessiano)
1. **Gradiente a cero:** saca fx, fy; iguala a 0; resuelve → puntos críticos.
2. **Hessiano:** f_xx, f_yy, f_xy → matriz [[f_xx, f_xy],[f_xy, f_yy]].
3. **Determinante:** det = f_xx·f_yy − (f_xy)². Si depende de x,y, evalúa en cada punto.
4. **Clasificar (mira det PRIMERO):**
   - det < 0 → **silla**
   - det > 0 y f_xx > 0 → **mínimo local**
   - det > 0 y f_xx < 0 → **máximo local**
   - det = 0 → no decide
   - **Respuesta = punto + tipo** (ej: "(3,−2) es mínimo local").

### TEMA 2 — Optimización región cerrada (máx/mín absolutos)
1. **Interior:** gradiente a cero → punto; ¿cae dentro? Evalúa f ahí.
2. **Frontera:** sustituye el borde en f → queda 1 variable → optimiza (crítico + extremos del intervalo).
3. **Comparar:** evalúa f en TODOS los candidatos. Mayor = máx abs, menor = mín abs.

### TEMA 3 — Lagrange (restricción g = c)
1. ∇f = λ∇g → ecuaciones: fx = λ·gx, fy = λ·gy.
2. Añade la restricción g = c (¡3ª ecuación!).
3. Resuelve el sistema → candidatos.
4. Evalúa f en cada candidato → mayor = máx, menor = mín.

### TEMA 4 — Integrales dobles
- **De adentro hacia afuera**, la otra variable constante.
- Tipo I: ∫(x:núm) ∫(y:func) f dy dx. Tipo II: ∫(y:núm) ∫(x:func) f dx dy.
- **Límite de afuera SIEMPRE número.**
- Armar región: hallar cortes de las curvas (límites de afuera) + cuál va arriba/abajo (límites de adentro).

### TEMA 5 — Cambio de variable / polares
- Fórmula: ∬ f dx dy = ∬ f(r cosθ, r senθ) · **r** dr dθ.
- Polares: x=r cosθ, y=r senθ, factor **r**. (x²+y² = r²)
- Disco completo: r de 0 a radio, θ de 0 a 2π.
- Jacobiano general: J = x_u·y_v − x_v·y_u, usar |J|.

### TEMA 6 — Triples + coordenadas 3D
- Triple = integrar 3 veces de adentro hacia afuera.
- **Cilíndricas:** x=r cosθ, y=r senθ, z=z. Factor **r** dz dr dθ.
- **Esféricas:** x=ρsenφcosθ, y=ρsenφsenθ, z=ρcosφ. Factor **ρ²senφ** dρ dφ dθ.
- φ de 0 a π (desde eje z), θ de 0 a 2π. Esfera: ρ=radio.
- Dato: ∫₀^π senφ dφ = 2.

### TEMA 7 — Centro de masa
- m = ∬ ρ dA (masa)
- My = ∬ x·ρ dA ; Mx = ∬ y·ρ dA (momentos)
- x̄ = My/m ; ȳ = Mx/m (centro)
- Simetría → el centro cae en el eje de simetría (justifícalo, ahorra cuentas).

---
---

## 🏋️ EJERCICIOS (haz al menos 3; empieza por optimización que es tu fuerte)

### Bloque A — Optimización (recomendados para el bus, no necesitan dibujar)

**A1.** Clasifica los puntos críticos de f(x,y) = x³ − 3x + y².
*(sale con 2 puntos críticos, Hessiano depende de x)*

**A2.** Clasifica los puntos críticos de f(x,y) = x² + y² − 4x + 2y + 1.
*(un solo punto, calentamiento)*

**A3.** Lagrange: máx y mín de f(x,y) = x + y sujeto a x² + y² = 4.

### Bloque B — Integrales (si tienes mesa/más comodidad)

**B1.** ∫₀¹ ∫₀² (x + 2y) dy dx   *(rectángulo)*

**B2.** ∫₀¹ ∫₀^(x) (2x) dy dx   *(tipo I)*

**B3.** Área del disco x²+y² ≤ 4 en polares (∬ 1 · r dr dθ).

---
---

## ✅ RESPUESTAS (no mirar hasta terminar)

**A1:** fx=3x²−3=0 → x=±1; fy=2y=0 → y=0. Puntos (1,0) y (−1,0).
Hess=[[6x,0],[0,2]], det=12x.
- (1,0): det=12>0, f_xx=6>0 → **mínimo local**.
- (−1,0): det=−12<0 → **punto silla**.

**A2:** fx=2x−4=0 → x=2; fy=2y+2=0 → y=−1. Punto (2,−1).
Hess=[[2,0],[0,2]], det=4>0, f_xx=2>0 → **mínimo local**.

**A3:** ∇f=(1,1), ∇g=(2x,2y). 1=λ2x, 1=λ2y → x=y. En x²+y²=4: 2x²=4 → x=±√2.
- (√2,√2): f=2√2 → **máximo**.
- (−√2,−√2): f=−2√2 → **mínimo**.

**B1:** adentro ∫₀²(x+2y)dy = xy+y² en y=2 → 2x+4. Afuera ∫₀¹(2x+4)dx = x²+4x en 1 = **5**.

**B2:** adentro ∫₀^x 2x dy = 2x·y en y=x → 2x². Afuera ∫₀¹ 2x² dx = 2x³/3 en 1 = **2/3**.

**B3:** ∫₀^(2π)∫₀² r dr dθ. Adentro: r²/2 en 2 = 2. Afuera: ∫₀^(2π) 2 dθ = **4π**. (= área del disco radio 2 ✅)

---

## 📌 Para contarme mañana en la noche
- ¿Cuáles salieron solos y cuáles con recordatorio?
- ¿Qué tema sentiste más flojo? (ahí nos enfocamos)
- Errores de signo (ojo con −(−2)² = −4).

> **Recuerda:** mente primero, recordatorio como red. Atascarte es donde más se aprende. ¡Vamos por ese parcial! 💪
