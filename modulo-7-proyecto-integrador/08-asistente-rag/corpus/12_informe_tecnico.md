# Análisis de datos de consumo eléctrico y diseño fotovoltaico con seguidor solar

**Caso de estudio:** finca agropecuaria sostenible, El Tambo (Cauca)  
**Autores:** Andrés Felipe Rodríguez · Brandon Meneses · Valeria Velasco  
**Docente:** [Nombre del docente]  
**Institución:** Corporación Universitaria Comfacauca — UNICOMFACAUCA · Popayán, Cauca · Noviembre de 2026

> Esta es la versión Markdown estructurada del informe. El archivo `informe_tecnico_original.docx` es la
> fuente autoritativa y conserva figuras y tablas originales. Las cifras aquí reproducidas se calcularon
> desde `../02-linea-base/datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`.

## Resumen

Se realizó la auditoría energética de una finca agropecuaria de El Tambo (Cauca) a partir de 1.000
mediciones horarias (1 de enero a 11 de febrero de 2025), mediante análisis exploratorio y el marco de
ISO 50001. El consumo promedio es **4,83 kWh/día** (144,83 kWh/mes), con potencia media de 201 W,
máximo de 2.542 W y factor de carga de 7,9 %. La nevera (38,7 %) y la picadora de pasto (20,5 %) son
Usos Significativos de Energía; la picadora tiene correlación 0,91 con la demanda total y determina los
picos. Se diseñó un sistema híbrido de 2,2 kWp con seguidor de un eje controlado por Arduino Uno,
batería de 5 kWh e inversor de 3 kW, que cubre 100 % de la demanda de un día promedio. El ahorro estimado
es de $1.762.132 COP/año, se evitan 0,29 t de CO₂ anuales y el retorno referencial es de 9,4 a 11,7 años.

**Palabras clave:** auditoría energética, ISO 50001, EDA, energía solar fotovoltaica, seguidor solar, Arduino.

## Abstract

An energy audit of a farm in El Tambo (Cauca) was carried out using 1,000 hourly electricity measurements
(January 1 to February 11, 2025), through exploratory data analysis and the ISO 50001 framework. Average
consumption is 4.83 kWh/day (144.8 kWh/month), with a load factor of 7.9 %. The refrigerator and the fodder
chopper were identified as Significant Energy Uses, and the chopper shows a correlation of 0.91 with total
demand. A 2.2 kWp hybrid photovoltaic system with a single-axis solar tracker controlled by an Arduino Uno
was designed. It covers 100 % of the average-day demand, saves about COP 1,762,132 per year and avoids 0.29 t
of CO2 annually. The simple payback is long (9.4 to 11.7 years), so the project is technically viable but
requires cost validation.

## 1. Introducción

### 1.1 Contexto

En El Tambo, Cauca, la actividad agropecuaria de pequeña escala depende de la electricidad para conservar
alimentos, preparar alimento animal e iluminar el hogar. El costo y la confiabilidad inciden en la
productividad y la calidad de vida. La gestión energética ofrece una ruta para reducir costos sin
sacrificar servicios, y la generación fotovoltaica aprovecha el recurso solar andino.

### 1.2 Planteamiento del problema

La finca no cuenta con caracterización cuantitativa de su demanda: se desconoce qué equipos dominan, en
qué horas se presentan los picos y cómo dimensionar una fuente propia. Sin línea base, las decisiones se
toman de forma intuitiva y hay riesgo de sobredimensionar o subdimensionar el sistema.

**Pregunta:** ¿cómo caracterizar con rigor analítico el consumo de energía activa y qué configuración
fotovoltaica con seguimiento solar permite cubrirlo técnica y económicamente de forma razonable?

### 1.3 Justificación

El proyecto integra auditoría ISO 50001, EDA y diseño renovable con seguidor de bajo costo. Los resultados
sirven como línea base replicable para predios rurales de la región y como insumo para decisiones de
inversión sustentadas en datos medidos.

