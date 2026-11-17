# Dashboard web — código local y deploy público

## ¿Qué hay aquí?

Código fuente **local** del dashboard de consumo eléctrico, incorporado desde
`C:\Users\ASUS\Documents\Proyecto predeterminado\gradio_dashboard\vercel_deploy\`.

Corresponde a la **Arquitectura A** del plan de despliegue: la interfaz Gradio corre en un
Hugging Face Space y Vercel sirve la landing y/o actúa como proxy mediante `rewrites`.
Es una alternativa reproducible al dashboard, **no el código del sitio en vivo**.

| Archivo / carpeta | Contenido |
| --- | --- |
| `hf-space/app.py` | Interfaz Gradio de 8 pestañas + tarjetas de KPIs |
| `hf-space/data.py` | Carga validada y cacheada, agregaciones y simulador |
| `hf-space/requirements.txt` | Dependencias del Space |
| `hf-space/dataset_consumo_electrico_rural_ElTambo_Cauca.csv` | Copia del dataset (1.000 filas) |
| `vercel-landing/` | Landing estática + `vercel.json` con prefijo `/app` |
| `vercel-simple/` | `vercel.json` de proxy de todo el dominio |
| `.env.example` | Plantilla de configuración |
| `DESPLIEGUE.md` | Pasos de despliegue, saneado de secretos |

## Cifras verificadas de la landing

Calculadas desde el CSV con pandas, sin datos nuevos:

| Indicador | Valor |
| --- | ---: |
| Registros | 1.000 |
| Energía total | 201,2 kWh |
| Pico de demanda | 2.541,9 W |
| Potencia media | 201,2 W |
| Equipo líder | Nevera (77,9 W) |

## Deploy público (evidencia real, verificada el 2026-11-17)

- URL: **https://energia-circular.vercel.app/**
- Respuesta HTTP: `200` (HTML, 47.023 bytes).
- CSV descargable en `/data/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`: `200` (64.173 bytes).
- Interfaz: 8 secciones (Explicación, Datos, Estadísticas, Univariado, Bivariado,
  Perfil diario, Correlación, Simulador de tarifa), tema claro/oscuro y botón de impresión.
- Implementación observada: **Next.js + funciones Python serverless (pandas)** — es decir,
  la **Arquitectura B** descrita en el plan, distinta del código Gradio/HF de esta carpeta.

### Estado real de la analítica en el deploy

> ⚠️ **No funciona completamente en este momento.** La petición `GET /api/kpis` responde
> `500` y la interfaz muestra «No pudimos cargar esta sección — El servidor no pudo procesar
> la solicitud». Al recorrer las pestañas también se observan llamadas a `/api/stats` y
> `/api/hourly`. Por eso el deploy se registra como **evidencia de publicación**, no como
> evidencia de analítica funcionando.

| Ítem | Estado |
| --- | --- |
| Sitio públicamente accesible | ✅ Verificado (HTTP 200) |
| CSV servido desde el deploy | ✅ Verificado (HTTP 200) |
| Funciones serverless respondiendo | 🟡 PENDIENTE: `/api/kpis` → 500 |
| Código fuente de la versión Next.js | 🟡 PENDIENTE: no estaba en los archivos compartidos |

## Despliegue local

```bash
# Hugging Face Space: subir el contenido de hf-space/ (SDK: Gradio)
# Vercel: elegir vercel-simple/ o vercel-landing/ y rellenar el placeholder
cd vercel-simple
vercel --prod
```

Los placeholders `TU-USUARIO-TU-SPACE.hf.space` son **PENDIENTE de reemplazar** con la URL
real del Space. Ver `DESPLIEGUE.md`.

## Seguridad

- El token de ngrok que aparecía en el cuaderno original **no se reproduce en este repositorio**.
- Sigue pendiente su **revocación/rotación en el panel de ngrok**.
- No hay otros secretos: `vercel.json` sólo contiene un placeholder público.

## Trazabilidad

- Mismo dataset que `../02-linea-base/datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`.
- Código tomado sin cambios funcionales de la carpeta local `gradio_dashboard/vercel_deploy/`.
- Única modificación: el texto del aviso de seguridad en `DESPLIEGUE.md`, para no reproducir el token.
