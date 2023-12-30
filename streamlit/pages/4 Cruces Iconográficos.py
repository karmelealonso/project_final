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

# Crear un multiselect en la barra lateral para las 5 columnas
columnas_interes = ["Objetos", "Personajes", "Flora", "Fauna", "Lugar"]
valores_seleccionados = {}
for columna in columnas_interes:
    valores = obras_estudio[columna].unique()
    valores_seleccionados[columna] = st.sidebar.multiselect(
        f'Selecciona valores de {columna}',
        valores
    )

# Filtrar el DataFrame según los valores seleccionados
condiciones = [
    obras_estudio[columna].isin(valores)
    for columna, valores in valores_seleccionados.items()
]
condicion_final = pd.concat(condiciones, axis=1).all(axis=1)
df_filtrado = obras_estudio[condicion_final]

# Calcular la frecuencia de cada combinación de categorías por TítuloID
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





