# Guion de sustentación — versión del equipo

Duración: 10 minutos. Reparto: P1 bloques 1–2, P2 bloque 3, P3 bloques 4–5.  
Versión extendida y preguntas del jurado: `../../docs/presentacion.md`.  
Fuente original: `idea_solucion_original.docx`.

## Bloque 1 — El gancho (0:00–1:30)

"Buenos días. Imaginen administrar una finca agropecuaria en El Tambo, Cauca, donde el recibo de la luz
llega cada mes, pero nadie sabe exactamente qué equipo está disparando el consumo ni a qué hora. Si hoy
quisiéramos instalar paneles solares allí a ciegas, correríamos dos riesgos: gastar de más
sobredimensionando el sistema, o quedarnos cortos cuando arranquen las máquinas del campo.

Para resolverlo combinamos auditoría ISO 50001, análisis de datos en Python y un sistema fotovoltaico con
seguidor controlado por Arduino. Analizamos 1.000 mediciones horarias reales —casi 42 días continuos sin un
solo dato perdido— para decidir con evidencia y no con intuición."

## Bloque 2 — Radiografía del consumo (1:30–4:00)

"La línea base: 4,83 kWh al día, 144,8 kWh al mes, por debajo del umbral de 173 kWh de la UPME. Pero tiene
dos mundos: de madrugada apenas 74 W; a las 5 de la tarde salta a 505 W y llegó a 2.542 W. Factor de carga
7,9 %: la instalación soporta picos altísimos muy poco tiempo.

Con Pareto encontramos dos USE que suman casi 60 %: nevera 38,7 %, que trabaja 24 horas; picadora 20,5 %,
que se prende unos 40 minutos al día —martes, jueves y sábados— pero pide más de 1.500 W. Correlación 0,91
con la demanda total: cuando la picadora se enciende, manda sobre toda la curva."

## Bloque 3 — Solución técnica (4:00–6:30)

"Diseñamos 2,2 kWp: cuatro paneles de 550 W, inversor híbrido de 3 kW con margen para el arranque y batería
de 5 kWh. Añadimos un seguidor de un eje Este-Oeste con Arduino Uno: dos fotorresistencias separadas por una
pantalla; si una queda en sombra, el Arduino mueve un actuador lineal hasta realinear.

La literatura reporta 25–30 % de ganancia; adoptamos 27,5 %. En simulación, la generación sube de 7,72 a
9,85 kWh diarios y cubre el 100 % del día promedio: 54,6 % directo y 45,4 % con batería. En día nublado,
96,9 %. Bajo criterios RETIE."

## Bloque 4 — Finanzas y propuesta compartida (6:30–8:45)

"Con sinceridad: 18,5 millones de inversión, 1.762.132 COP de ahorro al año, 0,29 t de CO₂ evitadas y
retorno de 9,4 a 11,7 años. Técnicamente viable, financieramente lento.

¿Por qué? Desaprovechamos 48,6 % de lo generado: sobran 4,78 kWh al día. Primero, mover la molienda al
mediodía baja el pico de 505 a 255 W sin costo. Segundo, compartir con una casa vecina: demanda conjunta
9,66 kWh, casi exacto con los 9,85 producidos. Con batería e interconexión de 1,5 millones, ahorro de 3,14
millones y retorno de 6,8 años. Sin batería y conectados a red, inversión de 12,2 millones y retorno de 3,9
años. Todo validando CREG 174 de 2021 y repartiendo costos fijos sin vender energía por kWh."

## Bloque 5 — Cierre (8:45–10:00)

"Tres conclusiones: los datos evitan sobrecostos; primero eficiencia, luego generación; y la energía circular
es comunitaria: un excedente aprovechado convierte una inversión lenta en una solución compartida. Muchas
gracias, quedamos atentos a sus preguntas."

## Gráficas de apoyo

- Figura 4 del informe: Pareto de equipos.
- Figura 5: perfil horario con pico a las 17:00.
- Figura 7: generación vs. demanda, señalando el área de excedente.
