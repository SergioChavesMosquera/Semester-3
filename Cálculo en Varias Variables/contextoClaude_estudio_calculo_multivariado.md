# Contexto: Preparación Parcial 1 - Cálculo en Varias Variables

## Datos generales
- **Estudiante:** Sergio, estudiante de Ingeniería de Sistemas y Computación, Universidad Nacional de Colombia (Sede Bogotá)
- **Profesor:** Leonardo A. Cano G.
- **Fecha del examen:** Miércoles 30 (hoy es 23, quedan 7 días)
- **Nivel de partida:** Sin base previa ("no sé nada de nada")
- **Preferencia de método:** NO copiar teoría pasiva. Aprender por resolución activa: ejemplo resuelto corto → el estudiante resuelve solo → se corrige el error puntual → se cierra con ejercicios de parciales reales.

## Estilo pedagógico que está funcionando
1. Un ejemplo resuelto breve (se lee, no se copia completo)
2. El estudiante resuelve un ejercicio similar sin ayuda
3. Corrección puntual del error específico (no repetir teoría)
4. Cierre con ejercicios de parciales reales del profesor
5. El estudiante solo copia en el cuaderno: el ejercicio, su intento, la versión corregida por él mismo, y una "idea clave" de 1-2 líneas en sus propias palabras.

## Cronograma de estudio (horas disponibles)
| Día | Horario | Tema(s) |
|---|---|---|
| Jue 24 | 14:00-19:00 | Tema 1: Dominio, límites, continuidad + Tema 2: Derivadas parciales y Jacobiana |
| Vie 25 | 18:00-20:00 | Tema 3: Regla de la cadena |
| Sáb 26 | 14:00-19:00 | Tema 4: Derivada direccional + gradiente / Tema 5: Plano tangente (inicio) |
| Dom 27 | Todo el día | Tema 5 (cierre) + Tema 6: Rotación de ejes/cónicas + Tema 7: Parametrización de superficies + Tema 8: Optimización básica |
| Lun 28 | Sin estudio | — |
| Mar 29 | 14:00-19:00 | Simulacro completo con los 4 parciales reales, cronometrado |

## Temario completo (8 temas, basado en parciales anteriores del profesor)
1. **Dominio, límites y continuidad**
2. **Derivadas parciales y matriz Jacobiana**
3. Regla de la cadena (multivariable)
4. Derivada direccional y vector gradiente
5. Plano tangente y diferenciabilidad
6. Rotación de ejes / cónicas
7. Parametrización de superficies e intersecciones
8. Optimización básica (puntos críticos, máx/mín)

---

## Preferencias y estilo del profesor (observado en parciales anteriores)
- **Exige justificación completa** — "Respuesta sin justificación no tendrá ningún valor" aparece en todos los parciales.
- Pide con frecuencia **usar la definición formal** (ej. "usando la definición de derivada direccional", "usando la definición de continuidad") en vez de solo aplicar fórmulas mecánicas.
- Le gusta pedir **plantear integrales/parametrizaciones sin resolverlas** ("no necesita calcular, solo enunciar/plantear").
- Reutiliza estructuras de examen a examen: límites por trayectorias, matriz derivada + regla de la cadena combinadas, plano tangente a superficies parametrizadas, cambio de variable en integrales dobles con elipses.
- Los parciales tienen 5-6 puntos de 10 puntos cada uno.
- Fechas de parciales anteriores revisados: Nov 2024 (Parcial 1), Mar 2021 (Parcial 1), Jul 2021 (Parcial 2), Feb 2025 (Parcial 3), Ene 2025 (Parcial 2 - de otro tema, integrales múltiples).

---

## TEMA 1: Dominio, límites y continuidad — ✅ COMPLETADO

### Idea clave 1 (límites por trayectorias)
Para **descartar** que un límite existe: basta encontrar 2 trayectorias con resultados distintos.
Para **confirmar** que existe (usualmente 0): probar 3-4 trayectorias, si todas dan lo mismo, sospechar y confirmar con acotamiento (teorema del sándwich).

### Idea clave 2 (acotamiento)
Ejemplo tipo: $\frac{x^2y}{x^2+y^2}$. Se separa en $\frac{x^2}{x^2+y^2}\cdot|y|$. Como $\frac{x^2}{x^2+y^2}\leq1$ (numerador es "parte" del denominador), queda $\leq|y|\to0$. Por sándwich, límite = 0.

**Error recurrente detectado:** intentar acotar con una cota falsa cuando ya hay trayectorias con resultados distintos (ej. $\frac{y^2}{x^2+y^4}\leq1$ es falso). Regla aprendida: **si ya hay 2 trayectorias con resultados distintos, no tiene sentido ni es válido acotar — ya se descartó el límite.**

**Error recurrente 2:** confundir un resultado que queda en función de una variable (ej. "$=y$", que SÍ tiende a 0 porque $y\to0$) con un resultado numérico fijo sin variables (ej. "$=1/2$", que es el límite real de ese camino, constante).

**Error recurrente 3 (álgebra):** combinar mal términos no semejantes al simplificar fracciones, ej. tratar $y^2+y^4$ como si fuera $2y^2$.

### Idea clave 3 (dominio)
Dominio = todo el plano/espacio MENOS donde la función se rompe (÷0, raíz de negativo, log de ≤0). Ojo con el uso correcto de $\leq$ vs $<$ (si el valor límite sí está permitido, como raíz de 0, se incluye el borde).

