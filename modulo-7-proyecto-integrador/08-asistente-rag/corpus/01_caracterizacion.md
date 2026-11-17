# 1. Caracterización del contexto, actores, problema y alcance

## Contexto territorial

El municipio de **El Tambo, Cauca** concentra agricultura de pequeña escala donde la electricidad sostiene
conservación de alimentos, preparación de alimento animal e iluminación del hogar. El costo y la
confiabilidad del suministro inciden directamente en productividad y calidad de vida.

**Caso:** finca agropecuaria sostenible típica del municipio.  
**Periodo observado:** 01/01/2025 00:00 – 11/02/2025 15:00 (41,7 días).  
**Fuente:** `../02-linea-base/datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`.

## Actores

| Actor | Rol / interés |
| --- | --- |
| Familia propietaria de la finca | Usuaria final; requiere confiabilidad y reducción de costos |
| Operador de red | Debe autorizar autogeneración y eventuales excedentes (CREG 174 de 2021) |
| Segunda vivienda vecina | Receptora del excedente en la propuesta de optimización |
| Equipo del diplomado | Auditoría, análisis, diseño y documentación |
| Docente / jurado | Validación técnica y aprovechamiento didáctico |

## Problema

La finca no cuenta con caracterización cuantitativa de su demanda: se desconoce qué equipos dominan el
consumo, en qué horas ocurren los picos y cómo dimensionar una fuente propia sin sobredimensionar o
quedarse corto. Las decisiones de inversión se tomaban de forma intuitiva.

**Pregunta del proyecto:** ¿cómo caracterizar con rigor analítico el consumo de energía activa y qué
configuración fotovoltaica con seguimiento solar permite cubrirlo técnica y económicamente de forma
razonable?

## Objetivos

**General.** Realizar la auditoría energética de la finca mediante EDA y diseñar un sistema fotovoltaico
híbrido con seguidor de un eje controlado por Arduino Uno que cubra su demanda.

**Específicos.**

1. Evaluar calidad e integridad de las 1.000 mediciones.
2. Caracterizar la demanda con estadística, distribuciones, correlaciones y perfiles.
3. Elaborar inventario de cargas, identificar USE y establecer línea base ISO 50001.
4. Dimensionar 2,2 kWp con almacenamiento y simular el balance horario.
5. Evaluar viabilidad económica, ambiental y proponer medidas priorizadas.

## Alcance

- Incluye: auditoría de energía activa, USE, línea base, diseño FV, seguidor conceptual, dashboards,
  carbono básico y evaluación financiera referencial.
- No incluye: diseño eléctrico legal firmado, certificación RETIE, medición de irradiancia en sitio,
  montaje del seguidor, RAG ejecutado ni activos 3D/multimodales (pendientes).

## Restricciones y supuestos declarados

- Serie de solo 41,7 días: no captura estacionalidad anual.
- Sin irradiancia medida: HSP = 4,5 kWh/m²·día tomado como referencia de la zona andina.
- Costos referenciales, no cotizaciones formales.
- Seguidor presentado como diseño conceptual con código de referencia, sin banco de pruebas.
- Tarifa de referencia: $1.000 COP/kWh; factor de emisión: 0,164 kgCO₂/kWh.

## Marco normativo aplicado

RETIE (seguridad eléctrica) · ISO 50001:2018 (límite base, EnPI y USE) · Ley 1715 de 2014
(incentivos renovables) · Resolución CREG 174 de 2021 (autogeneración y excedentes) · UPME 355 de 2004
(consumo de subsistencia de 173 kWh/mes).

## Criterio de éxito

Coherencia demostrable entre problema → datos → cálculo → decisión → prototipo → evidencia, sin inventar
resultados y conservando fuentes, parámetros y validación humana.
