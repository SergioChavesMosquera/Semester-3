# ✅ SOLUCIONES — Parcial I (24 Marzo 2021) · Prof. Cano

> Parcial 1 real de tu corte. 5 puntos de 10 c/u. JUSTIFICA TODO.

---

## Punto 1 (10 pts) — Rotación de ejes
**Enunciado:** Haga una rotación de ejes para identificar si las raíces de `p(x,y) = x² + xy + y² − 6` son elipse, parábola, circunferencia o hipérbola.

**Solución:**
La cónica es `x² + xy + y² = 6`. Coeficientes: `A=1` (x²), `B=1` (xy), `C=1` (y²).

**Método rápido — el discriminante `B² − 4AC`:**
- `B² − 4AC = 1² − 4(1)(1) = 1 − 4 = −3`
- Regla: si `B²−4AC < 0` → **ELIPSE** (o circunferencia); si `=0` → parábola; si `>0` → hipérbola.
- Como `−3 < 0` → es una **ELIPSE**.

**Con rotación (lo que pide explícitamente):**
El término `xy` indica rotación. El ángulo θ cumple `cot(2θ) = (A−C)/B = (1−1)/1 = 0` → `2θ = 90°` → **θ = 45°**.
Al rotar 45° con `x = (x'−y')/√2`, `y = (x'+y')/√2` y sustituir, el término `xy` desaparece y queda:
- `x²+xy+y²` se transforma en `(3/2)x'² + (1/2)y'²`
- Ecuación rotada: `(3/2)x'² + (1/2)y'² = 6` → `x'²/4 + y'²/12 = 1`
- Suma de cuadrados = 1 → **ELIPSE** ✓ (confirma el discriminante).

**Respuesta: ELIPSE.**

💡 Truco de examen: el discriminante `B²−4AC` te da la respuesta al instante. La rotación es para "mostrar el procedimiento".

---

## Punto 2 (10 pts) — Plano tangente a superficie parametrizada
**Enunciado:** `φ(x,y) = (x²+2y, y−x, xy)`. Encuentre la ecuación del plano tangente en el punto `(1,−1,0)`.

**Solución (método vectores tangentes + producto cruz):**

Primero, ¿qué `(x,y)` da el punto `(1,−1,0)`? Resolviendo `x²+2y=1`, `y−x=−1`, `xy=0`:
- De `xy=0`: x=0 o y=0. Si y=0: `y−x=−1`→x=1, y `x²+2y=1`✓. Entonces **(x,y)=(1,0)**.

Vectores tangentes (derivadas parciales de φ):
- `φ_x = ∂φ/∂x = (2x, −1, y)` → en (1,0) → `(2, −1, 0)`
- `φ_y = ∂φ/∂y = (2, 1, x)` → en (1,0) → `(2, 1, 1)`

Normal = `φ_x × φ_y` = `(2,−1,0) × (2,1,1)`:
- X: `(−1)(1) − (0)(1) = −1 − 0 = −1`
- Y: `−[(2)(1) − (0)(2)] = −[2−0] = −2`
- Z: `(2)(1) − (−1)(2) = 2 + 2 = 4`
- Normal = `(−1, −2, 4)`

Ecuación del plano en `P=(1,−1,0)`:
```
−1(x−1) − 2(y+1) + 4(z−0) = 0
−x + 1 − 2y − 2 + 4z = 0
−x − 2y + 4z − 1 = 0   →   x + 2y − 4z = −1
```

**Verificación:** meto (1,−1,0): `1 + 2(−1) − 4(0) = 1−2 = −1` ✓

**Respuesta: x + 2y − 4z = −1**

---

## Punto 3 (10+10 pts) — Matriz derivada + Regla de la cadena
**Enunciado:**
i) Matriz derivada de `f(x,y) = (−x², e^(x−y), cos(xy²))` y `g(x,y) = (−x²+y, x−y)`.
ii) Usando regla de la cadena, calcule `D(f∘g)` en (1,1).

**Solución i):**

**Df** (f va de R²→R³, matriz 3×2):
```
              ∂/∂x            ∂/∂y
f₁=−x²     [ −2x              0          ]
f₂=e^(x−y) [ e^(x−y)        −e^(x−y)     ]
f₃=cos(xy²)[ −y²·sen(xy²)   −2xy·sen(xy²)]
```

