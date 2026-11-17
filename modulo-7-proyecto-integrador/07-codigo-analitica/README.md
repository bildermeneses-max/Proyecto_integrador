# 7. Código fuente y analítica

| Archivo | Descripción | Origen |
| --- | --- | --- |
| `analisis_consumo.py` | Recalcula calidad, línea base, inventario, Pareto, perfil, correlaciones y escenarios FV desde el CSV | Nuevo, reproducible |
| `EDANUEV_sanitizado.ipynb` | EDA + red neuronal Keras del cuaderno original | `EDANUEV.ipynb` (sin cambios funcionales) |
| `Untitled17_sanitizado.ipynb` | Cuaderno de Gradio/Streamlit y despliegue | `Untitled17.ipynb` (token de ngrok eliminado) |
| `nota_modelo_red_neuronal.md` | Interpretación correcta de las métricas del modelo | Nuevo |
| `requirements.txt` | Dependencias mínimas | Nuevo |

## Ejecución

```bash
pip install -r requirements.txt
python analisis_consumo.py
```

El script imprime todas las cifras de la línea base y guarda un resumen en `resultados/`
(dentro de esta carpeta) cuando se ejecuta. El dataset se lee desde
`../02-linea-base/datos/` mediante ruta relativa al repositorio.

## Saneamiento de secretos

El cuaderno `Untitled17.ipynb` original contenía un token de ngrok en texto plano. En la copia
versionada:

- el valor se reemplazó por `os.environ.get("NGROK_AUTHTOKEN", "")`;
- se importó `os`;
- `demo.launch` usa `share=False` por defecto;
- el token original **no aparece** en este repositorio.

Acción pendiente del propietario: **revocar ese token en el panel de ngrok** y, si se necesita túnel,
generar uno nuevo y usarlo solo por variable de entorno.

## Trazabilidad

- Python 3 · pandas · NumPy · matplotlib · seaborn · scikit-learn · TensorFlow/Keras · Gradio · Streamlit.
- Correspondencia de cifras: `../02-linea-base/linea_base.md`, `../04-renovables-almacenamiento/diseno_fotovoltaico.md`
  e `informe_tecnico_original.docx`.
- Las gráficas del informe se reprodujeron desde el mismo dataset; los archivos fuente de las imágenes
  originales no estaban incluidos en los archivos compartidos.
