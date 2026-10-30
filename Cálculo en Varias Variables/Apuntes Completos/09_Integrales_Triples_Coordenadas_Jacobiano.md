# 09 · Integrales triples, coordenadas cilíndricas/esféricas y cambio de variable

> **Estado:** temas que **aún NO dio el profe** (al 28 Oct iba en integrales dobles tipo I/II), pero **SÍ salen en los parciales modelo** (jul 2021 P1-P2, ene 2025 P1-P3). Los preparamos por seguridad: el profe los puede meter en las ~2 clases restantes antes del parcial.
> **Idea en una línea:** triple = tres integrales anidadas (volumen de sólidos 3D). Las coordenadas cilíndricas/esféricas simplifican cuando hay cilindros/esferas. El Jacobiano es el "factor de corrección de área" al cambiar de variables.

---

## 1. Integrales triples: concepto y orden

Análogo exacto a las dobles, pero en 3D: `∭_E f(x,y,z) dV` sobre un sólido E ⊂ ℝ³. Se resuelve como **tres integrales anidadas**, de adentro hacia afuera.

**Orden típico dz dy dx** (proyectando al plano xy):
```
∭_E f dV = ∫_a^b ∫_{g₁(x)}^{g₂(x)} ∫_{u₁(x,y)}^{u₂(x,y)} f(x,y,z) dz dy dx
```
- **z** (adentro): límites = funciones de x,y (techo y piso del sólido).
- **y** (medio): límites = funciones de x (borde de la sombra en el plano xy).
- **x** (afuera): límites = constantes.

> **Regla de oro (igual que dobles):** el límite más exterior es **constante**; cada nivel hacia afuera pierde una variable en sus límites.

### Cómo plantear (receta)
1. Identifica el sólido E (qué lo acota por arriba/abajo → da los límites de z).
2. Proyecta E al plano xy → esa sombra es una región 2D tipo I/II (da límites de y, x).
3. Escribe la triple anidada.

El profe pide muchas veces **"plantear SIN calcular"** (dar los límites correctos). Lo clave es la geometría, no la aritmética.

---

## 2. Bosquejar el sólido y cambiar el orden (modelo jul2021 P1 / ene2025 P1)

**Ejemplo modelo:** dada `∫_0^1 ∫_0^{2x²} ∫_0^y f(x,y,z) dz dy dx`:
- (i) **Bosquejar** el sólido: x∈[0,1], y de 0 a 2x² (una región parabólica en el plano xy), z de 0 a y (techo inclinado z=y).
- (ii) **Reescribir** en otro orden (ej. dy dz dx): redibujar y re-derivar límites, igual que en dobles pero con una variable más.

**Receta para cambiar orden en triples:**
1. Entiende la región 3D de los límites dados.
2. Elige el nuevo orden (ej. primero y, luego z, luego x).
3. Para cada variable, pregunta: "fijadas las de afuera, ¿entre qué valores se mueve esta?" → casi siempre exige **proyectar** a un plano y mirar las desigualdades.

> Esto es puro "plantear sin resolver": vale por dar los límites correctos.

---

## 3. Coordenadas CILÍNDRICAS (modelo: esfera ∩ plano)

Cambio: `x=r cosθ, y=r senθ, z=z`. Es "polar en el plano xy + z normal".
**Factor (Jacobiano):** `dV = r dz dr dθ`  ← **NO olvidar la r**.

**Cuándo usar:** cuando hay **cilindros, paraboloides, o simetría alrededor del eje z**.

Límites típicos:
- θ: 0 a 2π (vuelta completa) o el sector que toque.
- r: de 0 (o curva interior) al radio exterior.
- z: del piso al techo (puede depender de r).

### Ejemplo modelo (sólido entre esfera radio a y plano z=k)
Esfera x²+y²+z²=a² → en cilíndricas r²+z²=a². Para el sólido entre z=k y la esfera:
```
V = ∫_0^{2π} ∫_{r₁}^{r₂} ∫_{k}^{√(a²−r²)} r dz dr dθ
```
(los límites de r salen de dónde el plano corta la esfera: k²+r²=a² → r=√(a²−k²)).
**El profe pide solo plantear** → basta dejar la integral con esos límites, sin resolver.

---

## 4. Coordenadas ESFÉRICAS (modelo: esfera ∩ plano)

Cambio: `x=ρ senφ cosθ, y=ρ senφ senθ, z=ρ cosφ`.
- ρ = distancia al origen (ρ≥0).
- φ = ángulo desde el eje z positivo (0 ≤ φ ≤ π).
- θ = ángulo en el plano xy (0 ≤ θ ≤ 2π).

**Factor (Jacobiano):** `dV = ρ² senφ dρ dφ dθ`  ← **NO olvidar ρ²senφ**.

**Cuándo usar:** **esferas, conos, simetría alrededor del origen**.

