# Progreso Repaso Parcial 1 — Cálculo en Varias Variables

**Estudiante:** Sergio · **Profe:** Leonardo A. Cano G. · **Examen:** Miércoles 30 sep
**Método:** ejemplo corto → resuelvo solo → corrección del error puntual → ejercicio de parcial real.

---

## Estado por tema

| Tema | Estado | Día |
|------|--------|-----|
| 1. Dominio, límites, continuidad | ✅ Completado | Jue 24 |
| 2. Derivadas parciales y Jacobiana | ✅ Completado | Jue 24 |
| 3. Regla de la cadena | ✅ Completado | Vie 25 |
| 4. Derivada direccional y gradiente | ✅ Mecanismo dominado (afinar aritmética de fracciones) | Dom 27 |
| 5. Plano tangente y diferenciabilidad | ✅ Completado (Escenario A y B) | Lun 28 |
| 6. Rotación de ejes / cónicas | ❌ NO cae (el profe no lo dio) | — |
| 7. Parametrización de superficies e intersecciones | ✅ Completado | Lun 28 |
| 8. Optimización básica | ❌ NO cae (el profe no lo dio) | — |
| Simulacros (con apuntes + solo) | ⏳ | Mar 29 |

---

## TEMA 2 — Derivadas parciales y Jacobiana ✅

### Ideas clave
- Derivada parcial ∂f/∂xᵢ = derivar respecto a esa variable tratando las demás como constantes. Significa "qué tan rápido cambia f si me muevo solo en esa dirección".
- La Jacobiana DF ES la derivada de una función vectorial (no solo "organiza"). Filas = componentes de salida, columnas = variables de entrada, cada casilla = una parcial.
- Proceso: (1) armar DF con variables → (2) evaluar en el punto → matriz de números.

### Errores corregidos
- Constante que SUMA desaparece al derivar (deriva a 0); constante que MULTIPLICA sobrevive. (Contrario al +C de integral.)
- La variable respecto a la cual derivo, si va sola (grado 1), deriva a 1 y desaparece — no arrastrarla.
- En producto x·sen(y): respecto a x queda sen(y); respecto a y queda x·cos(y). El cos SOLO sale en la columna de y.

### Ejercicio real del profe resuelto (Parcial Nov 2024, Punto 1)
- f(x,y,z)=(z+eˣᶻ, y·eᶻ), matriz en (1,1,0) → resultado [[0,0,2],[0,1,1]]. ✅ resuelto solo en <15 min.
- Trampas: cadena en eˣᶻ (×derivada del exponente), z que suma deriva a 1, e⁰=1 al evaluar.

---

## TEMA 3 — Regla de la cadena ✅

### Ideas clave
- Cadena multivariable = multiplicar Jacobianas: D(F∘G) = DF · DG. La de AFUERA primero.
- Igual que Cálculo 1 (f'(g(x))·g'(x)) pero con matrices en vez de números.
- Multiplicar matrices = FILA por COLUMNA: cada casilla es SUMA de productos.
- Dimensiones: (m×n)·(n×p) = m×p; el n del medio debe coincidir. Si no encajan → orden invertido.
- Antes de multiplicar, evaluar DF en el punto de adentro G(t).

### Errores corregidos
- Orden: hice DG·DF y bregaba → correcto es DF·DG (afuera adelante). A·B ≠ B·A.
- Sumar por fila: dejé los productos sueltos en una matriz 2×2 → cada casilla es la SUMA de los productos. Si R→R² el resultado debe ser columna 2×1; si me da 2×2, me faltó sumar.

### Ejercicio real del profe (Parcial Mar 2021, Punto 3)
- F(x,y)=(sen(x+y), eˣ), G(t)=(t², πt), D(F∘G) en t=1 → [[(2+π)cos(1+π)] ; [2e]] (2×1).
- Términos con cos(1+π) y e se dejan indicados.

---

## TEMA 4 — Derivada direccional y gradiente ✅ (afinar en simulacro)

### Ideas clave
- Gradiente: ∇f = (∂f/∂x, ∂f/∂y, ...). Vector que apunta a donde f crece más rápido.
- Fórmula rápida: D_u f(a) = ∇f(a) · u (producto punto). Pasos: normalizar u → gradiente → evaluar → producto punto.
- Definición (la que Cano EXIGE): D_u f(a) = lim_{h→0} [f(a+hu) − f(a)] / h.
- Dirección de punto A a punto B = B − A (destino menos origen). Luego normalizar.
- Vector unitario ⟺ norma = 1. Si ≠ 1, normalizar: u = v/‖v‖.

