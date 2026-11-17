# 4. Alternativa renovable, almacenamiento y seguidor solar

## Supuestos de diseño

| Parámetro | Valor | Origen |
| --- | --- | --- |
| Demanda objetivo | 4,83 kWh/día | Línea base medida |
| Horas sol pico (HSP) | 4,5 kWh/m²·día | Referencia zona andina; validar en sitio |
| Rendimiento global (PR) | 0,78 | Supuesto de ingeniería |
| Ganancia seguidor 1 eje | 27,5 % | Punto medio de rango literario 25–30 % |
| Módulos | 4 × 550 W monocristalinos = 2,2 kWp | Diseño |
| DoD batería LiFePO4 | 80 % (4,0 kWh útiles de 5 kWh) | Supuesto |
| Eficiencia carga/descarga | 95 % cada una | Supuesto |
| Tarifa | $1.000 COP/kWh | Lineamiento del diplomado |
| Factor de emisión | 0,164 kgCO₂/kWh | Lineamiento del diplomado |

## Componentes

| Componente | Especificación | Justificación |
| --- | --- | --- |
| Generador FV | 2,2 kWp (4 × 550 W) | Margen sobre 1,08 kWp mínimos con seguidor (1,38 kWp fijo) |
| Almacenamiento | 5 kWh nominales / 4,0 kWh útiles | Mínimo simulado 2,35 kWh útiles; autonomía 20 h |
| Inversor híbrido | 3 kW con MPPT | Cubre 2,54 kW máximos registrados y arranque de picadora |
| Seguidor | 1 eje Este-Oeste, Arduino Uno | +27,5 % de captación estimado |

La generación calculada es:

- Estructura fija: 2,2 kWp × 4,5 HSP × 0,78 = **7,72 kWh/día**.
- Con seguidor: 7,72 × 1,275 = **9,85 kWh/día**.

Se mantuvo 2,2 kWp en lugar de 1,08 kWp por margen ante nubosidad, crecimiento de carga y alta
exigencia de potencia de la picadora, a costa de un excedente discutido más adelante.

## Balance de un día promedio

| Concepto | kWh/día | % |
| --- | ---: | ---: |
| Generación con seguidor | 9,85 | 100 % de la generación |
| Demanda del predio | 4,83 | 100 % de la demanda |
| Autoconsumo directo | 2,64 | 54,6 % de la demanda |
| Energía desde batería | 2,19 | 45,4 % de la demanda |
| Excedente no aprovechado | 4,78 | 48,6 % de la generación |

La simulación usa una curva parametrizada de 06:00 a 18:00, más aplanada con seguidor. Solo se aprovecha
49,0 % de la energía generada. En un día con la mitad de generación la cobertura baja a 96,9 % y se
requieren 0,15 kWh de la red; el banco queda con 2,35 kWh útiles mínimos.

## Seguidor de un eje (Arduino Uno)

- Dos LDR con resistencias de 10 kΩ en divisor de tensión, montadas a lado y lado de una pantalla.
- Entradas analógicas A0 (Este) y A1 (Oeste); diferencia comparada con zona muerta de 40 cuentas ADC.
- Si la diferencia supera la zona muerta, un driver puente H mueve el actuador lineal en pulso de 1,5 s.
- Período de revisión: 10 s; finales de carrera evitan sobre-recorrido; de noche retorno al Este.
- Código de referencia en `../06-iot-demostrador/seguidor_arduino.ino`.

La ganancia de 27,5 % equivale a 2,12 kWh adicionales/día frente a estructura fija. El consumo del
actuador se considera marginal, pero **debe medirse en prototipo**; el diseño no fue validado en banco
de pruebas.

## Seguridad y normativa

- RETIE: seccionador y fusibles DC, termomagnético AC, DPS, conductores y puesta a tierra verificada.
- Baterías LiFePO4 en sitio ventilado con BMS y protección contra cortocircuito.
- Intervención de tableros solo sin tensión, con EPP dieléctrico y herramientas aisladas.
- Bloqueo/etiquetado, señalización y distancias de seguridad para la zona móvil del seguidor.
- CREG 174 de 2021 para autogeneración y entrega de excedentes; Ley 1715 de 2014 para incentivos.

## Oportunidad detectada: aprovechar el excedente

El excedente de 4,78 kWh/día motivó la propuesta de **compartir la generación con una segunda vivienda**
vecina (demanda conjunta 9,66 kWh/día vs. 9,85 kWh/día generados). Los escenarios financieros de esa
propuesta están en `../12-evaluacion-financiera/evaluacion_financiera.md`. Su viabilidad legal depende de
validar la autogeneración colectiva con el operador de red.
