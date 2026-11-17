# 3. Indicadores y cartera priorizada de medidas de eficiencia

Las medidas se priorizan con base en los USE y el perfil horario de la línea base
(`../02-linea-base/linea_base.md`). Los impactos son estimaciones del informe y deben verificarse
después de implementar.

| Prioridad | Medida | Impacto estimado | Inversión | Verificación |
| --- | --- | --- | --- | --- |
| 1 | Reprogramar molienda a 10:00–14:00; evitar 16:00–19:00 (hoy 59 % de la molienda cae en tarde/noche, solo 30 % entre 09:00 y 15:00) | Pico de 17:00: 505 → 255 W (−50 %); mismo kWh, más autoconsumo solar | $0 | Curva horaria antes/después y registro de horas de molienda |
| 2a | Mantenimiento de nevera: empaques, ubicación y termostato | −10 % de su consumo (supuesto) | Baja | Comparativo de kWh semanales de nevera |
| 2b | Regletas con interruptor para conectores en espera | −25 % de conectores (supuesto) | < $150.000 COP totales | Medición de consumo nocturno |
| 2c | Apagar iluminación con luz natural | 7,3 % de la energía de iluminación | $0 | Registro de horas de encendido |
| 3 | Sistema FV híbrido 2,2 kWp con seguidor | 100 % cobertura del día promedio; $1.762.132 COP/año | $18.500.000 COP referenciales | Balance horario y factura |

**Total medida 2:** 10,77 kWh/mes (7,4 % del consumo), ≈ $129.237 COP/año con inversión estimada
menor a $150.000 COP. Los supuestos de reducción son estimaciones por validar y **el impacto de las
medidas no es aditivo** al de la solución solar: al reducir demanda, el sistema FV puede redimensionarse.

## Criterios de priorización

1. **Costo cero/operación primero:** reprogramar la molienda no requiere compra alguna y ataca el pico que
   define el tamaño del inversor y la batería.
2. **USE primero:** nevera y picadora concentran 59,2 % de la energía; cualquier intervención allí tiene mayor
   trazabilidad.
3. **Eficiencia antes que generación:** bajar el pico de 505 a 255 W reduce estrés del inversor de 3 kW.
4. **Generación al final:** se dimensiona con la demanda ya optimizada; en el informe se mantuvo el
   arreglo de 2,2 kWp para dar margen y se documentó el excedente resultante.

## Indicadores de seguimiento

| Métrica | Línea base | Meta tras medidas 1–2 | Meta tras medida 3 |
| --- | ---: | ---: | ---: |
| Pico promedio 17:00 | 505 W | ≤ 255 W | ≤ 255 W |
| Consumo diario | 4,83 kWh | ≈ 4,48 kWh (si se valida −7,4 %) | Cubierto 100 % |
| Factor de carga | 7,9 % | Mejora al aplanar el pico | — |
| Energía de picadora en 16:00–19:00 | 59 % de sus horas | 0 % | 0 % |

## Plan de implementación

| Fase | Acción | Responsable | Plazo sugerido |
| --- | --- | --- | --- |
| 1 | Acordar nuevo horario de molienda y registrar 4 semanas | Familia + equipo | Mes 1 |
| 2 | Mantenimiento nevera, regletas y apagado de luces | Familia | Mes 1–2 |
| 3 | Repetir medición horaria y recalcular línea base | Equipo | Mes 2 |
| 4 | Redimensionar/validar sistema FV con la nueva línea base | Equipo + instalador | Mes 3 |

> Nota: el informe original mantuvo el diseño de 2,2 kWp calculado sobre la línea base sin ajustar. La
> fase 4 existe para que la decisión final de inversión use la línea base ya mejorada.
