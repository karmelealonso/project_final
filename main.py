import streamlit as st
import pandas as pd


# Cargar los nuevos DataFrames
personajes_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/personajes_streamlit.csv")
objetos_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/objetos_streamlit.csv")
fauna_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/fauna_streamlit.csv")
flora_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/flora_streamlit.csv")
lugar_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/lugar_streamlit.csv")

# Obtener los 10 elementos más repetidos en cada categoría
top_10_characters = ["Seleccionar Todas"] + personajes_streamlit['Personajes'].value_counts().head(10).index.tolist()
top_10_objects = ["Seleccionar Todas"] + objetos_streamlit['Objetos'].value_counts().head(10).index.tolist()
top_10_fauna = ["Seleccionar Todas"] + fauna_streamlit['Fauna'].value_counts().head(10).index.tolist()
top_10_flora = ["Seleccionar Todas"] + flora_streamlit['Flora'].value_counts().head(10).index.tolist()
top_10_place = ["Seleccionar Todas"] + lugar_streamlit['Lugar'].value_counts().head(10).index.tolist()

# Obtener todos los valores únicos en las categorías de Escuela y Año_rango
unique_escuelas = personajes_streamlit['Escuela'].dropna().unique()
unique_anio_rango = personajes_streamlit['Año_rango'].dropna().unique().tolist()

# Ordenar los años en orden ascendente según la lista proporcionada
orden_cronologico = ['(-400) - (-200)', '(-201) - 0', '1 - 200', '201 - 400', '401 - 600', '601 - 800', '801 - 1000', '1001 - 1200', '1201 - 1400', '1401 - 1600', '1601 - 1800', '1801 - 2000']
unique_anio_rango = sorted(unique_anio_rango, key=lambda x: orden_cronologico.index(x))

# Establecer los años mínimo y máximo
min_year = personajes_streamlit['Año'].min()
max_year = personajes_streamlit['Año'].max()

# Configuración del tema
st.set_page_config(
    page_title="Your App Name",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",  # Puedes cambiar esto a "collapsed" si prefieres que la barra lateral esté plegada inicialmente
)

# ESTILO DE LA APLICACIÓN

CSS_STYLE_ = """
<style>

MainMenu {
    visibility:hidden;
}

footer {
    visibility:visible;
}

# Font family for all text in the app, except code blocks. One of "sans serif", "serif", or "monospace".
font = "sans serif"

h1 {
    color: #FF8966;
}
h2 {
    color: #848C8E;
}
h3 {
    color: #022B3A;
}
h4 {
    color: #FAFAFA;
}

.badge-custom {
    color: #CCCCCC;
    background-color: #0000CC;
}

button[data-baseweb="tab"] {
    font-size: 18px;
    color: #FE4A4A;
}

</style>

<link rel="stylesheet" href="https://m axcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
"""


# Crear el menú lateral
page = st.sidebar.radio("", ["Home", "Analytical Studies", "Timeline"])

if page == "Home":
    st.title("Home")
    st.markdown("## Explanation of the project")
    # Añadir texto e imágenes para la sección de Explanation of the project
    st.markdown("---")
    st.markdown("## Hypothesis")
    # Añadir texto e imágenes para la sección de Hypothesis
    st.markdown("---")
    st.markdown("## General and specific objectives")
    # Añadir texto e imágenes para la sección de General and specific objectives
    st.markdown("---")
    st.markdown("## Materials and methods")
    # Añadir texto e imágenes para la sección de Materials and methods
    st.markdown("---")
    st.markdown("## Inclusion criteria")
    # Añadir texto e imágenes para la sección de Inclusion criteria


elif page == "Analytical Studies":
    # Crear el submenú para Analytical Studies
    sub_page = st.sidebar.radio("", ["Analytical Studies", "Characters", "Objects", "Fauna", "Flora", "Places"])

    if sub_page == "Analytical Studies":
        st.title("Analytical Studies")
        st.markdown("Analytical studies")

        # Definir el menú lateral para la sección "Analytical Studies"
        # Mover los filtros al menú lateral
        selected_characters = st.sidebar.multiselect('Select characters', top_10_characters)
        selected_objects = st.sidebar.multiselect('Select objects', top_10_objects)
        selected_fauna = st.sidebar.multiselect('Select fauna elements', top_10_fauna)
        selected_flora = st.sidebar.multiselect('Select flora elements', top_10_flora)
        selected_places = st.sidebar.multiselect('Select place elements', top_10_place)

        # Nuevo filtro para el rango de años
        st.sidebar.markdown("### Select year range:")
        selected_year_range = st.sidebar.slider(
            label="",
            min_value=-400,
            max_value=2000,
            value=(min_year, max_year),
            step=1,
            format="%d"
        )

    elif sub_page == "Characters":
        st.title("Characters")
        st.markdown("Here you can explore the analytical studies of characters.")
        # Añadir componentes interactivos para los estudios analíticos de personajes
        # Por ejemplo, puedes usar st.selectbox, st.slider, st.checkbox, etc.
        

    elif sub_page == "Objects":
        st.title("Objects")
        st.markdown("Analytical study of the objects")
        # Añadir contenido para la categoría de Objects

    elif sub_page == "Fauna":
        st.title("Fauna")
        st.markdown("Analytical study of the fauna")
        # Añadir contenido para la categoría de Fauna

    elif sub_page == "Flora":
        st.title("Flora")
        st.markdown("Analytical study of the flora")
        # Añadir contenido para la categoría de Flora

    elif sub_page == "Places":
        st.title("Places")
        st.markdown("Analytical study of the places")
        selected_escuela_places = st.sidebar.multiselect('Select school', unique_escuelas)
        selected_anio_rango_places = st.sidebar.mult

    # Nuevo filtro para Escuela
    selected_escuela = st.sidebar.multiselect('Select school', unique_escuelas)

    # Nuevo filtro para Año_rango
    selected_anio_rango = st.sidebar.multiselect('Select year range', unique_anio_rango)

