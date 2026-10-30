# 06 · Optimización libre: puntos críticos y Hessiano

> **Clases fuente:** 5 Oct (algoritmo de optimización), 7 Oct (Hessiano / máx-mín locales). Sección **4.2 Marsden-Tromba**.
> **Idea en una línea:** en varias variables, "derivada = 0" se vuelve "**gradiente = 0**", y "segunda derivada" se vuelve el **Hessiano** (una matriz). Con el signo del determinante del Hessiano decides máx, mín o silla.

---

## 1. De Cálculo 1 a varias variables (lo que ya sabes, reciclado)

En Cálculo 1, para hallar máx/mín de f(x):
1. Resolver f'(x) = 0 → puntos críticos (**Teorema de Fermat**: si hay un máx/mín en el interior, la derivada ahí es 0).
2. Mirar f''(x): si f''>0 es mínimo (cóncava arriba), si f''<0 es máximo.

En varias variables (f: ℝ² → ℝ) es **lo mismo con otro ropaje**:
1. f'(x)=0 se convierte en **∇f(p) = (0,0)** → los puntos donde el gradiente se anula son los **puntos críticos**.
2. f''(x) se convierte en el **Hessiano** (matriz de segundas parciales), y en vez de mirar su signo miras el **signo de su determinante**.

---

## 2. Puntos críticos: ∇f = 0

**Definición (profe).** `p` es **punto crítico** de f si `∇f(p) = 0`.

**Cómo se hace:** armas el gradiente, lo igualas al vector cero, y resuelves el **sistema** de ecuaciones.

### Definiciones del profe (máx/mín local y punto silla)
- `p` es **máximo local** si existe ε>0 tal que para todo `q` cercano (en la bola de radio ε), `f(q) ≤ f(p)`.
- **mínimo local**: igual pero `f(q) ≥ f(p)`.
- `p` es **punto silla** ⟺ es punto crítico pero **NO es máx ni mín local**. (Cerca de p, f toma valores mayores Y menores que f(p), según la dirección.)

> **Ejemplo del profe (5 Oct):** f(x,y)=xy. ∇f=(y,x)=(0,0) → punto crítico (0,0). Pero NO es máx ni mín: en el 1er cuadrante xy>0 y en el 2do xy<0, hay valores positivos y negativos arbitrariamente cerca de (0,0). Es un **punto silla**.

---

## 3. El Hessiano (clase 7 Oct) — "la segunda derivada" en matriz

**Definición (profe).** Si f: ℝ² → ℝ es **suave** (parciales iteradas de cualquier orden continuas), el **Hessiano** de f en p es:

```
                ⎡ ∂²f/∂x²(p)     ∂²f/∂x∂y(p) ⎤
Hess(f)(p)  =   ⎢                            ⎥
                ⎣ ∂²f/∂x∂y(p)    ∂²f/∂y²(p)  ⎦
```

Es una matriz **simétrica** (por Clairaut: las parciales cruzadas son iguales). Las entradas:
- esquina superior izq: deriva dos veces respecto a x → `f_xx`
- esquina inferior der: deriva dos veces respecto a y → `f_yy`
- las dos diagonales: la cruzada `f_xy` (= `f_yx`)

**El determinante** (el profe lo llama el **discriminante**):
```
det(Hess) = f_xx · f_yy − (f_xy)²
```

---

## 4. Criterio de clasificación (los dos teoremas del profe)

Sea p un punto crítico (∇f(p)=0). Mira `det(Hess(f)(p))`:

| det(Hess) | f_xx(p) | Conclusión |
|-----------|---------|------------|
| **< 0** | — (da igual) | **Punto SILLA** |
| **> 0** | f_xx < 0 | **Máximo local** |
| **> 0** | f_xx > 0 | **Mínimo local** |
| **= 0** | — | **Criterio NO decide** (caso dudoso) |

**Teoremas tal como los enunció el profe:**
- Si ∇f(p)=0 **y** det(Hess(f)(p)) **< 0** ⟹ p es **punto silla**.
- Si ∇f(p)=0 **y** det(Hess(f)(p)) **> 0** ⟹
  - (i) p es **máx local** si `∂²f/∂x²(p) < 0`
  - (ii) p es **mín local** si `∂²f/∂x²(p) > 0`

