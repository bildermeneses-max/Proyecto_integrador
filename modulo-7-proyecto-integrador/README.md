# Módulo 7 — Proyecto integrador de Energía Circular Inteligente 5.0

**Carga:** 20 h prácticas · **Peso global:** 25 %  
**Caso:** finca agropecuaria sostenible en El Tambo, Cauca  
**Equipo:** Andrés Felipe Rodríguez · Brandon Meneses · Valeria Velasco

## Entregables mínimos y estado real

| # | Entregable | Archivo / carpeta | Estado | Criterio rúbrica |
| ---: | --- | --- | --- | --- |
| 1 | Caracterización, actores, problema, alcance y restricciones | `01-caracterizacion/caracterizacion.md` | ✅ | Contexto 10 % |
| 2 | Línea base con inventario y datos justificados | `02-linea-base/linea_base.md` + `datos/` | ✅ | Línea base 15 % |
| 3 | Indicadores y cartera priorizada de medidas | `03-medidas-eficiencia/medidas_eficiencia.md` | ✅ | Solución 20 % |
| 4 | Alternativa renovable y almacenamiento | `04-renovables-almacenamiento/diseno_fotovoltaico.md` | ✅ | Solución 20 % |
| 5 | Circularidad, ACV simplificado y carbono | `05-circularidad-carbono/circularidad_carbono.md` | ✅ | Solución 20 % |
| 6 | Demostrador IoT real o emulado | `06-iot-demostrador/` | ✅ | IoT y código 15 % |
| 7 | Código documentado de análisis y visualización | `07-codigo-analitica/` (+ `dashboard_vercel/`) | ✅ Código local; deploy con API 500 | IoT y código 15 % |
| 8 | Asistente local RAG con corpus, citas y pruebas | `08-asistente-rag/` | 🟡 Falta ejecutar/validar | IA y validación 10 % |
| 9 | Producto visual (infografía real) | `09-producto-visual/` | ✅ | Imagen/3D 10 % |
| 10 | Modelo 3D depurado + fuente | `10-modelo-3d/` | 🟡 PENDIENTE | Imagen/3D 10 % |
| 11 | Evaluación financiera, sensibilidad y plan | `11-evaluacion-financiera/` | ✅ | Viabilidad 10 % |
| 12 | Informe, resumen, repositorio y sustentación | `12-informe-sustentacion/` | ✅ | Informe 10 % |

✅ = evidencia real integrada · 🟡 = estructura lista, falta producto o validación.

## Rúbrica resumida del proyecto

| Criterio | Peso |
| --- | ---: |
| Problema, alcance y contexto territorial | 10 % |
| Línea base, medición e indicadores | 15 % |
| Solución de eficiencia, renovables y circularidad | 20 % |
| Sistema IoT, código y analítica | 15 % |
| Asistente local de IA y validación | 10 % |
| Imagen y modelo 3D | 10 % |
| Viabilidad, riesgos y plan de implementación | 10 % |
| Informe, repositorio y sustentación | 10 % |

## Hilo conductor de la evidencia

1. **Medimos** 1.000 horas consecutivas en la finca (dataset en `02-linea-base/datos/`).
2. **Diagnosticamos** USE, pico de las 17:00 y factor de carga 7,9 % (`02-linea-base/`).
3. **Priorizamos** mover la molienda al mediodía y mantenimiento de nevera (`03-medidas-eficiencia/`).
4. **Diseñamos** 2,2 kWp + batería + seguidor Arduino (`04-renovables-almacenamiento/` y `06-iot-demostrador/`).
5. **Cuantificamos** carbono (0,29 t CO₂/año) y circularidad de baterías/paneles (`05-circularidad-carbono/`).
6. **Validamos** con código reproducible y dashboards (`07-codigo-analitica/`); el deploy público
   está en `https://energia-circular.vercel.app/` y su estado real se documenta en
   `07-codigo-analitica/dashboard_vercel/README.md`.
7. **Evaluamos** retorno del sistema individual y de la propuesta compartida (`11-evaluacion-financiera/`).
8. **Comunicamos** en el informe y el resumen ejecutivo (`12-informe-sustentacion/`).

## Autenticidad y seguridad

- No se inventaron mediciones: todas las cifras provienen del dataset o del informe del equipo.
- Los supuestos de irradiación, tarifa, costos y ganancia del seguidor están declarados como supuestos.
- El cuaderno original tenía un token de ngrok expuesto; las copias aquí están saneadas. **Revocar el token original.**
- Los entregables marcados como PENDIENTE deben completarse con archivos fuente, parámetros y validación humana.

## Checklist de cierre

- [x] Los entregables 1–7, 11 y 12 tienen evidencia real.
- [x] Cada dato tiene origen, unidad y método.
- [x] El IoT se demuestra con código Arduino y dashboards.
- [x] La evaluación financiera incluye tres escenarios y sensibilidad.
- [ ] Ejecutar y documentar el asistente RAG con citas y pruebas negativas.
- [x] Producto visual incorporado con ficha de procedencia.
- [x] Código local del dashboard y deploy público documentados con su estado real.
- [ ] Corregir las funciones serverless del deploy (`/api/kpis` responde 500).
- [ ] Generar modelo 3D con ficha de procedencia.
- [ ] Completar bitácora semanal y declaración de IA firmada por cada integrante.
- [ ] Verificar que el repositorio clonado reproduce los resultados.
