# Módulo 5 — Inteligencia artificial local, datos, RAG y desarrollo de código

**Carga:** 8 h teóricas + 10 h prácticas = 18 h · **Peso en evaluación:** 15 %

## Propósito formativo

Configurar un entorno local de IA que transforme datos y documentos energéticos en análisis
reproducibles y productos verificables. **El propósito no es delegar el razonamiento al modelo**, sino
construir infraestructura que ayude a consultar, escribir, revisar y documentar.

## Contenidos clave

Modelos de lenguaje, tokenización, contexto, cuantización, inferencia CPU/GPU, formatos GGUF,
embeddings, bases vectoriales, RAG, chunking, metadatos, citas, agentes, API local, privacidad,
seguridad, licencias, alucinaciones, evaluación, consumo computacional y soberanía de datos.
Herramientas: GPT4All, AnythingLLM, Ollama, Open WebUI, LM Studio y equivalentes.

## Prácticas y laboratorios

- Instalación local de GPT4All y ejecución de modelo cuantizado en CPU o GPU.
- AnythingLLM con proveedor local y base vectorial.
- Corpus RAG con normas, política pública, manuales y datos anonimizados.
- Pruebas para detectar respuestas sin evidencia o referencias inventadas.
- Generación asistida de Python para limpieza, indicadores, pronóstico y visualización.
- API o aplicación local con Streamlit o Gradio.
- Comparación de desempeño entre equipo básico y estación RTX 3050.
- Ficha de modelo con versión, licencia, requisitos, riesgos y uso permitido.

## Herramientas sugeridas

GPT4All y su API local · AnythingLLM · Ollama, Open WebUI y LM Studio · Python, Jupyter, VS Code, Git,
Streamlit y Gradio · LanceDB, Chroma u otra base vectorial local · Prometheus si hay servidor compartido.

## Contextualización territorial

Asistentes para consulta normativa de comunidades energéticas, apoyo a auditorías, lectura de manuales
de inversores, análisis de consumos, mantenimiento de bombeo y materiales de formación. **No cargar
datos personales, comerciales o comunitarios reales sin autorización y anonimización.**

## Evidencia de aprendizaje exigida

> Asistente local RAG funcional, repositorio de código, conjunto de pruebas, ficha técnica y reporte de
> consumo de recursos.

## Aporte al proyecto integrador

Alimenta **"Sistema IoT, código y analítica" (15 %)** y **"Asistente local de IA y validación" (10 %)**.
Copiar a `../modulo-7-proyecto-integrador/07-codigo-analitica/` y `08-asistente-rag/`.

## Checklist

- [ ] Corpus documental con procedencia, versión y licencia.
- [ ] Estrategia de chunking y metadatos documentada.
- [ ] Respuestas con citas verificables al documento fuente.
- [ ] Conjunto de pruebas con casos positivos y negativos (referencias inventadas).
- [ ] Comparación con y sin RAG.
- [ ] Código versionado y ejecutable desde la raíz del repo.
- [ ] Ficha de modelo completa.
- [ ] Reporte de tiempo, memoria y consumo aproximado.
- [ ] Declaración clara: calculado / generado / validado por persona.
