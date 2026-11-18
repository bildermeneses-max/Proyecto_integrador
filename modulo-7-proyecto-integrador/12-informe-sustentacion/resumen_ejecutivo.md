# Resumen ejecutivo

**Proyecto:** Análisis de datos de consumo eléctrico y diseño fotovoltaico con seguidor solar  
**Caso:** finca agropecuaria sostenible en El Tambo, Cauca  
**Equipo:** Andrés Felipe Rodríguez · Brandon Meneses · Valeria Velasco

## Problema

La finca no conocía qué equipos dominaban su consumo, cuándo ocurrían los picos ni cómo dimensionar una
fuente propia sin sobredimensionar o quedarse corto.

## Evidencia

- 1.000 mediciones horarias entre el 1 de enero y el 11 de febrero de 2025, sin nulos ni duplicados.
- Línea base: 4,83 kWh/día · 144,83 kWh/mes · 1.762,13 kWh/año · 201 W medios · 2.541,9 W máximos.
- USE: nevera (38,7 %) y picadora de pasto (20,5 %), 59,2 % conjuntos.
- Pico promedio: 17:00 con 505 W; carga nocturna ~74 W; factor de carga 7,9 %.

## Solución

Sistema híbrido de **2,2 kWp** (4 paneles de 550 W), inversor de 3 kW, batería LiFePO4 de 5 kWh y
seguidor de un eje con Arduino Uno. Generación simulada: **9,85 kWh/día** frente a 7,72 kWh/día sin
seguidor. Cobertura del 100 % del día promedio (54,6 % directo, 45,4 % batería) y 96,9 % en día nublado.

## Hallazgo clave

El sistema genera 4,78 kWh/día más de lo que consume la finca (**48,6 % de la generación**). Ese excedente
encarece el retorno: $18,5 M de inversión, $1,76 M/año de ahorro y 9,4–11,7 años de retorno.

## Propuesta de optimización

Compartir la generación con una segunda vivienda vecina (demanda conjunta supuesta de 9,66 kWh/día):

| Escenario | Inversión | Ahorro anual | Retorno |
| --- | ---: | ---: | ---: |
| Con batería + interconexión | $20,0 M COP | $3,14 M COP | 6,8 años |
| Sin batería, conectado a red | $12,2 M COP | $3,25 M COP | 3,9 años |

Requiere validar autogeneración colectiva según CREG 174 de 2021 y acordar reparto fijo de costos entre
las familias, sin vender energía por kWh.

## Impacto y siguientes pasos

Se evitan 0,29 t de CO₂ al año. Se recomienda ejecutar primero medidas de costo cero (mover la molienda al
mediodía reduce el pico de 505 a 255 W), ampliar el monitoreo a 12 meses, medir irradiancia y validar
cotizaciones antes de invertir.

## Estado de entregables

Listos: caracterización, línea base, medidas, diseño FV, circularidad, IoT/código, finanzas e informe.
Listo además: producto visual (`09-producto-visual/producto_visual_el_tambo.jpeg`).
Listo además: dashboard web desplegado en `https://energia-circular.vercel.app/` y su código local
en `07-codigo-analitica/dashboard_vercel/` (deploy accesible; analítica con error 500 documentado).
Listo además: presentación de 15 diapositivas en HTML dinámico y PDF 16:9, con gráficos generados
desde el CSV (`13-presentacion-diapositivas/`).
Pendientes de completar: asistente RAG ejecutado, modelo 3D, corrección de las funciones
serverless del deploy y validación humana de la presentación por los autores.

> Nota de seguridad: el cuaderno original contenía un token de ngrok expuesto; las copias versionadas están
> saneadas y el token debe revocarse en su proveedor.
