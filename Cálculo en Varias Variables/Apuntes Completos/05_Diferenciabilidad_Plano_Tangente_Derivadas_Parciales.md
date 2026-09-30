# Cálculo en Varias Variables — Plano Tangente, Derivadas Parciales y Gradiente 📈

### Prof. Leonardo A. Cano G. · Clase 16 de septiembre 2026 · UNAL

**Leyenda de colores:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Ley/principio · 🔵 Notación/símbolo especial · 🩷 Ejemplo/analogía · 💜 Advertencia/aclaración

---

## 1. Repaso: diferenciabilidad y curvas

- 🟢«f: Rⁿ → Rᵐ es diferenciable en p si existe una transformación lineal T tal que lim_{h→0} [F(p+h) − F(p) − T·h] / ‖h‖ = 0.»
- 🟠«Idea: una función diferenciable se puede aproximar cerca de p por una función lineal (Ax + b).»
- Caso curvas α: R → Rⁿ → diferenciable en t=a significa que 🩷«admite velocidad instantánea (vector velocidad α'(a)).»

- 🩷 Ejercicio (repasado): β(t) = (1−t², t³−2t). Función lineal que la aproxima en t=1.
  - Forma buscada: At + b, con A ∈ R², b ∈ R².
  - 🟡«b = β(1) = (0, −1)»  (el punto de paso)
  - 🟡«A = Dα(1) = β'(1) = (−2t, 3t²−2)|_{t=1} = (−2, 1)»  (la velocidad)
  - Función lineal (= recta tangente): 🟡«t ↦ t(−2,1) + (0,−1) = (−2t, −1+t)»

---

## 2. Plano tangente a f: R² → R ⭐

- 🟢«f: R² → R es diferenciable en a si su gráfica tiene un PLANO TANGENTE en (a, f(a)).»
- Para construirlo, se usan dos vectores tangentes (uno en cada dirección coordenada):
- 🟡«v = ( 1, 0, d/dt f(a+(t,0)) |_{t=0} )»  (dirección x)
- 🟡«w = ( 0, 1, d/dt f(a+(0,t)) |_{t=0} )»  (dirección y)
- 🔵«Estos v y w son vectores tangentes a la superficie gráfica de f en el punto (a, f(a)).»

- **Parametrización del plano tangente:**
- 🟡«φ(s,t) = (a, f(a)) + s·v + t·w»

- **Ecuación del plano tangente** (usando el producto cruz como vector normal):
- 🟡«(v × w) · ( X − (a, f(a)) ) = 0»
- 💜«El producto cruz v×w da un vector perpendicular al plano (la NORMAL). Luego usas la ecuación de plano de siempre: normal · (punto genérico − punto conocido) = 0.»

---

## 3. Ejemplo COMPLETO: plano tangente a f(x,y)=x²+y² en (0,1,1) ⭐

- 🩷 La superficie es x² + y² = z (paraboloide). Punto p = (0,1,1).
- **Paso 1 — Camino en dirección y:** α(t) = (0, 1+t, (1+t)²)
  - v = α'(0) = (0, 1, 2(1+t))|_{t=0} = 🟡«(0, 1, 2)»
- **Paso 2 — Camino en dirección x:** β(t) = (t, 1, t²+1)
  - w = β'(0) = (1, 0, 2t)|_{t=0} = 🟡«(1, 0, 0)»
- **Paso 3 — Normal = producto cruz** v × w:
  - v × w = det | i  j  k ; 0  1  2 ; 1  0  0 | = ( 1·0−2·0 , −(0·0−2·1) , 0·0−1·1 ) = 🟡«(0, 2, −1)»
- **Paso 4 — Ecuación del plano** (normal · (X − p) = 0):
  - (0, 2, −1) · (x, y−1, z−1) = 0  →  2(y−1) − (z−1) = 0  →  2y−2−z+1 = 0
  - 🟡«Plano tangente:  2y − z = 1»
- 💜«Truco del profe: para el plano tangente a una superficie z=f(x,y), arma 2 caminos (uno moviendo x, otro moviendo y), deriva cada uno en t=0 para tener v y w, cruza para la normal, y escribe la ecuación. Método 100% mecánico.»

---

## 4. Derivadas parciales ⭐

- 💜«Motivación: las derivadas de f a lo largo de a+(t,0) y a+(0,t) son justo límites del tipo [f(a+h·eᵢ)−f(a)]/h. Eso ES la derivada parcial.»
- 🟢«DEFINICIÓN: la derivada parcial de f respecto a xᵢ es:»
- 🟡«∂f/∂xᵢ (x) = ∂ᵢ(f)(x) = lim_{h→0} [ f(x + h·eᵢ) − f(x) ] / h»
- 🔵«eᵢ = (0,...,1,...,0) es el vector con un 1 en la i-ésima componente y 0 en el resto.»

- 🩷 Ejemplo (por definición): f(x₁,x₂) = 3x₁² − x₂. Calcular ∂f/∂x₂ (1,0).
  - lim_{h→0} [ f(x₁, x₂+h) − f(x₁, x₂) ] / h = lim [ 3x₁²−(x₂+h) − 3x₁²+x₂ ] / h = lim (−h)/h = **−1**

- 🟠«REGLA PRÁCTICA para calcular parciales: deriva respecto a UNA variable tratando TODAS las demás como constantes.»
- 🩷 Ejemplo (por reglas): f(x,y,z) = x²y·cos(xy)
  - ∂f/∂x = 2xy·cos(xy) − x²y²·sen(xy)   (regla del producto en x; ojo con la cadena en cos(xy))
  - ∂f/∂y = x²·cos(xy) − x³y·sen(xy)
  - ∂f/∂z = 0   (no aparece z → constante)

---

## 5. Derivada = gradiente (caso f: Rⁿ → R) ⭐

- 🟠«TEOREMA: si f: Rⁿ → R es diferenciable en a, su derivada es el vector gradiente:»
- 🟡«Df^(a) = ∇f^(a) = ( ∂f/∂x₁ , ∂f/∂x₂ , ... , ∂f/∂xₙ )  evaluado en a»
- 🔵«∇ (nabla) es el símbolo del gradiente. Es un VECTOR fila con todas las parciales.»

---

## 6. Criterio práctico de diferenciabilidad ⭐

- 🟠«TEOREMA: si las derivadas parciales de f existen Y son continuas, entonces f es diferenciable.»
- 💜«NOTA IMPORTANTE (típica trampa de examen): el recíproco NO vale. Hay funciones diferenciables cuyas parciales NO son continuas. O sea: "parciales continuas" ⟹ diferenciable, pero "diferenciable" NO obliga a que las parciales sean continuas.»
- 🩷 Ejercicio: mostrar que f(x,y,z) = xyz es diferenciable en su dominio (sus parciales ∂f=yz, xz, xy son polinomios → continuas → f diferenciable).

---

## 7. Matriz derivada / Jacobiana (caso F: Rⁿ → Rᵐ) ⭐

- 🟠«TEOREMA: si F = (f₁, ..., fₘ) es diferenciable en a, su matriz derivada tiene por entradas las parciales:»
- 🟡«(DF)^(a)_{ij} = ∂(fᵢ)/∂xⱼ (a)»   (fila i = componente fᵢ, columna j = variable xⱼ)
- Equivalentemente, cada FILA es el gradiente de una componente:
- 🟡«DFₐ = [ Df₁^(a) ; Df₂^(a) ; ... ; Dfₘ^(a) ]»
- 🔵«Esta matriz se llama la MATRIZ JACOBIANA. Es la generalización de la derivada a funciones vectoriales.»

- 🩷 Ejemplo: F(x,y,z) = (x²y, x+y, z). Calcular DF.
  - Fila 1 (f₁=x²y):   ∂/∂x=2xy,  ∂/∂y=x²,  ∂/∂z=0
  - Fila 2 (f₂=x+y):   ∂/∂x=1,    ∂/∂y=1,   ∂/∂z=0
  - Fila 3 (f₃=z):     ∂/∂x=0,    ∂/∂y=0,   ∂/∂z=1
- 🟡 Resultado:
  ```
  DF = [ 2xy   x²   0 ]
       [  1     1   0 ]
       [  0     0   1 ]
  ```
- 💜«La jacobiana ordena TODAS las parciales en una tabla: filas = componentes de salida, columnas = variables de entrada. Cuenta bien el tamaño: m filas × n columnas.»

---

## 📝 Problemas propuestos

1. Halla la recta tangente (función lineal aproximante) a α(t)=(t², t³, t) en t=1.
2. Encuentra la ecuación del plano tangente a f(x,y)=x²+y² en el punto (1,1,2). (Arma α, β; deriva; cruza; escribe.)
3. Encuentra el plano tangente a f(x,y)=xy en (1,2,2).
4. Calcula por DEFINICIÓN (con el límite) ∂f/∂x (2,1) para f(x,y)=x²+3y.
5. Calcula todas las parciales de f(x,y,z)=e^(xy)·sen(z) tratando las otras variables como constantes.
6. Escribe el gradiente ∇f de f(x,y,z)=x²+y²+z² y evalúalo en (1,2,3).
7. Argumenta por qué f(x,y)=x³ − 2xy + y² es diferenciable en todo R² (usa el criterio de parciales continuas).
8. Calcula la matriz jacobiana DF de F(x,y)=(x²−y, xy, x+y) e indica su tamaño (filas × columnas).
9. Calcula la jacobiana de F(x,y,z)=(xyz, x+y+z) y evalúala en (1,1,1).

---

*Este es el formato base para las próximas clases.*