**Dg** (g va de R²→R², matriz 2×2):
```
              ∂/∂x    ∂/∂y
g₁=−x²+y   [ −2x       1  ]
g₂=x−y     [  1       −1  ]
```

**Solución ii):**
Regla de la cadena: `D(f∘g)(1,1) = Df|_{g(1,1)} · Dg|_{(1,1)}`

Paso 1 — punto de adentro: `g(1,1) = (−1²+1, 1−1) = (0, 0)`.

Paso 2 — evaluar Df en (0,0) [x=0, y=0]:
- f₁: `(−2·0, 0) = (0, 0)`
- f₂: `(e⁰, −e⁰) = (1, −1)`
- f₃: `(−0·sen0, −0·sen0) = (0, 0)`
```
Df|_(0,0) = [ 0   0 ]
            [ 1  −1 ]
            [ 0   0 ]
```

Paso 3 — evaluar Dg en (1,1):
```
Dg|_(1,1) = [ −2   1 ]
            [  1  −1 ]
```

Paso 4 — multiplicar `Df · Dg` (3×2 · 2×2 = 3×2):
```
[ 0   0 ]   [ −2   1 ]   [ 0·−2+0·1    0·1+0·−1 ]   [ 0    0 ]
[ 1  −1 ] · [  1  −1 ] = [ 1·−2+−1·1   1·1+−1·−1] = [ −3   2 ]
[ 0   0 ]                [ 0·−2+0·1    0·1+0·−1 ]   [ 0    0 ]
```

**Respuesta: D(f∘g)(1,1) = [[0,0],[−3,2],[0,0]]**

---

## Punto 4 (10 pts) — Límite con función continua
**Enunciado:** Argumente por qué `lim_{(x,y)→(π, 1/2)} sen(xy) = 1`.

**Solución:**
- `sen` es una función **continua**, y el producto `xy` es continuo (polinomio).
- Por el teorema de composición de funciones continuas, el límite "entra" en la función continua:
```
lim_{(x,y)→(π,1/2)} sen(xy) = sen( lim_{(x,y)→(π,1/2)} xy ) = sen(π · 1/2) = sen(π/2) = 1
```
- Justificación: como sen es continua, `lim sen(xy) = sen(lim xy)`. Y `lim xy = π·(1/2) = π/2`. Y `sen(π/2)=1`.

**Respuesta: el límite es 1, porque sen es continua y permite meter el límite adentro.**

---

## Punto 5 (10 pts) — Continuidad por definición
**Enunciado:** Argumente usando la definición de continuidad por qué `f(x,y) = xy/(2x²+y²)` si (x,y)≠0, y `f(0,0)=1`, NO es continua en (0,0).

**Solución:**
Definición: f es continua en (0,0) si `lim_{(x,y)→(0,0)} f(x,y) = f(0,0) = 1`.
Basta mostrar que el límite NO da 1 (o que no existe) → no es continua.

**Muestro que el límite NO existe (2 caminos distintos):**
- Camino y=0 (eje x): `f(x,0) = (x·0)/(2x²+0) = 0/2x² = 0` → tiende a **0**
- Camino y=x: `f(x,x) = (x·x)/(2x²+x²) = x²/3x² = 1/3` → tiende a **1/3**

Como dos caminos dan valores distintos (0 y 1/3), **el límite NO existe.**
Por tanto `lim f(x,y) ≠ f(0,0)=1` → **f NO es continua en (0,0).** ∎

💡 Nota: incluso si el límite existiera, tendría que ser =1 para ser continua. Como ni siquiera existe, con más razón no es continua.

---

## 📊 Resumen de métodos usados
| Punto | Tema | Clave |
|-------|------|-------|
| 1 | Cónicas/rotación | discriminante B²−4AC<0 → elipse |
| 2 | Plano tangente param | φ_x×φ_y = normal → n·(X−P)=0 |
| 3 | Jacobiana + cadena | D(f∘g)=Df\|_{g}·Dg, evaluar en g(punto) |
| 4 | Límite continuo | meter límite en sen (continua) |
| 5 | Continuidad def | 2 caminos distintos → no existe → no continua |
