# Cálculo en Varias Variables — Límites por Caminos y Diferenciabilidad 🛤️

### Prof. Leonardo A. Cano G. · Clase 14 de septiembre 2026 · UNAL

**Leyenda de colores:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Ley/principio · 🔵 Notación/símbolo especial · 🩷 Ejemplo/analogía · 💜 Advertencia/aclaración

---

## 1. Teorema: el límite se conserva a lo largo de curvas ⭐

- 🟠«Si f: Rⁿ → R cumple lim_{x→a} f(x) = b, entonces para TODA curva α: (−c,c) → Rⁿ continua e inyectiva con α(0)=a, se tiene lim_{t→0} f(α(t)) = b.»
- 💜«Este es el fundamento del método de caminos: si el límite existe, da lo mismo por cualquier curva que llegue al punto. Por eso, si dos curvas dan valores distintos, el límite NO puede existir.»
- Idea de la prueba: para ε>0, el límite da un δ con f(Bδ(a)−{a}) ⊆ (b−ε, b+ε); como α es continua, hay un δ' con α((−δ',δ')−{0}) ⊆ Bδ(a)−{a}. Encadenando, f(α(t)) cae en (b−ε, b+ε).

---

## 2. Composición de funciones (repaso operativo)

- 🩷 Ejemplo i): α(t) = (t²−1, t+3),  g(x,y) = √(x²−y²). Calcular g∘α(t).
  - g(α(t)) = √( (t²−1)² − (t+3)² )  (reemplazo x=t²−1, y=t+3 dentro de g)
- 🩷 Ejemplo ii): F(x,y) = (x²−y, xy),  g(x,y) = (sen x, cos y, x+y). Calcular g∘F.
  - g(F(x,y)) = g(x²−y, xy) = ( sen(x²−y) , cos(xy) , (x²−y)+xy )
- 💜«ADVERTENCIA de dimensiones: F∘g NO se puede hacer aquí. g sale a R³ y F entra desde R², las dimensiones no encajan. Siempre revisa que la salida de una entre en la otra.»

---

## 3. Límites infinitos

- 🟢«lim_{x→a} f(x) = ∞ significa que f se dispara sin tope al acercarse a a.»
- 🟡«lim_{x→a} f(x) = ∞  ⟺  ∀N>0, ∃δ>0 tq  f( Bδ(a) − {a} ) ⊆ (N, ∞)»
- 💜«Cambia el "acercarse a b" por "superar cualquier cota N". Por grande que pongas la barra N, cerca de a la función ya la pasó.»
- 🩷 Ejemplo: lim_{x→0} 1/x² = ∞.

---

## 4. Coordenadas polares para límites en (0,0) ⭐

- 🔵«Cambio a polares: x = r·cosθ,  y = r·senθ.  Entonces (x,y)→(0,0) equivale a r→0.»
- 🟠«Regla práctica: sustituye y simplifica. Si al final el resultado depende SOLO de r (y r→0 lo manda a un número fijo), el límite existe. Si queda dependiendo de θ, el límite NO existe (porque θ es la dirección de acercamiento).»

- 🩷 Ejemplo i) (SÍ existe): lim_{(x,y)→(0,0)} x²y/(x+y)
  - En polares: r³(cos²θ·senθ) / ( r(cosθ+senθ) ) = r²·[ cos²θ·senθ / (cosθ+senθ) ]
  - El corchete es acotado (cociente de continuas periódicas), y r² → 0. Entonces el límite = **0**.

- 🩷 Ejemplo ii) (NO existe): lim_{(x,y)→(0,0)} (x²+y²)/(3x²+2y²)
  - En polares: r²·1 / ( r²(3cos²θ + 2sen²θ) ) = 🟡«1 / (3cos²θ + 2sen²θ)»
  - 💜«El resultado depende de θ (o sea, de la dirección) → el límite NO existe.»
  - Confirmación por caminos:
    - Eje x, α(t)=(t,0): lim x²/(3x²) = **1/3**
    - Eje y, β(t)=(0,t): lim t²/(2t²) = **1/2**
    - 1/3 ≠ 1/2 → NO existe. ✓

