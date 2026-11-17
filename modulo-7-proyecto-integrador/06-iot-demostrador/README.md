# 6. Demostrador IoT / medición (real o emulado)

Este entregable reúne el **control del seguidor solar** y los **dashboards de medición y visualización**.
El seguidor es un diseño conceptual con código de referencia; los dashboards son demostradores emulados
que consumen el dataset real de la finca.

| Archivo | Qué demuestra | Estado |
| --- | --- | --- |
| `seguidor_arduino.ino` | Lógica de seguimiento con dos LDR, zona muerta, finales de carrera y retorno nocturno | Código de referencia, sin banco de pruebas |
| `dashboard_gradio.py` | Filtros, estadísticas, univariado, bivariado, perfil horario, correlación y simulador de tarifa | Ejecutable con `python dashboard_gradio.py` |
| `dashboard_streamlit.py` | Misma funcionalidad en Streamlit, con pestañas | Ejecutable con `streamlit run dashboard_streamlit.py` |

## Variables y flujo de datos

- Entrada: `../02-linea-base/datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`.
- Variables monitorizadas: potencia de seis cargas, `total_W`, `total_kWh`, `hora` y `dia_semana`.
- Salida: tablas filtrables, histogramas, dispersiones, matriz de correlación, perfil horario y estimación
  de costo mensual.
- El seguidor no envía datos aún: su demostración es la lógica de control embebida. Para un prototipo real
  se requieren sensores, actuador, fuente, protecciones y registro de temperatura/estado.

## Puesta en marcha

```bash
pip install -r ../07-codigo-analitica/requirements.txt
python dashboard_gradio.py
# o
streamlit run dashboard_streamlit.py
```

Ambos scripts resuelven el dataset con ruta relativa al repositorio, por lo que funcionan si se ejecutan
desde cualquier directorio.

## Pruebas sugeridas (pendientes de registrar)

| Prueba | Criterio esperado |
| --- | --- |
| Filtro 51–2541,9 W | Devuelve hasta 100 filas coherentes con el rango |
| Perfil horario | Pico visible a las 17:00 (~505 W) y valle nocturno (~74 W) |
| Correlación | `picadora_pasto_W` vs `total_W` ≈ 0,91 |
| Simulador con 0,65 h de picadora y tarifa $1.000 | Orden de magnitud coherente con la línea base |
| Seguidor con lámpara lateral | El actuador gira hacia el lado con mayor lectura LDR |
| Seguidor con ambos LDR tapados | Retorno al Este y sin movimiento continuo |

## Seguridad

- No exponer dashboards públicamente sin autorización. El cuaderno original usaba un túnel ngrok con token
  embebido; aquí `demo.launch(share=False)` y ngrok, si se usa, debe configurarse con `NGROK_AUTHTOKEN`.
- En el montaje real: seccionador DC, fusibles, DPS, puesta a tierra, EPP y finales de carrera.

## Evidencia pendiente

- [ ] Capturas de los dashboards ejecutándose con datos reales.
- [ ] Registro de prueba del seguidor con horas de giro y consumo del actuador.
- [ ] Esquema eléctrico del prototipo y checklist RETIE.
