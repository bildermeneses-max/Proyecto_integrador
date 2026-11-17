# 11. Evaluación financiera preliminar, sensibilidad y plan

## Inversión referencial (sistema individual)

| Componente | Costo (COP) |
| --- | ---: |
| 4 módulos monocristalinos de 550 W | 2.600.000 |
| Inversor híbrido 3 kW con MPPT | 3.800.000 |
| Batería LiFePO4 5 kWh | 7.000.000 |
| Seguidor de un eje (estructura, Arduino, LDR, driver, actuador) | 1.800.000 |
| Protecciones DC/AC, cableado y puesta a tierra | 1.500.000 |
| Instalación, puesta en marcha e ingeniería | 1.800.000 |
| **Total** | **18.500.000** |

Son costos referenciales supuestos por el equipo; deben reemplazarse por cotizaciones formales.

## Ahorro y retorno

- Demanda cubierta: 1.762,13 kWh/año × $1.000/kWh = **$1.762.132 COP/año** ($146.844/mes).
- Operación y mantenimiento estimada: 1 % de la inversión = **$185.000 COP/año**.
- Ahorro neto: **$1.577.132 COP/año**.
- Retorno simple sin O&M: 10,5 años; con O&M, según escenario:

| Escenario | Supuesto | Retorno (años) | Flujo año 10 (COP) | Flujo año 15 (COP) |
| --- | --- | ---: | ---: | ---: |
| A | Tarifa constante | 11,7 | −2.728.682 | 5.156.977 |
| B | Tarifa +4 % anual | 9,7 | 806.343 | 14.009.201 |
| C | Inversión −20 % | 9,4 | 971.318 | 8.856.977 |

El plazo es largo porque el consumo es bajo y la tarifa de referencia moderada, pero es menor que la
vida útil esperada de los módulos (~25 años). No se monetizan continuidad del servicio ni incentivos de
la Ley 1715 de 2014, que podrían mejorar el resultado.

## Propuesta de optimización: autogeneración compartida

El balance mostró un excedente de **4,78 kWh/día (48,6 % de la generación)**. Al compartir con una
segunda vivienda de consumo similar:

| Concepto | Con batería 5 kWh + interconexión | Sin batería, conectado a red |
| --- | ---: | ---: |
| Demanda conjunta supuesta | 9,66 kWh/día | 9,66 kWh/día |
| Generación disponible | 9,85 kWh/día | 9,85 kWh/día |
| Cobertura de la demanda conjunta | 89 % | Casi toda la generación aprovechada |
| Inversión estimada | $20.000.000 COP | $12.200.000 COP |
| Ahorro anual estimado | $3.140.000 COP | $3.250.000 COP |
| Retorno simple | 6,8 años | 3,9 años |

Estas cifras provienen de `../12-informe-sustentacion/idea_solucion_original.docx`. Son una propuesta
del equipo: **los supuestos de perfil de la segunda vivienda, interconexión y reparto de costos deben
validarse** con medición real y simulación horaria antes de decidir la inversión.

Con batería, la cobertura baja a 89 % porque los 5 kWh atienden el consumo diurno de ambas casas y en la
noche se toma cerca de 11 % de la red. El inversor de 3 kW tiene margen siempre que no coincidan la
picadora de 1,5 kW y la lavadora en el mismo minuto.

## Análisis de sensibilidad

| Variable | Cambio | Efecto cualitativo |
| --- | --- | --- |
| Tarifa | +4 % anual | Retorno de 11,7 a 9,7 años |
| Inversión | −20 % | Retorno de 11,7 a 9,4 años |
| Demanda (eficiencia previa) | −7,4 % | Menor tamaño requerido; mejora el retorno si se ajusta el arreglo |
| HSP real | < 4,5 | Menor generación; revisar cobertura y batería |
| Segunda vivienda | Consumo real ≠ 4,83 | Cambia drásticamente el excedente aprovechado |
| O&M | > 1 % | Reduce flujo neto y alarga retorno |

## Riesgos y mitigación

| Riesgo | Mitigación |
| --- | --- |
| Cotizaciones desactualizadas | Solicitar tres cotizaciones formales antes de invertir |
| Irradiancia sobreestimada | Medir HSP en sitio al menos un año |
| Excedente sin comprador | Validar CREG 174 con el operador; acuerdo escrito con la vecina |
| Picos simultáneos | Coordinar horarios; verificar arranque del inversor de 3 kW |
| Degradación de batería | Garantía, BMS y plan de reemplazo/segundo uso |
| Reparto de costos conflictivo | Convenio entre familias sin venta de energía por kWh |

## Plan de implementación por fases

1. **Mes 1–2:** medidas de costo cero y bajo costo; nueva medición horaria.
2. **Mes 3:** cotizaciones, validación de irradiancia y redimensionamiento.
3. **Mes 4:** acuerdo legal con segunda vivienda y consulta al operador de red (CREG 174).
4. **Mes 5–6:** instalación con RETIE, puesta en marcha y medición de ganancia real del seguidor.
5. **Seguimiento:** indicadores mensuales de cobertura, excedente, ahorro y CO₂ evitado.

## Archivos relacionados

- `escenarios.csv` — resumen tabular de los escenarios.
- `../04-renovables-almacenamiento/diseno_fotovoltaico.md` — supuestos técnicos.
- `../02-linea-base/linea_base.md` — origen de la demanda.