Datos útiles:
- Esfera de radio a centrada en origen: ρ = a.
- Plano z=k: en esféricas ρ cosφ = k → ρ = k/cosφ.
- Semieje z positivo: φ=0; plano xy: φ=π/2.

### Ejemplo modelo (esfera radio 2, "tapada" por z=1)
Sólido V = parte de la esfera ρ≤2 con z≥1.
El plano z=1 en esféricas: ρ cosφ = 1 → ρ = 1/cosφ = secφ. Para cada φ, ρ va de secφ (plano) a 2 (esfera). El ángulo φ va de 0 al valor donde la esfera corta el plano: z=1 en ρ=2 → cosφ=1/2 → φ=π/3.
```
V = ∫_0^{2π} ∫_0^{π/3} ∫_{secφ}^{2} ρ² senφ dρ dφ dθ
```
**Solo plantear.** ✅

> **Nota del estilo del profe:** en estos puntos SIEMPRE dice "NO es necesario calcular, basta plantear". El puntaje está en los **límites correctos** y el factor (r ó ρ²senφ).

---

## 5. CAMBIO DE VARIABLE / Jacobiano (modelo: integral sobre elipse)

Cuando la región es "fea" (una elipse), un cambio de variable la vuelve un círculo/cuadrado fácil. El precio: multiplicar por el **Jacobiano** (corrige cómo se estira el área).

**Fórmula general (2 variables):** si x=x(u,v), y=y(u,v):
```
∬_R f(x,y) dx dy = ∬_S f(x(u,v), y(u,v)) · |J| du dv
```
donde el **Jacobiano** es el determinante:
```
       ⎡ ∂x/∂u   ∂x/∂v ⎤
J = det ⎢                ⎥ = (∂x/∂u)(∂y/∂v) − (∂x/∂v)(∂y/∂u)
       ⎣ ∂y/∂u   ∂y/∂v ⎦
```
Se usa **|J|** (valor absoluto).

### Ejemplo modelo (elipse — jul2021 P3 / ene2025 P3)
**∬_R x dx dy, R acotada por la elipse 3x²+2y²=1. Ayuda del profe: x=u/√3, y=v/√2.**

1. **Transformar la región:** 3x²+2y² = 3(u/√3)² + 2(v/√2)² = u² + v² = 1 → ¡la elipse se vuelve el **círculo unitario** u²+v²≤1! (Ese es el propósito del cambio.)
2. **Jacobiano:** ∂x/∂u=1/√3, ∂x/∂v=0, ∂y/∂u=0, ∂y/∂v=1/√2.
   J = (1/√3)(1/√2) − 0 = 1/√6. |J| = 1/√6.
3. **Reescribir:**
   ```
   ∬_R x dx dy = ∬_{u²+v²≤1} (u/√3) · (1/√6) du dv = (1/√18) ∬_{círculo} u du dv
   ```
4. Por **simetría**, ∬ u sobre el círculo centrado en origen = 0 (u es impar en u). → **integral = 0**. ✅

> Mismo método para 4x²+3y²=1 con x=u/2, y=v/√3 (jul 2021): se vuelve círculo unitario, Jacobiano = (1/2)(1/√3)=1/(2√3), y por simetría da 0.

---

## 6. Tabla resumen de factores (NO olvidar)

| Coordenadas | Cambio | Factor dV / dA |
|-------------|--------|----------------|
| Polares (2D) | x=r cosθ, y=r senθ | **r** dr dθ |
| Cilíndricas | x=r cosθ, y=r senθ, z=z | **r** dz dr dθ |
| Esféricas | x=ρsenφcosθ, y=ρsenφsenθ, z=ρcosφ | **ρ² senφ** dρ dφ dθ |
| Cambio general | x(u,v), y(u,v) | **\|J\|** du dv |

---

## 7. Errores típicos (trampas)
- **Olvidar el factor** (r, ρ²senφ, |J|). Es el error #1 y el profe lo castiga.
- **Confundir φ y θ** en esféricas (φ desde el eje z, θ en el plano).
- **Límite exterior con variable** (debe ser constante).
- **Jacobiano sin valor absoluto** o mal calculado (es un determinante 2×2).
- **No transformar la región** al nuevo dominio (la elipse DEBE volverse círculo).
- Intentar **calcular** cuando el profe dice "solo plantear" → pierdes tiempo.

---

## 8. Checklist mental
- [ ] ¿Identifiqué la geometría (cilindro/esfera/elipse) para elegir coordenadas?
- [ ] ¿Puse el factor correcto (r / ρ²senφ / |J|)?
- [ ] ¿Los límites exteriores son constantes?
- [ ] Cambio de variable: ¿transformé la región Y calculé bien el Jacobiano?
- [ ] ¿Aproveché simetrías (integrando impar sobre región simétrica = 0)?
- [ ] Si dice "plantear", ¿dejé la integral montada sin calcular?
