# Cálculo en Varias Variables — Funciones de Varias Variables y Superficies 📐

### Prof. Leonardo A. Cano G. · Clase 31 de agosto · UNAL

**Leyenda de colores:** 🟢 Definición · 🟡 Fórmula clave · 🟠 Ley/principio · 🔵 Notación/símbolo especial · 🩷 Ejemplo/analogía · 💜 Advertencia/aclaración

---

## 1. ¿Qué es una función de varias variables?

- 🟢«Una función de varias variables es una regla f que toma un vector de entrada de n coordenadas y devuelve un vector de salida de m coordenadas.»
- Se escribe: 🔵«f: Rⁿ → Rᵐ», donde n = cuántas variables entran, m = cuántas salen.
- 💜«El profe escribe las variables como VECTOR COLUMNA, no como (x,y). O sea f(x) con x arriba e y abajo. Acostúmbrate porque toda la clase es así.»
- Cuando m = 1 la función se llama 🟢«escalar (devuelve un solo número)»; cuando m > 1 se llama 🟢«vectorial (devuelve un vector)».

---

## 2. Dominio de una función ⭐

- 🟢«El dominio es el conjunto de TODOS los vectores de entrada para los que la fórmula tiene sentido (no se rompe).»
- Se prohíbe: dividir por 0, raíz par de número negativo, y logaritmo de número ≤ 0.
- 🟠«REGLA DE ORO para funciones vectoriales: el dominio total es la INTERSECCIÓN de los dominios de cada componente. Debe funcionar en TODAS a la vez.»

- 🩷 Ejemplo del profe: f(x,y) = ( √(4 − 2x² − y²) , ln(x+y) , 2 )
  - Componente 1: g(x,y) = √(4 − 2x² − y²) → necesita 🟡«4 − 2x² − y² ≥ 0» → 🟡«2x² + y² ≤ 4»
  - Componente 2: h(x,y) = ln(x+y) → necesita 🟡«x + y > 0» → o sea 🟡«y > −x»
  - Componente 3: constante 2 → existe siempre (dominio = todo R²)
  - Dominio total = intersección de las tres condiciones.

- 💜«Interpreta el dominio SIEMPRE de forma geométrica, no lo dejes como desigualdad suelta. Al profe le gusta el dibujo.»
  - 🩷«2x² + y² ≤ 4  ⟺  x²/2 + y²/4 ≤ 1 → interior de una ELIPSE con cortes en x = ±√2 y en y = ±2.»
  - 🩷«y > −x → todo lo que está POR ENCIMA de la recta y = −x, SIN incluir la recta (por eso va con > y no ≥).»

---

## 3. Truco de notación: distancias

- 🔵«El profe reescribe x² + y² como ( dist((x,y),(0,0)) )² — es decir, la distancia al origen elevada al cuadrado.»
- Sirve para "leer" geométricamente las expresiones: x² + y² = r² es un círculo de radio r centrado en el origen.
- 🩷«3 ≥ x² + y² se lee como: círculo centrado en (0,0) de radio √3 (y su interior).»

---

## 4. Ejercicio de intersección (recta con cuádrica)

- 🩷 Enunciado del profe: halle los puntos de intersección P y Q entre la elipse 4 = 2x² + y² (1) y la recta y = −x (2).
- Método: 🟠«sustitución — reemplazar (2) en (1).»
  - Paso 1: reemplazo y = −x en la elipse → 4 = 2x² + (−x)² = 2x² + x² = 3x²
  - Paso 2: despejo x → x² = 4/3 → 🟡«x = ± 2/√3 = ± 2√3/3»
  - Paso 3: como y = −x, cada valor de x da su punto:
    - P = ( 2/√3 , −2/√3 )
    - Q = ( −2/√3 , 2/√3 )
- 💜«Racionaliza al final: 2/√3 = 2√3/3. El profe lo deja racionalizado.»

---

## 5. Ejemplos de función: (1) Lineales

- 🟢«Una función lineal (afín) tiene la forma f(x) = ax + b en dimensión 1.»
- Forma general: 🟡«f: Rⁿ → Rᵐ,  x ↦ A·x + b», donde A es una matriz m×n y b ∈ Rᵐ.
- Casos especiales (rectas paramétricas):
  - 🔵«R → R²:  t ↦ (a,b) + t·(v₁,v₂)»  → (a,b) es el 🩷«punto inicial» y (v₁,v₂) el 🩷«vector director».
  - 🔵«R → R³:  t ↦ (a,b,c) + t·(v₁,v₂,v₃)»
