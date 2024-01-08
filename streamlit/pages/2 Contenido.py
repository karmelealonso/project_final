import streamlit as st
import pandas as pd
from PIL import Image

#Cargar DataFrames
obras_completo = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_def/obras_completo.csv")
obras_estudio = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_def/obras_estudio.csv")

# Establecer los años mínimo y máximo
min_year = obras_estudio['Año'].min()
max_year = obras_estudio['Año'].max()

# Obtener valores únicos para cada selector
titulo_list = obras_estudio["Titulo"].unique().tolist()
autor_list = obras_estudio["Autor"].unique().tolist()
escuela_list = obras_estudio["Escuela"].unique().tolist()
objetos_list = obras_estudio["Objetos"].unique().tolist()
personajes_list = obras_estudio["Personajes"].unique().tolist()
flora_list = obras_estudio["Flora"].unique().tolist()
fauna_list = obras_estudio["Fauna"].unique().tolist()
lugar_list = obras_estudio["Lugar"].unique().tolist()



st.title("¿Qué podemos encontrarnos?")
        
st.text('   ')

st.markdown("---")



# Selector de rango de años
selector_año_rango = st.slider("Selecciona Rango de Años", min_value=obras_estudio["Año"].min(), max_value=obras_estudio["Año"].max(), value=(obras_estudio["Año"].min(), obras_estudio["Año"].max()))

# Selector de Título
selector_titulos = st.multiselect("Título", titulo_list)

# Selector de Autor
selector_autores = st.multiselect("Autores", autor_list)

# Selector de Escuela
selector_escuelas = st.multiselect("Escuelas", escuela_list)

# Selector de Objetos
selector_objetos = st.multiselect("Objetos", objetos_list)

# Selector de Personajes
selector_personajes = st.multiselect("Personajes", personajes_list)

# Selector de Flora
selector_flora = st.multiselect("Flora", flora_list)

# Selector de Fauna
selector_fauna = st.multiselect("Fauna", fauna_list)

# Selector de Lugar
selector_lugar = st.multiselect("Lugar", lugar_list)


# Botón
boton_filtrado = st.button("Filtrar")

# Aplicar el filtrado cuando se presiona el botón
if boton_filtrado:
    # Filtrar el DataFrame basado en los filtrados seleccionados
    obras_estudio_filtrado = obras_estudio[
        (obras_estudio["Titulo"].isin(selector_titulos) if selector_titulos else True) &
        (obras_estudio["Autor"].isin(selector_autores) if selector_autores else True) &
        (obras_estudio["Escuela"].isin(selector_escuelas) if selector_escuelas else True) &
        (obras_estudio["Objetos"].isin(selector_objetos) if selector_objetos else True) &
        (obras_estudio["Personajes"].isin(selector_personajes) if selector_personajes else True) &
        (obras_estudio["Flora"].isin(selector_flora) if selector_flora else True) &
        (obras_estudio["Fauna"].isin(selector_fauna) if selector_fauna else True) &
        (obras_estudio["Lugar"].isin(selector_lugar) if selector_lugar else True) &
        (obras_estudio["Año"].between(selector_año_rango[0], selector_año_rango[1]))
    ]

    # Reemplazar valores nulos
    obras_estudio_filtrado = obras_estudio_filtrado.fillna("Desconocido")

    # Convertir la columna "Año" a enteros para quitar la coma
    obras_estudio_filtrado["Año"] = obras_estudio_filtrado["Año"].astype(int)

    
    
    st.title("Tabla Filtrada")

    # Seleccionar las columnas específicas a mostrar
    columnas_mostrar = ["Titulo", "Autor", "Objetos", "Personajes", "Escuela", "Flora", "Fauna", "Lugar", "Año"]
    st.dataframe(obras_estudio_filtrado[columnas_mostrar])
