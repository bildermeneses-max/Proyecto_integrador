from pathlib import Path
import pandas as pd

# Cargar el dataset de consumo eléctrico rural
DATA_PATH = Path(__file__).resolve().parents[2] / 'modulo-7-proyecto-integrador' / '02-linea-base' / 'datos' / 'dataset_consumo_electrico_rural_ElTambo_Cauca.csv'
df_model = pd.read_csv(DATA_PATH)

# Mostrar las primeras filas y estructura para entender las variables disponibles
print("Columnas del dataset:", df_model.columns.tolist())
print(df_model.head())
import gradio as gr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Obtener estadísticas básicas para el dataset
summary_stats = df_model.describe()

# Función para filtrar dinámicamente el DataFrame en la interfaz por potencia total (W)
def filtrar_datos(potencia_min, potencia_max):
    df_filtrado = df_model[(df_model['total_W'] >= potencia_min) & (df_model['total_W'] <= potencia_max)]
    return df_filtrado.head(100)

# Funciones de visualización dinámicas
def get_univariate_plot(variable):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df_model[variable], kde=True, color='#2a5298', ax=ax)
    ax.set_title(f'Distribución de {variable}')
    ax.set_xlabel(variable)
    ax.set_ylabel('Frecuencia')
    plt.tight_layout()
    return fig

def get_bivariate_plot(var_x, var_y):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df_model, x=var_x, y=var_y, color='#1e3c72', alpha=0.6, ax=ax)
    ax.set_title(f'Relación entre {var_x} y {var_y}')
    plt.tight_layout()
    return fig

def get_hourly_profile_plot():
    fig, ax = plt.subplots(figsize=(10, 5))
    perfil_hora = df_model.groupby('hora')[['nevera_W', 'lavadora_W', 'tv_W', 'picadora_pasto_W', 'iluminacion_10bombillos_W']].mean()
    perfil_hora.plot(kind='line', marker='o', ax=ax)
    ax.set_title('Perfil Promedio de Consumo por Hora del Día (W)')
    ax.set_ylabel('Watts (W)')
    ax.set_xlabel('Hora del Día')
    ax.grid(True, linestyle='--')
    plt.tight_layout()
    return fig

def get_correlation_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    columnas_numericas = df_model.select_dtypes(include=[np.number])
    sns.heatmap(columnas_numericas.corr(), annot=True, cmap='Blues', fmt='.2f', ax=ax)
    ax.set_title('Matriz de Correlación de Consumo Eléctrico')
    plt.tight_layout()
    return fig

# Función de cálculo/simulación de costo estimado mensual (Simulador)
def estimar_costo_mensual(nevera_h, lavadora_h, tv_h, picadora_h, bombillos_h, tarifa_kwh):
    # Consumos en Watts de los equipos promedio según el dataset
    p_nevera = df_model['nevera_W'].mean() if 'nevera_W' in df_model else 60
    p_lavadora = df_model['lavadora_W'].mean() if 'lavadora_W' in df_model else 350
    p_tv = df_model['tv_W'].mean() if 'tv_W' in df_model else 80
    p_picadora = df_model['picadora_pasto_W'].mean() if 'picadora_pasto_W' in df_model else 1500
    p_ilum = df_model['iluminacion_10bombillos_W'].mean() if 'iluminacion_10bombillos_W' in df_model else 100

    # Energía diaria calculada (kWh)
    e_nevera = (p_nevera * nevera_h) / 1000
    e_lavadora = (p_lavadora * lavadora_h) / 1000
    e_tv = (p_tv * tv_h) / 1000
    e_picadora = (p_picadora * picadora_h) / 1000
    e_ilum = (p_ilum * bombillos_h) / 1000

    energia_diaria_total = e_nevera + e_lavadora + e_tv + e_picadora + e_ilum
    energia_mensual = energia_diaria_total * 30
    costo_mensual = energia_mensual * tarifa_kwh

    html_output = f"""
    <div style="background-color: #f1f8e9; border-left: 6px solid #4caf50; padding: 15px; border-radius: 8px; font-family: sans-serif;">
        <h3 style="margin: 0; color: #2e7d32;">⚡ Consumo Estimado Mensual</h3>
        <p style="font-size: 20px; font-weight: bold; margin: 10px 0 5px 0; color: #1b5e20;">Energía: {energia_mensual:.2f} kWh / mes</p>
        <p style="font-size: 24px; font-weight: bold; margin: 0; color: #2e7d32;">Costo: ${costo_mensual:,.2f} COP</p>
    </div>
    """
    return html_output

