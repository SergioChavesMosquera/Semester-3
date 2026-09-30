# Cálculo en Varias Variables — Límites (Parte 2) y Continuidad 🔗

### Prof. Leonardo A. Cano G. · Clase 9 de septiembre 2026 · UNAL

**Leyenda de colores:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Ley/principio · 🔵 Notación/símbolo especial · 🩷 Ejemplo/analogía · 💜 Advertencia/aclaración

---

## 1. Propiedades algebraicas de los límites ⭐

- 🟠«Sean f, g: Rⁿ → R con lim_{x→a} f(x) = L₁ y lim_{x→a} g(x) = L₂. Entonces:»
  - i) 🟡«lim (f + g) = L₁ + L₂»  (el límite de la suma es la suma de los límites)
  - ii) 🟡«lim (f · g) = L₁ · L₂»  (el límite del producto es el producto de los límites)
  - iii) 🟡«Si L₂ ≠ 0:  lim (f / g) = L₁ / L₂»  (cociente, solo si el denominador no tiende a 0)
- 💜«Estas propiedades + el lema de componentes = casi todos los límites que "sí existen" se calculan reemplazando y usando estas reglas.»

---

## 2. Ejemplo de aplicación (suma, producto, cociente juntos)

- 🩷 Sea F(x₁,x₂,x₃) = ( x₁x₂ / (x₁+x₂+x₃) , x₁/x₂ ). Calcular lim_{x→(1,2,0)} F.
- Por el lema, componente a componente:
  - **Componente 1** (cociente → cociente de límites):
    - lim (x₁x₂) / lim (x₁+x₂+x₃) = (1·2) / (1+2+0) = 2/3
  - **Componente 2**: lim x₁ / lim x₂ = 1/2
- Resultado: 🟡«lim_{x→(1,2,0)} F = (2/3, 1/2)»
- 💜«El denominador de la 1ª componente da 3 ≠ 0, por eso se PUEDE usar la regla del cociente. Siempre verifica esto.»

---

## 3. Continuidad ⭐

- 🟢«Sea F: Rⁿ → Rᵐ. Decimos que F es continua en a ∈ Rⁿ si lim_{x→a} F(x) = F(a).»
- 🟡«F continua en a  ⟺  lim_{x→a} F(x) = F(a)»
- 💜«En cristiano: continua = "el límite existe Y coincide con el valor de la función en el punto". Sin saltos ni huecos.»

- 🩷 Ejemplo: mostrar que F(x,y) = ( x/(2y) , 3x−y ) es continua en (0,1).
  - Calculo el límite: lim_{(x,y)→(0,1)} ( x/(2y), 3x−y ) = ( 0/2 , 0−1 ) = (0, −1)
  - Evalúo la función: F(0,1) = (0, −1)
  - Como coinciden → 🟡«lim = F(0,1) → F es continua en (0,1)» ✓

---

## 4. Continuidad por componentes

- 🟠«F = (f₁, ..., fₘ) es continua en a  ⟺  cada componente fᵢ es continua en a.»
- 💜«Igual que con los límites: partes el problema vectorial en problemas escalares.»

---

## 5. Álgebra de funciones continuas

- 🟠«Si f, g: Rⁿ → R son continuas en a, entonces:»
  - i) f + g es continua en a
  - ii) f · g es continua en a
  - iii) si g(a) ≠ 0, f/g es continua en a
- Idea de la prueba (para el producto): lim (f·g) = lim f · lim g = f(a)·g(a) = (f·g)(a) → cumple la definición de continuidad.

---

## 6. Teorema: el límite "entra" en una función continua ⭐

- 🟠«Si lim_{x→a} G(x) = b y F es continua en b, entonces:»
- 🟡«lim_{x→a} F(G(x)) = F( lim_{x→a} G(x) ) = F(b)»
- 💜«Esto es lo que te deja meter el límite adentro de ln, sen, cos, exp, etc. (porque son continuas).»

- 🩷 Ejemplo: calcular lim_{(x,y)→(3,5)} ( ln(x+y) , sen(x/y) )
  - Meto el límite dentro de cada función continua:
  - = ( ln( lim(x+y) ) , sen( lim(x/y) ) ) = ( ln 8 , sen(3/5) )

---

## 7. Teorema: composición de funciones continuas