## 2. Objetivos y alcance

**General.** Realizar la auditoría energética de la finca mediante EDA y diseñar un sistema fotovoltaico
híbrido con seguidor de un eje controlado por Arduino Uno que cubra su demanda.

**Específicos.**

1. Evaluar calidad e integridad del conjunto de datos horarios.
2. Caracterizar la demanda mediante estadística, distribuciones, correlaciones y perfiles.
3. Elaborar inventario de cargas, identificar USE y establecer línea base ISO 50001.
4. Dimensionar 2,2 kWp con almacenamiento y seguidor, y simular el balance horario.
5. Evaluar viabilidad económica y ambiental y formular medidas priorizadas.

**Alcance y limitaciones.** El análisis cubre 41,7 días, por lo que no captura estacionalidad anual. No hay
irradiancia medida en sitio; la generación usa un modelo parametrizado con supuestos declarados. Los costos
son referenciales. El seguidor es un diseño conceptual con código de referencia, no validado en banco de
pruebas.

## 3. Marco teórico y normativo

- **ISO 50001:2018:** línea base energética, indicadores EnPI y Usos Significativos de Energía, bajo ciclo PHVA.
- **EDA y correlación:** resúmenes y gráficos antes de modelar; coeficiente de Pearson para dependencia lineal; Pareto para concentrar esfuerzos.
- **Sistemas híbridos y seguidores:** módulos + inversor MPPT + batería; seguidor de un eje con dos LDR y pantalla; literatura reporta 25–30 % de ganancia.
- **Normativa colombiana:** RETIE (seguridad), Ley 1715 de 2014 (incentivos), CREG 174 de 2021 (autogeneración y excedentes), UPME 355 de 2004 (subsistencia 173 kWh/mes).

## 4. Metodología

**Datos.** `dataset_consumo_electrico_rural_ElTambo_Cauca.csv`: 1.000 registros horarios y 11 variables
(marca de tiempo, hora, día, seis potencias de carga, `total_W` y `total_kWh`).

**Flujo.** Calidad → estadística y correlaciones → inventario y USE → dimensionamiento y simulación →
diseño del seguidor → evaluación económica y ambiental.

**Herramientas.** Python con pandas, NumPy, SciPy, Matplotlib y Seaborn. Todas las cifras se recalculan en
`../07-codigo-analitica/analisis_consumo.py` desde una única fuente de cálculo.

## 5. Resultados de la auditoría energética

### 5.1 Calidad e integridad

| Indicador | Resultado |
| --- | --- |
| Observaciones | 1.000 |
| Periodo | 01/01/2025 00:00 – 11/02/2025 15:00 |
| Frecuencia | 1 hora, sin saltos |
| Nulos / duplicados | 0 / 0 |
| Diferencia máxima suma equipos vs. `total_W` | 0,2 W (redondeo) |

### 5.2 Estadística descriptiva (W)

| Variable | Media | Desv. est. | Mín. | Mediana | Máx. |
| --- | ---: | ---: | ---: | ---: | ---: |
| nevera | 77,92 | 15,16 | 35,00 | 79,85 | 120,00 |
| lavadora | 18,81 | 106,44 | 0,00 | 0,00 | 743,70 |
| tv | 19,91 | 33,09 | 0,00 | 0,00 | 99,80 |
| picadora de pasto | 41,16 | 249,31 | 0,00 | 0,00 | 1.797,50 |
| iluminación (10 bombillos) | 20,71 | 30,47 | 0,00 | 0,00 | 120,00 |
| otros conectores | 22,64 | 12,58 | 5,00 | 19,30 | 64,50 |
| **total** | **201,16** | **286,12** | **51,00** | **127,55** | **2.541,90** |

La media supera la mediana y la desviación supera la media: distribución asimétrica (sesgo 4,87) con
eventos intermitentes de alta potencia. El 5,5 % de las horas supera 500 W.