with gr.Blocks(title="Dashboard de Consumo Eléctrico Rural El Tambo") as demo:

    gr.HTML("""
    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 25px; border-radius: 12px; text-align: center; color: white; margin-bottom: 20px; font-family: sans-serif;">
        <h1 style="margin: 0; font-size: 32px;">⚡ Dashboard Analítico de Consumo Eléctrico Rural</h1>
        <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">Monitoreo energético y simulación de carga para fincas en El Tambo, Cauca</p>
    </div>
    """)

    with gr.Tab("📖 1. Explicación del Ejercicio"):
        gr.Markdown("""
        ### 🎯 Objetivos y Contexto
        Este panel permite analizar el comportamiento del consumo de energía eléctrica de una vivienda rural productiva en El Tambo, Cauca:

        *   **Análisis por Electrodoméstico**: Monitoreo individualizado de la nevera, lavadora, televisor, iluminación, y la **picadora de pasto** (un elemento productivo clave en el campo).
        *   **Comprensión de Carga**: Identificación de los picos de demanda durante el día según las rutinas domésticas y del agro.
        *   **Simulador de Costos**: Herramienta interactiva para planificar gastos y promover la eficiencia energética en contextos rurales.
        """)

    with gr.Tab("📊 2. DataFrame Interactivo"):
        gr.Markdown("### Explore y Filtre el Dataset por Potencia Demandada")
        with gr.Row():
            pot_min_filter = gr.Slider(minimum=float(df_model['total_W'].min()), maximum=float(df_model['total_W'].max()), value=float(df_model['total_W'].min()), label="Potencia Mínima (W)")
            pot_max_filter = gr.Slider(minimum=float(df_model['total_W'].min()), maximum=float(df_model['total_W'].max()), value=float(df_model['total_W'].max()), label="Potencia Máxima (W)")
        btn_filtrar = gr.Button("🔍 Filtrar Datos", variant="primary")
        df_output = gr.Dataframe(value=df_model.head(100))
        btn_filtrar.click(fn=filtrar_datos, inputs=[pot_min_filter, pot_max_filter], outputs=df_output)

    with gr.Tab("📈 3. Estadísticas Descriptivas"):
        gr.Markdown("### Resumen de Métricas de Consumo (Watts)")
        gr.Dataframe(value=summary_stats.round(2))

    with gr.Tab("🔍 4. Análisis Univariado"):
        gr.Markdown("### Distribución de Consumo de los Equipos")
        var_select = gr.Dropdown(choices=['nevera_W', 'lavadora_W', 'tv_W', 'picadora_pasto_W', 'iluminacion_10bombillos_W', 'total_W'], value='total_W', label='Seleccione Equipo o Carga')
        plot_uni = gr.Plot(value=get_univariate_plot('total_W'))
        var_select.change(fn=get_univariate_plot, inputs=var_select, outputs=plot_uni)

    with gr.Tab("🔗 5. Análisis Bivariado"):
        gr.Markdown("### Relación entre diferentes Variables de Demanda")
        with gr.Row():
            x_select = gr.Dropdown(choices=['hora', 'nevera_W', 'picadora_pasto_W', 'total_W'], value='hora', label='Eje X')
            y_select = gr.Dropdown(choices=['total_W', 'total_kWh', 'picadora_pasto_W'], value='total_W', label='Eje Y')
        btn_bi = gr.Button("📁 Actualizar Gráfico Bivariado", variant="secondary")
        plot_bi = gr.Plot(value=get_bivariate_plot('hora', 'total_W'))
        btn_bi.click(fn=get_bivariate_plot, inputs=[x_select, y_select], outputs=plot_bi)

    with gr.Tab("⏰ 6. Perfil Diario de Carga"):
        gr.Markdown("### Curva de Carga Promedio por Hora")
        gr.Plot(value=get_hourly_profile_plot())

    with gr.Tab("🗺️ 7. Correlación Energética"):
        gr.Markdown("### Matriz de Relación de Consumos")
        gr.Plot(value=get_correlation_plot())

    with gr.Tab("💰 8. Simulador de Consumo y Tarifa"):
        gr.Markdown("### Defina el uso diario de los equipos para estimar la tarifa mensual")
        with gr.Row():
            with gr.Column():
                nev_h = gr.Slider(0, 24, 24, label='Nevera - Horas encendido al día')
                lav_h = gr.Slider(0, 5, 1, label='Lavadora - Horas de uso al día')
                tv_h = gr.Slider(0, 10, 4, label='Televisor - Horas de uso al día')
            with gr.Column():
                pic_h = gr.Slider(0, 6, 1, label='Picadora de Pasto - Horas de uso al día')
                bom_h = gr.Slider(0, 12, 6, label='Iluminación - Horas promedio al día')
                tarifa = gr.Number(value=850, label='Tarifa de Energía ($ COP por kWh)')
        btn_calc = gr.Button("⚡ Calcular Consumo Mensual y Costo", variant="primary")
        output_costo = gr.HTML(value="<div style='text-align: center; color: #777;'>Configure las horas y presione Calcular.</div>")
        btn_calc.click(fn=estimar_costo_mensual, inputs=[nev_h, lav_h, tv_h, pic_h, bom_h, tarifa], outputs=output_costo)

demo.launch(share=False, debug=False)  # share=True solo con autorizacion