- 🟠«Estas rectas representan movimientos inerciales (velocidad constante).»

---

## 6. Ejemplos de función: (1.3) Parametrización de un plano

- Una función φ: R² → R³ escrita con matriz genera un PLANO en el espacio:
- 🟡«φ(x,y) = c + x·a + y·b»
  - c = (c₁,c₂,c₃) es el 🩷«punto de anclaje del plano»
  - a = (a₁,a₂,a₃) y b = (b₁,b₂,b₃) son 🩷«las dos direcciones que "generan" (barren) el plano»
- 💜«Es el mismo A·x + b de antes, pero desarmado: al multiplicar la matriz por (x,y) obtienes x veces la primera columna más y veces la segunda columna, más el término independiente c.»

---

## 7. Funciones escalares cuadráticas

- 🟢«Función escalar cuadrática: va de R² a R y tiene términos al cuadrado.»
- Forma: 🟡«p(x,y) = ax² + by² + cx + dy + e»
- Para entenderlas usamos su gráfica (igual que en funciones de R a R el gráfico es la herramienta clave).

---

## 8. Gráfica y curvas de nivel ⭐

- 🟢«La gráfica de f es el conjunto de puntos (x, y, f(x,y)) en el espacio, para cada (x,y) del dominio.»
- 🟡«Graf(f) := { (x, y, f(x,y)) : (x,y) ∈ Dom f }»

- 🟢«Una curva de nivel es el conjunto de puntos del dominio donde la función vale una constante c fija.»
- Dado c ∈ R:
- 🟡«f⁻¹(c) := { (x,y) ∈ R² : f(x,y) = c }»
- 💜«Idea intuitiva: son como las líneas de altura de un mapa topográfico. Cortas la gráfica 3D a una altura c y ves qué figura queda proyectada en el plano.»

- 🩷 Ejemplos del profe (encuentre las curvas de nivel):
  - i) f(x,y) = x² + y²  → f⁻¹(c): x² + y² = c → CÍRCULOS de radio √c (para c > 0)
  - ii) f(x,y) = x² − y² → f⁻¹(c): x² − y² = c → HIPÉRBOLAS

---

## 9. Superficies de nivel (el equivalente en R³)

- 🟢«Una superficie de nivel es el equivalente de la curva de nivel, pero para funciones de R³ a R: el conjunto de puntos (x,y,z) donde la función vale una constante c.»
- 🟡«f⁻¹(c) := { (x,y,z) ∈ R³ : f(x,y,z) = c }»
- 💜«Diferencia clave: curva de nivel (f de R² a R) → da una CURVA en el plano. Superficie de nivel (f de R³ a R) → da una SUPERFICIE en el espacio.»
- 🩷 Ejemplo: f(x,y,z) = x²+y²+z². La superficie de nivel f=4 es x²+y²+z²=4 → una ESFERA de radio 2. Cada c da una esfera concéntrica distinta.

💜 TAREA AUTÓNOMA (dicha por el profe): hacer los ejercicios de la sección 1.1 (prerrequisitos) del Marsden-Tromba, EXCEPTO coordenadas esféricas/cilíndricas. Es el "fundamento asumido" (vectores, planos, rectas, productos punto/cruz) → ya cubierto en el Taller 1 resuelto.

---

## 📝 Problemas propuestos

1. Halla el dominio de f(x,y) = ( √(9 − x² − y²) , ln(y − x) ) e interprétalo geométricamente (dibújalo).
2. Halla los puntos de intersección entre la elipse x² + 2y² = 6 y la recta y = x, usando sustitución.
3. Escribe la parametrización φ(x,y) = c + x·a + y·b de un plano que pase por (1,0,2) con direcciones a=(1,1,0) y b=(0,1,1).
4. Encuentra y dibuja las curvas de nivel de f(x,y) = x² + y² para c = 1, c = 4 y c = 9.
5. Encuentra las curvas de nivel de f(x,y) = x² − y² para c = 0 (caso especial: ¿qué figura da?).
6. Reescribe la expresión x² + y² ≤ 5 usando el lenguaje de distancia al origen e interpreta la región.

---

*Este es el formato base para las próximas clases.*
