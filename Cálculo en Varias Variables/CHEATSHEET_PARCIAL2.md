# 🎯 CHEATSHEET — Parcial 2 Cálculo (móvil)

> Leer minutos antes del examen. Profe Cano. **Respuesta sin justificación = 0.** Le gusta "plantear sin resolver" y "hacer de dos formas".

---

## A · OPTIMIZACIÓN LIBRE (∇f=0 + Hessiano)
1. **Puntos críticos:** resolver ∇f=(0,0).
2. **Hessiano:** `Hess = [[f_xx, f_xy],[f_xy, f_yy]]`.
3. **Discriminante:** `det = f_xx·f_yy − (f_xy)²`.

| det(Hess) | f_xx | → |
|-----------|------|---|
| **< 0** | — | **SILLA** |
| **> 0** | <0 | **MÁX local** |
| **> 0** | >0 | **MÍN local** |
| **= 0** | — | test NO decide |

⚠️ Cruzada al cuadrado en el det. det<0 SIEMPRE silla.

---

## B · RESTRINGIDA (Lagrange / sustitución)
- **Lagrange:** `∇f = λ∇g` + la restricción g=c (¡3 ecuaciones!).
- **2 restricciones:** `∇f = λ₁∇g₁ + λ₂∇g₂`.
- **Sustitución:** parametrizar la curva → f queda de 1 variable → Cálculo 1.
- El profe pide **ambas formas** para verificar.

## C · MÁX/MÍN ABSOLUTO en región cerrada (1er algoritmo)
1. **Interior:** ∇f=0.
2. **Frontera:** parametrizar la curva/lados → optimizar f sobre ella.
3. **Vértices** (si es polígono).
4. Evaluar f en TODOS → mayor=máx, menor=mín.
- Justificar con Weierstrass (continua en cerrado+acotado → alcanza máx y mín).

---

## D · INTEGRALES DOBLES
**Iteradas de adentro hacia afuera** (la otra variable = constante).

- **Rectángulo [a,b]×[c,d] (Fubini):** orden libre.
- **Tipo I** (dy primero): `∫_a^b ∫_{g₁(x)}^{g₂(x)} f dy dx` — abajo/arriba son y=g(x); rayas verticales.
- **Tipo II** (dx primero): `∫_c^d ∫_{h₁(y)}^{h₂(y)} f dx dy` — izq/der son x=h(y); rayas horizontales.

⚠️ **Límite exterior SIEMPRE constante.** Siempre **DIBUJA la región**.

**Cambiar orden:** redibuja la MISMA región y reinterprétala en el otro orden.
**Volumen:** proyecta el sólido al plano xy para hallar los límites.

---

## E · INTEGRALES TRIPLES
`∫∫∫ f dz dy dx` — z (adentro, techo/piso f(x,y)) → y (sombra) → x (constante).
Plantear = dar límites correctos. Proyectar al plano para los límites.

## F · COORDENADAS (¡no olvidar el factor!)
| | cambio | factor |
|---|--------|--------|
| Polares | x=r cosθ, y=r senθ | **r** dr dθ |
| Cilíndricas | +z=z | **r** dz dr dθ |
| Esféricas | x=ρsenφcosθ, y=ρsenφsenθ, z=ρcosφ | **ρ²senφ** dρ dφ dθ |

- Esféricas: φ desde eje z (0..π), θ en plano (0..2π), ρ≥0.
- Esfera radio a: ρ=a. Plano z=k: ρ=k/cosφ=secφ·k.
- El profe: **"solo plantear, no calcular"**.

## G · CAMBIO DE VARIABLE (Jacobiano)
`∬ f dx dy = ∬ f(x(u,v),y(u,v)) |J| du dv`
`J = det[[x_u, x_v],[y_u, y_v]] = x_u·y_v − x_v·y_u` → usar **|J|**.
- **Elipse → círculo:** con el cambio dado (ej. x=u/√3, y=v/√2), la elipse se vuelve u²+v²=1.
- **Simetría:** ∬ (integrando impar) sobre región simétrica = **0**.

---

## 🚨 TRAMPAS FRECUENTES
- det<0 = silla (no máximo).
- Cruzada al cuadrado: det = f_xx f_yy − (f_xy)².
- Lagrange: incluir la restricción como 3ª ecuación.
- Región cerrada: NO olvidar la frontera ni los vértices.
- Integrales: límite exterior constante; DIBUJAR siempre.
- Coordenadas: factor r / ρ²senφ / |J| SIEMPRE.
- Si dice "plantear", NO calcules.
- **JUSTIFICAR TODO** (citar el teorema).

---

## ✍️ Frases de justificación (estilo profe)
- "∇f(p)=0 y det(Hess(f)(p))>0 con f_xx>0 ⟹ mínimo local (teorema 7 Oct)."
- "f continua en región cerrada y acotada ⟹ por Weierstrass alcanza máx y mín."
- "∇g ⊥ al nivel ⟹ en el óptimo ∇f=λ∇g (Lagrange)."
- "Parciales continuas pues son sumas/productos/composiciones de continuas."
