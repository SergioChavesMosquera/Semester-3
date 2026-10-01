# FORMULARIO COMPLETO — Fundamentos de Electricidad y Magnetismo

**Basado en:** Magistrales 1–5 y Talleres 1–5 · Prof. Felipe Valencia Hernández.

> Convención: SI, vectores en negrita o con flecha. `r` es distancia; `r⃗` es vector; `r̂ = r⃗/r`. En fórmulas electrostáticas, `k = 1/(4π ε₀)`.

---

# 0. Constantes, unidades y herramientas matemáticas

- Carga elemental: `e = 1,602×10⁻¹⁹ C`.
- Carga del electrón: `qₑ = −e`; protón: `+e`.
- Permitividad del vacío: `ε₀ = 8,854×10⁻¹² C²/(N·m²)`.
- `k = 1/(4π ε₀) ≈ 8,988×10⁹ N·m²/C²`.
- Permeabilidad del vacío: `μ₀ = 4π×10⁻⁷ T·m/A`.
- `1 N = 1 kg·m/s²`; `1 J = 1 N·m`; `1 V = 1 J/C`.
- `1 T = 1 N/(A·m)`; `1 C = 1 A·s`.

## Vectores

- Norma: `|a⃗| = √(aₓ²+aᵧ²+a_z²)`.
- Unitario: `â = a⃗/|a⃗|`.
- Producto punto: `a⃗·b⃗ = aₓbₓ+aᵧbᵧ+a_zb_z = |a||b|cosθ`.
- Producto cruz: `a⃗×b⃗` es perpendicular a ambos; `|a×b|=|a||b|senθ`.
- Triple escalar: `a·(b×c)`.
- Identidad: `a×(b×c)=b(a·c)−c(a·b)`.
- Elemento de línea: `dℓ⃗ = dx î + dy ĵ + dz k̂`.
- Elemento de área orientado: `dA⃗ = n̂ dA`.
- Producto cruz con coordenadas: `(a₂b₃−a₃b₂, a₃b₁−a₁b₃, a₁b₂−a₂b₁)`.

## Operadores vectoriales

- Gradiente: `∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)`.
- Divergencia: `∇·A⃗ = ∂Aₓ/∂x + ∂Aᵧ/∂y + ∂A_z/∂z`.
- Rotacional: `∇×A⃗`.
- Laplaciano escalar: `∇²V = ∂²V/∂x²+∂²V/∂y²+∂²V/∂z²`.
- Identidades: `∇×(∇V)=0`; `∇·(∇×A⃗)=0`.

---

# 1. Taller 1 — Ley de Coulomb y vectores

## Carga

- Dos tipos: positiva y negativa.
- Cargas iguales se repelen; opuestas se atraen.
- Conservación: la carga total de un sistema aislado permanece constante.
- Cuantización: `q = n e`, con `n` entero.
- Superposición: la fuerza total es la suma vectorial de todas las fuerzas.

## Ley de Coulomb

- Magnitud:
  `F = k |q₁q₂|/r²`.
- Forma vectorial, fuerza sobre 1 debida a 2:
  `F⃗₁₂ = k q₁q₂ (r⃗₁−r⃗₂)/|r⃗₁−r⃗₂|³`.
- Alternativa:
  `F⃗₁₂ = k q₁q₂ r̂₂→₁/r²`.
- Fuerza total:
  `F⃗₁ = Σᵢ F⃗₁ᵢ`.

## Distribuciones discretas

- Posición relativa: `r⃗ = r⃗_obs − r⃗_carga`.
- Campo de cargas puntuales:
  `E⃗(r⃗) = k Σᵢ qᵢ (r⃗−r⃗ᵢ)/|r⃗−r⃗ᵢ|³`.
- Fuerza sobre una carga de prueba: `F⃗ = q₀ E⃗`.

## Procedimiento típico

1. Dibuja cada carga y el punto de observación.
2. Escribe cada vector desde la carga hacia el punto.
3. Normaliza cada dirección.
4. Calcula cada contribución y suma componentes.
5. Revisa que la dirección sea coherente con atracción/repulsión.

---

