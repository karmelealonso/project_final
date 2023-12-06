import streamlit as st
import pandas as pd
import altair as alt

# Cargar tus datos desde tu archivo CSV

# Cargar los nuevos DataFrames
obras_completo = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/obras_completo.csv")


# Crear el gráfico de línea temporal
chart = alt.Chart(obras_completo).mark_circle().encode(
    x='Año:T',
    y=alt.Y('Título:N', sort='-x'),
    color='Título:N',
    tooltip=['Título', 'Año', 'Imágenes']
).properties(
    width=800,
    height=300
)

# Mostrar el gráfico
st.altair_chart(chart, use_container_width=True)

# Mostrar las imágenes en Streamlit
for index, row in obras_completo.iterrows():
    st.image(row['Imágenes'], caption=row['Título'], use_column_width=True)
