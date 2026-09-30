# 📱 REPASO FINAL — Parcial Cálculo (miércoles 16:00) · Prof. Cano

> Leer esto en el bus / Discretas / almuerzo. Es tu resumen para el celular.
> Escala 0-5. Son ~6 puntos. JUSTIFICA TODO ("respuesta sin justificación no vale").

---

## ⭐ LOS 5 REMATES QUE ME CUESTAN (aquí pierdo puntos fáciles)

1. **Límite que existe (=0) → CERRAR el sándwich.**
   Factorizo el |x| o |y|, el resto lo acoto por 1, y eso → 0:
   `xy²/(x²+y²) = |x|·[y²/(x²+y²)] ≤ |x|·1 = |x| → 0`
   `x²y/(x²+y²) = |y|·[x²/(x²+y²)] ≤ |y| → 0`

2. **Plano tangente SIEMPRE termina en la ECUACIÓN, no en la normal.**
   Después de sacar la normal (gradiente): `A(x−x₀)+B(y−y₀)+C(z−z₀)=0`, distribuir y ordenar.

3. **Dominio → decir "f es continua en TODO su dominio"** (una línea, punto gratis).

4. **Parametrización → escribir el rango `t ∈ [0, 2π]`.**

5. **Derivada direccional → hacer las 2 formas (definición + gradiente) y verificar.**

---

## 🚨 NO CONFUNDIR MÉTODOS (esto me pasó)

- **"Parametrizar intersección"** = igualar superficie y plano → sacar cónica → cos/sen. NO es gradiente.
- **"Plano tangente"** = gradiente = normal → ecuación del plano. NO es parametrizar.

---

## 📐 MINI-FORMULARIO POR TEMA

### Derivadas parciales / Jacobiana
- Derivar respecto a una variable, las demás CONSTANTES.
- Jacobiana: filas=salidas, columnas=variables. Tamaño (salidas)×(entradas).
- Constante que SUMA → 0. Constante que MULTIPLICA → se queda.
- e⁰=1, sen(0)=0, cos(0)=1. Cadena en eˣᶻ: ×derivada del exponente.

### Límites
- NO existe: 2 caminos distintos (ejes (t,0),(0,t); y=mx; y=x²).
- Polares x=r cosθ, y=r senθ: si depende de θ → NO existe.
- Existe (=0): sándwich (ver remate 1).

### Regla de la cadena
- D(F∘G)=DF·DG (afuera primero). Evaluar DF en G(t).
- Matrices: fila×columna, cada casilla SUMA de productos.

### Derivada direccional (Cano NO normaliza, v directo)
- Definición: D_v f(p)=lim_{h→0}[f(p+hv)−f(p)]/h
- Gradiente: D_v f(p)=∇f(p)·v
- Dividir por h término a término (cada uno pierde 1 h). NO homogenizar.
- ⚠️ Menos delante de paréntesis → repartir a TODOS. −(1+4h)= −1−4h.
- ⚠️ −2(a)(b): multiplico los binomios PRIMERO, reparto el −2 DESPUÉS.

### Plano tangente (método gradiente, el rápido)
- Superficie z=g(x,y) → f = g−z = 0. O si ya es f(x,y,z)=c, úsala.
- ∇f evaluado = NORMAL → A(x−x₀)+B(y−y₀)+C(z−z₀)=0.
- Ej: z=x²+y² en (1,2,5): ∇f=(2x,2y,−1)→(2,4,−1) → 2x+4y−z=5.
- VERIFICAR: meter el punto en la ecuación.

### Diferenciabilidad
- Diferenciable ⟺ tiene plano tangente. Parciales existen Y continuas ⟹ diferenciable.
- Justificar: "parciales son sumas/productos/composiciones de continuas → continuas".
- Recíproco NO vale.

### Dominio + continuidad
- Quitar: ÷0, raíz par de negativo (pide ≥0), log de ≤0 (pide >0 estricto).
- Vectorial: INTERSECCIÓN de dominios de cada componente.
- Interpretar: disco x²+y²≤r² / semiplano y>−x / etc. (≤ borde sí, < borde no).

### Parametrizar intersección (superficie ∩ z=k)
- Igualar → cónica. Círculo x²+y²=r² → (r cos t, r sen t, k), t∈[0,2π].
- Elipse x²/a²+y²/b²=1 → (a cos t, b sen t, k).

### 🌟 Gradiente (teoría que Cano puede preguntar — clase 28 sep)
- ∇f apunta a la dirección de MÁXIMO CRECIMIENTO.
- ∇f es PERPENDICULAR a las curvas/superficies de nivel.
  (Prueba: f(α(t))=c → ∇f·α'=0 → perpendiculares.)
- Puntos críticos: máx/mín → ∇f=0.

---

## ✅ CHECKLIST MENTAL DURANTE EL PARCIAL
- [ ] ¿Justifiqué cada paso? (sin justificación = 0)
- [ ] Derivada direccional: ¿hice las 2 formas y coinciden?
- [ ] Límite que da 0: ¿cerré el sándwich?
- [ ] Plano tangente: ¿escribí la ECUACIÓN final (no solo la normal)?
- [ ] Plano tangente: ¿verifiqué metiendo el punto?
- [ ] Dominio: ¿dije "continua en su dominio" + dibujo?
- [ ] Parametrización: ¿puse t∈[0,2π]?
- [ ] ¿Repartí bien los signos (menos delante de paréntesis)?

---

## 💪 RECORDATORIO
- Los 2 simulacros: 7.2/10 (con apuntes) y 3.3/5 (solo). AMBOS APROBADOS.
- Mis errores son de REMATE, no de concepto. Si cierro bien → ~5.0.
- Temas fuertes: parciales/Jacobiana y derivada direccional (perfectos siempre).
- Respira, lee el enunciado 2 veces, identifica QUÉ método pide. Tú puedes.
