import pandas as pd
import plotly.express as px
import streamlit as st      

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Visualizador de datos')
st.dataframe(car_data) #muestra el dataframe

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncio de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

build_barplot = st.checkbox('Construir gráfico de barras')

if build_barplot:
    st.write('Creación de gráfico de barras para tipo de vehículo y transmisión')
    exp = car_data.reset_index()
    exp = exp.groupby(['type','transmission'])['index'].count()
    exp = exp.to_frame()
    exp = exp.reset_index(['type','transmission'])
    fig = px.bar(exp, x='type', y='index',color='transmission')
    st.plotly_chart(fig, use_container_width=True)


