import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#Cargar DataFrames
obras_completo = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_def/obras_completo.csv")
obras_estudio = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_def/obras_estudio.csv")


# BARRA LATERAL
st.sidebar.header("Selección de Valores")

# Obtener valores únicos para cada selector
objetos_list = obras_estudio["Objetos"].unique().tolist()
personajes_list = obras_estudio["Personajes"].unique().tolist()
flora_list = obras_estudio["Flora"].unique().tolist()
fauna_list = obras_estudio["Fauna"].unique().tolist()
lugar_list = obras_estudio["Lugar"].unique().tolist()

# Selector de Objetos
selector_objetos = st.sidebar.multiselect("Objetos", objetos_list)

# Selector de Personajes
selector_personajes = st.sidebar.multiselect("Personajes", personajes_list)

# Selector de Flora
selector_flora = st.sidebar.multiselect("Flora", flora_list)

# Selector de Fauna
selector_fauna = st.sidebar.multiselect("Fauna", fauna_list)

# Selector de Lugar
selector_lugar = st.sidebar.multiselect("Lugar", lugar_list)

# Filtrar el DataFrame basado en los filtrados seleccionados
df_filtrado = obras_estudio[
    obras_estudio["Objetos"].isin(selector_objetos) &
    obras_estudio["Personajes"].isin(selector_personajes) &
    obras_estudio["Flora"].isin(selector_flora) &
    obras_estudio["Fauna"].isin(selector_fauna) &
    obras_estudio["Lugar"].isin(selector_lugar)
]

# Calcular el número de veces que aparecen juntos bajo el mismo TituloID
conteo_juntos = df_filtrado.groupby("TituloID").size().reset_index(name='Apariciones')

# Mostrar el resultado
st.title("Número de veces que aparecen juntos:")
st.dataframe(conteo_juntos)

"""# Calcular la frecuencia de cada combinación de categorías por TítuloID
df_frecuencias = df_filtrado.groupby(['TituloID'] + columnas_interes).size().reset_index(name='Frecuencia')

# Crear la matriz de relaciones
matriz_relaciones = pd.DataFrame(0, index=columnas_interes, columns=columnas_interes)

for _, row in df_frecuencias.iterrows():
    categorias_presentes = row[columnas_interes].dropna().tolist()

    for i in range(len(categorias_presentes)):
        for j in range(i + 1, len(categorias_presentes)):
            categoria1 = categorias_presentes[i]
            categoria2 = categorias_presentes[j]

            matriz_relaciones.at[categoria1, categoria2] += row['Frecuencia']
            matriz_relaciones.at[categoria2, categoria1] += row['Frecuencia']

# Crear el heatmap interactivo
fig_relaciones = px.imshow(
    matriz_relaciones.values,
    x=matriz_relaciones.columns,
    y=matriz_relaciones.index,
    labels=dict(color="Frecuencia"),
    title='Relaciones regulares entre categorías representadas en el Museo del Prado',
    color_continuous_scale='viridis',
    width=1000, height=600
)

# Añadir el texto de frecuencia a la matriz
annotations_relaciones = []
for i, categoria1 in enumerate(matriz_relaciones.index):
    for j, categoria2 in enumerate(matriz_relaciones.columns):
        value = matriz_relaciones.at[categoria1, categoria2]
        annotations_relaciones.append(dict(text=str(value), x=categoria2, y=categoria1,
                                           xref='x1', yref='y1', showarrow=False, font=dict(color='white')))

fig_relaciones.update_layout(annotations=annotations_relaciones)

# Mostrar el heatmap interactivo
st.plotly_chart(fig_relaciones)




# Selector de elementos
selected_objects = st.multiselect('Selecciona elementos de Objetos', obras_estudio['Objetos'].unique())
selected_characters = st.multiselect('Selecciona elementos de Personajes', obras_estudio['Personajes'].unique())
selected_fauna = st.multiselect('Selecciona elementos de Fauna', obras_estudio['Fauna'].unique())
selected_flora = st.multiselect('Selecciona elementos de Flora', obras_estudio['Flora'].unique())
selected_places = st.multiselect('Selecciona elementos de Lugar', obras_estudio['Lugar'].unique())


# Filtrar el DataFrame según los elementos seleccionados
filtered_obras_estudio = obras_estudio[obras_estudio['Objetos'].isin(selected_objects) &
                     obras_estudio['Personajes'].isin(selected_characters) &
                     obras_estudio['Fauna'].isin(selected_fauna) &
                     obras_estudio['Flora'].isin(selected_flora) &
                     obras_estudio['Lugar'].isin(selected_places)]

# Contar las apariciones conjuntas
counted_obras_estudio = filtered_obras_estudio.groupby('TituloID').size().reset_index(name='Apariciones')

# Filtrar el DataFrame según los elementos seleccionados
filtered_obras_estudio = obras_estudio[obras_estudio['Objetos'].isin(selected_objects) &
                     obras_estudio['Personajes'].isin(selected_characters) &
                     obras_estudio['Fauna'].isin(selected_fauna) &
                     obras_estudio['Flora'].isin(selected_flora) &
                     obras_estudio['Lugar'].isin(selected_places)]

# Contar las apariciones conjuntas
counted_obras_estudio = filtered_obras_estudio.groupby('TituloID').size().reset_index(name='Apariciones')

st.write(counted_obras_estudio)
"""