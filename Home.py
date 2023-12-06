import streamlit as st
import pandas as pd

# Cargar los nuevos DataFrames
obras_completo = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/obras_completo.csv")
personajes_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/personajes_streamlit.csv")
objetos_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/objetos_streamlit.csv")
fauna_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/fauna_streamlit.csv")
flora_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/flora_streamlit.csv")
lugar_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/lugar_streamlit.csv")

# Función para obtener los top 10 elementos según la categoría seleccionada
def get_top_10_elements(category_df):
    return ["Seleccionar Todas"] + category_df.iloc[:, 0].value_counts().head(10).index.tolist()

# Cargar los top 10 elementos iniciales y valores únicos de rango de años para cada categoría
top_10_personajes = get_top_10_elements(personajes_streamlit)
top_10_objetos = get_top_10_elements(objetos_streamlit)
top_10_fauna = get_top_10_elements(fauna_streamlit)
top_10_flora = get_top_10_elements(flora_streamlit)
top_10_lugar = get_top_10_elements(lugar_streamlit)


# Obtener todos los valores únicos en las categorías de Escuela y Año_rango
unique_escuelas = personajes_streamlit['Escuela'].dropna().unique()
unique_anio_rango = personajes_streamlit['Año_rango'].dropna().unique().tolist()

# Establecer los años mínimo y máximo
min_year = personajes_streamlit['Año'].min()
max_year = personajes_streamlit['Año'].max()

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


# Aplicar el estilo a la aplicación
st.markdown(CSS_STYLE_, unsafe_allow_html=True)


st.title("Home")

st.title("Una aproximación a un modelo de iconografía analítica sobre la base de la iconografía del Museo Del Prado")
# Añadir texto e imágenes para la sección de Explanation of the project
def apartado1():
    st.markdown(
        f"""
        <div style='text-align: justify;'>
            <h6 style='font-size: 16px; color: #545458;'> El los métodos estadísticos predictivos y el Aprendizaje Automático, junto con
            otras técnicas de Analítica de Datos de base estadística, es actualmente la
            herramienta una de las herramientas más potentes para la detección
            automática de patrones en conjuntos de datos masivos. Esa clase de patrones
            revelan relaciones regulares en los datos que nos posibilitan tomar decisiones,
            predecir y evitar riesgos o conocer simplemente cómo está organizado el
            mundo en un determinado dominio de conocimiento.
            </h6>
        </div>
        """, 
        unsafe_allow_html=True)
    
    # Mostrar imagen en la segunda columna
    col1, col2 = st.columns(2)
    with col2:
        st.image("Imagen")

# Función para el segundo apartado
def apartado2():
    # Mostrar imagen en la primera columna
    col1, col2 = st.columns(2)
    with col1:
        st.image("Imagen")  # Reemplaza "Imagen" con tu variable de imagen

    st.markdown(
        f"""
        <div style='text-align: justify;'>
            <h6 style='font-size: 16px; color: #545458;'> Tradicionalmente, los sistemas de  Analítica Avanzada de Datos y el
            Aprendizaje Automático se han utilizado, y utilizan, con diversas finalidades y
            en diversos sectores, como Defensa, Sanidad, Investigación, Finanzas,
            Seguridad, Análisis de Marcados…:
                 Diagnóstico médico
                 Diseño de fármacos
                 Mantenimiento predictivo de maquinaria industrial, de vehículos, etc…
                 Predicciones climáticas
                 Gestión de datos de clientes
                 Perfilado y personalización de la experiencia de usuario
                 Ciberseguridad y detección predictiva de anomalías
                 Detección de fraudes
                 Gestión del riesgo
                 Realización de estudios de mercado
                 …
            </h6>
        </div>
        """, 
        unsafe_allow_html=True)

# Función para el tercer apartado
def apartado3():
    st.markdown(
        f"""
        <div style='text-align: justify;'>
            <h6 style='font-size: 16px; color: #545458;'> La Analítica de Datos aportaría las evidencias necesarias para poder
            desarrollar procesos de Inteligencia de Negocio (Business Intelligence), que es
            aquella disciplina, conjunto de métodos y prácticas orientadas a comprender la
            información más relevante para tomar decisiones de negocio acertadas.

            La Inteligencia de Negocio (Business Intelligence), combina la minería de datos
            y sus visualizaciones con métodos de análisis con el fin de ayudar a las
            organizaciones a tomar decisiones basadas en los datos. Para ello, debe
            disponerse de una visión integral y enlazada de los datos que afectan a la
            organización, integrando datos internos con datos procedentes del exterior. La
            preparación de los datos incluye los procesos de agregación y transformación
            de los datos, la minería de datos, la minería y lectura automática de textos, el
            análisis de series temporales, el análisis predictivo y la visualización de los
            datos.
            </h6>
        </div>
        """, 
        unsafe_allow_html=True)
    
    # Mostrar imagen en la segunda columna
    col1, col2 = st.columns(2)
    with col2:
        st.image("Imagen")  # Reemplaza "Imagen" con tu variable de imagen

# Usar las funciones en tu aplicación
st.title("Home")

# Añadir los tres apartados
apartado1()
st.markdown("---")
apartado2()
st.markdown("---")
apartado3()
    

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