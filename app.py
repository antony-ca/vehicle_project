import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la app
st.header('Análisis de vehículos en EE.UU.')

# Casilla de verificación para histograma
build_histogram = st.checkbox('Mostrar histograma de odómetro')

if build_histogram:
    st.write('Histograma: kilometraje de los vehículos (odometer)')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para scatter plot
build_scatter = st.checkbox('Mostrar gráfico de dispersión (precio vs año)')

if build_scatter:
    st.write('Gráfico de dispersión: precio vs año del vehículo')
    fig_scatter = px.scatter(car_data, x="model_year", y="price",
                             color="type", hover_data=["model"])
    st.plotly_chart(fig_scatter, use_container_width=True)
