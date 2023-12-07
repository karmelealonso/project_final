import streamlit as st
import pandas as pd
from PIL import Image



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


st.markdown("## Home")

st.text('   ')


st.markdown("---")

st.title("Un análisis iconográfico de la colección del Museo Del Prado")

st.text('   ')


st.markdown("---")

floreros = Image.open("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/imagenes/Floreros, Nuzzi, Mario (1640-1642).png")
el_oido = Image.open("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/imagenes/El oído.png")
en_vue = Image.open("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/imagenes/En vue.png")
leon_lobos = Image.open("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/imagenes/Un leon y tres lobos.png")

def apartado1():
    col1, col2 = st.columns(2)
    with col1:
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
            Tradicionalmente, los sistemas de  Analítica Avanzada de Datos y el
            Aprendizaje Automático se han utilizado, y utilizan, con diversas finalidades y
            en diversos sectores, como Defensa, Sanidad, Investigación, Finanzas,
            Seguridad, Análisis de Marcados…
            </h6>
            <h6 style='font-size: 16px; color: #545458;'> Tradicionalmente, los sistemas de  Analítica Avanzada de Datos y el
            Aprendizaje Automático se han utilizado, y utilizan, con diversas finalidades y
            en diversos sectores, como Defensa, Sanidad, Investigación, Finanzas,
            Seguridad, Análisis de Marcados…
            </h6>
        </div>
        """, 
        unsafe_allow_html=True)
    
    # Mostrar imagen en la segunda columna
    with col2:
        st.image(leon_lobos, caption='"Un león y tres lobos"; Vos, Paul de (Siglo XVII)')



# Función para el segundo apartado
def apartado2():
    # Mostrar imagen en la primera columna
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(en_vue, caption='"En Vue"; Palmaroli González, Vicente (1834-1896)')

    with col2:
        st.markdown(
        f"""
        <div style='text-align: justify;'>
            <h6 style='font-size: 16px; color: #545458;'> Algunos ejemplos son:
            </h6>
            <ul>
                <li>Diagnóstico médico</li>
                <li>Diseño de fármacos</li>
                <li>Mantenimiento predictivo de maquinaria industrial, de vehículos, etc…</li>
                <li>Predicciones climáticas</li>
                <li>Gestión de datos de clientes</li>
                <li>Perfilado y personalización de la experiencia de usuario</li>
                <li>Ciberseguridad y detección predictiva de anomalías</li>
                <li>Detección de fraudes</li>
                <li>Gestión del riesgo</li>
                <li>Realización de estudios de mercado</li>
                <!-- Agrega más elementos según sea necesario -->
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )
# Función para el tercer apartado
def apartado3():
    col1, col2 = st.columns(2)
    with col1:
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
    
    with col2:
        st.image(el_oido, caption='"Floreros"; Brueghel el Viejo, Jan (1617-1618)')


# Añadir los tres apartados
apartado1()
st.markdown("---")
apartado2()
st.markdown("---")
apartado3()
