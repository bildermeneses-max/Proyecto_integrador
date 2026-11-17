"""Recalcula la línea base y los indicadores del proyecto El Tambo (Cauca).

Uso:
    python analisis_consumo.py

El dataset se toma de ../02-linea-base/datos/ mediante una ruta relativa al
repositorio, por lo que el script funciona desde cualquier directorio.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = (
    ROOT
    / "modulo-7-proyecto-integrador"
    / "02-linea-base"
    / "datos"
    / "dataset_consumo_electrico_rural_ElTambo_Cauca.csv"
)
OUT_DIR = Path(__file__).resolve().parent / "resultados"

EQUIPOS = [
    "nevera_W",
    "lavadora_W",
    "tv_W",
    "picadora_pasto_W",
    "iluminacion_10bombillos_W",
    "otros_conectores_W",
]


def main() -> None:
    df = pd.read_csv(DATA, parse_dates=["timestamp"])
    dias = len(df) / 24

    print("=== CALIDAD DEL DATO ===")
    print(f"Observaciones: {len(df)}")
    print(f"Periodo: {df['timestamp'].min()} a {df['timestamp'].max()}")
    print(f"Días equivalentes: {dias:.2f}")
    print(f"Nulos: {int(df.isna().sum().sum())} | Duplicados: {int(df.duplicated().sum())}")
    diff = (df[EQUIPOS].sum(axis=1) - df["total_W"]).abs().max()
    print(f"Máxima diferencia suma equipos vs total_W: {diff:.2f} W")

    print("\n=== LÍNEA BASE ===")
    energia_total = df["total_kWh"].sum()
    kwh_dia = energia_total / dias
    kwh_mes = kwh_dia * 30
    kwh_anio = kwh_dia * 365
    p_media = df["total_W"].mean()
    p_max = df["total_W"].max()
    print(f"Energía total observada: {energia_total:.2f} kWh")
    print(f"Consumo diario: {kwh_dia:.2f} kWh/día")
    print(f"Consumo mensual (30 días): {kwh_mes:.2f} kWh/mes")
    print(f"Consumo anual proyectado: {kwh_anio:.2f} kWh/año")
    print(f"Potencia media: {p_media:.2f} W | Máxima: {p_max:.1f} W")
    print(f"Factor de carga: {p_media / p_max * 100:.1f} %")

    print("\n=== INVENTARIO DE CARGAS ===")
    filas = []
    for col in EQUIPOS:
        activos = df.loc[df[col] > 0, col]
        p_encendido = activos.mean() / 1000 if len(activos) else 0.0
        horas_dia = len(activos) / dias
        kwh_mes_eq = p_encendido * horas_dia * 30
        filas.append(
            {
                "equipo": col,
                "potencia_encendido_kW": p_encendido,
                "horas_dia": horas_dia,
                "kwh_mes": kwh_mes_eq,
            }
        )
    inv = pd.DataFrame(filas)
    inv["participacion_pct"] = inv["kwh_mes"] / inv["kwh_mes"].sum() * 100
    inv["acumulado_pct"] = inv["participacion_pct"].cumsum()
    inv = inv.sort_values("participacion_pct", ascending=False).reset_index(drop=True)
    print(inv.round(3).to_string(index=False))
    print(f"Total coincidente con línea base: {inv['kwh_mes'].sum():.2f} kWh/mes")

    print("\n=== PERFIL Y CORRELACIONES ===")
    perfil = df.groupby("hora")["total_W"].mean()
    print(f"Hora pico: {int(perfil.idxmax())}:00 con {perfil.max():.0f} W")
    print(f"Carga 01:00-04:00: {df.loc[df['hora'].between(1, 4), 'total_W'].mean():.0f} W")
    corr = df[EQUIPOS + ["total_W"]].corr()["total_W"].sort_values(ascending=False)
    print(corr.round(3).to_string())

    print("\n=== DISEÑO FOTOVOLTAICO ===")
    hsp, pr, ganancia = 4.5, 0.78, 0.275
    potencia_kwp = 2.2
    fijo = potencia_kwp * hsp * pr
    con_seguidor = fijo * (1 + ganancia)
    demanda_cubierta = min(kwh_dia, con_seguidor)
    excedente = con_seguidor - demanda_cubierta
    print(f"Generación fija: {fijo:.2f} kWh/día")
    print(f"Generación con seguidor: {con_seguidor:.2f} kWh/día")
    print(f"Excedente: {excedente:.2f} kWh/día ({excedente / con_seguidor * 100:.1f} % de la generación)")
    ahorro = kwh_anio * 1000
    print(f"Ahorro bruto referencial: ${ahorro:,.0f} COP/año")
    print(f"Inversión referencial: $18.500.000 COP | retorno simple: {18_500_000 / ahorro:.1f} años")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    resumen = pd.DataFrame(
        [
            ("observaciones", len(df), "registros"),
            ("consumo_diario_kwh", kwh_dia, "kWh/día"),
            ("consumo_mensual_kwh", kwh_mes, "kWh/mes"),
            ("consumo_anual_kwh", kwh_anio, "kWh/año"),
            ("potencia_media_w", p_media, "W"),
            ("potencia_maxima_w", p_max, "W"),
            ("factor_carga_pct", p_media / p_max * 100, "%"),
            ("generacion_fija_kwh_dia", fijo, "kWh/día"),
            ("generacion_seguidor_kwh_dia", con_seguidor, "kWh/día"),
            ("excedente_kwh_dia", excedente, "kWh/día"),
            ("ahorro_bruto_cop_anio", ahorro, "COP/año"),
        ],
        columns=["indicador", "valor", "unidad"],
    )
    resumen.to_csv(OUT_DIR / "resumen.csv", index=False)
    print(f"\nResumen guardado en {OUT_DIR / 'resumen.csv'}")


if __name__ == "__main__":
    main()
