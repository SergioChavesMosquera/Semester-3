# 📝 Guía autónoma — para tus 2 horas en la U (12 nov, ¡feliz cumple! 🎂)

> **Cómo usarla:** lee el resumen, haz los ejercicios en papel SIN mirar las respuestas, y al final te autocorriges. Marca los que te costaron para contarme en la noche. No necesitas computador, solo papel y lápiz.

---

## ✅ Lo que YA dominas (arranca con confianza)

1. **Optimización libre** (Hessiano): gradiente a cero → Hessiano → determinante → clasificar.
   - det<0 = silla; det>0 y f_xx>0 = mín; det>0 y f_xx<0 = máx.
2. **Lagrange:** ∇f = λ∇g + la restricción. Resolver sistema → evaluar candidatos.
3. **Región cerrada:** interior (∇f=0) + frontera lado por lado + vértices → comparar todo.
4. **Integrales dobles sobre rectángulos:** integrar de adentro hacia afuera, una variable constante.

Lo de hoy (regiones tipo I) es lo único que quedó a medias. La guía arranca justo ahí.

---

## 🎯 TEMA DE HOY: Integrales dobles sobre regiones tipo I

### La idea
Cuando la región NO es rectángulo, los límites de la integral de ADENTRO son **funciones** (dependen de x), no números.

```
∫(x de a a b) ∫(y de abajo(x) a arriba(x))  f(x,y) dy dx
```
- Adentro (y): límites son curvas/funciones de x.
- Afuera (x): límites son NÚMEROS siempre.

**Regla de oro:** el límite de afuera SIEMPRE es numérico. Si queda una variable ahí, está mal.

### Cómo se resuelve (igual que rectángulos, con un detalle)
1. Integral de adentro: integras respecto a y, con x constante. Al evaluar, en el límite de arriba metes la **función** (ej. x², o x), no un número.
2. Integral de afuera: el resultado queda en x; lo integras entre los números.

---

### EJEMPLO RESUELTO A (guía — estúdialo primero)

**Calcular ∫₀¹ ∫₀^(x) (x + y) dy dx**

**Paso 1 — adentro** (∫₀^x (x+y) dy, x constante):
- primitiva (en y): x·y + y²/2
- evalúo y de 0 a **x** (el límite de arriba es x):
  - en y=x: x·(x) + (x)²/2 = x² + x²/2 = 3x²/2
  - en y=0: 0
  - resultado: **3x²/2**

**Paso 2 — afuera** (∫₀¹ (3x²/2) dx):
- primitiva: (3/2)·x³/3 = x³/2
- en x=1: 1/2 ; en x=0: 0
- **resultado: 1/2**

> Lo nuevo: al evaluar el límite de arriba (y=x), reemplazas y por x, y pueden aparecer x², x³, etc. Eso es normal.

---

### EJEMPLO RESUELTO B (guía — con parábola)

**Calcular ∫₀¹ ∫₀^(x²) 2y dy dx** (la y va de 0 a x²)

**Paso 1 — adentro** (∫₀^(x²) 2y dy):
- primitiva: y²
- en y=x²: (x²)² = x⁴ ; en y=0: 0
- resultado: **x⁴**

**Paso 2 — afuera** (∫₀¹ x⁴ dx):
- primitiva: x⁵/5
- en x=1: 1/5 ; en x=0: 0
- **resultado: 1/5**

---

## 🏋️ EJERCICIOS PARA TI (resuelve en papel, sin mirar respuestas)

### Bloque 1 — Integrales dobles tipo I (lo de hoy)

**E1.** ∫₀¹ ∫₀^(x) (x + y) dy dx   *(este es el que quedó pendiente anoche)*

**E2.** ∫₀² ∫₀^(x) x dy dx

**E3.** ∫₀¹ ∫ₓ^(1) (x + y) dy dx   *(ojo: aquí y va DESDE x HASTA 1)*

**E4.** ∫₀¹ ∫₀^(x²) 6x dy dx

### Bloque 2 — Repaso de rectángulos (para calentar / afianzar)

**E5.** ∫₀¹ ∫₀² (4x + y) dy dx

**E6.** ∫₁² ∫₀¹ (x·y) dy dx

### Bloque 3 — Repaso de optimización (que ya dominas, para no oxidarte)

**E7.** Clasifica el punto crítico de f(x,y) = x² + y² − 4x + 6y.

**E8.** Clasifica los puntos críticos de f(x,y) = x³ − 3x + y². *(da DOS puntos; clasifica cada uno)*

---
---
---

## ✅ RESPUESTAS (no mirar hasta terminar)

**E1 = 1/2.**
Adentro: ∫₀^x (x+y)dy = xy+y²/2; en y=x: x²+x²/2 = 3x²/2. Afuera: ∫₀¹ (3x²/2) dx = x³/2; en 1 = **1/2**.

**E2 = 8/3.**
Adentro: ∫₀^x x dy = x·y; en y=x: x·x = x². Afuera: ∫₀² x² dx = x³/3; en 2 = **8/3**.

**E3 = 1/2.**
Adentro: ∫ₓ¹ (x+y)dy = xy+y²/2; en y=1: x+1/2; en y=x: 3x²/2. Resta: x + 1/2 − 3x²/2.
Afuera: ∫₀¹ (x + 1/2 − 3x²/2) dx = x²/2 + x/2 − x³/2; en 1: 1/2 + 1/2 − 1/2 = **1/2**.

**E4 = 3/2.**
Adentro: ∫₀^(x²) 6x dy = 6x·y; en y=x²: 6x·x² = 6x³. Afuera: ∫₀¹ 6x³ dx = 6·x⁴/4 = 3x⁴/2; en 1 = **3/2**.

**E5 = 6.**
Adentro: ∫₀² (4x+y)dy = 4xy+y²/2; en y=2: 8x+2. Afuera: ∫₀¹ (8x+2)dx = 4x²+2x; en 1 = **6**.

**E6 = 3/4.**
Adentro: ∫₀¹ xy dy = x·y²/2; en y=1: x/2. Afuera: ∫₁² (x/2)dx = x²/4; en 2: 1; en 1: 1/4. Resta: 1 − 1/4 = **3/4**.

**E7:** punto crítico (2, −3). Hessiano [[2,0],[0,2]], det=4>0, f_xx=2>0 → **mínimo local**.

**E8:** fx=3x²−3=0 → x=±1; fy=2y=0 → y=0. Puntos (1,0) y (−1,0). Hess=[[6x,0],[0,2]], det=12x.
- (1,0): det=12>0, f_xx=6>0 → **mínimo local**.
- (−1,0): det=−12<0 → **punto silla**.

**Chequeo rápido de respuestas correctas:** E1=1/2, E2=8/3, E3=1/2, E4=3/2, E5=6, E6=3/4.

## 📌 Para contarme en la noche
- ¿Cuáles te salieron solos?
- ¿En cuál te trabaste y por qué?
- ¿El tipo I (límites con función) te quedó claro o necesitamos más?