### 🚨 CORRECCIÓN CLAVE (verificado en clase del profe 23 Sep)
- El profe NO NORMALIZA el vector. Usa v tal cual en la definición Y en la fórmula del gradiente.
- Definición del profe: D_v f(p) = lim_{h→0} [f(p+hv) − f(p)] / h  (con v directo, sin normalizar)
- Teorema del profe: D_v f(p) = ∇f(p) · v  (con v directo)
- ESTO ELIMINA el problema de las fracciones al normalizar. El método es más simple: NO hay que dividir por la norma.
- TRUCO PARA EL PARCIAL: hacer por definición (el límite) Y verificar con ∇f·v. El profe pide ambas formas para el mismo ejercicio.
- Nota: los ejercicios que practicamos normalizando dan otro número; con el método del profe (v directo) es más fácil.

### Ejercicios hechos
- f=x²+xy en (1,2) dir (3,4) → 16/5 (fórmula) ✅
- f=xy²+e^(xz) en (2,1,0) dir (1,2,2) → 13/3 (fórmula, solo) ✅
- f=x²sen(y)+3xy en (1,0) dir de (1,0) a (4,4) → 16/5 (fórmula, solo) ✅
- Por definición: f=x²+y en (0,1) dir (1,0) → 0 ✅; f=x²+xy en (1,1) dir (1,0) → 3 ✅
- Pendientes de afinar (aritmética): f=x²−2y² en (1,1) dir (4,3) → correcto −4/5; f=x²+y² en (1,2) dir (3,4) → correcto 22/5.

---

## TEMA 5 — Plano tangente y diferenciabilidad ✅

### Escenario A: superficie z = f(x,y)
- Plano tangente en (a,b): z = f(a,b) + ∂f/∂x(a,b)·(x−a) + ∂f/∂y(a,b)·(y−b)
- Las parciales evaluadas SON el gradiente. Ordenar signos al distribuir.
- Ejercicio hecho: f=x²+3y² en (2,1) → z = 4x+6y−7 ✅

### Escenario B: superficie parametrizada φ(u,v) (producto cruz)
1. φ_u = ∂φ/∂u, φ_v = ∂φ/∂v (derivadas parciales, componente a componente)
2. normal = φ_u × φ_v (producto cruz)
3. Evaluar normal en el punto (u,v) dado; hallar P = φ(u,v)
4. Ecuación: n·(X−P)=0 → A(x−x₀)+B(y−y₀)+C(z−z₀)=0
- Ejercicio hecho: φ(u,v)=(u,v,u²−v) en (1,2) → −2x+y+z+1=0 ✅

### Producto cruz — truco andamiaje
- X = ↘−↙ (tapa col x) ; Y = −(↘−↙) (tapa col y, MENOS) ; Z = ↘−↙ (tapa col z). Patrón + − +.
- Fórmula equivalente: (a₂b₃−a₃b₂, a₃b₁−a₁b₃, a₁b₂−a₂b₁).
- TRAMPA doble negativo: al reemplazar números negativos, encerrarlos en paréntesis. Ej: −(1)(−1)=+1.

### Ecuación de plano (de dónde sale)
- Un plano = punto P + normal n. La normal es ⊥ a todo vector (X−P) del plano → producto punto 0.
- n·(X−P)=0. Verificar: meter P en la ecuación debe dar 0.

### Diferenciabilidad (teoría que Cano puede preguntar)
- Diferenciable en un punto ⟺ tiene plano tangente ahí.
- Criterio: parciales existen Y son continuas ⟹ diferenciable. RECÍPROCO NO VALE (trampa).

### 🌟 TRUCO NUEVO (clase 28 sep): gradiente como normal del plano tangente
- TEOREMA: ∇f es ORTOGONAL (perpendicular) a las superficies/curvas de nivel de f.
- Demostración: f(α(t))=c → d/dt[f(α(t))] = ∇f·α' = 0 → perpendiculares.
- APLICACIÓN CLAVE: para plano tangente, reescribe la superficie como nivel f(x,y,z)=c, entonces ∇f = LA NORMAL directamente (¡sin caminos ni producto cruz!).
- Ejemplo: x²+y²=z → f=x²+y²−z=0 → ∇f=(2x,2y,−1) → en (1,1,2)=(2,2,−1) → plano 2x+2y−z=2.
- Ejemplo: xyz=1 → ∇f=(yz,xz,xy) → en (1,1,1)=(1,1,1) → plano x+y+z=3.
- Este método es MÁS RÁPIDO que el de los 2 caminos + cruz. Ambos válidos, dan lo mismo.

