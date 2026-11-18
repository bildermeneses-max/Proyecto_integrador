# Bitácora del proyecto y declaración de uso de IA

> Registro reconstruido a partir de los entregables reales compartidos por el equipo (informe, cuadernos y
> código). Las fechas de ejecución originales deben ser confirmadas por los autores.

## Datos generales

| Campo | Valor |
| --- | --- |
| Caso de estudio | Finca agropecuaria sostenible, El Tambo (Cauca) |
| Integrantes | Andrés Felipe Rodríguez, Brandon Meneses, Valeria Velasco |
| Institución | Corporación Universitaria Comfacauca — UNICOMFACAUCA |
| Docente / asesor | PENDIENTE (figura como `[Nombre del docente]` en el informe) |
| Modalidad | Diplomado en Energía Circular Inteligente 5.0 |
| Periodo de datos | 01/01/2025 00:00 – 11/02/2025 15:00 |

## Registro semanal (reconstruido)

### Semana 1 — Selección y marco

- **Actividades:** selección del caso rural, formulación del problema y marco normativo (ISO 50001, RETIE, Ley 1715, CREG 174, UPME).
- **Evidencia:** `modulo-7-proyecto-integrador/01-caracterizacion/caracterizacion.md`; `docs/rubrica.md`.
- **Decisión:** trabajar con datos horarios reales en lugar de estimaciones de tiempo de uso.
- **Validación:** revisión interna del planteamiento (pendiente de firma del docente).

### Semana 2 — Línea base

- **Actividades:** verificación de calidad del dataset, estadística descriptiva e inventario de cargas.
- **Evidencia:** `02-linea-base/datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`; `02-linea-base/linea_base.md`.
- **Datos incorporados:** 1.000 registros horarios, 11 variables, sin nulos ni duplicados.
- **Decisión:** usar 30 días/mes para homogenizar el consumo mensual; periodo real de 41,7 días.

### Semana 3 — Usos significativos y medidas

- **Actividades:** Pareto, correlaciones, perfil horario y priorización de medidas.
- **Evidencia:** `03-medidas-eficiencia/medidas_eficiencia.md`.
- **Decisión:** clasificar nevera y picadora como USE; desplazar molienda a 10:00–14:00.

### Semana 4 — Diseño fotovoltaico

- **Actividades:** predimensionamiento, supuestos de irradiación y simulación horaria.
- **Evidencia:** `04-renovables-almacenamiento/diseno_fotovoltaico.md`.
- **Decisión:** mantener 2,2 kWp pese al excedente, por margen ante nubosidad y picos de la picadora.

### Semana 5 — Seguidor y demostrador

- **Actividades:** código de referencia Arduino Uno, dashboards Gradio y Streamlit.
- **Evidencia:** `06-iot-demostrador/`.
- **Incidente de seguridad:** el cuaderno original incluía un token de ngrok embebido. Se saneó en las copias versionadas y se usa variable de entorno. **Pendiente: revocar el token en ngrok.**

### Semana 6 — Circularidad y carbono

- **Actividades:** estimación de emisiones evitadas (0,29 t CO₂/año) y circularidad de baterías/paneles.
- **Evidencia:** `05-circularidad-carbono/circularidad_carbono.md`.

### Semana 7 — Analítica y modelo

- **Actividades:** EDA en Python y red neuronal MLP para `total_W`.
- **Evidencia:** `07-codigo-analitica/EDANUEV_sanitizado.ipynb`; `nota_modelo_red_neuronal.md`.
- **Decisión:** tratar la red neuronal como ejercicio complementario, no como pronóstico independiente, porque `total_W` es la suma de las potencias de los equipos.

### Semana 8 — Viabilidad

- **Actividades:** inversión referencial, ahorro, retorno y propuesta de autogeneración compartida.
- **Evidencia:** `11-evaluacion-financiera/evaluacion_financiera.md`; `escenarios.csv`; `12-informe-sustentacion/idea_solucion_original.docx`.

