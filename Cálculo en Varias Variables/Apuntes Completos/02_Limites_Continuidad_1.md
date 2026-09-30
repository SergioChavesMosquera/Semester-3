# Cálculo en Varias Variables — Límites (Parte 1) 🎯

### Prof. Leonardo A. Cano G. · Clase 7 de septiembre 2026 · UNAL

**Leyenda de colores:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Ley/principio · 🔵 Notación/símbolo especial · 🩷 Ejemplo/analogía · 💜 Advertencia/aclaración

---

## 1. Intuición: cómo "ver" cada tipo de función

- Antes de definir límite, conviene tener la imagen mental de cada función:
  - 🩷«funciones de R a R → sus gráficas son curvas en R²»
  - 🩷«funciones de R² a R → sus gráficas son superficies en R³»
  - 🩷«α: R → Rⁿ es una curva parametrizada (un "camino" en el espacio)»
- Pregunta central de la clase: 💜«¿Qué hacemos para funciones generales Rⁿ → Rᵐ? Necesitamos una definición que sirva para todas a la vez.»

---

## 2. Notación: bolas abiertas ⭐

- 🟢«Una bola abierta de radio r centrada en a es el conjunto de todos los puntos que están a distancia menor que r del centro a.»
- 🔵«Bᵣ(a) := { x ∈ Rⁿ : ‖x − a‖ < r }»
- 💜«"Abierta" = NO incluye el borde (por eso es < estricto, no ≤). En R es un intervalo (a−r, a+r), en R² es un disco sin borde, en R³ es una esfera maciza sin cáscara.»

---

## 3. Definición de límite (con bolas) ⭐

- 🟢«Sea F: Rⁿ → Rᵐ tal que una bola perforada Bᵣ(a) − {a} está dentro del dominio. Decimos que lim_{x→a} F(x) = b si: para todo radio ε>0 (por pequeño que sea), existe un radio δ>0 tal que al meter la bola perforada Bδ(a)−{a} en F, toda su imagen cae dentro de Bε(b).»
- 🟡«lim_{x→a} F(x) = b  ⟺  ∀ε>0, ∃δ>0 tq  F( Bδ(a) − {a} ) ⊆ Bε(b)»
- Escrito con normas (la versión que más se usa en cuentas):
- 🟡«Si 0 < ‖x − a‖ < δ  ⟹  ‖F(x) − b‖ < ε»
- 💜«El {a} se quita (bola perforada) porque el límite NO mira qué pasa EN el punto a, solo qué pasa CERCA de a.»
- 💜«ε lo elige el "enemigo" (tan pequeño como quiera); δ lo debes encontrar TÚ en función de ε.»

---

## 4. Ejemplos ε-δ básicos

- 🩷 Ejemplo (función constante): si F es constante = c, prueba que lim_{x→a} F(x) = c.
  - Observa que 🟡«∀δ>0: F(Bδ(a)−{a}) = {c} ⊆ Bε(c)» (la imagen es siempre el punto c, que obviamente está en cualquier bola centrada en c). Sirve cualquier δ.

- 🩷 Ejemplo (lim_{x→1} x² = 1):
  - Sea ε>0. Factoriza: 🟡«|x² − 1| = |x−1|·|x+1|»
  - Queremos que esto sea < ε 💜«controlando el factor |x+1|, que es el "problemático".»
  - Truco: 🟠«si restringimos x a la bola B₁(1) = (0,2), entonces |x+1| < 3 (acotamos el factor molesto).»
  - Tomamos 🟡«δ = Mín{ δ₁, 1 }  con  δ₁ < ε/3»
  - Entonces si 0 < |x−1| < δ:  |f(x)−1| = |x+1|·|x−1| ≤ 3·δ₁ < ε ✓
  - 💜«La idea del δ = Mín{...} es asegurar DOS cosas a la vez: quedarse en la zona donde el factor está acotado (el 1) y que el producto sea < ε (el ε/3).»

---

## 5. Teorema: límite de la suma

- 🟠«Si lim_{x→a} F₁(x) = L₁ y lim_{x→a} F₂(x) = L₂, entonces lim_{x→a} (F₁+F₂)(x) = L₁ + L₂.»
- Idea de la demostración (técnica del ε/2):
  - Para ε dado, cada límite me da su δᵢ tal que 🟡«‖Lᵢ − Fᵢ(x)‖ < ε/2»
  - Tomo 🟡«δ = Mín{δ₁, δ₂}» (para que valgan las dos a la vez)
  - Junto con 🟠«desigualdad triangular: ‖u+v‖ ≤ ‖u‖ + ‖v‖»:
  - ‖(L₁+L₂) − (F₁(x)+F₂(x))‖ ≤ ‖L₁−F₁(x)‖ + ‖L₂−F₂(x)‖ < ε/2 + ε/2 = ε ✓
