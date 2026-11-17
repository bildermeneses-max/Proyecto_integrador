# 2. Línea base energética e indicadores

**Datos:** `datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv` · 1.000 registros horarios · 11 variables.  
**Método:** Python/pandas; mismas formulas en `../07-codigo-analitica/analisis_consumo.py`.

## Calidad e integridad

| Indicador | Resultado |
| --- | --- |
| Observaciones | 1.000 |
| Periodo | 01/01/2025 00:00 – 11/02/2025 15:00 |
| Frecuencia | 1 hora, sin saltos |
| Valores nulos | 0 |
| Registros duplicados | 0 |
| Diferencia máxima suma equipos vs. `total_W` | 0,2 W (redondeo) |
| `total_kWh` | igual a `total_W / 1000` |

## Estadística descriptiva de potencia (W)

| Variable | Media | Desv. est. | Mín. | Mediana | Máx. |
| --- | ---: | ---: | ---: | ---: | ---: |
| `nevera_W` | 77,92 | 15,16 | 35,00 | 79,85 | 120,00 |
| `lavadora_W` | 18,81 | 106,44 | 0,00 | 0,00 | 743,70 |
| `tv_W` | 19,91 | 33,09 | 0,00 | 0,00 | 99,80 |
| `picadora_pasto_W` | 41,16 | 249,31 | 0,00 | 0,00 | 1.797,50 |
| `iluminacion_10bombillos_W` | 20,71 | 30,47 | 0,00 | 0,00 | 120,00 |
| `otros_conectores_W` | 22,64 | 12,58 | 5,00 | 19,30 | 64,50 |
| **`total_W`** | **201,16** | **286,12** | **51,00** | **127,55** | **2.541,90** |

La distribución es asimétrica (sesgo 4,87): carga de fondo baja con eventos intermitentes de alta
potencia. El 5,5 % de las horas supera 500 W.

## Inventario de cargas y Pareto

Potencia unitaria = promedio medido con el equipo encendido; uso = horas/día con consumo registrado;
30 días/mes.

| Equipo | Cant. | Pot. encendido (kW) | h/día | kWh/mes | Part. % | Acum. % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Nevera | 1 | 0,078 | 24,00 | 56,10 | 38,7 | 38,7 |
| Picadora de pasto | 1 | 1,525 | 0,65 | 29,64 | 20,5 | 59,2 |
| Otros conectores | 1 | 0,023 | 24,00 | 16,30 | 11,3 | 70,5 |
| Iluminación (10 bombillos) | 10 | 0,050 | 9,94 | 14,91 | 10,3 | 80,8 |
| Televisor | 1 | 0,072 | 6,67 | 14,34 | 9,9 | 90,7 |
| Lavadora | 1 | 0,607 | 0,74 | 13,54 | 9,3 | 100,0 |
| **TOTAL** | 15 | — | — | **144,83** | **100,0** | — |

**Usos Significativos de Energía (USE):** nevera y picadora (59,2 %). La picadora aporta 251 W de los
505 W del pico de las 17:00 (49,6 %) con solo 0,65 h/día.

## Línea base energética (LBe)

| Indicador | Valor | Unidad / nota |
| --- | ---: | --- |
| Consumo diario promedio | 4,83 | kWh/día |
| Consumo mensual | 144,83 | kWh/mes (30 días) |
| Consumo anual proyectado | 1.762,13 | kWh/año |
| Potencia media | 201,16 | W |
| Demanda máxima registrada | 2.541,9 | W |
| Factor de carga | 7,9 | % (media / máxima) |
| Carga base nocturna (01:00–04:00) | 74 | W |
| Hora pico promedio | 17:00 | 505 W |
| Variación diaria observada | 3,08 – 10,19 | kWh (41 días completos) |

El consumo mensual equivale al **83,7 %** del umbral de subsistencia de 173 kWh/mes (UPME, 2004).

## Perfil y variación semanal

- 00:00–05:00: ~74 W (nevera + conectores).
- 10:00: primer repunte, 260 W.
- 17:00: pico de 505 W (molienda + TV + iluminación), coincide con el final de la ventana solar.
- Sábado 7,15 kWh/día; martes 5,95; jueves 5,68; resto 3,54–3,99. Esos tres días concentran las 27 h
  de operación de la picadora: actividad programable y desplazable.

## Correlaciones relevantes

- `picadora_pasto_W` ↔ `total_W`: r = 0,91 (parcialmente estructural, pues `total_W` es su suma).
- `lavadora_W` ↔ `total_W`: r = 0,44; `nevera_W` ↔ `total_W`: r = 0,22.
- `hora` ↔ `tv_W`: r = 0,58; `hora` ↔ iluminación: r = 0,48 (hábitos vespertinos).

## Indicadores de desempeño propuestos (EnPI)

| EnPI | Fórmula | Frecuencia | Línea base |
| --- | --- | --- | --- |
| Consumo específico diario | Σ `total_kWh` / días | Mensual | 4,83 kWh/día |
| Factor de carga | P_media / P_máxima | Mensual | 7,9 % |
| Participación USE | Energía USE / energía total | Mensual | 59,2 % |
| Pico vespertino | Media de `total_W` a las 17:00 | Semanal | 505 W |
| Cobertura solar (post-intervención) | Demanda cubierta / demanda | Mensual | Meta 100 % día promedio |

## Limitaciones

Serie de 41,7 días; sin irradiancia en sitio; sin medición de factor de potencia ni calidad de energía.
La red neuronal del cuaderno no se usa como EnPI porque reproduce una identidad aditiva.
