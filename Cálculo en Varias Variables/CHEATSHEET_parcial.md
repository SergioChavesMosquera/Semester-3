# 🎯 CHEAT-SHEET — Parcial 1 Cálculo Multivariable (Prof. Cano)

> Regla de oro: JUSTIFICA TODO ("respuesta sin justificación no vale"). Cuando puedas, haz el ejercicio de 2 formas y verifica.

---

## 1️⃣ DERIVADAS PARCIALES + JACOBIANA
- Parcial ∂f/∂xᵢ = derivar respecto a esa variable, las demás CONSTANTES.
- Jacobiana DF: filas = componentes de salida, columnas = variables. Tamaño = (salidas)×(entradas).
- Constante que SUMA → desaparece (deriva a 0). Constante que MULTIPLICA → se queda.
- Cadena en eˣᶻ: multiplicar por derivada del exponente. e⁰=1, sen(0)=0, cos(0)=1.

## 2️⃣ LÍMITES
- NO EXISTE: 2 caminos con resultados distintos (ejes (t,0),(0,t); recta y=mx; y=x²).
- Polares: x=r cosθ, y=r senθ. Si depende de θ → NO existe. Si queda r·(acotado) → 0.
- SÍ EXISTE (=0): ACOTAMIENTO / sándwich. REMATE que se me olvida:
  ```
  x²|y|/(x²+y²) = |y| · [x²/(x²+y²)]   ← el corchete ≤ 1
                ≤ |y| · 1 = |y| → 0
  ```
  Truco: factoriza el |x| o |y|, el resto acótalo por 1, y eso → 0.

## 3️⃣ REGLA DE LA CADENA
- D(F∘G) = DF · DG. AFUERA primero. Evaluar DF en el punto de adentro G(t).
- Multiplicar matrices: fila × columna, cada casilla es SUMA de productos.
- Dimensiones (m×n)·(n×p)=m×p. Si no encajan → orden invertido.

## 4️⃣ DERIVADA DIRECCIONAL (el profe NO normaliza, usa v directo)
- Definición: D_v f(p) = lim_{h→0} [f(p+hv) − f(p)] / h
- Gradiente: D_v f(p) = ∇f(p) · v      (∇f = (∂f/∂x, ∂f/∂y, ...))
- HACER LAS 2 FORMAS y verificar que coincidan (mi estrategia anti-error).
- Al dividir por h: término por término, cada uno pierde UNA h. NO homogenizar.
- ⚠️ Menos delante de paréntesis → repartir a TODOS: −(1+4h+4h²) = −1−4h−4h².
- ⚠️ −2(2+h)(1+3h): primero multiplico los binomios, DESPUÉS reparto el −2.

## 5️⃣ PLANO TANGENTE (2 métodos, ambos válidos)
**Método gradiente (RÁPIDO):**
- Superficie z=g(x,y) → reescribe f = g − z = 0. O si ya es f(x,y,z)=c, úsala directo.
- ∇f evaluado = NORMAL. Luego: A(x−x₀)+B(y−y₀)+C(z−z₀)=0. Distribuir, ordenar.
- Ej: z=x²+y² en (1,2,5): f=x²+y²−z, ∇f=(2x,2y,−1)→(2,4,−1) → 2x+4y−z=5.
- VERIFICAR: meter el punto en la ecuación debe cumplirse.

**Método caminos + cruz (Escenario B, superficie parametrizada φ(u,v)):**
- φ_u=∂φ/∂u, φ_v=∂φ/∂v → normal = φ_u × φ_v → n·(X−P)=0.

**Producto cruz (andamiaje):** X=↘−↙ ; Y=−(↘−↙) [¡MENOS!] ; Z=↘−↙. Doble negativo: usar paréntesis.

## 6️⃣ DIFERENCIABILIDAD
- Diferenciable ⟺ tiene plano tangente. Criterio: parciales existen Y continuas ⟹ diferenciable.
- Justificar: "las parciales son sumas/productos/composiciones de continuas → continuas → f diferenciable".
- RECÍPROCO NO VALE (diferenciable NO obliga parciales continuas).

## 7️⃣ DOMINIO + CONTINUIDAD
- Dominio = todo MENOS donde se rompe: ÷0, raíz par de negativo (≥0), log de ≤0 (>0 estricto).
- Función vectorial: dominio = INTERSECCIÓN de dominios de cada componente.
- Interpretar GEOMÉTRICAMENTE (círculo/disco/elipse/semiplano) y decir si borde incluido (≤ sí, < no).
- ¡SIEMPRE rematar!: "f es continua en TODO su dominio" (suma/producto/composición de continuas).

## 8️⃣ PARAMETRIZAR INTERSECCIÓN (superficie ∩ plano z=k)
- Igualar → ecuación en x,y → identificar cónica.
- Círculo x²+y²=r² → (r cos t, r sen t, k). Elipse x²/a²+y²/b²=1 → (a cos t, b sen t, k).
- ¡SIEMPRE escribir el rango!: t ∈ [0, 2π].

## 🌟 GRADIENTE — datos que Cano puede preguntar en teoría (clase 28 sep)
- ∇f apunta en la dirección de MÁXIMO CRECIMIENTO de f.
- ∇f es ORTOGONAL (perpendicular) a las curvas/superficies de nivel.
  Prueba: f(α(t))=c → d/dt = ∇f·α' = 0 → perpendiculares.
- Puntos críticos: en máx/mín local, ∇f=0. (Si ∇f=0 → máx, mín, o punto de silla.)

## ✅ REMATES QUE NO PUEDO OLVIDAR (puntos gratis)
1. Límite que existe → cerrar el sándwich (factor |y|, resto ≤1, → 0).
2. Dominio → decir "continua en todo su dominio" + dibujo/interpretación.
3. Parametrización → escribir t ∈ [0,2π].
4. Plano tangente → verificar metiendo el punto.
5. Derivada direccional → hacer definición Y gradiente, verificar.
