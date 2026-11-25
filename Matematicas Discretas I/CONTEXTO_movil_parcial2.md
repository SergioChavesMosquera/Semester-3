# 📱 Contexto para estudiar desde el celular — Parcial 2 Discretas

> Pega este archivo (o su contenido) al inicio de una conversación con cualquier asistente para que arranque sabiendo quién eres, cómo estudias y en qué vas. Está pensado para consultarse en el móvil.

---

## Quién soy y cómo estudio
- Soy **Sergio**, Ing. de Sistemas y Computación, Universidad Nacional de Colombia (sede Bogotá), semestre 3.
- Aprendo rápido, prefiero entender el **porqué** antes que memorizar, y resuelvo mucho **de cabeza**.
- Me rinde más con **lenguaje normal y analogías** que con formalismo seco.
- Método de estudio (5 pasos): leer apunte corto → resolver el ejercicio del preparcial → resolver un ejercicio nuevo del tutor → corrección puntual del error → avanzar.
- Para parciales con cuaderno permitido: quiero el **solucionario completo paso a paso** para transcribirlo y tenerlo de consulta.
- Documento maestro del sistema: `COMO_TRABAJAMOS.md` (en la raíz del repo del semestre).

## Qué parcial estoy preparando
- **Segundo (y último) parcial de Matemáticas Discretas I** (el profe la llama "Matemática Estructural").
- Entra todo lo del **segundo preparcial** (archivo `Parciales/Pre_Segundo_Parcial_Discretas.pdf`). El parcial será un subconjunto más corto: mismos temas, menos ejercicios.
- Material en el repo `SergioChavesMosquera/Semester-3`, carpeta `Matematicas Discretas I/`.

## Temas del parcial (4 bloques)
- **A. Funciones:** composición, inyectiva/sobreyectiva/biyectiva, imagen directa f[X], imagen inversa f⁻¹[Y], propiedades X⊆f⁻¹[f[X]] y f[f⁻¹[Y]]⊆Y, V/F con demostración o contraejemplo.
- **B. Inducción matemática:** sumas, desigualdades, divisibilidad. Dominar la estructura base + paso inductivo.
- **C. Relaciones de equivalencia:** contar relaciones/particiones, demostrar reflexiva+simétrica+transitiva, clases de equivalencia, conjunto cociente X/E, representantes.
- **D. Grafos:** isomorfismo y no-isomorfismo (invariantes: grados, # aristas, adyacencias), contar grafos no isomorfos, distancia/diámetro, desigualdad triangular, algoritmo de Dijkstra (camino más corto).

## Reglas clave que ya aprendí (para no repetir errores)
- En V/F: si es **verdadero** → demostración formal ("sea x..."); si es **falso** → **contraejemplo concreto**.
- "Para todo" → necesita argumento general. "Existe" → basta UN ejemplo. Un ejemplo solo prueba falsedad (contraejemplo), no verdad universal.
- Par de propiedades espejo: **X ⊆ f⁻¹[f[X]]** con igualdad ⟺ f **inyectiva**; **f[f⁻¹[Y]] ⊆ Y** con igualdad ⟺ f **sobreyectiva**.
- Grafos: cuando las secuencias de grados coinciden, buscar un invariante de adyacencia más fino.
- Dijkstra: cerrar siempre el de menor costo; relajar vecinos (costo+peso < actual ⟹ actualizar); guardar predecesor para reconstruir el camino.

## Estado de los puntos del preparcial (al día de hoy)
- ✅ Punto 1a (composición sobreyectiva con una no sobre) — resuelto
- ✅ Punto 2a (X ⊆ f⁻¹[f[X]], igualdad ⟺ inyectiva) + gemelo con Y — resuelto
- ✅ Punto 8 (grafos no isomorfos: invariante = adyacencia entre los dos vértices de grado 4) — resuelto
- ✅ Punto 10 (desigualdad triangular de distancias) — resuelto
- ✅ Punto 11 (diám(G)>3 ⟹ diám(Gᶜ)<3; clave: camino v–x–y–u de longitud 3) — resuelto
- 🟡 Punto 12 (Dijkstra) — método aprendido; falta leer bien los pesos del grafo y llenar la tabla
- ⏳ Pendientes: punto 3 (V/F sobre imágenes), punto 4 (contar relaciones de equivalencia), punto 5 (E_f equivalencia + biyección con Y), punto 6 (relación sobre ℝ²∖{0}), punto 7 (inducción, 15 incisos), punto 9 (once grafos no isomorfos con 4 vértices)

## Dónde está cada cosa en el repo
- Apuntes: `Matematicas Discretas I/Apuntes Completos/0X_*.md`
- Soluciones paso a paso del parcial 1: `SOLUCIONES_Preparcial.md`
- Cheatsheets: `CHEATSHEET_parcial.md` (lógica/conjuntos/relaciones), `CHEATSHEET_grafos_quiz.md`
- Progreso y bitácora de errores: `progreso_repaso_parcial.md`
- Preparcial 2: `Parciales/Pre_Segundo_Parcial_Discretas.pdf`
