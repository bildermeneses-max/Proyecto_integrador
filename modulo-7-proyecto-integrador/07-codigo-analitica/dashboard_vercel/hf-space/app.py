"""Dashboard Analítico de Consumo Eléctrico Rural El Tambo.

Versión mejorada para Hugging Face Spaces, pensada para servirse detrás de
Vercel mediante un rewrite. La UI mantiene las 8 pestañas del notebook.
"""

from __future__ import annotations

import os

import gradio as gr
import matplotlib.pyplot as plt
import seaborn as sns

from data import (
    EQUIPOS,
    filtrar,
    kpis,
    load_data,
    matriz_correlacion,
    perfil_hora,
    serie_univariada,
    simular,
    summary_stats,
    datos_bivariados,
)

sns.set_theme(style="whitegrid")
plt.rcParams["axes.unicode_minus"] = False


def _figuraUNI(variable: str):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(serie_univariada(variable), kde=True, color="#2a5298", ax=ax)
    ax.set_title(f"Distribución de {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Frecuencia")
    fig.tight_layout()
    plt.close(fig)
    return fig


def _figura_bi(var_x: str, var_y: str):
    datos = datos_bivariados(var_x, var_y)
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=datos, x=var_x, y=var_y, color="#1e3c72", alpha=0.6, ax=ax)
    ax.set_title(f"Relación entre {var_x} y {var_y}")
    fig.tight_layout()
    plt.close(fig)
    return fig


def _figura_perfil():
    fig, ax = plt.subplots(figsize=(10, 5))
    perfil_hora().plot(kind="line", marker="o", ax=ax)
    ax.set_title("Perfil promedio de consumo por hora del día (W)")
    ax.set_ylabel("Watts (W)")
    ax.set_xlabel("Hora del día")
    ax.grid(True, linestyle="--")
    fig.tight_layout()
    plt.close(fig)
    return fig


def _figura_correlacion():
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(matriz_correlacion(), annot=True, cmap="Blues", fmt=".2f", ax=ax)
    ax.set_title("Matriz de correlación de consumo eléctrico")
    fig.tight_layout()
    plt.close(fig)
    return fig


def _tarjetas_kpi() -> str:
    k = kpis()
    return f"""
    <div style="display:flex; gap:12px; flex-wrap:wrap; margin:4px 0 18px 0; font-family:sans-serif;">
      <div style="flex:1; min-width:150px; background:#f1f8e9; border-left:5px solid #4caf50; padding:12px; border-radius:10px;">
        <div style="font-size:12px; color:#2e7d32; text-transform:uppercase;">Registros</div>
        <div style="font-size:24px; font-weight:700; color:#1b5e20;">{k['filas']:,}</div>
      </div>
      <div style="flex:1; min-width:150px; background:#e8f5e9; border-left:5px solid #2e7d32; padding:12px; border-radius:10px;">
        <div style="font-size:12px; color:#2e7d32; text-transform:uppercase;">Energía total</div>
        <div style="font-size:24px; font-weight:700; color:#1b5e20;">{k['energia_total_kwh']:,.1f} kWh</div>
      </div>
      <div style="flex:1; min-width:150px; background:#fff8e1; border-left:5px solid #ffa000; padding:12px; border-radius:10px;">
        <div style="font-size:12px; color:#e65100; text-transform:uppercase;">Pico de demanda</div>
        <div style="font-size:24px; font-weight:700; color:#e65100;">{k['pico_w']:,.1f} W</div>
      </div>
      <div style="flex:1; min-width:150px; background:#e3f2fd; border-left:5px solid #1976d2; padding:12px; border-radius:10px;">
        <div style="font-size:12px; color:#1565c0; text-transform:uppercase;">Equipo líder</div>
        <div style="font-size:20px; font-weight:700; color:#0d47a1;">{k['equipo_top']} ({k['equipo_top_w']:.1f} W)</div>
      </div>
    </div>
    """


def _resultado_simulador(nevera_h, lavadora_h, tv_h, picadora_h, bombillos_h, tarifa):
    energia, costo = simular(
        nevera_h, lavadora_h, tv_h, picadora_h, bombillos_h, tarifa
    )
    return f"""
    <div style="background-color:#f1f8e9; border-left:6px solid #4caf50; padding:15px; border-radius:8px; font-family:sans-serif;">
      <h3 style="margin:0; color:#2e7d32;">⚡ Consumo estimado mensual</h3>
      <p style="font-size:20px; font-weight:bold; margin:10px 0 5px 0; color:#1b5e20;">Energía: {energia:,.2f} kWh / mes</p>
      <p style="font-size:24px; font-weight:bold; margin:0; color:#2e7d32;">Costo: ${costo:,.2f} COP</p>
    </div>
    """


