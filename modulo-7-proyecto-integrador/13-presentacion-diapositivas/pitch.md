# Pitch de sustentación — 15 diapositivas en 5 minutos

**Duración total:** ~5 minutos (15–25 s por diapositiva).  
**Formato:** usa las flechas del teclado y el modo presentación (`F`).  
**Tono:** técnico, cercano y honesto. Cada cifra dicha está en el dataset o en los documentos del repo.

> Regla de oro: si te preguntan por algo que no está en el repositorio, responde
> «eso quedó marcado como PENDIENTE», no lo improvises.

---

## Versión de 5 minutos, diapositiva por diapositiva

### 1 · Portada (20 s)

> Buenos días. Somos Andrés Felipe Rodríguez, Brandon Meneses y Valeria Velasco.
> Les presentamos nuestro proyecto integrador de **Energía Circular Inteligente 5.0**,
> a partir de un caso real en **El Tambo, Cauca**. Nuestra idea fue simple:
> **primero medir, después entender y recién ahí proponer**.

### 2 · El caso (20 s)

> Medimos **1.000 horas consecutivas**, casi 42 días entre enero y febrero de 2025,
> con 11 variables, **cero nulos y cero duplicados**. No inventamos ni un dato:
> toda la línea base sale de ese CSV.

### 3 · Metodología (15 s)

> Cuatro pasos: **medir, diagnosticar, diseñar y validar**. Y una regla de rigor:
> llamamos *pico* a toda hora por encima de la media más dos desviaciones estándar.

### 4 · Radiografía (25 s)

> El consumo es de **4,83 kWh al día**, pero no es parejo. De noche bastan **74 vatios**;
> a las **17:00 sube a 505 vatios**, cuando ya no hay sol. El factor de carga es de solo **7,9 %**.

**Frase ancla:** *«El pico llega cuando se apaga el sol.»*

### 5 · Usos significativos (25 s)

> **Nevera y picadora explican el 59,2 %** del consumo. La nevera es carga base;
> la picadora aporta **251 de los 505 vatios** del pico y opera solo 0,65 h al día.
> Es carga programable: mover la molienda al mediodía baja el pico de 505 a 255 vatios, sin comprar nada.

### 6 · Distribución y picos (20 s)

> El máximo puntual fue de **2.541,9 vatios**, pero solo el **5,5 % de las horas** supera los 500.
> La lección: un promedio diario esconde el problema; **hay que mirar la forma de la curva**.

### 7 · Correlaciones (15 s)

> La picadora se mueve con el total (**r = 0,91**); la TV y la iluminación siguen la hora del día
> (**0,58** y **0,48**). Hay oportunidad de cambiar horarios antes que de comprar equipos.

### 8 · Solución fotovoltaica (25 s)

> Diseñamos **2,2 kWp** en cuatro paneles de 550 W, inversor híbrido de 3 kW
> y batería LiFePO₄ de 5 kWh. Generamos **9,85 kWh al día con seguidor** frente a 7,72 fijo,
> y cubrimos el 100 % del día promedio.

**Aclaración:** *«La demanda es medida; la generación es simulada con supuestos declarados.»*

### 9 · Seguidor Arduino (20 s)

> Dos sensores LDR este–oeste, un Arduino Uno y un actuador lineal con pulsos de 1,5 s.
> Ganancia estimada: **27,5 %**. Es un esquema conceptual: **no es foto del prototipo**.

### 10 · Excedente compartido (25 s)

> Generamos 9,85, consumimos 4,83 y sobran **4,78 kWh al día**. Una segunda vivienda
> eleva la demanda conjunta a **9,66 kWh** y encaja con lo generado. El retorno baja de
> **11,7 años** a **6,8 con batería** y **3,9 sin batería**.

**Frase ancla:** *«El excedente dejó de ser un problema y se volvió el modelo de negocio.»*

### 11 · Circularidad y carbono (15 s)

> Batería LiFePO₄ con BMS, ventilación y ruta de reciclaje por definir.
> Evitamos **0,29 toneladas de CO₂ al año**, bajo RETIE, CREG 174 de 2021 y Ley 1715.

### 12 · Viabilidad (20 s)

