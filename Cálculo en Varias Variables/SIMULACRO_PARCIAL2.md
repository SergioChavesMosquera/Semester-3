# 🧪 SIMULACRO — Parcial 2 Cálculo en Varias Variables

> Ejercicios NUEVOS (variantes de los 3 modelos). **Resuelve con los enunciados tapando las soluciones** (abajo). Tiempo sugerido: 90 min. Recuerda: JUSTIFICAR TODO, y donde diga "plantear" NO calcular.

---

## ENUNCIADOS

**1. (10 pts)** Calcule la integral doble de f(x,y) = 2x + y sobre el rectángulo de vértices (1,0), (1,3), (4,0), (4,3).

**2. (10 pts)** Calcule ∬_D xy dA, donde D es la región acotada por y = x² y y = 2x.

**3. (10 pts)** Encuentre a₁,...,a₆ tales que
∫_{a₁}^{a₂} ∫_{a₃}^{a₄} ∫_{a₅}^{a₆} z dz dy dx
corresponda a la integral de f(x,y,z)=z sobre el sólido acotado por el paraboloide z=x²+y² y el plano z=4. **NO calcule**, solo dé los límites si integra primero z, luego y, luego x.

**4. (10 pts)** Una caja rectangular sin tapa debe tener volumen 32. Halle las dimensiones que minimizan el área de material (superficie). Resuélvalo con **Lagrange** y verifique por **sustitución**.

**5. (10 pts)** Encuentre y clasifique (máx/mín local o silla) los puntos críticos de f(x,y) = x³ + y³ − 3xy.

**6. (10 pts)** Encuentre los valores máximo y mínimo absolutos de f(x,y) = x² + y² − x − y en el triángulo de vértices (0,0), (1,0), (0,1).

**7. (10 pts, bono tipo jul2021)** Plantee (sin calcular) la integral que da el volumen del sólido encerrado por la esfera de radio 3 centrada en el origen y el plano z=1, en coordenadas **esféricas** y en **cilíndricas**.

---
---
---

## SOLUCIONES (no mirar antes)

### 1.
Rectángulo R=[1,4]×[0,3]. ∫_1^4 ∫_0^3 (2x+y) dy dx.
Adentro: ∫_0^3 (2x+y) dy = [2xy + y²/2]_0^3 = 6x + 9/2.
Afuera: ∫_1^4 (6x + 9/2) dx = [3x² + (9/2)x]_1^4 = (48+18) − (3+4.5) = 66 − 7.5 = **58.5** (= 117/2).

### 2.
Cortes y=x² y y=2x: x²=2x → x=0, x=2. Para x∈[0,2], la recta y=2x va por encima de la parábola y=x² (prueba x=1: 2 vs 1). **Tipo I**:
∫_0^2 ∫_{x²}^{2x} xy dy dx.
Adentro: x·[y²/2]_{x²}^{2x} = x·( (4x²)/2 − (x⁴)/2 ) = x·(2x² − x⁴/2) = 2x³ − x⁵/2.
Afuera: ∫_0^2 (2x³ − x⁵/2) dx = [x⁴/2 − x⁶/12]_0^2 = (16/2) − (64/12) = 8 − 16/3 = **8/3**.

### 3.
Paraboloide z=x²+y² (abajo) y plano z=4 (arriba). La sombra en xy: donde se cortan, 4=x²+y² → círculo radio 2.
- z: de x²+y² a 4.
- Sombra círculo x²+y²≤4. En orden dy dx (tipo I): x∈[−2,2], y de −√(4−x²) a √(4−x²).
**Límites:** a₁=−2, a₂=2, a₃=−√(4−x²), a₄=√(4−x²), a₅=x²+y², a₆=4.
(Solo plantear, como pide el estilo del profe.)

### 4.
Caja sin tapa, base x·y, altura z. Volumen xyz=32. Superficie (sin tapa): S = xy + 2xz + 2yz.
**Lagrange:** minimizar S sujeto a g=xyz=32. ∇S=(y+2z, x+2z, 2x+2y), ∇g=(yz, xz, xy).
Sistema: y+2z=λyz; x+2z=λxz; 2x+2y=λxy.
De las dos primeras (restando o por simetría) sale x=y. De ahí y con la tercera: 4x = λx² → λ=4/x; y de la primera x+2z=λxz=4z → x=2z → z=x/2.
Restricción: x·x·(x/2)=32 → x³/2=32 → x³=64 → x=4. Entonces y=4, z=2.
**Dimensiones: base 4×4, altura 2.** S=16+16+16=48.
**Verificación sustitución:** z=32/(xy), S=xy+2x·32/(xy)+2y·32/(xy)=xy+64/y+64/x. ∂S/∂x=y−64/x²=0, ∂S/∂y=x−64/y²=0 → x²y=64, xy²=64 → x=y, x³=64 → x=4. ✅ mismo resultado.

### 5.
∇f=(3x²−3y, 3y²−3x)=(0,0) → x²=y, y²=x. Sustituyendo: x⁴=x → x(x³−1)=0 → x=0 o x=1.
- x=0→y=0: punto (0,0). x=1→y=1: punto (1,1).
Hessiano: f_xx=6x, f_yy=6y, f_xy=−3. det=36xy−9.
- En (0,0): det=0−9=**−9<0 → SILLA**.
- En (1,1): det=36−9=27>0, f_xx=6>0 → **MÍN local**.

### 6.
**Interior:** ∇f=(2x−1, 2y−1)=0 → x=1/2, y=1/2. ¿Está dentro del triángulo (x+y<1)? 1/2+1/2=1, está sobre la hipotenusa (frontera), no en el interior estricto. f(1/2,1/2)=1/4+1/4−1/2−1/2 = −1/2.
**Frontera:**
- y=0, x∈[0,1]: f=x²−x, mín en x=1/2 (f=−1/4), extremos f(0)=0, f(1)=0.
- x=0, y∈[0,1]: f=y²−y, mín en y=1/2 (f=−1/4), extremos 0 y 0.
- x+y=1 (y=1−x), x∈[0,1]: f=x²+(1−x)²−x−(1−x)=2x²−2x+1−1=2x²−2x. Mín en x=1/2 → f=2(1/4)−1=−1/2. Extremos f(0,1)=0, f(1,0)=0.
**Comparar:** candidatos dan {0, −1/4, −1/2}.
**Máx absoluto = 0** (en los vértices); **mín absoluto = −1/2** (en (1/2,1/2)).
Justificar: f continua, triángulo cerrado y acotado → Weierstrass.

### 7.
Esfera radio 3: ρ=3 (esféricas) o r²+z²=9 (cilíndricas). Sólido z≥1 dentro de la esfera.
**Esféricas:** plano z=1 → ρ=1/cosφ=secφ. Corte esfera∩plano: z=1 en ρ=3 → cosφ=1/3 → φ=arccos(1/3). φ de 0 a arccos(1/3); ρ de secφ a 3.
V = ∫_0^{2π} ∫_0^{arccos(1/3)} ∫_{secφ}^{3} ρ² senφ dρ dφ dθ.
**Cilíndricas:** z de 1 a √(9−r²); el plano corta la esfera en z=1 → r²=8 → r de 0 a 2√2; θ de 0 a 2π.
V = ∫_0^{2π} ∫_0^{2√2} ∫_1^{√(9−r²)} r dz dr dθ.
(Solo plantear.)

---

### 📊 Autoevaluación
- 6-7 bien → listo para el parcial.
- 4-5 bien → repasa los temas fallados con el apunte.
- <4 → vuelve a los ejemplos resueltos de los apuntes 06-09 antes de reintentar.