### Ejercicios resueltos y corregidos hoy (Tema 1)
1. Continuidad de $f(x,y)=xy/(2x^2+y^2)$ en (0,0) — ejemplo guía, no continua.
2. $\lim_{(x,y,z)\to(0,0,0)} z^3/(xy)$ — no existe (caminos $z=0$ vs $x=t,y=t^2,z=t$).
3. $\lim_{(x,y)\to(0,0)} x^2y/(x^4+y^2)$ — ejemplo guía, no existe (con $y=x^2$).
4. $\lim_{(x,y)\to(0,0)} xy^2/(x^2+y^4)$ — resuelto por el estudiante, no existe (0 vs 1/2), con error de factorización corregido.
5. Dominios de: $\sqrt{9-x^2-y^2}$ (corregido: era $x^2+y^2\leq9$, no $x^2-y^2<9$), $\ln(x+y-1)$ ✅, $1/(x^2+y^2-z)$ ✅.
6. Continuidad de $x^2y/(x^2+y^2)$ en (0,0) — SÍ continua, con acotamiento correcto.
7. Continuidad de $xy^2/(x^2+y^4)$ en (0,0) — el estudiante concluyó mal inicialmente (dijo continua tras un acotamiento inválido), se corrigió: NO es continua (mismo resultado que ejercicio 4, dos trayectorias ya bastan).
8. Continuidad de $(x^3+y^3)/(x^2+y^2)$ en (0,0) — resuelto correctamente por el estudiante solo: SÍ es continua, con acotamiento completo y válido ($\leq |x|+|y|\to0$).

### Hoja de resumen final del estudiante (Tema 1)
```
1. Para NO EXISTE: busco 2 caminos con resultados distintos (basta 1 par)
2. Para SÍ EXISTE (=0): pruebo 3-4 caminos, si todos dan 0, sospecho
   → confirmo con acotamiento: separo, acoto cada factor ≤1,
     me queda ≤ |x| o |y|, que tiende a 0 → sándwich → límite=0
3. Continuidad = límite existe Y coincide con f(punto)
4. Dominio = todo el plano/espacio MENOS donde se rompe
   (÷0, raíz de negativo, log de ≤0)
```

---

## TEMA 2: Derivadas parciales y matriz Jacobiana — 🔶 EN PROGRESO

### Estado actual
- Se intentó explicar directamente con matriz Jacobiana (funciones $\mathbb{R}^2\to\mathbb{R}^3$) — **el estudiante se perdió, faltaba base de derivadas parciales simples**.
- Se retrocedió a explicar desde cero qué es una función vectorial (una entrada, varias salidas empaquetadas) y qué es una derivada parcial (derivar respecto a una variable tratando las demás como constantes).
- Practicó derivadas parciales simples: $x^3y^2$ → correcto ($3x^2y^2$ y $2yx^3$).
- Practicó $e^{xy}$ → correcto ambas parciales.
- Practicó $\sin(x^2y)$ → **error activo, sin corregir aún**: le faltó multiplicar por la derivada interna completa (regla de la cadena incompleta). Puso $\cos(x^2y)\cdot 2x$ en vez de $\cos(x^2y)\cdot 2xy$, y $\cos(x^2y)$ en vez de $\cos(x^2y)\cdot x^2$.

### 🔴 Próximo paso inmediato (retomar aquí)
1. Corregir el error de $\sin(x^2y)$ — reforzar regla de la cadena en derivadas parciales (derivar función compuesta × derivada completa de "adentro" respecto a la variable correspondiente).
2. Dar 1-2 ejercicios más de derivadas parciales con funciones compuestas (producto, cociente, cadena) hasta consolidar.
3. Recién ahí retomar el concepto de matriz Jacobiana (ya se explicó una vez de forma simple: filas = funciones de salida, columnas = variables de entrada, cada casilla es una derivada parcial) con un ejemplo bien desglosado.
4. Ejercicio pendiente de reintentar: $g(x,y)=(x^2y,\ 3x+y^2)$ → armar $Dg$.
5. Cerrar con ejercicios reales del profe: Parcial I (2021) punto 1 (matriz de derivadas parciales en un punto) y punto 3 (matriz derivada + regla de la cadena combinada — esto conecta con Tema 3).

---

## Temas pendientes (aún no iniciados)
- **Tema 3:** Regla de la cadena multivariable (aparece en Parcial I 2021 combinada con matriz derivada — clave revisar bien Tema 2 primero).
- **Tema 4:** Derivada direccional y gradiente (el profe pide a veces "usando la definición", no solo la fórmula del gradiente — ver Parcial I 2021 punto 3).
- **Tema 5:** Plano tangente y diferenciabilidad (aparece con superficies parametrizadas, ej. Parcial I 2021 punto 2 y Parcial I 2025 punto 5).
- **Tema 6:** Rotación de ejes / cónicas (Parcial I 2021 punto 1).
- **Tema 7:** Parametrización de superficies e intersecciones (Parcial I 2025 puntos 5-6, Parcial 3 2025 puntos 1-3).
- **Tema 8:** Optimización básica — puntos críticos, máx/mín con restricciones (Parcial 2 2025 puntos 4-6, aunque es de otro corte, el profe puede repetir estilo).

## Objetivo final
Llegar al martes 29 con los 8 temas cubiertos al menos una vez, para dedicar el bloque de 14:00-19:00 de ese día a un **simulacro completo cronometrado** usando los parciales reales ya recopilados (Parcial I Nov 2024, Parcial I Mar 2021, Parcial II Jul 2021, Parcial 3 Feb 2025), y llegar al examen del miércoles 30 con soltura en justificación formal (el profesor no da puntos sin justificación) y dominio de los tipos de ejercicio que se repiten examen tras examen.