> **Truco mnemotécnico:** det>0 significa "copa" (hacia arriba o hacia abajo) → es máx o mín; el signo de f_xx te dice cuál (como la cóncava de Cálculo 1). det<0 significa "silla de montar". det=0 → el test se lava las manos, hay que analizar a mano.

### De dónde sale (la conexión con cuádricas, lo que motivó el profe)
El profe lo justificó desde la **clasificación de cuádricas** (parcial 1): todo polinomio cuadrático p(x,y)=ax²+by²+cxy+... se puede llevar por rotación/traslación a la forma Ax'²+By'²+C. Los **valores propios** de la matriz simétrica asociada dicen la forma: ambos del mismo signo → paraboloide (copa = máx/mín); signos opuestos → silla. El determinante del Hessiano = producto de valores propios, por eso su signo clasifica.

---

## 5. ALGORITMO completo (optimización LIBRE)

Para f: ℝ² → ℝ sin restricciones:

1. **Gradiente a cero:** resolver ∇f(x,y)=(0,0) → puntos críticos.
2. **Hessiano:** armar Hess(f) con las segundas parciales.
3. **Evaluar y clasificar:** meter cada punto crítico en el Hessiano, calcular det y f_xx, aplicar la tabla.
4. **Justificar** (el profe lo exige): decir explícitamente "det>0 y f_xx>0, luego mínimo local", etc.

---

## 6. EJEMPLO RESUELTO 1 (básico)

**Clasificar los puntos críticos de f(x,y) = x² + y² − xy.**

**Paso 1 — gradiente a cero:**
∇f = (2x − y, 2y − x) = (0,0)
→ 2x − y = 0 y 2y − x = 0 → y=2x, y sustituyendo x=2y=4x → x=0, y=0.
Único punto crítico: **(0,0)**.

**Paso 2 — Hessiano:**
f_xx=2, f_yy=2, f_xy=−1.
```
Hess = ⎡ 2   −1 ⎤
       ⎣ −1   2 ⎦
```

**Paso 3 — clasificar:**
det = (2)(2) − (−1)² = 4 − 1 = **3 > 0**, y f_xx = 2 **> 0**.
**⟹ (0,0) es mínimo local.** ✅

---

## 7. EJEMPLO RESUELTO 2 (sabor parcial — modelo P5 del Parcial 2)

**Encuentre los puntos críticos de f(x,y) = 3 + xy − x − 2y y clasifíquelos.**

**Paso 1 — gradiente:**
∂f/∂x = y − 1, ∂f/∂y = x − 2.
(y−1, x−2) = (0,0) → y=1, x=2. Punto crítico: **(2,1)**.

**Paso 2 — Hessiano:**
f_xx = 0, f_yy = 0, f_xy = 1.
```
Hess = ⎡ 0   1 ⎤
       ⎣ 1   0 ⎦
```

**Paso 3 — clasificar:**
det = (0)(0) − (1)² = **−1 < 0**.
**⟹ (2,1) es un punto silla.** ✅

> Justificación formal para el parcial: "Como ∇f(2,1)=0, (2,1) es punto crítico; y como det(Hess(f)(2,1)) = −1 < 0, por el teorema (7 Oct) es un punto silla."

---

## 8. Errores típicos a evitar (trampas del profe)
- **Confundir det<0 con máximo.** det<0 SIEMPRE es silla, sin importar f_xx.
- **Olvidar el cuadrado en la cruzada:** det = f_xx·f_yy − **(f_xy)²**, el término cruzado va al cuadrado.
- **Dar la respuesta sin justificar.** "Es mínimo" sin decir "det>0 y f_xx>0" = 0 puntos.
- **det=0 y creer que el test decide.** Si da 0, el criterio NO concluye; hay que analizar a mano (ver qué pasa en distintas direcciones, como el ejemplo xy).
- **Mal sistema de ∇f=0:** revisa que resolviste bien el sistema; a veces hay varios puntos críticos.

---

## 9. Checklist mental
- [ ] ¿Armé ∇f y lo igualé a (0,0)?
- [ ] ¿Resolví TODO el sistema (puede haber varios puntos)?
- [ ] ¿Hessiano con las 4 entradas bien (cruzada al cuadrado en el det)?
- [ ] ¿Clasifiqué con la tabla y JUSTIFIQUÉ con el teorema?
- [ ] ¿Revisé el caso det=0 por si cae?
