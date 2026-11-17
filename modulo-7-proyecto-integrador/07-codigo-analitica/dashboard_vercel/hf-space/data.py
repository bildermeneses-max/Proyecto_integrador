"""Capa de datos del dashboard de consumo eléctrico rural.

Separa por completo la lógica de datos de la interfaz (Gradio).
Incluye validación de esquema, carga cacheada, agregaciones y simulador.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

CSV_NAME = "dataset_consumo_electrico_rural_ElTambo_Cauca.csv"

COLUMNAS_ESPERADAS = [
    "timestamp",
    "hora",
    "dia_semana",
    "nevera_W",
    "lavadora_W",
    "tv_W",
    "picadora_pasto_W",
    "iluminacion_10bombillos_W",
    "otros_conectores_W",
    "total_W",
    "total_kWh",
]

EQUIPOS = [
    "nevera_W",
    "lavadora_W",
    "tv_W",
    "picadora_pasto_W",
    "iluminacion_10bombillos_W",
    "otros_conectores_W",
]


def _rutas_candidatas() -> list[Path]:
    return [
        Path(__file__).resolve().parent / CSV_NAME,
        Path("/content") / CSV_NAME,
        Path.cwd() / CSV_NAME,
    ]


@lru_cache(maxsize=1)
def load_data() -> pd.DataFrame:
    """Carga y valida el dataset una sola vez por proceso."""
    ruta = next((p for p in _rutas_candidatas() if p.exists()), None)
    if ruta is None:
        raise FileNotFoundError(
            f"No se encontró {CSV_NAME}. Sube el CSV al espacio junto a app.py."
        )

    df = pd.read_csv(ruta)
    faltan = [c for c in COLUMNAS_ESPERADAS if c not in df.columns]
    if faltan:
        raise ValueError(f"El CSV no tiene las columnas esperadas: {faltan}")

    for columna in COLUMNAS_ESPERADAS:
        if columna != "timestamp":
            df[columna] = pd.to_numeric(df[columna], errors="coerce")

    if df[COLUMNAS_ESPERADAS].isna().any().any():
        raise ValueError("El CSV contiene valores no numéricos en columnas numéricas.")

    return df


@lru_cache(maxsize=1)
def summary_stats() -> pd.DataFrame:
    """Estadísticas descriptivas redondeadas a 2 decimales."""
    return load_data().describe().round(2)


@lru_cache(maxsize=1)
def kpis() -> dict[str, float | str | int]:
    """Indicadores clave calculados sobre el dataset completo."""
    df = load_data()
    medias = df[EQUIPOS].mean()
    equipo_top = str(medias.idxmax())
    media_total = float(df["total_W"].mean())
    desviacion = float(df["total_W"].std())
    umbral_pico = media_total + 2 * desviacion

    return {
        "filas": int(len(df)),
        "energia_total_kwh": float(df["total_kWh"].sum()),
        "pico_w": float(df["total_W"].max()),
        "promedio_w": media_total,
        "equipo_top": equipo_top.replace("_W", "").replace("_", " "),
        "equipo_top_w": float(medias.max()),
        "picos": int((df["total_W"] > umbral_pico).sum()),
        "umbral_pico_w": umbral_pico,
    }


def filtrar(potencia_min: float, potencia_max: float, limite: int = 100) -> pd.DataFrame:
    """Filtra filas por rango de potencia total (W)."""
    df = load_data()
    return df[(df["total_W"] >= potencia_min) & (df["total_W"] <= potencia_max)].head(
        limite
    )


@lru_cache(maxsize=32)
def serie_univariada(variable: str) -> pd.Series:
    """Serie numérica para el histograma univariado."""
    if variable not in COLUMNAS_ESPERADAS:
        raise ValueError(f"Variable desconocida: {variable}")
    return load_data()[variable].dropna()


@lru_cache(maxsize=32)
def datos_bivariados(var_x: str, var_y: str) -> pd.DataFrame:
    """Par de columnas para el gráfico de dispersión."""
    df = load_data()
    for variable in (var_x, var_y):
        if variable not in df.columns:
            raise ValueError(f"Variable desconocida: {variable}")
    return df[[var_x, var_y]].dropna()


@lru_cache(maxsize=1)
def perfil_hora() -> pd.DataFrame:
    """Consumo promedio por hora y equipo."""
    columnas = [c for c in EQUIPOS if c != "otros_conectores_W"]
    return load_data().groupby("hora")[columnas].mean()


@lru_cache(maxsize=1)
def matriz_correlacion() -> pd.DataFrame:
    """Correlación de Pearson entre variables numéricas."""
    df = load_data().select_dtypes(include=[np.number])
    return df.corr()


@lru_cache(maxsize=64)
def simular(
    nevera_h: float,
    lavadora_h: float,
    tv_h: float,
    picadora_h: float,
    bombillos_h: float,
    tarifa_kwh: float,
) -> tuple[float, float]:
    """Estima energía mensual (kWh) y costo (COP) a partir de potencias reales."""
    df = load_data()
    potencias = {
        "nevera_W": nevera_h,
        "lavadora_W": lavadora_h,
        "tv_W": tv_h,
        "picadora_pasto_W": picadora_h,
        "iluminacion_10bombillos_W": bombillos_h,
    }
    energia_diaria = sum(
        float(df[equipo].mean()) * horas / 1000 for equipo, horas in potencias.items()
    )
    energia_mensual = energia_diaria * 30
    return energia_mensual, energia_mensual * float(tarifa_kwh)
