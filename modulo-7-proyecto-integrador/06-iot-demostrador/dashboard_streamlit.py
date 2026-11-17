from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de página
st.set_page_config(page_title="Dashboard de Consumo Eléctrico Rural El Tambo", layout="wide")

# Cargar datos
DATA_PATH = Path(__file__).resolve().parents[2] / 'modulo-7-proyecto-integrador' / '02-linea-base' / 'datos' / 'dataset_consumo_electrico_rural_ElTambo_Cauca.csv'
df_model = pd.read_csv(DATA_PATH)
summary_stats = df_model.describe()

# Encabezado
st.markdown("""
<div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 25px; border-radius: 12px; text-align: center; color: white; margin-bottom: 20px; font-family: sans-serif;">
    <h1 style="margin: 0; font-size: 32px;">⚡ Dashboard Analítico de Consumo Eléctrico Rural</h1>
    <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">Monitoreo energético y simulación de carga para fincas en El Tambo, Cauca (Streamlit)</p>
</div>
""", unsafe_allow_html=True)

# Menú lateral / Pestañas
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Contexto",
    "📊 Datos & Filtros",
    "📈 Estadísticas",
    "🔍 Gráficos Analíticos",
    "⏰ Perfil Diario & Correlación",
    "💰 Simulador de Tarifas"
])

with tab1:
    st.markdown("""
    ### 🎯 Objetivos y Contexto
    Este panel permite analizar el comportamiento del consumo de energía eléctrica de una vivienda rural productiva en El Tambo, Cauca:
    *   **Análisis por Electrodoméstico**: Monitoreo individualizado de la nevera, lavadora, televisor, iluminación, y la **picadora de pasto**.
    *   **Comprensión de Carga**: Identificación de los picos de demanda durante el día.
    *   **Simulador de Costos**: Herramienta interactiva para planificar gastos energéticos en contextos rurales.
    """)

with tab2:
    st.subheader("Explore y Filtre el Dataset por Potencia Demandada")
    min_w = float(df_model['total_W'].min())
    max_w = float(df_model['total_W'].max())
    pot_rango = st.slider("Rango de Potencia (W)", min_w, max_w, (min_w, max_w))
    df_filtrado = df_model[(df_model['total_W'] >= pot_rango[0]) & (df_model['total_W'] <= pot_rango[1])]
    st.dataframe(df_filtrado.head(100))

with tab3:
    st.subheader("Resumen de Métricas de Consumo (Watts)")
    st.dataframe(summary_stats.round(2))

with tab4:
    st.subheader("Análisis de Distribución y Relaciones")
    col1, col2 = st.columns(2)
    with col1:
        var_uni = st.selectbox('Seleccione Variable (Univariado)', ['nevera_W', 'lavadora_W', 'tv_W', 'picadora_pasto_W', 'iluminacion_10bombillos_W', 'total_W'])
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df_model[var_uni], kde=True, color='#2a5298', ax=ax)
        ax.set_title(f'Distribución de {var_uni}')
        st.pyplot(fig)
    with col2:
        var_x = st.selectbox('Eje X (Bivariado)', ['hora', 'nevera_W', 'picadora_pasto_W', 'total_W'])
        var_y = st.selectbox('Eje Y (Bivariado)', ['total_W', 'total_kWh', 'picadora_pasto_W'])
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=df_model, x=var_x, y=var_y, color='#1e3c72', alpha=0.6, ax=ax2)
        ax2.set_title(f'Relación {var_x} vs {var_y}')
        st.pyplot(fig2)

with tab5:
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.subheader("Perfil Diario de Carga")
        fig3, ax3 = plt.subplots(figsize=(6, 4.5))
        perfil_hora = df_model.groupby('hora')[['nevera_W', 'lavadora_W', 'tv_W', 'picadora_pasto_W', 'iluminacion_10bombillos_W']].mean()
        perfil_hora.plot(kind='line', marker='o', ax=ax3)
        ax3.set_ylabel('Watts (W)')
        ax3.grid(True, linestyle='--')
        st.pyplot(fig3)
    with col_p2:
        st.subheader("Matriz de Correlación")
        fig4, ax4 = plt.subplots(figsize=(6, 4.5))
        columnas_numericas = df_model.select_dtypes(include=[np.number])
        sns.heatmap(columnas_numericas.corr(), annot=True, cmap='Blues', fmt='.2f', ax=ax4, cbar=False)
        st.pyplot(fig4)

with tab6:
    st.subheader("Calculadora de Consumo y Costo Mensual")
    c1, c2 = st.columns(2)
    with c1:
        nev_h = st.slider('Nevera - Horas al día', 0, 24, 24)
        lav_h = st.slider('Lavadora - Horas al día', 0, 5, 1)
        tv_h = st.slider('Televisor - Horas al día', 0, 10, 4)
    with c2:
        pic_h = st.slider('Picadora de Pasto - Horas al día', 0, 6, 1)
        bom_h = st.slider('Iluminación - Horas al día', 0, 12, 6)
        tarifa = st.number_input('Tarifa de Energía ($ COP por kWh)', value=850)

    p_nevera = df_model['nevera_W'].mean() if 'nevera_W' in df_model else 60
    p_lavadora = df_model['lavadora_W'].mean() if 'lavadora_W' in df_model else 350
    p_tv = df_model['tv_W'].mean() if 'tv_W' in df_model else 80
    p_picadora = df_model['picadora_pasto_W'].mean() if 'picadora_pasto_W' in df_model else 1500
    p_ilum = df_model['iluminacion_10bombillos_W'].mean() if 'iluminacion_10bombillos_W' in df_model else 100

    e_nevera = (p_nevera * nev_h) / 1000
    e_lavadora = (p_lavadora * lav_h) / 1000
    e_tv = (p_tv * tv_h) / 1000
    e_picadora = (p_picadora * pic_h) / 1000
    e_ilum = (p_ilum * bom_h) / 1000

    energia_diaria = e_nevera + e_lavadora + e_tv + e_picadora + e_ilum
    energia_mensual = energia_diaria * 30
    costo_mensual = energia_mensual * tarifa

    st.markdown(f"""
    <div style="background-color: #f1f8e9; border-left: 6px solid #4caf50; padding: 15px; border-radius: 8px; font-family: sans-serif; margin-top:15px;">
        <h3 style="margin: 0; color: #2e7d32;">⚡ Consumo Estimado Mensual</h3>
        <p style="font-size: 18px; font-weight: bold; margin: 10px 0 5px 0; color: #1b5e20;">Energía: {energia_mensual:.2f} kWh / mes</p>
        <p style="font-size: 22px; font-weight: bold; margin: 0; color: #2e7d32;">Costo estimado: ${costo_mensual:,.2f} COP</p>
    </div>
    """, unsafe_allow_html=True)