import pandas as pd
import streamlit as st

import numpy as np

csv_file = "libros.csv"

database = pd.read_csv(csv_file)

st.markdown('# Análisis de libros')
st.markdown('---')

st.markdown('### Tabla con todos los datos')
st.dataframe(database, 1000, 400)
st.markdown('---')


st.markdown('### Buscar un libro')

title = st.text_input('Escribe el título del libro que quieres buscar', '1984')
data_grouped = database[database['Título'] == title]
st.dataframe(data_grouped, 1000, 50)

st.markdown('---')

st.markdown('### Datos acotados')

st.markdown('##### - Por autor -')
author = st.selectbox('Mostrar libros de un autor', database["Autor"].unique())
data_grouped = database[database['Autor'] == author]
st.dataframe(data_grouped, 1000, 200)

st.markdown('##### - Por editorial -')
editorial = st.selectbox('Mostrar libros de una editorial', database["Editorial"].unique())
data_grouped = database[database['Editorial'] == editorial]
st.dataframe(data_grouped, 1000, 200)

st.markdown('##### - Por género -')
genre = st.selectbox('Mostrar libros de un género', database["Género"].unique())
data_grouped = database[database['Género'] == genre]
st.dataframe(data_grouped, 1000, 200)

st.markdown('##### - Por año -')

year_min = int(database["Año"].min())
year_max = int(database["Año"].max())

year = st.slider('Mostrar libros publicados a partir del año', year_min, year_max, 1967)
data_grouped = database[database['Año'] >= year]
st.dataframe(data_grouped, 1000, 200)

year = st.slider('Mostrar libros publicados antes del año', year_min, year_max, 1580)
data_grouped = database[database['Año'] <= year]
st.dataframe(data_grouped, 1000, 200)

st.markdown('##### - Por rango de precio -')
price_min = database["Precio"].min()
price_max = database["Precio"].max()
price_min, price_max = st.select_slider('Mostrar con un precio entre', options=database.sort_values(by="Precio")["Precio"].unique(), value=(price_min, price_max))
data_grouped = database[(database['Precio'] >= price_min) & (database['Precio'] <= price_max)]
st.dataframe(data_grouped, 1000, 200)

st.markdown('##### - Por rango de páginas -')
pages_min = database["Páginas"].min()
pages_max = database["Páginas"].max()
pages_min, pages_max = st.select_slider('Mostrar con un número de páginas entre', options=database.sort_values(by="Páginas")["Páginas"].unique(), value=(pages_min, pages_max))
data_grouped = database[(database['Páginas'] >= pages_min) & (database['Páginas'] <= pages_max)]
st.dataframe(data_grouped, 1000, 200)

st.markdown('---')

st.markdown('### Gráficas')

st.markdown('##### Tendencias representadas en una gráfica de barras')

showBy = st.selectbox('Puedes escoger en base a qué quieres ver la gráfica', ('Editorial', 'Precio', 'Año', 'Páginas'))

data_grouped = database.groupby(showBy).size()

st.bar_chart(data_grouped)