# 2. Taller 2 — Campos eléctrico y magnético

## Campo eléctrico

- Definición: `E⃗ = lim_{q₀→0} F⃗/q₀`.
- Carga puntual: `E⃗ = k q r̂/r²`.
- Distribución continua:
  `dE⃗ = k dq r̂/R² = k dq (r⃗−r⃗')/|r⃗−r⃗'|³`.
- Campo total:
  `E⃗(r⃗)=k∫ (r⃗−r⃗')/|r⃗−r⃗'|³ dq`.

## Densidades de carga

- Lineal: `λ = dq/dℓ`; `dq=λ dℓ`.
- Superficial: `σ = dq/dA`; `dq=σ dA`.
- Volumétrica: `ρ = dq/dτ`; `dq=ρ dτ`.
- Carga total: `Q=∫λ dℓ = ∫σ dA = ∫ρ dτ`.

## Campo magnético

- Fuerza magnética sobre carga móvil:
  `F⃗_B = q v⃗×B⃗`.
- Magnitud:
  `F_B = |q|vB senθ`.
- Fuerza de Lorentz completa:
  `F⃗ = q(E⃗ + v⃗×B⃗)`.
- Si `v⃗ ∥ B⃗`, fuerza magnética nula.
- Si `v⃗ ⟂ B⃗`, fuerza magnética máxima.
- La fuerza magnética no realiza trabajo:
  `P_B = F⃗_B·v⃗ = q(v⃗×B⃗)·v⃗ = 0`.

## Movimiento en campo magnético uniforme

- Radio de trayectoria circular, si `v⊥B`:
  `R = mv/(|q|B)`.
- Frecuencia angular:
  `ω = |q|B/m`.
- Período:
  `T = 2πm/(|q|B)`.
- Si hay componente paralela, la trayectoria es helicoidal.

## Corriente y densidad de corriente

- Corriente: `I = dq/dt`.
- Densidad de corriente: `J⃗ = ρ v⃗`.
- Corriente a través de superficie:
  `I = ∫_S J⃗·dA⃗`.

## Ley de Biot–Savart

- Elemento de corriente:
  `dB⃗ = (μ₀/4π) I dℓ⃗×R̂/R²`.
- Forma integral:
  `B⃗ = (μ₀ I/4π) ∫ dℓ⃗×R̂/R²`.

## Resultados frecuentes

- Hilo recto infinito:
  `B = μ₀ I/(2πr)`.
- Solenoide largo:
  `B ≈ μ₀ n I`, donde `n=N/L`.
- Fuerza por unidad de longitud entre hilos paralelos:
  `F/L = μ₀ I₁I₂/(2πd)`.
- Dirección de `B`: regla de la mano derecha.

## Flujo

- Flujo de campo vectorial:
  `Φ_F = ∫_S F⃗·dA⃗`.
- Para campo uniforme y superficie plana:
  `Φ = FA cosθ`.
- Superficie cerrada: orientación hacia afuera.
- La corriente como flujo:
  `I = ∫_S J⃗·dA⃗`.

---

# 3. Taller 3 — Trabajo, energía y potencial eléctrico

## Trabajo

- Trabajo diferencial: `dW = F⃗·dℓ⃗`.
- Trabajo total:
  `W_{A→B}=∫_A^B F⃗·dℓ⃗`.
- Para fuerza eléctrica:
  `Wₑ = q∫_A^B E⃗·dℓ⃗`.
- Trabajo neto: `W_net = ΔK`.
- Fuerza conservativa:
  `∮ F⃗·dℓ⃗ = 0`.

## Energía potencial eléctrica

- `ΔU = U_B−U_A = −Wₑ`.
- Dos cargas puntuales:
  `U = k q₁q₂/r`.
- Sistema de cargas:
  `U = Σ_{i<j} k qᵢqⱼ/rᵢⱼ`.
- Relación con potencial:
  `U=qV` para una carga en un potencial externo.

## Potencial eléctrico

- Definición:
  `V(B)−V(A)=−∫_A^B E⃗·dℓ⃗`.
- Carga puntual tomando `V(∞)=0`:
  `V(r)=kq/r`.