### Semana 9 — Comunicación

- **Actividades:** informe técnico, resumen ejecutivo y presentación visual de sustentación.
- **Evidencia:** `12-informe-sustentacion/` y `13-presentacion-diapositivas/`.
- **Producto visual:** `09-producto-visual/producto_visual_el_tambo.jpeg` y su ficha de procedencia.
- **Presentación:** 15 diapositivas en HTML dinámico + PDF 16:9; ocho gráficos regenerados desde el
  CSV (`generar_graficos.py`). Cifras verificadas; sin ilustraciones IA incluidas (el generador
  devolvió credencial inválida).
- **Pendiente:** modelo 3D con ficha de procedencia.

### Semana 10 — Integración

- **Actividades:** organización del repositorio y verificación de trazabilidad; incorporación del
  código local del dashboard web y documentación de su deploy público.
- **Evidencia:** este archivo, el README general y
  `modulo-7-proyecto-integrador/07-codigo-analitica/dashboard_vercel/`.
- **Deploy verificado:** `https://energia-circular.vercel.app/` responde 200 y sirve el CSV;
  `GET /api/kpis` devuelve 500 y la interfaz muestra error de carga. Estado registrado sin ocultarlo.
- **Pendiente:** corregir las funciones serverless del deploy, RAG ejecutado con pruebas,
  validación final del docente y ajustes del jurado.

## Declaración transparente de uso de IA

| Herramienta / modelo | Uso declarado | Parámetros conservados | Archivo fuente | Validación humana |
| --- | --- | --- | --- | --- |
| Asistente de IA de OpenCode | Extracción de rúbrica, armado de estructura, redacción de documentación y saneamiento de secretos | Conversación y prompts en la sesión de trabajo | Repositorio y este archivo | Revisión pendiente de los autores |
| IA asistiva / código Python | Generación y adaptación de dashboards y análisis | Versiones en `requirements.txt` | `06-iot-demostrador/`, `07-codigo-analitica/` | Ejecución pendiente en entorno local |
| Red neuronal Keras | Predicción de `total_W` en cuaderno | Arquitectura 64→32→16→1, Adam, 100 épocas, `random_state=42` | `EDANUEV_sanitizado.ipynb` | Interpretación corregida: variable objetivo es aditiva |
| Generador de ilustraciones IA | Intento de cuatro ilustraciones para la presentación | Sin parámetros conservados: la solicitud devolvió `Invalid credential` | Ninguno; no se incluyeron imágenes sintéticas | Se sustituyeron por infografía real, gráficos del CSV y un esquema SVG propio |

**Regla aplicada:** para cada producto se distingue qué fue **calculado** con datos, qué fue **generado**
con IA y qué fue **revisado** por una persona. La validación final de los autores queda registrada como
pendiente y debe completarse antes de la sustentación.

## Registro de datos

| Archivo | Origen | Periodo | Unidades | Uso |
| --- | --- | --- | --- | --- |
| `dataset_consumo_electrico_rural_ElTambo_Cauca.csv` | Medición/serie temporal compartida por el equipo | 2025-01-01 a 2025-02-11 | W y kWh por hora | Línea base, Pareto, perfil y dashboards |
| `informe_tecnico_original.docx` | Elaborado por el equipo | Noviembre 2026 | — | Informe fuente |
| `idea_solucion_original.docx` | Elaborado por el equipo | Noviembre 2026 | — | Propuesta de solución |

## Checklist de cierre

- [x] Caso, autores y periodo documentados.
- [x] Decisiones técnicas justificadas.
- [x] Incidente de token documentado y copias saneadas.
- [ ] Declaración firmada por cada integrante.
- [ ] Validación humana de IA completada.
- [x] Producto visual incorporado con ficha de procedencia.
- [ ] RAG y modelo 3D incorporados.
