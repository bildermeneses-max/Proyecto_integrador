# Proyecto Integrador — Diplomado en Energía Circular Inteligente 5.0

**Caso de estudio:** finca agropecuaria sostenible en **El Tambo, Cauca**  
**Autores:** Andrés Felipe Rodríguez · Brandon Meneses · Valeria Velasco  
**Institución:** Corporación Universitaria Comfacauca — UNICOMFACAUCA  
**Ubicación:** Popayán, Cauca · Noviembre de 2026

---

## Estado del repositorio

Se integraron los entregables reales disponibles: informe técnico, idea de solución, dataset de 1.000
mediciones horarias, cuadernos de EDA/red neuronal y código Gradio/Streamlit.

| Entregable | Estado |
| --- | --- |
| Caracterización, línea base, medidas, diseño FV, circularidad, finanzas | ✅ Con datos reales del informe |
| Demostrador IoT (Arduino + dashboards) y analítica | ✅ Código y documentación incluidos |
| Dashboard web desplegado en Vercel | ✅ Publicado y verificado; analítica con error 500 pendiente de corregir |
| Informe técnico y resumen ejecutivo | ✅ Incluidos |
| Asistente RAG ejecutado con citas y pruebas | 🟡 Estructura y plan listos; falta ejecutar y validar |
| Producto visual (infografía real del caso) | ✅ Imagen y ficha de procedencia incluidas |
| Modelo 3D depurado + fuente | 🟡 Pendiente de generar y documentar procedencia |

> **Seguridad:** el cuaderno original `Untitled17.ipynb` contenía un token de ngrok hardcodeado.
> Las copias versionadas aquí están saneadas y usan `NGROK_AUTHTOKEN` por variable de entorno.
> **El token original debe revocarse en el panel de ngrok.** No se reproduce en este repositorio.

## Mapa de módulos

| Módulo | Denominación | Horas | Peso | Evidencia principal |
| --- | --- | ---: | ---: | --- |
| 1 | Transición energética, política pública y contexto territorial | 12 | 8 % | Mapa territorial, normativa y problema |
| 2 | Eficiencia energética, medición e ISO 50001 | 18 | 15 % | Auditoría, datos, código y cartera de medidas |
| 3 | Renovables, almacenamiento y comunidades energéticas | 18 | 12 % | Predimensionamiento y balance |
| 4 | Economía circular, ciclo de vida y carbono | 16 | 12 % | Mapa circular y carbono |
| 5 | IA local, datos, RAG y código | 18 | 15 % | Código, dashboards y asistente |
| 6 | IA generativa multimodal, 2D a 3D | 18 | 13 % | Imagen y modelo 3D |
| 7 | Proyecto integrador | 20 | 25 % | 12 entregables + informe y sustentación |
| **Total** | | **120** | **100 %** | |

La progresión es deliberada: los módulos 1–4 construyen criterio energético, normativo y circular;
el 5 aporta datos e IA local; el 6 produce comunicación multimodal; el 7 integra todo en el caso real.

## Estructura del repositorio

```text
├── README.md
├── .gitignore
├── docs/
│   ├── rubrica.md
│   ├── plan_de_trabajo.md
│   └── bitacora.md
├── modulo-1-transicion-energetica/ ... modulo-6-multimodal-3d/
└── modulo-7-proyecto-integrador/
    ├── 01-caracterizacion/
    ├── 02-linea-base/            ← dataset real + línea base
    ├── 03-medidas-eficiencia/
    ├── 04-renovables-almacenamiento/
    ├── 05-circularidad-carbono/
    ├── 06-iot-demostrador/       ← Arduino, Gradio y Streamlit
    ├── 07-codigo-analitica/      ← cuadernos saneados y análisis reproducible
    ├── 08-asistente-rag/
    ├── 09-producto-visual/
    ├── 10-modelo-3d/
    ├── 11-evaluacion-financiera/
    └── 12-informe-sustentacion/  ← informe original y resumen
```

Cada módulo tiene su `README.md`. El README del módulo 7 mapea los 12 entregables a su carpeta,
archivo y criterio de la rúbrica.

## Resultados centrales del caso

- 1.000 mediciones horarias (01/01/2025 – 11/02/2025), sin nulos ni duplicados.
- Demanda: **4,83 kWh/día** · 144,83 kWh/mes · 1.762,13 kWh/año · 201,16 W medios · 2.541,9 W máximos.
- Usos significativos: nevera (38,7 %) y picadora de pasto (20,5 %); juntas 59,2 %.
- Pico promedio: 17:00 con 505 W; carga nocturna: ~74 W; factor de carga 7,9 %.
- Diseño: 2,2 kWp (4 × 550 W), inversor híbrido 3 kW, batería LiFePO4 5 kWh y seguidor Arduino Uno.
- Generación simulada: 7,72 kWh/día fijo → 9,85 kWh/día con seguidor; cobertura 100 % del día promedio.
- Excedente: 4,78 kWh/día (48,6 % de la generación), base de la propuesta de compartir con una segunda vivienda.
- Inversión referencial: $18.500.000 COP; ahorro $1.762.132 COP/año; retorno 9,4–11,7 años.
- Propuesta de autogeneración compartida: retorno 6,8 años con batería o 3,9 años conectado a red sin batería.

## Principio de autenticidad

La rúbrica no premia la cantidad de herramientas, sino la coherencia entre **problema, datos, cálculo,
decisión, prototipo y evidencia**. Todo resultado generado conserva fuente, parámetros y validación
humana. Los espacios sin evidencia real aparecen marcados como `PENDIENTE` y no se inventan datos.

Ver `docs/bitacora.md` para la declaración de uso de IA y `docs/rubrica.md` para la rúbrica completa.

## Reproducción rápida

```bash
pip install -r modulo-7-proyecto-integrador/07-codigo-analitica/requirements.txt
python modulo-7-proyecto-integrador/07-codigo-analitica/analisis_consumo.py
streamlit run modulo-7-proyecto-integrador/06-iot-demostrador/dashboard_streamlit.py
python modulo-7-proyecto-integrador/06-iot-demostrador/dashboard_gradio.py
```

Los dashboards leen el dataset desde `modulo-7-proyecto-integrador/02-linea-base/datos/` mediante una
ruta relativa al repositorio. Para publicar un túnel con ngrok, configurar `NGROK_AUTHTOKEN` en el
entorno; nunca pegar el token en el código.
