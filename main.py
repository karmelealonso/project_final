# Importar la biblioteca Streamlit
import streamlit as st
import pandas as pd

#PRIMERO IMPORTO LOS DATOS:

# Load the data
df = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/obras_completo_para_estudio.csv")
personajes_año_rango = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/personajes_año_rango_para_streamlit.csv")


# Llenar los valores nulos con 'Desconocidos' o 'Desconocida'
df['Objetos'] = df['Objetos'].fillna('Desconocidos')
df['Fauna'] = df['Fauna'].fillna('Desconocida')
df['Lugar'] = df['Lugar'].fillna('Desconocido')
personajes_año_rango['Personajes'] = df['Personajes'].fillna('Desconocidos')

# Filtrar categorías desconocidas
df_filtered = df[
    (df['Objetos'] != 'Desconocidos') &
    (df['Fauna'] != 'Desconocida') &
    (df['Lugar'] != 'Desconocido') &
    (df['Personajes'] != 'Desconocidos')
]

# Get the 10 most repeated elements in each category
top_10_characters = personajes_año_rango['Personajes'].value_counts().head(10).index.tolist()
top_10_objects = df_filtered['Objetos'].value_counts().head(10).index.tolist()
top_10_fauna = df_filtered['Fauna'].value_counts().head(10).index.tolist()
top_10_flora = df_filtered['Flora'].value_counts().head(10).index.tolist()
top_10_place = df_filtered['Lugar'].value_counts().head(10).index.tolist()

# Estilo CSS
st.markdown(
    """
    <style>
    body {
        color: #FAFAFA;
        background-color: #848C8E;
        font-family: sans-serif;
    }
    .stApp {
        background-color: #848C8E;
        color: #FAFAFA;
    }
    .stSelectbox, .stSlider, .stCheckbox, .stMultiselect {
        background-color: #022B3A;
        color: #FAFAFA;
    }
    .stTextInput, .stTextArea {
        background-color: #022B3A;
        color: #FAFAFA;
    }
    .stMarkdown {
        color: #FAFAFA;
    }
    .stButton {
        background-color: #FF8966;
        color: #FAFAFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

        # Define the sidebar menu for the "Analytical Studies" section
        # Move the filters into the sidebar
        selected_characters = st.sidebar.multiselect('Select characters', top_10_characters)
        selected_objects = st.sidebar.multiselect('Select objects', top_10_objects)
        selected_fauna = st.sidebar.multiselect('Select fauna elements', top_10_fauna)
        selected_flora = st.sidebar.multiselect('Select flora elements', top_10_flora)
        selected_places = st.sidebar.multiselect('Select place elements', top_10_place)

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
        # Añadir contenido para la categoría de Places