- Varias cargas:
  `V(r)=kΣᵢqᵢ/rᵢ`.
- Distribución continua:
  `V(r)=k∫dq/R`.
- Campo a partir del potencial:
  `E⃗=−∇V`.
- En coordenadas cartesianas:
  `Eₓ=−∂V/∂x`, `Eᵧ=−∂V/∂y`, `E_z=−∂V/∂z`.
- Equipotenciales: `V=constante`; el campo es perpendicular a ellas.

## Relaciones útiles

- `ΔV = −∫E⃗·dℓ⃗`.
- Trabajo del campo:
  `Wₑ=q(V_A−V_B)`.
- Trabajo externo cuasiestático:
  `W_ext=q(V_B−V_A)=ΔU`.
- Energía total electrostática:
  `E_total=K+U` constante si solo actúan fuerzas eléctricas.

## Dipolo eléctrico

- Momento dipolar: `p⃗=q d⃗`, dirigido de carga negativa a positiva.
- Torque en campo uniforme:
  `τ⃗=p⃗×E⃗`; `τ=pE senθ`.
- Energía:
  `U=−p⃗·E⃗=−pE cosθ`.
- Potencial lejano:
  `V≈k p⃗·r̂/r²`.
- Campo lejano:
  `E⃗ = [k/r³][3(p⃗·r̂)r̂−p⃗]`.

---

# 4. Taller 4 — Distribuciones, Gauss, Poisson y Laplace

## Ley de Gauss

- Forma integral:
  `∮_S E⃗·dA⃗ = Q_enc/ε₀`.
- Forma diferencial:
  `∇·E⃗ = ρ/ε₀`.
- La ley es siempre válida; solo es fácil de usar cuando hay simetría.

## Método de una superficie gaussiana

1. Identifica la simetría: esférica, cilíndrica o planar.
2. Elige una superficie donde `|E|` sea constante.
3. Decide dónde `E⃗·dA⃗` es cero por perpendicularidad.
4. Calcula el área de la superficie.
5. Determina `Q_enc`.
6. Aplica `E·A=Q_enc/ε₀`.

## Resultados con simetría

### Carga puntual o esfera con simetría esférica

- Superficie gaussiana: esfera de radio r.
- Área: `A=4πr²`.
- Carga puntual:
  `E(r)=kQ/r²` hacia afuera si Q>0.
- Esfera maciza con densidad uniforme ρ y radio R:
  - Interior `r<R`: `Q_enc=ρ(4πr³/3)` y `E=ρr/(3ε₀)`.
  - Exterior `r>R`: `E=kQ/r²`.

### Hilo infinito

- Superficie: cilindro coaxial de radio r y longitud L.
- Área lateral: `A=2πrL`.
- `Q_enc=λL`.
- `E=λ/(2π ε₀ r)` radial.

### Plano infinito

- Superficie: pastilla cilíndrica que atraviesa el plano.
- Flujo por dos tapas: `2EA`.
- `Q_enc=σA`.
- `E=σ/(2ε₀)` a cada lado de una lámina aislada.
- Para dos placas infinitas opuestas: `E=σ/ε₀` entre ellas y aproximadamente cero afuera.

## Potencial de distribuciones

- `E⃗=−∇V`.
- Esfera conductora cargada: exterior `V=kQ/r`; interior `V=kQ/R` constante.
- Hilo infinito: el potencial absoluto requiere referencia; diferencias:
  `V(r₂)−V(r₁)=−∫_{r₁}^{r₂} E(r)dr`.
- Plano infinito: diferencias de potencial se obtienen de `ΔV=−∫E·dℓ`.

## Poisson y Laplace

- Como `E⃗=−∇V` y `∇·E⃗=ρ/ε₀`:
  `∇²V = −ρ/ε₀`  (Poisson).
- En región sin carga:
  `∇²V=0`  (Laplace).
- En una dimensión:
  `d²V/dx²=−ρ(x)/ε₀`.
- Sin carga en una dimensión:
  `d²V/dx²=0` → `V(x)=Ax+B`.
- Campo unidimensional:
  `E_x=−dV/dx`.