with gr.Blocks(
    title="Dashboard de Consumo Eléctrico Rural El Tambo",
    theme=gr.themes.Soft(primary_hue="emerald", secondary_hue="teal"),
) as demo:
    gr.HTML(
        """
    <div style="background:linear-gradient(135deg,#11998e 0%,#38ef7d 100%); padding:25px; border-radius:12px; text-align:center; color:white; margin-bottom:16px; font-family:sans-serif;">
      <h1 style="margin:0; font-size:32px;">⚡ Dashboard Analítico de Consumo Eléctrico Rural</h1>
      <p style="margin:10px 0 0 0; font-size:16px; opacity:.9;">Monitoreo energético y simulación de carga para fincas en El Tambo, Cauca</p>
    </div>
    """
    )
    gr.HTML(_tarjetas_kpi())

    with gr.Tab("📖 1. Explicación del Ejercicio"):
        gr.Markdown(
            """
        ### 🎯 Objetivos y contexto
        Este panel analiza el consumo de energía de una vivienda rural productiva en El Tambo, Cauca:

        * **Análisis por electrodoméstico**: nevera, lavadora, televisor, iluminación y **picadora de pasto**.
        * **Comprensión de carga**: identificación de picos de demanda según rutinas domésticas y del agro.
        * **Simulador de costos**: planificación de gastos y eficiencia energética.
        """
        )

    with gr.Tab("📊 2. DataFrame Interactivo"):
        gr.Markdown("### Explore y filtre el dataset por potencia demandada")
        df = load_data()
        minimo, maximo = float(df["total_W"].min()), float(df["total_W"].max())
        with gr.Row():
            pot_min = gr.Slider(minimo, maximo, minimo, label="Potencia mínima (W)")
            pot_max = gr.Slider(minimo, maximo, maximo, label="Potencia máxima (W)")
        gr.Button("🔍 Filtrar datos", variant="primary").click(
            fn=filtrar, inputs=[pot_min, pot_max], outputs=gr.Dataframe(value=df.head(100))
        )

    with gr.Tab("📈 3. Estadísticas Descriptivas"):
        gr.Markdown("### Resumen de métricas de consumo (W)")
        gr.Dataframe(value=summary_stats())

    with gr.Tab("🔍 4. Análisis Univariado"):
        gr.Markdown("### Distribución del consumo de los equipos")
        variable = gr.Dropdown(
            choices=EQUIPOS + ["total_W", "total_kWh"],
            value="total_W",
            label="Seleccione equipo o carga",
        )
        grafico_uni = gr.Plot(value=_figuraUNI("total_W"))
        variable.change(fn=_figuraUNI, inputs=variable, outputs=grafico_uni)

    with gr.Tab("🔗 5. Análisis Bivariado"):
        gr.Markdown("### Relación entre variables de demanda")
        with gr.Row():
            eje_x = gr.Dropdown(
                choices=["hora", "nevera_W", "picadora_pasto_W", "total_W"],
                value="hora", label="Eje X",
            )
            eje_y = gr.Dropdown(
                choices=["total_W", "total_kWh", "picadora_pasto_W"],
                value="total_W", label="Eje Y",
            )
        grafico_bi = gr.Plot(value=_figura_bi("hora", "total_W"))
        gr.Button("📁 Actualizar gráfico", variant="secondary").click(
            fn=_figura_bi, inputs=[eje_x, eje_y], outputs=grafico_bi
        )

    with gr.Tab("⏰ 6. Perfil Diario de Carga"):
        gr.Markdown("### Curva de carga promedio por hora")
        gr.Plot(value=_figura_perfil())

    with gr.Tab("🗺️ 7. Correlación Energética"):
        gr.Markdown("### Matriz de relación de consumos")
        gr.Plot(value=_figura_correlacion())

    with gr.Tab("💰 8. Simulador de Consumo y Tarifa"):
        gr.Markdown("### Defina el uso diario de los equipos")
        with gr.Row():
            with gr.Column():
                nev = gr.Slider(0, 24, 24, label="Nevera — horas/día")
                lav = gr.Slider(0, 5, 1, label="Lavadora — horas/día")
                tv = gr.Slider(0, 10, 4, label="Televisor — horas/día")
            with gr.Column():
                pic = gr.Slider(0, 6, 1, label="Picadora de pasto — horas/día")
                bom = gr.Slider(0, 12, 6, label="Iluminación — horas/día")
                tarifa = gr.Number(850, label="Tarifa ($ COP por kWh)")
        salida = gr.HTML(
            value="<div style='text-align:center;color:#777;'>Ajuste las horas y presione Calcular.</div>"
        )
        gr.Button("⚡ Calcular consumo y costo", variant="primary").click(
            fn=_resultado_simulador,
            inputs=[nev, lav, tv, pic, bom, tarifa],
            outputs=salida,
        )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", "7860")),
        share=False,
        root_path=os.getenv("GRADIO_ROOT_PATH") or None,
        show_error=True,
    )
