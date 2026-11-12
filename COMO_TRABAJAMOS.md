# 📚 Cómo trabajamos — Sistema de estudio de Sergio

> Este documento describe el método completo con el que preparamos los parciales. Sirve de guía para replicarlo en cualquier materia del semestre. Si abro una sesión nueva, con leer este archivo entiendo todo el sistema.

---

## 1. Quién es quién

- **Sergio** — estudiante de Ingeniería de Sistemas y Computación, Universidad Nacional de Colombia (sede Bogotá). Semestre 3.
- **El asistente (Kiro)** — tutor que organiza el material, crea apuntes, resuelve ejemplos, pone ejercicios, lleva el progreso y hace los commits.

### Perfil de aprendizaje de Sergio
- Aprende rápido y suele "remontar" materias 1-2 días antes del parcial.
- Prefiere entender el **porqué** sobre memorizar.
- Resuelve mucho **de cabeza**; no le gusta copiar teoría pasiva.
- Rinde mejor con explicaciones en lenguaje normal / analogías de la vida real antes que con formalismo seco.

---

## 2. Estructura de carpetas (igual en TODAS las materias)

Cada materia replica exactamente esta estructura. Referencia: `Cálculo en Varias Variables` y `Matematicas Discretas I`.

```
<Nombre de la Materia>/
├── Apuntes Completos/          # Apuntes por tema, numerados (01_, 02_, ...), en Markdown
│   ├── 01_<Tema>.md
│   ├── 02_<Tema>.md
│   └── ...
├── Libro/                      # Libro(s) de referencia en PDF
│   └── Capitulos sueltos/      # Capítulos individuales si los hay
├── Parciales/                  # Parciales anteriores, preparciales (PDF o imágenes)
├── PDFs Clases (originales)/   # PDFs de las clases del profe (anotados)
├── Talleres/                   # Talleres y sus soluciones
├── _paginas/                   # PDFs convertidos a PNG (una subcarpeta por clase)
│   └── <fecha_tema>/
│       └── *.png
├── _convert_pdf.py             # Script para convertir PDF → PNG (ver sección 6)
├── contextoClaude_estudio_<materia>.md   # Contexto general del curso y del parcial
├── CHEATSHEET_parcial.md       # Resumen ultra-condensado para repaso final
├── progreso_repaso_parcial.md  # Estado por tema + bitácora de errores + plan
├── SOLUCIONES_<preparcial/parcial>.md    # Soluciones resueltas paso a paso
└── SIMULACRO_tipo_Parcial.md   # Ejercicios nuevos tipo parcial, con soluciones al final
```

### Qué va en cada archivo clave
- **contextoClaude_estudio_*.md** — datos del profe, fecha del examen, temario completo, estilo del profe, lo que cae y lo que no.
- **CHEATSHEET_parcial.md** — todo lo esencial en 1-2 páginas: fórmulas, trampas, errores frecuentes. Es lo que se lee minutos antes del examen (y en el teléfono).
- **progreso_repaso_parcial.md** — tabla de estado por tema (✅/🟡/⏳), checklist de bloques, bitácora de errores corregidos, y el plan de horas.
- **SOLUCIONES_*.md** — el preparcial/parcial real resuelto completo con justificación formal.
- **SIMULACRO_*.md** — ejercicios NUEVOS (variantes) para practicar en frío. Enunciados arriba, soluciones al final (para no tentarse).

### Convención de nombres
- Apuntes numerados con dos dígitos: `01_`, `02_`, ...
- Prefijo `_` para archivos de trabajo interno (`_paginas`, `_convert_pdf.py`).
- Nombres de clases/PDFs mantienen la fecha del profe (ej: `07Sep_Est.pdf`).

---

## 3. Cómo me cuenta Sergio lo que necesita

- Me dice la materia, la fecha del parcial, y qué material ya tiene en la carpeta.
- Me pasa el **preparcial** o parciales anteriores (los convierto a imágenes y los leo).
- Me cuenta cuántas **horas libres** tiene y en qué días/bloques.
- A veces es informal ("el profe la llama X pero es lo mismo") — yo lo tomo en cuenta y no me enredo.
- Puede mandar fotos de clases, tableros, enunciados — los leo y los incorporo.

---

## 4. Cómo definimos deadlines y horario