## Condiciones de frontera frecuentes

- El potencial es continuo en una interfaz electrostática.
- Componente tangencial de E es continua en electrostática:
  `E₁,t=E₂,t`.
- Salto de componente normal por una densidad superficial:
  `n̂·(E₂−E₁)=σ/ε₀`.

---

# 5. Taller 5 — Conductores, capacitores y capacitancia

## Conductores en equilibrio electrostático

- Campo dentro del material conductor: `E⃗=0`.
- Potencial del conductor: constante; es equipotencial.
- Campo tangencial en la superficie: `E_t=0`.
- Campo justo afuera:
  `E_n=σ/ε₀` en vacío.
- El campo justo afuera es normal a la superficie.
- El exceso de carga se ubica en la superficie.
- Una cavidad sin carga interna tiene `E=0` en la cavidad; una carga dentro de una cavidad induce carga total `−q` en la superficie interna.
- La superficie exterior porta la carga restante según la geometría.

## Capacitancia

- Definición:
  `C=Q/|ΔV|`.
- Unidad: faradio, `1 F=1 C/V`.
- Capacitor de placas paralelas:
  `C=ε₀A/d`.
- Con dieléctrico lineal de constante κ:
  `C=κε₀A/d`; `ε=κε₀`.
- Esfera aislada:
  `C=4π ε₀R`.
- Capacitor esférico, radios a y b:
  `C=4π ε₀ ab/(b−a)`.
- Capacitor cilíndrico coaxial, radios a y b, longitud L:
  `C=2π ε₀L/ln(b/a)`.

## Combinaciones

- Paralelo:
  `C_eq=C₁+C₂+...`; mismo ΔV.
- Serie:
  `1/C_eq=1/C₁+1/C₂+...`; misma carga en cada capacitor.
- Para dos en serie:
  `C_eq=C₁C₂/(C₁+C₂)`.

## Energía del capacitor

- `U=½QΔV`.
- `U=Q²/(2C)`.
- `U=½C(ΔV)²`.
- Densidad de energía:
  `u=½εE²`.
- Placas ideales: `E≈ΔV/d`.

## Dieléctricos

- `D⃗=ε₀E⃗+P⃗`.
- En medio lineal: `D⃗=εE⃗=κε₀E⃗`.
- Carga libre: `∮D⃗·dA⃗=Q_libre,enc`.
- Polarización: `P⃗=ε₀χₑE⃗`; `κ=1+χₑ`.
- Si el capacitor permanece conectado a batería: `ΔV` constante.
- Si queda aislado: `Q` constante.

---

# 6. Integrales y coordenadas que pueden aparecer

- Cartesianas: `dτ=dx dy dz`.
- Cilíndricas: `x=s cosφ`, `y=s senφ`, `dτ=s ds dφ dz`.
- Esféricas: `x=r senθ cosφ`, `y=r senθ senφ`, `z=r cosθ`, `dτ=r² senθ dr dθ dφ`.
- Área de esfera: `4πR²`; volumen: `4πR³/3`.
- Área lateral de cilindro: `2πRL`; volumen: `πR²L`.
- Integrales de potencia:
  `∫ rⁿ dr = rⁿ⁺¹/(n+1)` si n≠−1; `∫dr/r=ln r`.

---

# 7. Errores típicos que cuestan puntos

- Usar magnitudes cuando el problema pide vector.
- No elevar r al cubo en la forma vectorial de Coulomb.
- Sumar potenciales como vectores: V es escalar.
- Aplicar Gauss sin justificar simetría.
- Usar `Q_total` en vez de `Q_enc`.
- Olvidar la carga encerrada es cero dentro de un conductor en equilibrio.
- Confundir `W_campo=q(V_A−V_B)` con `W_externo=q(V_B−V_A)`.
- Decir que la fuerza magnética hace trabajo: no lo hace.
- Olvidar el factor geométrico `4πr²`, `2πrL` o `2A`.
- Mezclar `σ`, `λ` y `ρ`.
- Entregar solo el resultado: escribir dibujo, ley, sustitución, unidades y conclusión.
