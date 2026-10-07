# Progreso Repaso Parcial 1 — Matemáticas Discretas I (Matemática Estructural)

**Estudiante:** Sergio · **Examen:** Mañana (martes 7 oct) · **Hoy:** casi todo el día libre
**Método:** ejemplo corto → resuelvo solo → corrección del error puntual → ejercicio tipo parcial.

---

## Estado por tema

| Tema | Estado | Prioridad |
|------|--------|-----------|
| 1. Lógica proposicional (tablas, tautologías) | ✅ Completado (tablas, contrapositiva, prueba por casos) | 🔴 Alta (cae seguro) |
| 2. Conjuntos básicos (⊆, =, 𝒫) | ✅ Completado (∈ vs ⊆, 𝒫 anidado, conversión mágica) | 🔴 Alta |
| 3. Operaciones (∪, ∩, \, ᶜ) + demos | ✅ Completado (V/F 2 y 3 resueltos solo; falta solo pulir redacción formal mañana) | 🔴 Alta |
| 4. Conjunto potencia (trampas ∈ vs ⊆) | ✅ Completado (resolvió 2a=F y 2b=V del preparcial solo) | 🔴 Alta (cae en 2a/2b) |
| 5. Describir conjuntos intensionalmente | ✅ Completado (punto 3 resuelto solo: 4n+2, patrón lineal) | 🟡 Media |
| 6. Cardinalidad / generalizadas | ⏳ Pendiente | 🟢 Baja (poco probable) |
| 7. Producto cartesiano | ⏳ Pendiente | 🟢 Baja |
| 8. Relaciones y propiedades | ✅ Completado (reflexiva; resolvió R∪S y R∩S solo; entendió diferencia ∪ "una basta" vs ∩ "ambas") | 🟡 Media (cae en V/F 4) |
| Preparcial completo resuelto | ⏳ | 🔴 Clave |

---

## ⏱️ PLAN DE HOY (ver abajo la distribución según tus horas)

Marca cada tema a medida que lo cierras:
- [x] Bloque 1 — Lógica + tautología del preparcial
- [x] Bloque 2 — Conjuntos y 𝒫 (puntos 2a, 2b)
- [x] Bloque 3 — Operaciones y demostraciones (V/F 2, 3)
- [x] Bloque 4 — Relaciones (V/F 4) + describir conjunto (punto 3)
- [ ] Bloque 5 — Simulacro completo cronometrado

---

## Bitácora de errores corregidos
(Se irá llenando a medida que estudiamos)

| Tema | Error cometido | Corrección / idea clave |
|------|----------------|-------------------------|
| Lógica | Al principio no veía para qué servían ∧/∨ | ∧ = exige las dos (V solo si ambas V); ∨ = basta una (F solo si ambas F) |
| Lógica | — | Clave: F→cualquier cosa = V. Para leer tautología rápido, revisar solo filas donde el antecedente es V. |
| Potencia | Duda de cómo construir 𝒫(𝒫(A)) | Renombrar B=𝒫(A) y aplicar 𝒫 otra vez. Objetos se "hunden" una capa de llaves por cada 𝒫. |
| Potencia | — | A⊆𝒫(𝒫(A))=F (1 no es elemento directo, queda enterrado). 𝒫(A)∈𝒫(𝒫(A))=V (porque 𝒫(A)⊆𝒫(A)). Diferencia ∈ vs ⊆. |
| Operaciones | Resolvió V/F 2 solo con ejemplo A={1},B={2} → VERDADERO ✅ | OJO: ejemplo da intuición pero "para todo" exige argumento general con "sea X...". Ejemplo solo prueba FALSOS (contraejemplos). |
| Operaciones | V/F 3 (A∪B)\A=B\A resuelto de cabeza → VERDADERO ✅ | Al redactar, decir que x∈A ∧ x∉A es "contradicción" (esa palabra da el punto). |
| Relaciones | V/F 4 (R∪S reflexiva) entendido tras explicación con "ser hermano/≤" | Reflexiva = (a,a)∈R ∀a. R∪S: basta una reflexiva. R∩S: necesita ambas. Unir nunca borra parejas. |

---

## Notas rápidas
- El profe exige JUSTIFICACIÓN en todo (igual que en Cálculo).
- V/F: si es verdadero → demostración; si es falso → contraejemplo concreto.
- Trampa recurrente: ∈ vs ⊆. Siempre evaluar con un conjunto chiquito (A={1}).