> Inversión de **$18.500.000 COP** y ahorro de **$1.762.132 anuales**.
> Cinco escenarios trazables: de 11,7 años en el individual a **6,8 compartido con batería**
> y **3,9 sin ella**.

### 13 · Dashboard publicado (20 s)

> Publicamos en `energia-circular.vercel.app`: sitio y CSV responden 200 y hay ocho secciones.
> **Transparencia:** `/api/kpis` devuelve 500; quedó documentado como pendiente,
> no lo presentamos como un éxito.

### 14 · Estado real (15 s)

> Listos: datos, diseño, IoT, finanzas, informe, infografía, dashboard y esta presentación.
> Pendientes: RAG ejecutado, modelo 3D, corrección de la API y revocación del token de ngrok.
> **Sin evidencia real no afirmamos resultado.**

### 15 · Cierre (20 s)

> Medimos 1.000 horas, encontramos un 59,2 % concentrado en dos equipos, generamos 9,85 kWh
> al día y detectamos 4,78 kWh compartibles. **Pasamos del diagnóstico a una propuesta con impacto
> ambiental, económico y territorial.** Está todo en
> `github.com/bildermeneses-max/Proyecto_integrador`. Gracias.

**Gesto:** quédate en la infografía mientras respondes.

---

## Versión relámpago (60 segundos)

> Somos Andrés, Brandon y Valeria. Medimos 1.000 horas reales en una finca de El Tambo, Cauca,
> y encontramos que el 59,2 % del consumo se concentra en nevera y picadora, con un pico de 505 vatios
> a las 5 de la tarde, justo cuando se apaga el sol.
>
> Diseñamos un sistema de 2,2 kWp con batería de 5 kWh y seguidor Arduino: genera 9,85 kWh al día,
> cubre toda la demanda y deja 4,78 kWh de excedente. Al compartirlo con una segunda vivienda,
> el retorno baja de 11,7 a 6,8 años con batería y a 3,9 sin ella. Además evitamos 0,29 toneladas
> de CO₂ al año.
>
> Todo está en el repositorio, con datos medidos, supuestos declarados y pendientes marcados. Gracias.

---

## Preguntas probables y respuestas cortas

| Pregunta | Respuesta sugerida |
| --- | --- |
| ¿Los consumos son simulados? | **No.** La demanda viene de 1.000 mediciones horarias. La generación sí es simulada, con HSP 4,5, PR 0,78 y ganancia del seguidor 27,5 %, todos declarados. |
| ¿Por qué compartir la generación? | Porque el 48,6 % de lo generado quedaba como excedente. La demanda conjunta estimada, 9,66 kWh/día, casi iguala los 9,85 generados. |
| ¿Es legal compartir? | El marco es la CREG 174 de 2021 y la Ley 1715. **Falta validar el esquema con el operador de red**; por eso está marcado como supuesto. |
| ¿El seguidor está construido? | Hay código Arduino y un esquema conceptual. **No hay foto ni medición del prototipo en banco**; es un pendiente real. |
| ¿El dashboard funciona completo? | El sitio y el CSV responden 200, pero `/api/kpis` da 500. Es un pendiente documentado, no un logro oculto. |
| ¿Y el asistente RAG / modelo 3D? | Estructura y corpus listos; falta ejecutar el RAG con citas y generar el modelo 3D con ficha de procedencia. |
| ¿Qué pasó con el token de ngrok? | Se saneó de todas las copias versionadas. **Su revocación en el panel de ngrok sigue pendiente.** |
| ¿De dónde sale el 59,2 %? | De la línea base calculada con pandas desde el CSV: nevera 38,7 % + picadora 20,5 %. |

---

## Antes de sustentar

- [ ] Ensayar dos veces con cronómetro: versión completa ~5 min, relámpago ~60 s.
- [ ] Si te sobra tiempo, desarrolla la diapositiva 10 (el excedente compartido); es el giro del proyecto.
- [ ] Si vas corto de tiempo, salta la diapositiva 7 y pasa directo de correlaciones a la solución FV.
- [ ] Confirmar con los autores el nombre del docente y la duración exacta exigida.
- [ ] No abrir el video ni el guion antiguo: no forman parte de este entregable.
