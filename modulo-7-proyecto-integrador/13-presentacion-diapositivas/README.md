# 13. Presentación dinámica del proyecto integrador

Presentación visual de **15 diapositivas 16:9**, pensada para sustentación: más imágenes que texto,
con gráficos calculados desde los datos reales del caso.

| Archivo | Uso |
| --- | --- |
| `index.html` | Presentación dinámica (navegación, transiciones, contadores animados, autoplay, pantalla completa). |
| `presentacion_proyecto_integrador.pdf` | Versión impresa de 15 páginas 16:9 (2,69 MB), generada desde el HTML. |
| `assets/01…08_*.png` | Ocho gráficos generados desde el dataset y los escenarios. |
| `assets/producto_visual_el_tambo.jpeg` | Copia de la infografía real del caso (ver `../09-producto-visual/README.md`). |
| `generar_graficos.py` | Script reproducible que regenera los ocho gráficos. |

## Cómo verla

- **Opción simple:** abrir `index.html` con doble clic en Chrome o Edge.
- **Opción con servidor local** (recomendada si el navegador bloquea archivos locales):

  ```bash
  cd modulo-7-proyecto-integrador/13-presentacion-diapositivas
  python -m http.server 8769
  # abrir http://127.0.0.1:8769/
  ```

- **Controles:** `←` / `→` navegan · `Espacio` avanza · `Inicio`/`Fin` · `F` pantalla completa ·
  `P` imprime/exporta a PDF. También hay botones inferiores y gestos de deslizamiento en móvil.
- **Autoplay:** botón `▶` (8 s por diapositiva); `❚❚` lo detiene.

## Cómo exportar el PDF

El PDF ya está incluido y tiene 15 páginas de 16 × 9 in con la regla `@media print` del HTML.
Para regenerarlo con Chrome/Edge:

```powershell
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$url = "http://127.0.0.1:8769/index.html"
$out = "presentacion_proyecto_integrador.pdf"
& $chrome --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf=$out $url
```

## Guion visual de las diapositivas

| # | Diapositiva | Pieza visual principal |
| ---: | --- | --- |
| 1 | Portada: «Del consumo medido a la energía compartida» | Infografía real del caso |
| 2 | El caso: 1.000 mediciones, 41,7 días, 11 variables | Infografía + tarjetas de cifras |
| 3 | Metodología en cuatro pasos | Histograma de potencia + flujo |
| 4 | Radiografía: el pico llega cuando se apaga el sol | Perfil horario + KPIs |
| 5 | Usos significativos: 59,2 % en dos equipos | Donut + Pareto |
| 6 | Distribución y picos: carga base + eventos intensos | Histograma + regla media + 2σ |
| 7 | Correlaciones entre equipos | Mapa de calor |
| 8 | Solución FV: 2,2 kWp + batería | Balance diario + flujo de componentes |
| 9 | Seguidor solar con Arduino | Esquema SVG dibujado para la presentación |
| 10 | Excedente compartido: 9,85 − 4,83 = 4,78 kWh/día | Flujo de balance |
| 11 | Circularidad y carbono: 0,29 t CO₂/año | Barra de carbono + tarjetas |
| 12 | Viabilidad: retorno de 3,9 a 11,7 años | Gráfico de cinco escenarios |
| 13 | Analítica publicada en Vercel | Esquema de la interfaz (8 secciones) |
| 14 | Estado real: listo vs. pendiente | Checklist visual |
| 15 | Cierre: de los datos a la acción energética | Infografía real + cifras centrales |

## Cifras y trazabilidad

Todas las cifras visibles se verificaron contra el dataset o contra los documentos del repositorio.

| Cifra | Valor | Origen |
| --- | --- | --- |
| Mediciones / variables / periodo | 1.000 / 11 / 01-01-2025 → 11-02-2025 15:00 | CSV de línea base |
| Demanda media | 4,83 kWh/día · 201,16 W · 2.541,9 W máx. | `02-linea-base/linea_base.md` |
| Pico horario | 505 W a las 17:00 (250,9 W de picadora) | CSV, media por hora |
| Carga nocturna (01–04 h) | 74,3 W | CSV |
| Horas > 500 W | 5,5 % | CSV |
| Sesgo de la distribución | 4,88 | CSV |
| Factor de carga | 7,9 % | CSV, media / máximo |
| USE (nevera + picadora) | 59,2 % (38,7 % + 20,5 %) | `02-linea-base/linea_base.md` |
| Correlaciones | picadora-total 0,91; lavadora-total 0,44; hora-TV 0,58; hora-iluminación 0,48 | CSV |
| Generación / excedente | 9,85 / 4,78 kWh/día | `04-renovables-almacenamiento/diseno_fotovoltaico.md` |
| Demanda conjunta supuesta | 9,66 kWh/día | `11-evaluacion-financiera/evaluacion_financiera.md` |
| Retornos | 11,7 / 9,7 / 9,4 / 6,8 / 3,9 años | `11-evaluacion-financiera/escenarios.csv` |
| Carbono evitado | 0,29 t CO₂/año (factor 0,164 kgCO₂/kWh) | `05-circularidad-carbono/circularidad_carbono.md` |
| Dashboard público | HTTP 200, CSV 200, `/api/kpis` → 500 | Verificación del 2026-11-17 |

El esquema del seguidor (diapositiva 9) es un **dibujo conceptual** del código de referencia
`seguidor_arduino.ino`, no una fotografía del prototipo; está rotulado así en la diapositiva.

## Origen de las imágenes y declaración de IA

- **Infografía:** imagen real/captura fotográfica aportada por el equipo, versionada en
  `../09-producto-visual/`. Su ficha mantiene en `PENDIENTE` los datos de dispositivo, fecha y
  archivo editable que no fueron confirmados. No se extrajo texto de la imagen por OCR.
- **Gráficos:** generados con matplotlib/seaborn desde el CSV y los escenarios; `generar_graficos.py`
  reproduce los ocho archivos sin diferencias de SHA-256.
- **Ilustraciones IA:** se intentaron cuatro ilustraciones para las diapositivas 1, 8, 10 y 11, pero
  el generador devolvió `Invalid credential`. **No se incluyó ninguna imagen generada con IA.**
  La versión entregada usa únicamente la infografía real, gráficos calculados y un esquema SVG propio.
- **HTML/PDF:** ensamblado y verificado en este repositorio; sin herramientas de Canva (no accesible
  desde este entorno). El resultado es editable en cualquier editor de texto y exportable a PDF.

## Estado real

- ✅ HTML verificado: 15 diapositivas, 12 referencias de imagen cargadas, 0 errores de consola,
  sin desbordes de contenido en 912 × 670 px.
- ✅ PDF verificado: 15 páginas, 15 objetos `/MediaBox` de 16 × 9 in.
- ✅ Cifras verificadas contra el CSV y los documentos de origen.
- 🟡 PENDIENTE: sustituir la infografía por una versión editable si el equipo la entrega; completar
  la validación humana de la presentación por los tres autores.
