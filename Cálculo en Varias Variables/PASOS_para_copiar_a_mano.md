# ✍️ Pasos por tema — PARA COPIAR A MANO (noche antes del parcial)

> Copia esto en papel con tu letra. El objetivo es grabar el ORDEN de los pasos. No tienes que entender nada nuevo, solo escribir. Mañana haces ejercicios con esto al lado.

---

## 1. OPTIMIZACIÓN LIBRE (Hessiano)
1. Gradiente a cero: fx=0 y fy=0 → resolver sistema → puntos críticos.
2. Hessiano: f_xx, f_yy, f_xy.
3. det = f_xx·f_yy − (f_xy)². (Si tiene x,y, evaluar en cada punto.)
4. Clasificar (det PRIMERO):
   - det<0 → SILLA
   - det>0 y f_xx>0 → MÍNIMO local
   - det>0 y f_xx<0 → MÁXIMO local
5. Respuesta = PUNTO + TIPO.

## 2. OPTIMIZACIÓN REGIÓN CERRADA (máx/mín absolutos)
1. INTERIOR: gradiente a cero → punto; ¿cae dentro? → evaluar f.
2. FRONTERA: sustituir el borde en f → queda 1 variable → optimizar (crítico + extremos del intervalo).
3. COMPARAR todos los f: mayor = máx abs, menor = mín abs.
4. Justificar: f continua en cerrado y acotado → Weierstrass.

## 3. LAGRANGE (restricción g=c)
1. ∇f = λ∇g → fx=λ·gx , fy=λ·gy.
2. + la restricción g=c (¡3ª ecuación!).
3. Resolver sistema → candidatos.
4. Evaluar f en cada candidato → mayor=máx, menor=mín.

## 4. INTEGRALES DOBLES
- De ADENTRO hacia AFUERA, otra variable constante.
- Tipo I: ∫(x:núm)∫(y:func) f dy dx.
- Tipo II: ∫(y:núm)∫(x:func) f dx dy.
- Límite de AFUERA siempre NÚMERO.
- Armar región: cortes de curvas = límites afuera; cuál va arriba/abajo = límites adentro.
- Cambiar orden: DIBUJAR región, rayas al revés (entra/sale).

## 5. CAMBIO DE VARIABLE / POLARES
- ∬ f dx dy = ∬ f(r cosθ, r senθ)·r dr dθ.   FACTOR = r
- Polares: x=r cosθ, y=r senθ. (x²+y²=r²)
- Disco completo: r de 0 a radio, θ de 0 a 2π.
- Jacobiano general: J = x_u·y_v − x_v·y_u → usar |J|.

## 6. TRIPLES + COORDENADAS 3D
- Triple = integrar 3 veces, adentro hacia afuera.
- CILÍNDRICAS: x=r cosθ, y=r senθ, z=z. FACTOR = r dz dr dθ.
- ESFÉRICAS: x=ρsenφcosθ, y=ρsenφsenθ, z=ρcosφ. FACTOR = ρ²senφ dρ dφ dθ.
- φ: 0 a π (desde eje z). θ: 0 a 2π. Esfera: ρ=radio.
- Dato: ∫₀^π senφ dφ = 2.

## 7. CENTRO DE MASA
1. m = ∬ ρ dA
2. My = ∬ x·ρ dA ; Mx = ∬ y·ρ dA
3. x̄ = My/m ; ȳ = Mx/m
4. Simetría → centro cae en el eje de simetría (justificar).

---

## 🚨 TRAMPAS (anótalas también, valen puntos)
- det<0 = SILLA (no máximo).
- cruzada al cuadrado: det = f_xx·f_yy − (f_xy)².
- Lagrange: incluir la restricción (3ª ecuación).
- región cerrada: NO olvidar frontera ni vértices.
- integrales: límite exterior NÚMERO; DIBUJAR siempre.
- coordenadas: FACTOR r / ρ²senφ SIEMPRE.
- cuidado con signos: −(−2)² = −4.
- JUSTIFICAR todo (el profe lo exige).
- si dice "plantear", NO calcular.

---

## 📋 MAÑANA: orden del machaque (mente fresca)
1. Parcial modelo P2 (29 ene 2025) — el más completo.
2. Taller del profe (TallerParcial2CalcVectorial) — ejercicios calcados.
3. Lo que sientas flojo, repetir.
4. Justo antes de entrar: releer estos pasos.
