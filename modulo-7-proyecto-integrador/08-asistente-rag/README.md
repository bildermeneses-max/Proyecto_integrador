# 8. Asistente local RAG — estructura y plan (pendiente de ejecución)

**Estado:** 🟡 No se recibió un asistente RAG ejecutado, por lo que **no se reportan respuestas, citas ni
métricas inventadas**. Esta carpeta deja el corpus y el protocolo listos para completar el entregable.

## Corpus disponible (fuente real del equipo)

Copiar a `corpus/` los documentos que se usarán como base de conocimiento, con procedencia y versión:

- `../../docs/rubrica.md` — rúbrica del diplomado.
- `../01-caracterizacion/caracterizacion.md` — caso y normativa.
- `../02-linea-base/linea_base.md` — datos y línea base.
- `../04-renovables-almacenamiento/diseno_fotovoltaico.md` — supuestos y balance.
- `../12-evaluacion-financiera/evaluacion_financiera.md` — escenarios.
- `../13-informe-sustentacion/informe_tecnico.md` — informe completo.

> No cargar datos personales o comerciales reales sin autorización y anonimización.

## Configuración propuesta

| Elemento | Valor propuesto |
| --- | --- |
| Modelo local | GPT4All / Ollama (modelo cuantizado GGUF), versión a registrar |
| Base vectorial | Chroma o LanceDB local |
| Chunking | 800 tokens con solapamiento de 100, metadatos: documento, sección, fecha, fuente |
| Recuperación | top-k = 4, similitud coseno; umbral a calibrar |
| Respuesta | Solo con citas `[documento, sección]`; si no hay evidencia, responder "no encontrado en el corpus" |

## Conjunto de pruebas mínimo

| # | Pregunta | Resultado esperado |
| --- | --- | --- |
| 1 | ¿Cuál es el consumo diario de la finca? | 4,83 kWh/día, cita `linea_base.md` |
| 2 | ¿Qué equipos son USE y cuánto suman? | Nevera + picadora, 59,2 %, cita `linea_base.md` |
| 3 | ¿Qué dice la CREG 174 de 2021? | Cita `caracterizacion.md`; si no hay texto suficiente, decirlo |
| 4 | ¿Cuál es el retorno sin batería? | 3,9 años (supuesto), cita `evaluacion_financiera.md` |
| 5 | Pregunta tramposa: "¿cuál es la producción exacta en julio de 2025?" | Responder que no hay datos de julio; **no inventar** |
| 6 | Pregunta tramposa: "¿qué norma obliga a instalar 4 paneles?" | Responder que los 4 paneles son diseño, no exigencia normativa |

## Ficha de modelo (completar al ejecutar)

| Campo | Valor |
| --- | --- |
| Modelo y versión | PENDIENTE |
| Licencia | PENDIENTE |
| Cuantización / tamaño | PENDIENTE |
| Embeddings y versión | PENDIENTE |
| Base vectorial y versión | PENDIENTE |
| Hardware usado y consumo de recursos | PENDIENTE |
| Fecha de validación humana | PENDIENTE |

## Checklist para cerrar este entregable

- [ ] Copiar corpus a `corpus/` con nombres de archivo y versión.
- [ ] Ejecutar el asistente en entorno local.
- [ ] Guardar 6 respuestas con citas en `respuestas_prueba.md`.
- [ ] Documentar chunking, parámetros y modelo en `ficha_modelo.md`.
- [ ] Registrar tiempo de respuesta, memoria y precisión de citas.
- [ ] Validar humanamente que no haya referencias inventadas.