### 5.3 Correlación

`total_W` correlaciona 0,91 con la picadora, 0,44 con la lavadora y 0,22 con la nevera. La hora correlaciona
0,58 con el televisor y 0,48 con iluminación, reflejando hábitos vespertinos. Parte de la correlación con
`total_W` es estructural porque es la suma de los equipos.

### 5.4 Inventario, Pareto y USE

| Equipo | Pot. encendido (kW) | h/día | kWh/mes | Part. % | Acum. % |
| --- | ---: | ---: | ---: | ---: | ---: |
| Nevera | 0,078 | 24,00 | 56,10 | 38,7 | 38,7 |
| Picadora de pasto | 1,525 | 0,65 | 29,64 | 20,5 | 59,2 |
| Otros conectores | 0,023 | 24,00 | 16,30 | 11,3 | 70,5 |
| Iluminación (10 bombillos) | 0,050 | 9,94 | 14,91 | 10,3 | 80,8 |
| Televisor | 0,072 | 6,67 | 14,34 | 9,9 | 90,7 |
| Lavadora | 0,607 | 0,74 | 13,54 | 9,3 | 100,0 |
| **Total** | — | — | **144,83** | **100,0** | — |

Cuatro equipos alcanzan 80,8 % del consumo. Se clasifican como USE la nevera y la picadora (59,2 %). La
picadora opera 0,65 h/día a 1,525 kW y aporta 251 W de los 505 W del pico de las 17:00.

### 5.5 Línea base

| Indicador | Valor |
| --- | ---: |
| Consumo diario | 4,83 kWh/día |
| Consumo mensual (30 días) | 144,83 kWh/mes |
| Consumo anual proyectado | 1.762,13 kWh/año |
| Potencia media | 201,16 W |
| Demanda máxima | 2.541,9 W |
| Factor de carga | 7,9 % |
| Carga nocturna (01:00–04:00) | 74 W |
| Hora pico promedio | 17:00 (505 W) |

El consumo mensual es 83,7 % del umbral de subsistencia UPME (173 kWh/mes).

### 5.6 Perfil horario y variación semanal

De 00:00 a 05:00 la carga ronda 74 W; a las 10:00 sube a 260 W; a las 17:00 alcanza 505 W por molienda,
TV e iluminación. El pico coincide con el final de la ventana solar y exigirá batería. El consumo es mayor
en sábado (7,15 kWh), martes (5,95) y jueves (5,68); esos días concentran las 27 h de molienda, actividad
programable.

## 6. Diseño fotovoltaico con seguidor solar

### 6.1 Supuestos

HSP 4,5 kWh/m²·día, PR 0,78, ganancia del seguidor 27,5 %, 4 módulos de 550 W, DoD 80 %, eficiencia de
carga/descarga 95 %, tarifa $1.000/kWh y factor de emisión 0,164 kgCO₂/kWh.

### 6.2 Dimensionamiento

- Generación fija: 2,2 × 4,5 × 0,78 = **7,72 kWh/día**.
- Con seguidor: 7,72 × 1,275 = **9,85 kWh/día**.
- Mínimo por energía: 1,08 kWp con seguidor; se mantiene 2,2 kWp por margen ante nubosidad, crecimiento y picos.

Componentes: batería LiFePO4 5 kWh (4,0 útiles), inversor híbrido 3 kW con MPPT y seguidor Arduino Uno.

### 6.3 Balance de un día promedio

| Concepto | kWh/día | Porcentaje |
| --- | ---: | ---: |
| Generación con seguidor | 9,85 | 100 % de la generación |
| Demanda | 4,83 | 100 % de la demanda |
| Autoconsumo directo | 2,64 | 54,6 % de la demanda |
| Desde batería | 2,19 | 45,4 % de la demanda |
| Excedente | 4,78 | 48,6 % de la generación |