### Derivadas parciales iteradas (clase 28 sep, solo enunciado — profe no desarrolló)
- Derivar parcial dos veces: ∂²f/∂x², ∂²f/∂y², cruzadas ∂²f/∂x∂y y ∂²f/∂y∂x.
- Clairaut: las cruzadas son iguales ∂²f/∂x∂y = ∂²f/∂y∂x.
- Poco probable en el parcial (quedó en blanco en las notas), pero saber derivar 2 veces por si acaso.

---

## TEMA 7 — Parametrizar curvas e intersecciones ✅

### Ideas clave
- Parametrizar = describir la curva con un control t: r(t)=(x(t),y(t),z(t)). Mueves t, trazas la curva. (NO es integral ni Newton.)
- Intersección superficie ∩ plano z=k: igualar → sale ecuación en x,y → identificar cónica.
- Elipse x²/a²+y²/b²=1 → x=a·cos t, y=b·sen t, z=k, t∈[0,2π]. (Funciona por cos²t+sen²t=1: los a²,b² se cancelan.)
- Las trig SÍ cambian según la figura:
  - Elipse/círculo → cos, sen
  - Parábola o variable sin cuadrado → hacer esa variable = t (lo más fácil)
  - Hipérbola → cosh, senh (raro en este parcial)

### Ejercicios hechos
- Intersección z=2x²+3y² con z=6 (Parcial Nov 2024 P5) → x²/3+y²/2=1 → r(t)=(√3 cos t, √2 sen t, 6) ✅
- Intersección z=x²+4y² con z=4 → r(t)=(2cos t, sen t, 4) ✅ (solo)

---

## TEMARIO REAL DEL PARCIAL (VERIFICADO leyendo TODAS las clases del profe)
Parcial confirmado por el propio profe en su apunte del 21 Sep: "Parcial 1: miércoles 30 de septiembre".
Última clase: "Derivadas direccionales" (Sep 23). Contenido cubierto hasta ahí:
- ✅ CAE SEGURO: T1 (límites/continuidad/dominio), T2 (parciales/Jacobiana), T3 (regla cadena D(F∘G)=DF·DG), T4 (deriv direccional POR DEFINICIÓN + gradiente ∇f·v), T5 (plano tangente/diferenciabilidad).
- ✅ PUEDE CAER (versión ligera): T7 (parametrizar intersección — salió en Nov 2024 P5); T6 rotación de ejes SOLO identificar cónica (salió en Mar 2021 P1); concepto de puntos críticos ∇f=0 y máx/mín/silla (visto al final de clase 23 Sep, nivel conceptual).
- ❌ NO CAE: optimización pesada (Hessiana), integrales/Green/hélices (cortes 2 y 3).

## Estilo del profe confirmado en sus clases
- Justifica diferenciabilidad diciendo: "parciales continuas pues son sumas/productos/composiciones de funciones continuas".
- Pide hacer los ejercicios de las DOS formas (directo Y con la regla) → usar una para verificar la otra.
- Remite al Marsden-Tromba (secciones 1.1, 2.4). Da por sabido el prerrequisito de vectores/planos.
- Gradiente ∇f apunta en la dirección de máximo crecimiento (puede preguntarlo en teoría).

## Parcial 1 Nov 2024 (el modelo) — mapa de puntos
1. Matriz parciales en (1,1,0) → T2 ✅
2. Límite existe/no + propiedades → T1 ✅
3. Derivada direccional POR DEFINICIÓN → T4 ✅
4. Dominio + continuidad en dominio → T1 ✅
5. Parametrizar intersección z=2x²+3y² con z=6 → T7 ✅
6. Parametrización plano tangente a paraboloide z=x²+y² en (1,1,2) → T5 ✅

## Preferencias del profe (recordatorio)
- "Respuesta sin justificación no vale" → siempre justificar.
- Pide usar la DEFINICIÓN formal (derivada direccional, continuidad).
- Le gusta "plantear sin resolver" (integrales/parametrizaciones).
- Tu parcial 1 se parece a Parcial I Nov 2024 y Mar 2021 (NO integrales/Green/hélices, eso es corte 2 y 3).