---

## 5. Diferenciabilidad (definición con h) ⭐

- 🟢«f: Rⁿ → Rᵐ es diferenciable en p si existe una transformación lineal T: Rⁿ → Rᵐ tal que:»
- 🟡«lim_{h→0} [ F(p+h) − F(p) − T·h ] / ‖h‖ = 0»
- 🟠«Intuición: las funciones diferenciables son las que se pueden APROXIMAR (cerca de p) por funciones lineales.»
- 💜«Es la misma idea de siempre: la derivada es la mejor aproximación lineal. Aquí "la pendiente" es la transformación lineal T (que como matriz será la derivada). El h es el desplazamiento pequeño desde p.»

---

## 6. Caso curvas α: R → Rⁿ (velocidad instantánea)

- 🟢«Una curva α: R → Rⁿ es diferenciable en t=a si admite velocidad instantánea (vector velocidad) en ese punto.»

- 🩷 Ejercicio: β(t) = (1−t², t³−2t).
  - i) Encuentra la función lineal que aproxima β en t=1.
    - Se usa 🟡«L(t) = β(a) + β'(a)·(t−a)»  (punto + velocidad·desplazamiento)
    - β(1) = (1−1, 1−2) = (0, −1)
    - β'(t) = (−2t, 3t²−2)  →  β'(1) = (−2, 1)
    - L(t) = (0,−1) + (−2, 1)·(t−1) = ( −2(t−1) , −1 + (t−1) )
  - ii) La recta tangente a β en β(1) es exactamente esa: 🟡«(x,y) = β(1) + t·β'(1) = (0,−1) + t·(−2,1)»
- 💜«Fíjate: la "función lineal que aproxima" y la "recta tangente" son la misma cosa. Punto de paso β(a) + dirección β'(a).»

---

## 7. Caso f: R² → R (plano tangente)

- 🟢«f: R² → R es diferenciable en a si la gráfica de f tiene un PLANO TANGENTE en el punto (a, f(a)).»
- 🟠«El plano tangente es el análogo (una dimensión arriba) de la recta tangente en R.»
- 💜«Imagen mental: pones una "tabla plana" que toca la superficie en el punto (a, f(a)) sin atravesarla. Si esa tabla existe y ajusta bien en todas las direcciones, f es diferenciable ahí. Los dos caminos a+(t,0) y a+(0,t) barren ese plano.»

---

## 📝 Problemas propuestos

1. Sea α(t)=(t, t²) y g(x,y)=x²+y. Calcula g∘α(t) y su límite cuando t→0.
2. Dadas F(x,y)=(x+y, x−y) y g(u,v)=(u², v², uv), calcula g∘F(x,y). ¿Se puede hacer F∘g? Justifica por dimensiones.
3. Usando coordenadas polares, decide si existe lim_{(x,y)→(0,0)} xy/(x²+y²). (Debe quedar dependiendo de θ.)
4. Usando polares, calcula lim_{(x,y)→(0,0)} (x³+y³)/(x²+y²). (Debe quedar acotado·r → 0.)
5. Muestra que lim_{(x,y)→(0,0)} (xy)/(x²+y²) NO existe usando los caminos y=0 y y=x.
6. Prueba con la definición de límite infinito que lim_{(x,y)→(0,0)} 1/(x²+y²) = ∞.
7. Sea β(t)=(cos t, sen t, t). Encuentra β'(t), el vector velocidad en t=0, y la recta tangente en β(0).
8. Para β(t)=(t²+1, 2t, t³) halla la función lineal que la aproxima en t=1 y la recta tangente en β(1).

---

*Este es el formato base para las próximas clases.*
