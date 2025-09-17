import plotly.express as px
import pandas as pd
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
