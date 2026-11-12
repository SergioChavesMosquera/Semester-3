# Progreso Repaso PARCIAL 2 — Cálculo en Varias Variables

**Estudiante:** Sergio · **Profe:** Leonardo A. Cano G. · **Examen:** ✅ CONFIRMADO miércoles 18 nov 2026.
**Método:** ejemplo corto → resuelvo solo → corrección puntual → ejercicio de parcial real.
**Presupuesto:** ~17.5h en 7 días (10-17 nov), ~2.5h/día.

## TEMARIO OFICIAL (del tablón del profe, 10 nov)
1. Optimización: 1.1 Hessiano/clasificar · 1.2 región cerrada y acotada · 1.3 Lagrange
2. Integración múltiple: 2.1 def. Riemann (dobles y triples) · 2.2 iteradas (Cavalieri, Fubini, cambiar orden) · 2.3 cambio de variable (polares 2D, cilíndricas/esféricas 3D) · 2.4 aplicaciones (área, volumen, masa, centro de masa)

## PLAN DE REMONTADA (meta: 5.0; venimos de 2.7 en P1)
| Día | Tema | Horas |
|-----|------|-------|
| Mar 11 | 1. Optimización (cerrar región cerrada + repaso Hessiano/Lagrange) | 2h |
| Mié 12 | 2. Integrales dobles (Riemann, Fubini, tipo I/II, cambiar orden) | 2.5h |
| Jue 13 | 3. Cambio de variable 2D (Jacobiano, polares, trapecio) | 2.5h |
| Vie 14 | 4. Integrales triples + coordenadas 3D (cilíndricas, esféricas) | 3h |
| Sáb 15 | 5. Centro de masa (lámina + sólido) — TEMA NUEVO, por crear apunte | 2.5h |
| Dom 16 | 6. Simulacro con taller del profe + repaso flojos | 3h |
| Lun 17 | Repaso final cheatsheet + ejercicios difíciles | 2h |

> **Taller oficial del profe** `TallerParcial2CalcVectorial.pdf` (12 ejercicios) = mapa exacto del parcial. Ej 1-4 optimización, 5-7 dobles, 8-10 cambio de variable, 11-12 centro de masa.
> **PENDIENTE:** crear apunte de centro de masa (sin PDF del profe, usar Stewart 15.5/15.6).

---

## Estado por tema

| Tema | Estado | Bloque |
|------|--------|--------|
| A. Optimización libre (puntos críticos + Hessiano) | ⏳ Pendiente | 1 |
| B. Optimización restringida (Lagrange + sustitución) | ⏳ Pendiente | 2 |
| C. Máx/mín absolutos en región cerrada | ⏳ Pendiente | 2 |
| D. Integrales dobles (rectángulos + tipo I/II) | ⏳ Pendiente | 3 |
| E. Integrales triples (plantear, cambiar orden) | ⏳ Pendiente | 4 |
| F. Coordenadas cilíndricas/esféricas (plantear) | ⏳ Pendiente | 4 |
| G. Cambio de variable / Jacobiano | ⏳ Pendiente | 4 |
| Simulacro cronometrado + cheatsheet | ⏳ Pendiente | 5 |

Leyenda: ✅ completado · 🟡 a medias/afinar · ⏳ pendiente · ❌ no cae

---

## Plan de bloques (~10h)

| # | Contenido | Horas | Apunte | Material |
|---|-----------|-------|--------|----------|
| 1 | **Optimización libre** — ∇f=0 → puntos críticos; Hessiano H; criterio del determinante (máx/mín/silla) | 2h | `06_Optimizacion_Hessiano.md` | ✅ listo |
| 2 | **Optimización restringida** — Lagrange (∇f=λ∇g), sustitución, + máx/mín absolutos en región cerrada (interior+frontera) | 2h | `07_Lagrange_y_Optimizacion_Restringida.md` | ✅ listo |
| 3 | **Integrales dobles** — sobre rectángulos (Fubini), tipo I y II, cambiar orden de integración | 2h | `08_Integrales_Dobles.md` | ✅ listo |
| 4 | **Triples + coordenadas + Jacobiano** — triples (plantear/orden), cilíndricas, esféricas, cambio de variable | 2h | `09_Integrales_Triples_Coordenadas_Jacobiano.md` | ✅ listo |
| 5 | **Remate** — simulacro cronometrado tipo parcial + repaso `CHEATSHEET_PARCIAL2.md` | 2h | `SIMULACRO_PARCIAL2.md` | ✅ listo |

> **Material 100% creado (29 oct).** Apuntes, cheatsheet y simulacro escritos con la notación y ejemplos del profe. PDFs convertidos a PNG en `_paginas/`.
>
> **Actualización 4 nov:** el profe dio **polares + cambio de variable (Jacobiano)** (PDF "28Octubre..."). Confirma que el apunte 09 está alineado. Falta solo triples y cilíndricas/esféricas (probable si el parcial es 16-18 nov). Fecha del parcial aún sin confirmar. Hoy arranca el estudio activo por el Bloque 1.

### Sugerencia de calendario (ajustable)
- **Mar 4** (día más libre, ~7.5h): bloques 1 + 2 + empezar 3.
- **Jue 6 / Vie 7**: bloque 3 y 4.
- **Sáb 8 / Dom 9**: bloque 5 (simulacro) + afinar lo flojo.
- Lun/Mié: repaso ligero del cheatsheet.

---

## Bitácora de errores corregidos
_(se va llenando a medida que estudiamos)_

---

## Recordatorios del estilo del profe
- Justificar SIEMPRE (respuesta sin justificación = 0).
- Le gusta "plantear sin resolver" integrales → practicar dar límites correctos.
- Pide dos métodos (Lagrange Y sustitución) para verificar.
- Hessiano motivado desde cuádricas.