1. **Deadline = fecha del parcial.** Sergio me la da (ej: "el parcial es mañana", "en 5 días").
2. Yo **estimo las horas totales** necesarias según la dificultad del material y comparando con materias previas (ej: Cálculo necesitó ~20h; Discretas ~5h por ser más fácil).
3. Sergio me dice sus **bloques de tiempo libre** reales (ej: "4 horas hoy + 2 mañana").
4. **Distribuimos** el temario en esos bloques, priorizando lo que más cae en el parcial (🔴 alta / 🟡 media / 🟢 baja).
5. El plan queda escrito en `progreso_repaso_parcial.md` como tabla de bloques + checklist.

> Regla: siempre planear como si el parcial fuera **individual**, aunque pueda ser en parejas. Si cae en parejas, es un bono.

---

## 5. Cómo planeamos y estudiamos cada examen

### El método de 5 pasos (el que funciona)
Para cada tema:
1. **Leo** el apunte corto del tema (lenguaje claro, con analogías).
2. **Resuelvo el ejercicio del preparcial** de ese tema (si lo hay).
3. **Resuelvo un ejercicio que el tutor me pone** (una variante).
4. **El tutor me corrige el error puntual** (no repite teoría, solo señala el fallo).
5. **Avanzo** al siguiente tema.

### Variante que Sergio pidió y funciona
> "Antes de ponerme un ejercicio: muéstrame 1-2 ejemplos resueltos paso a paso (según cuántos sabores del tema haya en el preparcial), los leo, con eso resuelvo el del preparcial y después el que me das."

### Reglas del tutor al enseñar
- Un ejemplo resuelto breve primero; Sergio no copia todo, solo lo lee.
- Explicar con lenguaje normal / vida real antes que con símbolos.
- Corrección puntual del error específico, sin sermón de teoría.
- Cerrar cada tema con una **"idea clave"** de 1-2 líneas.
- Registrar cada error en la **bitácora** de `progreso_repaso_parcial.md`.
- Marcar progreso (✅/🟡/⏳) a medida que se cierra cada bloque.
- Ser honesto: si algo quedó a medias o un razonamiento está mal, decirlo (no dar falso "vas perfecto").

### Fases típicas de preparación
1. **Setup** — organizar carpeta, convertir PDFs, leer preparcial, crear apuntes + contexto + cheatsheet + progreso.
2. **Estimación** — calcular horas y distribuir en los bloques libres.
3. **Estudio por bloques** — tema por tema con el método de 5 pasos.
4. **Remate** — pulir redacción formal + simulacro cronometrado + repaso del cheatsheet.
5. **Commit** — subir todo a GitHub para tenerlo en el teléfono.

---

## 6. Herramientas y flujo técnico

### Conversión de PDF a imágenes
Los PDFs de clases/parciales se convierten a PNG para poder leerlos. Script: `_convert_pdf.py` (usa PyMuPDF).

```powershell
python "_convert_pdf.py" "PDFs Clases (originales)\<archivo>.pdf" "_paginas\<carpeta_destino>"
```

### Control de versiones (Git)
- El semestre completo es un repo Git (`main`), remoto en GitHub.
- Al terminar una sesión de estudio, se hace **commit + push** para sincronizar con el teléfono.
- **Regla:** commitear solo los archivos de la materia trabajada (no mezclar cambios sueltos de otras materias). Staging por carpeta: `git add "<Materia>/"`.
- Mensajes de commit descriptivos en español.

---

## 7. Estado actual del semestre

| Materia | Estado parcial |
|---------|----------------|
| Cálculo en Varias Variables | ✅ Parcial 1 presentado (nota 4.6) |
| Matemáticas Discretas I | 🟡 Parcial 1 en preparación (hoy) — Lógica, Conjuntos, Relaciones |
| Elementos de Computadores | — |
| Fundamentos de Electricidad y Magnetismo | — |

---

## 8. Resumen en una línea

> Organizo la carpeta igual en toda materia → leo el preparcial → creo apuntes/cheatsheet/soluciones → estimo horas y las reparto en los bloques libres de Sergio → estudiamos tema por tema con ejemplos resueltos + ejercicios + corrección puntual → rematamos con simulacro → commit a GitHub para el teléfono.