Con la mitad de generación (día nublado) la cobertura baja a 96,9 % y se requieren 0,15 kWh de la red.
Solo 49,0 % de la energía generada se aprovecha: oportunidad para inyectar a la red (CREG 174) o compartir.

### 6.4 Seguidor y seguridad

Dos LDR con divisor de 10 kΩ en A0/A1, zona muerta de 40 cuentas, pulso de 1,5 s, periodo de 10 s,
finales de carrera y retorno al Este de noche. Código en `../06-iot-demostrador/seguidor_arduino.ino`.
Seguridad RETIE: seccionador y fusibles DC, termomagnético AC, DPS, puesta a tierra, batería ventilada
con BMS, EPP y bloqueo/etiquetado.

## 7. Viabilidad económica y ambiental

### 7.1 Inversión

$18.500.000 COP referenciales: módulos $2,6 M, inversor $3,8 M, batería $7 M, seguidor $1,8 M,
protecciones $1,5 M, instalación $1,8 M.

### 7.2 Escenarios

Ahorro bruto $1.762.132 COP/año; O&M $185.000; neto $1.577.132. Retorno: 11,7 años (tarifa constante),
9,7 años (tarifa +4 %) y 9,4 años (inversión −20 %).

### 7.3 Impacto ambiental

1.762,13 kWh/año × 0,164 kgCO₂/kWh = **289 kgCO₂/año** (0,29 t/año), ~7,2 t en 25 años sin degradación.

### 7.4 Medidas priorizadas

1. Mover molienda a 10:00–14:00: pico 505 → 255 W, costo $0.
2. Nevera, regletas e iluminación: 10,77 kWh/mes (7,4 %), ≈ $129.237/año, inversión < $150.000.
3. Sistema FV híbrido: cobertura 100 %, $1.762.132/año.

Los impactos no son aditivos y los supuestos de reducción requieren validación.

## 8. Conclusiones y recomendaciones

1. El conjunto de 1.000 registros es continuo, sin nulos ni duplicados y coherente: apto como línea base.
2. La demanda es asimétrica: 74 W de fondo, 5,5 % de horas > 500 W, pico de 505 W a las 17:00.
3. Nevera y picadora son USE y concentran 59,2 % de la energía.
4. El sistema de 2,2 kWp con seguidor cubre el día promedio y 96,9 % en día nublado; solo aprovecha 49 % de su generación.
5. El proyecto es técnicamente viable y financieramente de largo plazo, sujeto a validación de costos.

**Recomendaciones:** ampliar monitoreo a 12 meses y medir irradiancia; obtener cotizaciones y evaluar
incentivos de la Ley 1715; revisar arreglo menor o aprovechamiento del excedente bajo CREG 174;
implementar medidas de costo cero; construir prototipo del seguidor y medir su ganancia; incorporar
monitoreo en tiempo real y modelos predictivos como trabajo futuro.

## Referencias

- CREG (2021). Resolución CREG 174 de 2021.
- Congreso de la República (2014). Ley 1715 de 2014.
- Duffie & Beckman (2013). *Solar Engineering of Thermal Processes*, 4.ª ed.
- IDEAM, UPME & MADS (2015). *Atlas de radiación solar, ultravioleta y ozono de Colombia*.
- ISO (2018). *ISO 50001:2018*.
- Masters (2004). *Renewable and Efficient Electric Power Systems*.
- Mousazadeh et al. (2009). *Renewable and Sustainable Energy Reviews*, 13(8), 1800–1818.
- Pearson (1895). *Proceedings of the Royal Society of London*, 58, 240–242.
- Tukey (1977). *Exploratory Data Analysis*.
- UPME (2004). Resolución 355 de 2004.

## Anexos

- **A. Diccionario de datos:** ver `../02-linea-base/linea_base.md` y el CSV.
- **B. Código del seguidor:** `../06-iot-demostrador/seguidor_arduino.ino`.
- **C. Código de análisis:** `../07-codigo-analitica/analisis_consumo.py` y cuadernos saneados.
