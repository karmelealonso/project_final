import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


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

elementos_seleccionados = []

if filtro_elementos == "Seleccionar elementos específicos":
    st.sidebar.subheader(f"Seleccionar {iconografia_seleccionada}")
    opciones_elementos = obras_estudio[iconografia_seleccionada].unique()
    
    # Asegurarse de que los valores predeterminados estén en las opciones
    valores_predeterminados = st.sidebar.multiselect(
        f"Seleccionar {iconografia_seleccionada}", opciones_elementos
    )

    elementos_seleccionados = valores_predeterminados if valores_predeterminados else opciones_elementos

elif filtro_elementos == "Top 10 elementos más frecuentes":
    st.sidebar.subheader(f"Top 10 {iconografia_seleccionada}")
    
    # Obtener los top 10 elementos más frecuentes automáticamente
    top_10_elementos = get_top_10_elements(obras_estudio, iconografia_seleccionada)

    # Seleccionar automáticamente los 10 elementos más frecuentes
    elementos_seleccionados = top_10_elementos

# Aplicar los filtros seleccionados para ambos gráficos
df_filtrado = obras_estudio[
    obras_estudio[iconografia_seleccionada].isin(elementos_seleccionados)&
    obras_estudio['Año'].between(*decadas_range)
]


# CREACIÓN DE GRÁFICOS

# 1. PIE CHART

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

# 2. CREACIÓN DE GRÁFICO DE LÍNEAS

# Calcular la frecuencia de cada elemento a lo largo del tiempo
df_filtrado_line_chart = df_filtrado.groupby(['Año', iconografia_seleccionada]).size().reset_index(name='Frecuencia')

line_chart = px.line(
    df_filtrado_line_chart,
    x='Año',
    y='Frecuencia',
    color=iconografia_seleccionada,
    labels={'Frecuencia': 'Cantidad'},
    title=f'Frecuencia de {iconografia_seleccionada} a lo largo del tiempo',
)

# Establecer dimensiones del gráfico
line_chart.update_layout(width=1000, height=600)

# Mostrar el gráfico de líneas
st.plotly_chart(line_chart)


# 3. CREACIÓN DE GRÁFICO DE BARRAS

# Calcular la frecuencia de cada elemento según las escuelas
df_filtrado_bar_chart = df_filtrado.groupby(['Escuela', iconografia_seleccionada]).size().reset_index(name='Frecuencia')

bar_chart = px.bar(
    df_filtrado_bar_chart,
    x='Escuela',
    y='Frecuencia',
    color=iconografia_seleccionada,
    labels={'Frecuencia': 'Cantidad'},
    title=f'Comparación de Frecuencia de {iconografia_seleccionada} por Escuela',
)

# Establecer dimensiones del gráfico
bar_chart.update_layout(width=1000, height=600)

# Mostrar el gráfico de barras
st.plotly_chart(bar_chart)




heatmap_chart = px.imshow(
    df_filtrado_line_chart.pivot_table(
        values='Frecuencia',
        index='Año',
        columns=iconografia_seleccionada,
        aggfunc='sum',
    ),
    labels={'color': 'Frecuencia'},
    title=f'Mapa de Calor de Frecuencia de {iconografia_seleccionada} a lo largo de los Años',
)
heatmap_chart.update_layout(width=1000, height=600)
st.plotly_chart(heatmap_chart)


# CREACIÓN DEL GRÁFICO DE BARRAS DE FRECUENCIA ACUMULADA
bar_chart_cumsum = px.bar(
    df_filtrado,
    x=iconografia_seleccionada,
    y=df_filtrado.groupby(iconografia_seleccionada)['Frecuencia'].cumsum(),
    color='Año',  # Puedes ajustar esto según tus necesidades o eliminarlo
    labels={'y': 'Frecuencia Acumulada'},
    title=f'Frecuencia Acumulada de {iconografia_seleccionada}',
)

bar_chart_cumsum.update_layout(width=1000, height=600)
st.plotly_chart(bar_chart_cumsum)











