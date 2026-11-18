"""Regenera los ocho gráficos de la presentación desde el dataset y el archivo de escenarios.

Uso (desde cualquier directorio):
    python generar_graficos.py

No introduce datos nuevos: todas las cifras salen de
`../02-linea-base/datos/dataset_consumo_electrico_rural_ElTambo_Cauca.csv`,
de `../11-evaluacion-financiera/escenarios.csv` o de los supuestos declarados en
`../04-renovables-almacenamiento/diseno_fotovoltaico.md`.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
OUT = HERE / "assets"
OUT.mkdir(parents=True, exist_ok=True)

CSV = BASE / "02-linea-base" / "datos" / "dataset_consumo_electrico_rural_ElTambo_Cauca.csv"
ESC = BASE / "11-evaluacion-financiera" / "escenarios.csv"

df = pd.read_csv(CSV)
esc = pd.read_csv(ESC)

BG = "#F6FAF8"
GREEN = "#0B6B54"
TEAL = "#11998E"
LIME = "#38EF7D"
AMBER = "#FFA000"
DARK = "#10231F"
GREY = "#5B7A72"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.titlesize": 18,
    "axes.titleweight": "bold",
    "axes.labelsize": 13,
    "axes.edgecolor": "#CBD5D1",
    "axes.labelcolor": DARK,
    "text.color": DARK,
    "xtick.color": GREY,
    "ytick.color": GREY,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=170, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(name)


# 1. Perfil horario
perfil = df.groupby("hora")["total_W"].mean()
fig, ax = plt.subplots(figsize=(10, 5.2))
ax.fill_between(perfil.index, perfil.values, color=TEAL, alpha=0.18)
ax.plot(perfil.index, perfil.values, color=GREEN, lw=3, marker="o", ms=5)
pico_h = int(perfil.idxmax())
pico_v = float(perfil.max())
ax.scatter([pico_h], [pico_v], s=220, color=AMBER, zorder=5)
ax.annotate(f"Pico {pico_v:.0f} W · {pico_h}:00", (pico_h, pico_v),
            xytext=(pico_h - 5.5, pico_v + 65), color=AMBER, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=AMBER, lw=2))
ax.set_title("Potencia media por hora del día")
ax.set_xlabel("Hora")
ax.set_ylabel("W")
ax.set_xticks(range(0, 24, 2))
ax.grid(axis="y", alpha=0.25)
save(fig, "01_perfil_horario.png")

# 2. Pareto de equipos: kWh/mes documentados en 02-linea-base/linea_base.md
eq = ["Nevera", "Picadora", "Conectores", "Iluminación", "TV", "Lavadora"]
kwh = [56.10, 29.64, 16.30, 14.91, 14.34, 13.54]
acum = np.cumsum(kwh) / sum(kwh) * 100
fig, ax = plt.subplots(figsize=(10, 5.2))
y = np.arange(len(eq))[::-1]
ax.barh(y, kwh, color=[GREEN, AMBER, TEAL, TEAL, TEAL, TEAL], height=0.62)
for yi, v in zip(y, kwh):
    ax.text(v + 0.8, yi, f"{v:.1f}", va="center", fontsize=11, color=DARK)
ax.set_yticks(y)
ax.set_yticklabels(eq)
ax.set_xlim(0, 68)
ax.set_xlabel("kWh / mes")
ax2 = ax.twiny()
ax2.plot(acum, y, color=AMBER, marker="o", lw=2)
ax2.set_xlim(0, 100)
ax2.set_xlabel("Acumulado %", color=AMBER)
ax2.tick_params(axis="x", colors=AMBER)
ax.set_title("Usos Significativos de Energía: 59,2 %")
ax.grid(axis="x", alpha=0.2)
save(fig, "02_pareto_usos.png")

# 3. Distribución de potencia total con regla media + 2σ
media, desv = df["total_W"].mean(), df["total_W"].std()
umbral = media + 2 * desv
fig, ax = plt.subplots(figsize=(10, 5.2))
ax.hist(df["total_W"], bins=60, color=TEAL, alpha=0.8, edgecolor="white")
ax.axvline(umbral, color=AMBER, lw=2.5, ls="--", label=f"Umbral pico {umbral:.0f} W")
ax.axvline(media, color=GREEN, lw=2, label=f"Media {media:.0f} W")
ax.set_title("Distribución de potencia total (1.000 horas)")
ax.set_xlabel("W")
ax.set_ylabel("Frecuencia")
ax.legend(frameon=False)
ax.grid(axis="y", alpha=0.2)
save(fig, "03_distribucion_potencia.png")

# 4. Correlaciones
cols = ["nevera_W", "lavadora_W", "tv_W", "picadora_pasto_W",
        "iluminacion_10bombillos_W", "otros_conectores_W", "total_W"]
corr = df[cols].corr()
labels = ["Nevera", "Lavadora", "TV", "Picadora", "Ilum.", "Conect.", "Total"]
fig, ax = plt.subplots(figsize=(8.2, 6.6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="YlGnBu", ax=ax,
            xticklabels=labels, yticklabels=labels,
            cbar_kws={"label": "r de Pearson"}, annot_kws={"size": 10},
            linewidths=0.5, linecolor="white")
ax.set_title("Correlaciones entre equipos")
save(fig, "04_correlacion.png")

# 5. Balance diario (supuestos declarados en el diseño fotovoltaico)
fig, ax = plt.subplots(figsize=(10, 5.2))
ax.bar(["Generación\ncon seguidor"], [9.85], color=TEAL, width=0.5, label="Generación")
ax.bar(["Demanda"], [2.64], color=GREEN, width=0.5, label="Autoconsumo directo")
ax.bar(["Demanda"], [2.19], bottom=2.64, color=LIME, width=0.5, label="Desde batería")
ax.bar(["Excedente"], [4.78], color=AMBER, width=0.5, label="Excedente")
for x, v in [(0, 9.85), (1, 4.83), (2, 4.78)]:
    ax.text(x, v + 0.15, f"{v:.2f}", ha="center", fontweight="bold")
ax.set_ylabel("kWh / día")
ax.set_ylim(0, 11)
ax.set_title("Balance de un día promedio")
ax.legend(frameon=False, loc="upper right", fontsize=10)
ax.grid(axis="y", alpha=0.2)
save(fig, "05_balance_energia.png")

# 6. Retorno por escenario (escenarios.csv)
fig, ax = plt.subplots(figsize=(10, 5.2))
names = {
    "A_sistema_individual": "A · individual tarifa fija",
    "B_sistema_individual": "B · individual tarifa +4 %",
    "C_sistema_individual": "C · individual -20 % inversión",
    "D_compartida_con_bateria": "D · compartida con batería",
    "E_compartida_sin_bateria": "E · compartida sin batería",
}
orden = esc.sort_values("retorno_anios")
vals = orden["retorno_anios"].values
labs = [names.get(x, x) for x in orden["escenario"]]
colors = [AMBER if "compartida" in x else TEAL for x in orden["escenario"]]
bars = ax.barh(labs, vals, color=colors, height=0.6)
for b, v in zip(bars, vals):
    ax.text(v + 0.15, b.get_y() + b.get_height() / 2, f"{v:.1f} años",
            va="center", fontweight="bold")
ax.set_xlabel("Años")
ax.set_xlim(0, 13.5)
ax.set_title("Retorno de la inversión por escenario")
ax.grid(axis="x", alpha=0.2)
save(fig, "06_retorno_escenarios.png")

# 7. USE
fig, ax = plt.subplots(figsize=(7.2, 5.6))
ax.pie([59.2, 40.8], labels=["Nevera + picadora\n(USE)", "Otros usos"],
       colors=[GREEN, "#D9E6E1"], startangle=90, counterclock=False,
       wedgeprops=dict(width=0.38), autopct="%1.1f%%", pctdistance=0.80,
       textprops=dict(fontsize=12))
ax.text(0, 0, "59,2 %\nUSE", ha="center", va="center", fontsize=20,
        fontweight="bold", color=GREEN)
ax.set_title("Dónde se va la energía")
save(fig, "07_use_donut.png")

# 8. Carbono evitado (factor declarado 0,164 kgCO₂/kWh)
carbono = 1762.13 * 0.164 / 1000
fig, ax = plt.subplots(figsize=(9.5, 3.6))
ax.barh(["CO₂ evitado / año"], [carbono], color=[GREEN], height=0.45)
ax.text(carbono + 0.008, 0, f"{carbono:.2f} t CO₂/año", va="center",
        fontweight="bold", fontsize=16, color=GREEN)
ax.set_xlim(0, 0.40)
ax.set_xticks([])
ax.grid(False)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_title("Aporte ambiental (factor 0,164 kgCO₂/kWh)", loc="left")
save(fig, "08_carbono.png")

print("Gráficos listos en", OUT)
