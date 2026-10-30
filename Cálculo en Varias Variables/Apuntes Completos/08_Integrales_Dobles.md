# 08 · Integrales dobles: rectángulos y regiones tipo I / II

> **Clases fuente:** 21 Oct (integrales sobre rectángulos, definición, Cavalieri, integrales iteradas), 26 Oct (regiones tipo I y II — clase virtual sin PDF), 28 Oct (ejercicios 15.3 Stewart). Secciones **15.1–15.3 Stewart 6ª ed.**
> **Idea en una línea:** una integral doble suma el "volumen bajo la superficie" sobre una región del plano. Se calcula como **dos integrales simples anidadas** (iteradas), de adentro hacia afuera.

---

## 1. Qué es una integral doble (definición del profe, 21 Oct)

Sobre un rectángulo R = [a,b]×[c,d], se define como límite de **sumas de Riemann**:
```
∬_R f(x,y) dA  =  ∬_R f(x,y) dx dy  =  lim_{|P|→0}  Σ_{i,j} f(x*_ij) · A_ij
```
donde se parte R en subrectángulos de área A_ij, se evalúa f en un punto muestra x*_ij de cada uno, se suma, y se toma el límite cuando la partición se hace fina (|P|→0 = el subrectángulo más grande tiende a 0).

> No vas a calcular integrales dobles con este límite en el parcial, pero el profe lo puede preguntar como **definición** (su estilo: exige la definición formal). El ejercicio que hizo (f=x−y, partición {0,1,2,3}×{1,2,3,5}, punto muestra = esquina inferior izquierda) dio −13: es sumar f(punto)·área por cada subrectángulo.

### Motivación: principio de Cavalieri
"Si dos sólidos tienen secciones transversales de la misma área, tienen el mismo volumen." → el **volumen = integral de las áreas de las secciones transversales**. Esto justifica por qué integrar "rebanada por rebanada" (iteradas) da el volumen.

---

## 2. Integrales iteradas sobre RECTÁNGULOS (Teorema de Fubini)

Sobre R = [a,b]×[c,d], se calcula como **dos integrales simples anidadas**:
```
∬_R f dA  =  ∫_a^b ( ∫_c^d f(x,y) dy ) dx   =   ∫_c^d ( ∫_a^b f(x,y) dx ) dy
```
**Fubini:** en un rectángulo con límites constantes, **el orden no importa**, da lo mismo integrar primero en y o primero en x.

**Cómo se hace (de adentro hacia afuera):**
1. Integral de adentro: integra respecto a UNA variable, tratando la otra como **constante** (como una parcial, al revés).
2. Evalúa en los límites de esa variable → queda una función de la otra variable.
3. Integral de afuera: integra el resultado respecto a la segunda variable.

### EJEMPLO RESUELTO 1 (rectángulo — modelo P1 del Parcial 2)
**∬_R (x+y) dA sobre R=[3,6]×[−2,2].**
```
∫_3^6 ∫_{−2}^2 (x+y) dy dx
```
Adentro (en y, x constante): ∫_{−2}^2 (x+y) dy = [xy + y²/2]_{−2}^2 = (2x+2) − (−2x+2) = 4x.
Afuera (en x): ∫_3^6 4x dx = [2x²]_3^6 = 72 − 18 = **54**. ✅

---

## 3. Regiones TIPO I y TIPO II (clase 26 Oct — el corazón del parcial)

Cuando la región **NO es un rectángulo** (está acotada por curvas), los límites de la integral de adentro **dependen de la otra variable**.

### TIPO I — "tapa y piso son funciones de x" (integra dy primero)
La región está entre dos curvas y = g₁(x) (abajo) y y = g₂(x) (arriba), con x ∈ [a,b]:
```
∬_D f dA  =  ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x,y) dy dx
```
- Límites de **y** (adentro): funciones de x (g₁, g₂).
- Límites de **x** (afuera): números constantes (a, b).
- **Visual:** barres con rayas **verticales**; cada raya entra por g₁ y sale por g₂.

### TIPO II — "pared izq y der son funciones de y" (integra dx primero)
La región está entre x = h₁(y) (izquierda) y x = h₂(y) (derecha), con y ∈ [c,d]:
```
∬_D f dA  =  ∫_c^d ∫_{h₁(y)}^{h₂(y)} f(x,y) dx dy
```
- Límites de **x** (adentro): funciones de y.
- Límites de **y** (afuera): constantes.
- **Visual:** barres con rayas **horizontales**.

