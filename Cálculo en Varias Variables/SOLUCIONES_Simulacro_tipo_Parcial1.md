# ✅ SOLUCIONES — Simulacro tipo Parcial 1 (estilo Cano)

> Ejercicios nuevos del mismo tipo y dificultad que caen en tu parcial. Resuelve tú primero, luego compara. JUSTIFICA TODO.

---

## Punto 1 (10 pts) — Matriz de derivadas parciales
**Enunciado:** Encuentre la matriz de derivadas parciales en `(0,1,0)` de:
`f(x,y,z) = ( x·y + z , e^(xz) , y·cos(z) )`

**Solución:** R³→R³, matriz 3×3.
```
                ∂/∂x       ∂/∂y      ∂/∂z
f₁=xy+z      [  y          x         1        ]
f₂=e^(xz)    [  z·e^(xz)   0         x·e^(xz) ]
f₃=y·cos z   [  0          cos z     −y·sen z ]
```
Evalúo en (0,1,0): recuerda e^(xz)=e⁰=1, cos0=1, sen0=0.
- Fila 1: (1, 0, 1)   [y=1, x=0, 1]
- Fila 2: (0·1, 0, 0·1) = (0, 0, 0)   [z=0, x=0]
- Fila 3: (0, cos0, −1·sen0) = (0, 1, 0)
```
Df(0,1,0) = [ 1  0  1 ]
            [ 0  0  0 ]
            [ 0  1  0 ]
```

---

## Punto 2 (10 pts) — Límite
**Enunciado:** ¿Existe `lim_{(x,y)→(0,0)} (x³ + y³)/(x² + y²)`? Justifique.

**Solución (acotamiento / sándwich):**
Todos los caminos dan 0 → sospecho que existe y vale 0. Confirmo:
```
|(x³+y³)/(x²+y²)| ≤ |x³|/(x²+y²) + |y³|/(x²+y²)
                  = |x|·[x²/(x²+y²)] + |y|·[y²/(x²+y²)]
                  ≤ |x|·1 + |y|·1 = |x| + |y| → 0
```
(cada corchete ≤ 1). Por sándwich, **el límite = 0**.

💡 REMATE: separo en dos fracciones, factorizo |x| y |y|, acoto los corchetes por 1, → 0.

---

## Punto 3 (10 pts) — Derivada direccional por definición
**Enunciado:** Usando la definición, calcule la derivada direccional de `f(x,y) = x² + xy` en `p=(1,2)` dirección `v=(1,3)`. Verifique con el gradiente.

**Por definición (v directo, sin normalizar):**
- `p+hv = (1+h, 2+3h)`
- `f(1+h, 2+3h) = (1+h)² + (1+h)(2+3h)`
  - `(1+h)² = 1 + 2h + h²`
  - `(1+h)(2+3h) = 2 + 3h + 2h + 3h² = 2 + 5h + 3h²`
  - suma: `3 + 7h + 4h²`
- `f(1,2) = 1 + 2 = 3`
- cociente: `[(3+7h+4h²) − 3]/h = [7h+4h²]/h = 7 + 4h`
- límite h→0: **7**

**Verificación gradiente:**
- `∇f = (2x+y, x)` → `∇f(1,2) = (2·1+2, 1) = (4, 1)`
- `∇f·v = (4,1)·(1,3) = 4 + 3 = 7` ✓

**Respuesta: D_v f(1,2) = 7.**

---

## Punto 4 (10 pts) — Dominio y continuidad
**Enunciado:** Encuentre el dominio de `f(x,y) = ln(x+y) + √(1 − x² − y²)` y diga dónde es continua.

**Solución:** Dos condiciones (intersección):
- Log: `x + y > 0` → `y > −x` (semiplano estricto sobre la recta y=−x, sin la recta).
- Raíz: `1 − x² − y² ≥ 0` → `x² + y² ≤ 1` (disco cerrado radio 1, con borde).

```
Dom(f) = { (x,y) : x+y>0  Y  x²+y²≤1 }
```
Geométricamente: **la parte del disco unitario (radio 1) que está por encima de la recta y=−x**; borde curvo incluido, recta NO.

**Continuidad:** f es continua en TODO su dominio (suma de ln y raíz, ambas continuas donde están definidas; composición/suma de continuas). ∎

---

## Punto 5 (10 pts) — Parametrizar intersección
**Enunciado:** Parametrice la curva intersección del paraboloide `z = x² + y²` con el plano `z = 4`.

**Solución:**
- Igualo: `x² + y² = 4` → círculo de radio 2 a la altura z=4.
- Parametrización:
```
r(t) = ( 2cos t, 2sen t, 4 ),   t ∈ [0, 2π]
```
💡 REMATE: escribir el rango t∈[0,2π].

---

## Punto 6 (10 pts) — Plano tangente (método gradiente)
**Enunciado:** Encuentre la ecuación del plano tangente a `z = x² + 2y²` en el punto `(1,1,3)`.

**Solución (gradiente = normal):**
- Reescribo como superficie de nivel: `f(x,y,z) = x²+2y²−z = 0`
- `∇f = (2x, 4y, −1)` → en (1,1,3) → `(2, 4, −1)` = normal
- Ecuación: `2(x−1) + 4(y−1) − (z−3) = 0`
  - `2x−2 + 4y−4 − z+3 = 0`
  - `2x + 4y − z − 3 = 0` → **2x + 4y − z = 3**
- Verificación: meto (1,1,3): `2+4−3 = 3` ✓

**Respuesta: 2x + 4y − z = 3.**

---

## 📊 Resumen
| Punto | Tema | Remate a no olvidar |
|-------|------|---------------------|
| 1 | Jacobiana | e⁰=1, cos0=1, sen0=0 al evaluar |
| 2 | Límite | separar, factorizar \|x\|,\|y\|, acotar ≤1, →0 |
| 3 | Deriv direccional | 2 formas (def+gradiente), coinciden |
| 4 | Dominio | decir "continua en dominio" + dibujo |
| 5 | Parametrizar | escribir t∈[0,2π] |
| 6 | Plano tangente | gradiente=normal → ecuación → verificar |
