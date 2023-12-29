import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pyecharts import options as opts
from pyecharts.charts import Line
import plotly.express as px
from pyecharts.globals import ThemeType

import random


#Cargar DataFrames
obras_completo = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_def/obras_completo.csv")
obras_estudio = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_def/obras_estudio.csv")


#BARRA LATERAL

# Definir una clave única para el filtro de iconografía
key_iconografia_filter = "iconografia_filter"

# Obtener las columnas del DataFrame como opciones de iconografía
opciones_iconografia = ["Objetos", "Personajes", "Flora", "Fauna", "Lugar"]


# Función para obtener los top 10 elementos según la categoría seleccionada
def get_top_10_elements(category_df, column_name):
    return category_df[column_name].value_counts().head(10).index.tolist()


# Cargar los top 10 elementos iniciales y valores únicos de rango de años para cada categoría
top_10_objetos = get_top_10_elements(obras_estudio, 'Objetos')
top_10_personajes = get_top_10_elements(obras_estudio, 'Personajes')
top_10_fauna = get_top_10_elements(obras_estudio, 'Fauna')
top_10_flora = get_top_10_elements(obras_estudio, 'Flora')
top_10_lugar = get_top_10_elements(obras_estudio, 'Lugar')


# Filtro para seleccionar iconografía
iconografia_seleccionada = st.sidebar.radio("Selecciona un tipo de iconografía", opciones_iconografia, key=key_iconografia_filter)

# Filtro para seleccionar elementos específicos, los top 10 elementos más frecuentes o ambos
filtro_elementos = st.sidebar.radio("Selecciona el tipo de elementos", ["Seleccionar elementos específicos", "Top 10 elementos más frecuentes"])

# Crear un rango de décadas basado en los valores del DataFrame
decadas_range = st.sidebar.slider(
    "Seleccionar Rango de Décadas",
    min_value=obras_estudio['Año'].min(),
    max_value=obras_estudio['Año'].max(),
    value=(obras_estudio['Año'].min(), obras_estudio['Año'].max())
)

# Mostrar la lista de elementos únicos o top 10 según la iconografía seleccionada
if filtro_elementos == "Seleccionar elementos específicos":
    st.sidebar.subheader(f"Seleccionar {iconografia_seleccionada}")
    opciones_elementos = obras_estudio[iconografia_seleccionada].unique()
    
    # Asegurarse de que los valores predeterminados estén en las opciones
    default_values = st.sidebar.multiselect(
        f"Seleccionar {iconografia_seleccionada}", opciones_elementos
    )

    elementos_seleccionados = default_values if default_values else opciones_elementos

elif filtro_elementos == "Top 10 elementos más frecuentes":
    st.sidebar.subheader(f"Top 10 {iconografia_seleccionada}")

    # Obtener los top 10 elementos más frecuentes automáticamente
    top_10_elementos = obras_estudio[iconografia_seleccionada].value_counts().head(10).index.tolist()

    elementos_seleccionados = st.sidebar.multiselect(
        f"Seleccionar Top 10 {iconografia_seleccionada}", top_10_elementos
    )


# Aplicar los filtros seleccionados
df_filtrado = obras_estudio[
    obras_estudio[iconografia_seleccionada].isin(elementos_seleccionados) &
    obras_estudio['Año'].between(*decadas_range)
]

gardenela vaginalis

#CREACIÓN DE GRÁFICOS

# Calcular la frecuencia
df_filtrado['Frecuencia'] = df_filtrado.groupby(iconografia_seleccionada)[iconografia_seleccionada].transform('count')

# Calcular la frecuencia total
frecuencia_total = df_filtrado['Frecuencia'].sum()

# Crear el gráfico pie
pie_chart = px.pie(
    df_filtrado,
    names=iconografia_seleccionada,
    values='Frecuencia',
    title=f'Distribución de Frecuencia de {iconografia_seleccionada}',
    hover_data=[iconografia_seleccionada, 'Frecuencia'],
    labels={'Frecuencia': 'Porcentaje'},
    hole=0.4
)

# Establecer dimensiones del gráfico
pie_chart.update_layout(width=1000, height=600)

# Mostrar el gráfico
st.plotly_chart(pie_chart)