> **Regla de oro:** los límites de la integral **de afuera SIEMPRE son constantes** (números). Si te queda una variable en el límite exterior, algo está mal.

### EJEMPLO RESUELTO 2 (región tipo I — modelo P2 del Parcial 2)
**∬_D 3xy dA, D acotada por y=x² y y=3** ... ojo, el modelo dice "y − 3 = 0" o sea y=3. Tomemos D entre la parábola y=x² (abajo) y la recta y=3 (arriba).

Cortes: x²=3 → x=±√3. Entonces x ∈ [−√3, √3], y para cada x, y va de x² hasta 3. Es **tipo I**:
```
∫_{−√3}^{√3} ∫_{x²}^{3} 3xy dy dx
```
Adentro (en y): ∫_{x²}^3 3xy dy = 3x·[y²/2]_{x²}^3 = 3x·(9/2 − x⁴/2) = (27x/2) − (3x⁵/2).
Afuera (en x): ∫_{−√3}^{√3} (27x/2 − 3x⁵/2) dx. El integrando es **impar** y el intervalo simétrico → **= 0**. ✅
(Si el modelo usaba otra recta o f, el método es idéntico; aquí sale 0 por simetría.)

---

## 4. CAMBIAR EL ORDEN de integración (cae mucho en los modelos)

A veces te dan la integral en un orden (ej. dy dx) y piden reescribirla en el otro (dx dy), o el cálculo es imposible en un orden pero fácil en el otro.

**Receta:**
1. **Dibuja la región** D a partir de los límites dados (lo más importante).
2. **Reinterpreta** la MISMA región en el otro orden:
   - Si venías tipo I (dy dx), reescribe como tipo II: ¿entre qué x=h₁(y) y x=h₂(y) está?, ¿qué rango de y?
3. Escribe la nueva integral. **La región no cambia, solo cómo la recorres.**

### EJEMPLO RESUELTO 3 (cambiar orden)
**Cambiar ∫_0^1 ∫_x^1 f dy dx al orden dx dy.**
Región: x∈[0,1], y de x a 1 → es el triángulo 0≤x≤y≤1.
Reinterpretado en dx dy: y∈[0,1], x de 0 a y:
```
∫_0^1 ∫_0^y f dx dy
```
✅ (Mismo triángulo, barrido horizontal en vez de vertical.)

---

## 5. Volumen y el ejercicio del profe (28 Oct)

La integral doble de f≥0 sobre D = **volumen bajo la superficie z=f(x,y)** sobre D.

> **El ejercicio que al profe le costó (ej. 24, sección 15.3):** volumen del sólido acotado por z=x, y=x, x+y=2, z=0. La clave que él recalcó: **proyectar al plano xy** y hallar la región acotada por las rectas y=x, x+y=2 y **x=0** (esta última viene de z=x ∩ z=0). Esas tres rectas forman un **triángulo**, que es la región D sobre la que se plantea la integral del volumen ∬_D x dA. Moraleja: para hallar los límites, **proyecta el sólido al plano xy** y encuentra las rectas frontera (intersecciones de los planos con z=0).

---

## 6. Estrategia para elegir tipo I vs II
- Mira la región: si las curvas de arriba/abajo son **y=f(x)** limpias → tipo I.
- Si las de izq/der son **x=f(y)** limpias → tipo II.
- Si en un orden tendrías que **partir** la región en varios pedazos pero en el otro no → elige el que NO parte.
- Para "plantear sin resolver" (estilo profe): basta con dar los límites correctos.

---

## 7. Errores típicos (trampas)
- **Límite exterior con variable:** el de afuera SIEMPRE es constante.
- **Confundir qué curva va arriba/abajo** (o izq/der): dibuja y verifica con un punto interior.
- **Olvidar el signo/orden de los cortes** al hallar dónde se cruzan las curvas.
- **Al cambiar orden, re-derivar los límites mal:** siempre redibuja la región primero.
- **No dibujar la región.** El 90% de los errores se evitan con el dibujo.
- Tratar mal la variable "constante" en la integral de adentro (es como integrar parcial).

---

## 8. Checklist mental
- [ ] ¿Dibujé la región D?
- [ ] ¿Es rectángulo (Fubini, orden libre) o región tipo I/II?
- [ ] ¿Los límites de afuera son constantes?
- [ ] ¿Integré de adentro hacia afuera, tratando la otra variable como constante?
- [ ] Si piden cambiar orden: ¿redibujé y reinterpreté la MISMA región?
- [ ] ¿Justifiqué / planteé bien (estilo "plantear sin resolver" si lo piden)?
