# Guion de sustentación — caso El Tambo, Cauca

Duración sugerida: **10 minutos** + preguntas.  
Reparto sugerido: Persona 1 → bloques 1–2, Persona 2 → bloque 3, Persona 3 → bloques 4–5.

Fuente: `modulo-7-proyecto-integrador/13-informe-sustentacion/idea_solucion_original.docx`
y `informe_tecnico_original.docx`.

---

## Bloque 1 — El gancho (0:00 – 1:30)

> "Buenos días. Imaginen administrar una finca agropecuaria en El Tambo, Cauca, donde el recibo de la luz
> llega cada mes, pero nadie sabe exactamente qué equipo está disparando el consumo ni a qué hora. Si hoy
> quisiéramos instalar paneles solares allí a ciegas, correríamos dos riesgos: gastar de más
> sobredimensionando el sistema, o quedarnos cortos cuando arranquen las máquinas del campo.
>
> Para resolverlo combinamos una auditoría bajo ISO 50001, análisis de datos en Python y un sistema
> fotovoltaico con seguidor controlado por Arduino. Analizamos 1.000 mediciones horarias reales —casi 42
> días continuos sin un solo dato perdido— para decidir con evidencia y no con intuición."

**Apoyo:** diapositiva con el mapa del Cauca y la foto/diagrama de la finca.

## Bloque 2 — La radiografía del consumo (1:30 – 4:00)

> "¿Qué nos dijeron esos 1.000 datos? La línea base: 4,83 kWh al día, 144,8 kWh al mes. Es un consumo
> moderado —por debajo del umbral de subsistencia de 173 kWh de la UPME— pero con un comportamiento
> especial.
>
> Vive en dos mundos: de madrugada apenas 74 W; a las 5 de la tarde salta a un pico promedio de 505 W y
> llegó a 2.542 W. El factor de carga es de solo 7,9 %: la red interna debe soportar picos altísimos
> durante muy poco tiempo.
>
> Con Pareto identificamos dos Usos Significativos de Energía que suman casi el 60 %: la nevera, 38,7 %,
> que trabaja 24 horas; y la picadora de pasto, 20,5 %, que solo se prende unos 40 minutos al día —
> martes, jueves y sábados— pero pide más de 1.500 W. Su correlación con la demanda total es 0,91:
> cuando la picadora se enciende, manda sobre toda la curva eléctrica."

**Apoyo:** Figura 4 (Pareto) y Figura 5 (perfil horario). Hacer pausa al decir 0,91.

## Bloque 3 — La solución técnica (4:00 – 6:30)

> "Con esa radiografía diseñamos un sistema híbrido de 2,2 kWp: cuatro paneles de 550 W, inversor
> híbrido de 3 kW —con margen para el arranque de la picadora— y batería de litio de 5 kWh.
>
> Añadimos innovación de bajo costo: seguidor de un eje Este-Oeste con Arduino Uno. Dos fotorresistencias
> separadas por una pantalla; cuando el sol se mueve y una queda en sombra, el Arduino detecta la
> diferencia de voltaje y acciona un motor lineal hasta realinear los paneles.
>
> Según literatura técnica, eso aumenta la captación cerca de 27,5 %. En nuestra simulación horaria la
> generación sube de 7,72 a 9,85 kWh diarios y cubre el 100 % del día promedio: 54,6 % directo y 45,4 %
> con batería en el pico de las 17:00 y la noche. En un día nublado la cobertura aún es 96,9 %. Todo bajo
> criterios RETIE."

**Apoyo:** Figura 7 (generación vs demanda) y diagrama del seguidor (Anexo B del informe).

## Bloque 4 — El giro financiero y la propuesta compartida (6:30 – 8:45)

> "Hablemos con sinceridad de dinero. Inversión referencial: 18,5 millones de pesos. Ahorro bruto:
> 1.762.132 COP al año, evitando 0,29 toneladas de CO₂. Retorno: 9,4 a 11,7 años. Técnicamente viable,
> financieramente lento.
>
> ¿Por qué? Porque nuestro balance reveló que desaprovechamos el 48,6 % de lo generado: producimos 9,85
> kWh y la finca solo usa 4,83. Nos sobran 4,78 kWh diarios.
>
> Primero, medidas de costo cero: mover la molienda al mediodía baja el pico de 505 a 255 W.
>
> Segundo, una solución de alto impacto: compartir el sistema con una segunda vivienda vecina. Si consume
> lo mismo, la demanda conjunta sube a 9,66 kWh y encaja casi exacto con los 9,85 que ya producimos. Con
> batería e inversión de 1,5 millones en interconexión cubrimos el 89 %, el ahorro sube a 3,14 millones
> al año y el retorno cae a 6,8 años. Sin batería y conectados a red, la inversión baja a 12,2 millones y
> el retorno es de apenas 3,9 años.
>
> Eso sí: hay que validar con el operador de red la autogeneración colectiva de la CREG 174 de 2021 y
> acordar reparto fijo de costos entre las familias, sin vender energía por kWh como comercializador
> informal."

**Apoyo:** Figura 7 señalando el área amarilla de excedente y tabla de escenarios. Pausa antes de 3,9 años.

## Bloque 5 — Cierre (8:45 – 10:00)

> "Tres conclusiones:
> 1. Los datos evitan sobrecostos: sin auditoría no habríamos visto que un equipo usado 40 minutos
>    gobernaba toda la instalación.
> 2. Primero eficiencia, luego generación: reprogramar horarios cuesta cero y reduce la exigencia sobre
>    la batería.
> 3. La energía circular es comunitaria: un sistema sobredimensionado deja de ser una inversión lenta
>    cuando sus excedentes se aprovechan bajo el marco normativo vigente.
>
> Muchas gracias, quedamos atentos a sus preguntas."

## Preguntas probables y respuesta corta

| Pregunta | Respuesta |
| --- | --- |
| ¿Por qué baja al 89 % la cobertura con dos casas? | La batería sigue siendo de 5 kWh: atiende el día y parte de la noche; el 11 % restante viene de la red. |
| ¿Alcanza el inversor de 3 kW? | Sí, siempre que no coincidan exactamente la picadora de 1,5 kW y la lavadora; se recomienda coordinar horarios. |
| ¿Es confiable la línea base? | Son 1.000 horas consecutivas, sin nulos ni duplicados; pero solo 41,7 días, por eso se recomienda ampliar a 12 meses. |
| ¿De dónde sale el 27,5 % del seguidor? | Es el punto medio del rango 25–30 % reportado en literatura; debe medirse en banco de pruebas. |
| ¿El modelo 3D sirve para fabricar? | No sin revisión y dimensionamiento profesional; es material de comunicación. |
