import streamlit as st
import pandas as pd
from PIL import Image
from pymongo import MongoClient


#Enlazar con la Base de Datos creada en Mongo
client = MongoClient("mongodb://localhost:27017/")
db = client.icongrafia_cuadros_prado
collection = db.cuadros_estudio 

query = collection.find()
cuadros_estudio = pd.DataFrame(query)


# Filtrar las filas que contienen "Desconocido" en la columna "Fecha"
cuadros_estudio = cuadros_estudio[cuadros_estudio["Fecha"] != "Desconocido"]

# Establecer los años mínimo y máximo
min_year = pd.to_numeric(cuadros_estudio['Fecha'].min(), errors="coerce")
max_year = pd.to_numeric(cuadros_estudio['Fecha'].max(), errors="coerce")

# Obtener valores únicos para cada selector
titulo_list = cuadros_estudio["Titulo"].unique().tolist()
autor_list = cuadros_estudio["Autor"].unique().tolist()
escuela_list = cuadros_estudio["Escuela"].unique().tolist()
objetos_list = cuadros_estudio["Objetos"].unique().tolist()
personajes_list = cuadros_estudio["Personajes"].unique().tolist()
flora_list = cuadros_estudio["Flora"].unique().tolist()
fauna_list = cuadros_estudio["Fauna"].unique().tolist()
geografico_list = cuadros_estudio["Geografico"].unique().tolist()
soporte_list = cuadros_estudio["Soporte"].unique().tolist()
ubicacion_list = cuadros_estudio["Ubicacion"].unique().tolist()



st.title("¿Qué podemos encontrarnos?")
        
st.text('   ')

st.markdown("---")



# Selector de rango de años
selector_año_rango = st.slider("Selecciona Rango de Fechas", min_value=min_year, max_value=max_year, value=(min_year, max_year))

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

# Selector de Soporte
selector_soporte = st.multiselect("Soporte", soporte_list)

# Selector de Geografico
selector_geografico = st.multiselect("Geografico", geografico_list)

# Selector de Ubicacion
selector_ubicacion = st.multiselect("Ubicacion", ubicacion_list)


# Botón
boton_filtrado = st.button("Filtrar")

# Aplicar el filtrado cuando se presiona el botón
if boton_filtrado:
    # Filtrar el DataFrame basado en los filtrados seleccionados
    cuadros_estudio_filtrado = cuadros_estudio[
        (cuadros_estudio["Titulo"].isin(selector_titulos) if selector_titulos else True) &
        (cuadros_estudio["Autor"].isin(selector_autores) if selector_autores else True) &
        (cuadros_estudio["Escuela"].isin(selector_escuelas) if selector_escuelas else True) &
        (cuadros_estudio["Objetos"].isin(selector_objetos) if selector_objetos else True) &
        (cuadros_estudio["Personajes"].isin(selector_personajes) if selector_personajes else True) &
        (cuadros_estudio["Flora"].isin(selector_flora) if selector_flora else True) &
        (cuadros_estudio["Fauna"].isin(selector_fauna) if selector_fauna else True) &
        (cuadros_estudio["Soporte"].isin(selector_soporte) if selector_soporte else True) &
        (cuadros_estudio["Ubicacion"].isin(selector_ubicacion) if selector_ubicacion else True) &
        (cuadros_estudio["Geografico"].isin(selector_geografico) if selector_geografico else True) &
        (cuadros_estudio["Fecha"].between(selector_año_rango[0], selector_año_rango[1]))
    ]

    # Reemplazar valores nulos
    cuadros_estudio_filtrado = cuadros_estudio_filtrado.fillna("Desconocido")

    # Convertir la columna "Fecha" a enteros 
    cuadros_estudio_filtrado["Fecha"] = cuadros_estudio_filtrado["Fecha"].astype(int)

    
    
    st.title("Tabla Filtrada")

    # Seleccionar las columnas específicas a mostrar
    columnas_mostrar = ["Titulo", "Autor", "Objetos", "Personajes", "Escuela", "Flora", "Fauna", "Geografico", "Soporte", "Fecha", "Ubicacion"]
    st.dataframe(cuadros_estudio_filtrado[columnas_mostrar])
