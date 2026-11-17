# Hugging Face Space — runtime de Gradio

Este es el motor de la app. Vercel sólo hace de proxy/landing; Gradio corre aquí.

## Archivos

- `app.py` — interfaz Gradio (8 pestañas + KPIs).
- `data.py` — carga validada y cacheada, agregaciones, simulador.
- `dataset_consumo_electrico_rural_ElTambo_Cauca.csv` — 1000 filas.
- `requirements.txt` — dependencias.

## Crear el Space

1. Entra a https://huggingface.co/new-space
2. **SDK**: Gradio · **Visibility**: Public · nombre, p. ej. `dashboard-consumo-el-tambo`.
3. Sube los 4 archivos de esta carpeta al repo del Space.
4. Espera a que el estado cambie a **Running**. URL: `https://<TU-USUARIO>-<TU-SPACE>.hf.space`.

## Variable de entorno (sólo si usas la landing con prefijo `/app`)

En **Settings → Variables and secrets**, crea:

```
GRADIO_ROOT_PATH = /app
```

Si usas `vercel-simple` (proxy de todo el dominio), **no hace falta** definirla.

## Notas

- El free tier se duerme tras un tiempo de inactividad; el primer request puede tardar unos segundos.
- `share=False`: no se genera enlace `gradio.live`; el acceso es por el dominio del Space o por tu dominio de Vercel.
- No hay tokens en el código. Si el notebook original tenía un token de ngrok, revoquélo en ngrok.
