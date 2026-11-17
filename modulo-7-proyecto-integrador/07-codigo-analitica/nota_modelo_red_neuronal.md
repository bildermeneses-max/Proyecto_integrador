# Nota técnica: red neuronal del cuaderno `EDANUEV_sanitizado.ipynb`

## Qué se entrenó

- Objetivo: `total_W`.
- Predictoras: `hora`, `dia_semana` y las seis potencias de equipos.
- Arquitectura: densa `64 → 32 → 16 → 1`, ReLU, optimizador Adam, 100 épocas, `batch_size=32`,
  `random_state=42`, split 80/20 y `StandardScaler`.
- Métricas reportadas en el cuaderno: MSE 34,97; RMSE 5,91 W; MAE 4,17 W; R² 0,9997.

## Interpretación correcta

`total_W` es, salvo redondeo de hasta 0,2 W, la **suma de las potencias de los equipos**. Por eso el
modelo aprendizaje una identidad aditiva: un R² de 0,9997 no demuestra capacidad de pronóstico, sino que
la variable objetivo ya contiene la información de las predictoras.

En el propio cuaderno se indica:

> "las variables de electrodomésticos particulares suman exactamente para dar como resultado la variable
> predictora final `total_W`".

## Uso adecuado en el proyecto

- ✅ Ejercicio formativo de regresión, escalamiento y evaluación con Keras.
- ✅ Complemento para mostrar que la desagregación por equipo explica la demanda total.
- ❌ No presentarlo como pronóstico independiente de demanda ni como base para dimensionar la batería.
- ❌ No usar sus métricas como evidencia de "IA predictiva avanzada" sin la salvedad anterior.

## Cómo convertirlo en un pronóstico real (trabajo futuro)

1. Definir el horizonte (por ejemplo, `total_W` de la siguiente hora).
2. Usar solo variables disponibles **antes** del horizonte: hora, día, consumo de horas previas,
   temperatura si se mide, y eventos programados.
3. Excluir las potencias simultáneas de los equipos si no se conocen de antemano.
4. Comparar contra una línea base ingenua (media móvil de 24 h y persistencia de la hora anterior).
5. Reportar MAE/RMSE en W y kWh, con intervalos de incertidumbre.

Esta distinción refuerza el criterio de autenticidad de la rúbrica: coherencia entre datos, cálculo y
decisión, sin atribuir al modelo capacidades que no tiene.