- 🟠«Si G es continua en a, y F es continua en b = G(a), entonces F∘G es continua en a.»
- Prueba: lim_{x→a} F(G(x)) = F( lim G(x) ) = F(b) = F(G(a)) ✓
- 🩷 Ejemplo: f(x,y) = ( ln(3x²−xy) , e^(3cos(x³y)) ) es continua en su dominio, porque es composición/álgebra de funciones continuas (polinomios, ln, cos, exp).
- 🩷 Ejemplo: f(x,y) = ( xy/(x+y) , (3x²−xy)/(xy−y) ) es continua en su dominio.
  - 🟢 Sol 1 (por álgebra): x, y son continuas → xy y x+y continuas → su cociente es continuo siempre que x+y ≠ 0 (que es justo lo que pide el dominio). Similar para la otra componente.
  - 🟢 Sol 2 (por cuentas): para a=(a₁,a₂) en el dominio, lim xy/(x+y) = (a₁a₂)/(a₁+a₂) = [ xy/(x+y) ] evaluado en (a₁,a₂). El límite = el valor → continua.

---

## 8. Diferenciabilidad y Derivadas (arranque) ⭐

- Repaso (caso R → R):
- 🟢«f: R → R es diferenciable en a si se puede APROXIMAR cerca de a por una función lineal m(x−a)+f(a).»
- El "buen ajuste" se mide con un límite que debe dar 0:
- 🟡«lim_{x→a} [ f(x) − f'(a)(x−a) − f(a) ] / (x − a) = 0»,  donde 🟡«m = lim_{x→a} [f(x)−f(a)]/(x−a) = f'(a)»

- 🟢«Función lineal (afín): F: Rⁿ → Rᵐ es lineal si tiene la forma F(x) = M·x + b, con b ∈ Rᵐ y M ∈ M_{m×n}(R) (una matriz).»

- 🟢«DEFINICIÓN (diferenciabilidad en Rⁿ): F: Rⁿ → Rᵐ es diferenciable en a ⟺ existe una matriz M ∈ M_{m×n}(R) tal que:»
- 🟡«lim_{x→a} [ F(x) − M(x−a) − F(a) ] / ‖x − a‖ = 0»
- 💜«La idea es la MISMA que en R: acercarse a la función con algo lineal (ahora la "pendiente" es una matriz M, y abajo va la NORMA ‖x−a‖ porque x−a es un vector, no se puede dividir por un vector).»

---

## 9. Cómo probar que un límite NO existe: el método de los caminos ⭐

- 🟠«PRINCIPIO: si el límite existe, debe dar el MISMO valor sin importar por qué camino te acerques al punto. Si dos caminos dan valores distintos → el límite NO existe.»
- 💜«ADVERTENCIA típica del profe: NO puedes evaluar directo cuando queda 0/0. Ejemplo: x²/(x²+y²) en (0,0) da 0/0, que es indeterminado (NO es 1).»

- 🩷 Ejemplo: mostrar que lim_{(x,y)→(0,0)} x²/(x²+y²) NO existe.
  - Camino 1 — acércate por el eje x: 🔵«α(t) = (t, 0)»
    - F(t,0) = t²/(t²+0) = t²/t² = 1 → el límite por este camino es **1**
  - Camino 2 — acércate por el eje y: 🔵«β(t) = (0, t)»
    - F(0,t) = 0/(0+t²) = 0 → el límite por este camino es **0**
  - Como 1 ≠ 0, 🟡«el límite NO existe» ✓
- 💜«Truco de examen: para MOSTRAR QUE NO EXISTE basta encontrar 2 caminos con resultados distintos. Los caminos más fáciles: los ejes (t,0) y (0,t), y las rectas y=mx (que dejan el resultado en función de m).»

---

## 📝 Problemas propuestos

1. Calcula lim_{(x,y,z)→(2,1,3)} ( xyz/(x+y+z) , (x²−z)/y ) usando las propiedades algebraicas. Verifica que los denominadores no se anulen.
2. Muestra que F(x,y) = ( x²+y , cos(xy) ) es continua en (1,0) (calcula el límite y compáralo con F(1,0)).
3. Argumenta por qué f(x,y) = ln(x² + y² + 1) es continua en todo R² (usa composición de continuas).
4. Calcula lim_{(x,y)→(1,2)} ( e^(x−y) , sen(πx/y) ) metiendo el límite dentro de las funciones continuas.
5. Muestra que lim_{(x,y)→(0,0)} xy/(x²+y²) NO existe (usa el camino y=0 y el camino y=x).
6. Reto (quedó pendiente en clase): estudia lim_{(x,y)→(0,0)} x²/(x+y). ¿Existe? (prueba caminos como y=0, x=0, y=−x+x²... ten cuidado con el que anula el denominador).
7. Escribe la definición de diferenciabilidad en Rⁿ con tus palabras y explica por qué abajo del límite va ‖x−a‖ y no (x−a).

---

*Este es el formato base para las próximas clases.*