- 💜«El ε/2 se usa para que al sumar los dos errores el total no pase de ε. Es una técnica que se repite en TODAS estas demostraciones.»

---

## 6. Teorema: límite del producto (escalar por vectorial)

- 🟠«Si lim_{x→a} f(x) = λ (escalar) y lim_{x→a} F(x) = b (vectorial), entonces lim_{x→a} f(x)·F(x) = λ·b.»
- Truco de la demostración: 🟠«sumar y restar un término intermedio (f·b) para poder separar.»
- 🟡«‖f·F − λ·b‖ = ‖f·F − f·b + f·b − λ·b‖ ≤ ‖f·(F−b)‖ + ‖b·(f−λ)‖»
- 💜«"Sumar y restar el mismo término" + desigualdad triangular es EL truco estrella para productos. Memorízalo.»

---

## 7. Lema clave: límites por componentes ⭐

- 🟠«El límite de una función vectorial se calcula COMPONENTE POR COMPONENTE.»
- Si F(x) = ( f₁(x), ..., fₙ(x) ), entonces:
- 🟡«lim_{x→a} F(x) = b = (b₁,...,bₙ)  ⟺  lim_{x→a} fᵢ(x) = bᵢ  para cada i = 1,...,n»
- Herramienta de la prueba: 🟡«‖F(x) − b‖² = Σᵢ (fᵢ(x) − bᵢ)²»
  - (⟸) Si cada componente < ε²/m, al sumar los m términos queda < ε², luego la norma < ε.
  - (⟹) Como cada |fᵢ(x)−bᵢ|² ≤ ‖F(x)−b‖², si la norma total es pequeña, cada componente también lo es.
- 💜«Este lema es el que te SALVA la vida: en vez de pelear con un límite vectorial, lo partes en límites de una variable de salida cada uno.»

---

## 8. Ejercicio: límite de una proyección

- 🩷 Pruebe con la definición que lim_{(x,y)→(a,b)} x = a  (el límite de "quedarse solo con la x").
- Solución (elegante):
  - Observa que 🟡«|x−a|² ≤ |x−a|² + |y−b|² = ‖(a,b) − (x,y)‖²»
  - O sea |x−a| ≤ ‖(x,y)−(a,b)‖. 🟠«Simplemente toma δ < ε.»
  - Pues si 0 < ‖(a,b)−(x,y)‖ < δ, entonces |a−x| ≤ ‖(a,b)−(x,y)‖ < δ < ε ✓
- 💜«Idea: una coordenada suelta siempre es ≤ la distancia total. Por eso proyectar "no aleja".»

---

## 9. Ejercicio de aplicación (juntando todo)

- 🩷 Calcule lim_{(x,y)→(2,3)} ( x+y , x²−y² )
- 🟠«Por el lema, me ocupo de cada componente por separado.»
- Datos base (por el ejercicio de proyección): lim x = 2  y  lim y = 3.
  - **Componente 1** (usando límite de la suma):
    - lim (x+y) = lim x + lim y = 2 + 3 = **5**
  - **Componente 2** (usando límite del producto):
    - lim (x²−y²) = (lim x)(lim x) − (lim y)(lim y) = 2·2 − 3·3 = 4 − 9 = **−5**
- Resultado: 🟡«lim_{(x,y)→(2,3)} (x+y, x²−y²) = (5, −5)»
- 💜«Fíjate en el método del profe: NO reemplaza directo. Descompone en proyecciones + suma + producto, justificando cada paso con un teorema. Así lo va a querer en el parcial.»

---

## 📝 Problemas propuestos

1. Escribe explícitamente qué conjunto es B₂((1,−1)) en R² y dibújalo (disco, centro, radio).
2. Prueba con la definición ε-δ que lim_{x→2} x² = 4 (imita el ejemplo de x²=1: factoriza, acota, toma δ=Mín{...}).
3. Prueba que el límite de una función constante F(x)=(3,−2) cuando x→a es (3,−2).
4. Usando el teorema de la suma y del producto, calcula lim_{(x,y)→(1,4)} ( x−y , x·y ).
5. Prueba que lim_{(x,y)→(a,b)} y = b (análogo al ejercicio de proyección, pero con la otra coordenada).
6. Calcula lim_{(x,y)→(2,1)} ( 3x+2y , x²+y² , 5 ) usando el lema de componentes.
7. Explica con tus palabras por qué en la definición de límite se usa la bola PERFORADA Bδ(a)−{a} y no la bola completa.

---

*Este es el formato base para las próximas clases.*
