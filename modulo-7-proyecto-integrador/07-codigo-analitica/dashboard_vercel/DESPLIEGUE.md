# Despliegue en Vercel — pasos exactos

> Todo ya está preparado. Sólo faltan tus credenciales y rellenar un placeholder.

## Por qué esta arquitectura

Vercel es serverless: **no puede ejecutar un servidor Gradio persistente** (ni su cola de eventos por SSE/WebSocket). Por eso:

- **Gradio corre en Hugging Face Spaces** (arquitectura A del prompt maestro).
- **Vercel** sirve la landing y/o hace de proxy con un `rewrite`.

No hay que instalar Gradio en Vercel ni pelearse con `vercel.json` de Python.

## Estructura

```
dashboard_vercel/
├── hf-space/                 # subir tal cual a un Space de Hugging Face
│   ├── app.py
│   ├── data.py
│   ├── requirements.txt
│   ├── README.md
│   └── dataset_consumo_electrico_rural_ElTambo_Cauca.csv
├── vercel-simple/            # opción 1: todo el dominio apunta al Space
│   └── vercel.json
└── vercel-landing/           # opción 2: landing en / + app en /app
    ├── vercel.json
    └── index.html
```

---

## Paso 1 — Crear el Space (5 min)

1. Abre https://huggingface.co/new-space
2. Configura:
   - **Owner**: tu usuario
   - **Space name**: `dashboard-consumo-el-tambo` (o el que quieras)
   - **SDK**: `Gradio`
   - **Visibility**: `Public`
3. Crea el Space y sube **los 5 archivos** de `hf-space/`.
   - Puedes arrastrarlos en la pestaña **Files and versions**, o:
   ```bash
   git clone https://huggingface.co/spaces/TU-USUARIO/TU-SPACE
   cp hf-space/* TU-SPACE/
   cd TU-SPACE && git add . && git commit -m "deploy" && git push
   ```
4. Espera a que el estado sea **Running**. Anota la URL:
   ```
   https://TU-USUARIO-TU-SPACE.hf.space
   ```

---

## Paso 2 — Elegir variante de Vercel

### Opción 1 (recomendada, más robusta): proxy de todo el dominio

```bash
cd vercel-simple
```

Edita `vercel.json` y reemplaza el placeholder:

```json
"destination": "https://TU-USUARIO-TU-SPACE.hf.space/$1"
```

→ por ejemplo `https://juan-dashboard-consumo-el-tambo.hf.space/$1`.

Ventaja: no hay que tocar `root_path`; la app funciona igual en el Space y en tu dominio de Vercel.

### Opción 2: landing propia + app en `/app`

```bash
cd vercel-landing
```

1. Reemplaza los dos placeholders de `vercel.json` con tu URL del Space.
2. En el Space: **Settings → Variables and secrets → New variable**
   ```
   GRADIO_ROOT_PATH = /app
   ```
3. Reinicia el Space.
4. La landing queda en `/` y el dashboard en `/app`.

---

## Paso 3 — Desplegar en Vercel

Primera vez en esta máquina:

```powershell
npm install -g vercel
vercel login
```

Desde la carpeta de la variante elegida:

```powershell
vercel            # preview (opcional)
vercel --prod     # producción
```

Si te pregunta por el proyecto, acepta los valores por defecto. Vercel detecta `vercel.json` automáticamente.

---

## Paso 4 — Verificar

```powershell
curl -I https://TU-PROYECTO.vercel.app
```

Comprueba en el navegador:

- [ ] Cargan las 8 pestañas.
- [ ] El filtro de potencia devuelve filas.
- [ ] Los dropdowns redibujan los gráficos.
- [ ] El simulador muestra energía y costo en COP.

Si la **Opción 2** muestra la página pero el dashboard queda en blanco, casi siempre es `GRADIO_ROOT_PATH` mal puesto o falta el rewrite `/app/(.*)`. Usa la Opción 1.

---

## Notas importantes

- **Cold start**: el plan gratuito de HF duerme el Space. El primer acceso puede tardar 10–30 s. Avísalo en la landing o usa un plan con `always-on`.
- **SSE**: Gradio usa SSE por defecto; los rewrites de Vercel lo soportan. Si los botones no responden, revisa la pestaña Network del navegador.
- **Seguridad**: el cuaderno original contenía un token de ngrok en texto plano. Ese valor **no se usó ni se reproduce en este repositorio**. Debe revocarse/rotarse en el panel de ngrok.
- **Secretos**: no hay tokens en estos archivos. Si algún día los necesitas, usa variables de entorno de Vercel/HF, nunca texto plano.

## Comandos rápidos (resumen)

```bash
# 1. Subir hf-space/ a Hugging Face y copiar su URL
# 2. Pegar la URL en vercel.json
# 3. Desplegar
npm i -g vercel
vercel login
cd vercel-simple   # o vercel-landing
vercel --prod
```
