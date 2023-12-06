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
floreros = Image.open("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/imagenes/Floreros, Nuzzi, Mario.png")

# Aplicar el estilo a la aplicación
st.markdown(CSS_STYLE_, unsafe_allow_html=True)


st.title("Planteamiento del proyecto: una visión analítica de la iconografía representada en la colección del Museo del Prado.")
# Añadir texto e imágenes para la sección de Explanation of the project
st.markdown(
    f"""
    <div style='text-align: justify;'>
        <h6 style='font-size: 16px; color: #545458;'> En el presente trabajo nos hemos propuesto trasladar el conjunto de métodos
        analíticos basados en la automatización de los procesos de cálculo de las
        máquinas, al terreno del arte y en concreto al área de análisis iconográfico. La
        iconografía es un término que resulta etimológicamente de la unión de los
        vocablos griegos “iconos” (imagen) y “graphein” (escribir) y que podría definirse
        como la disciplina cuyo objeto de estudio es la descripción de las imágenes, o
        cdesde un punto de vista superior, la escritura en imágenes.
        </h6>
        <h6 style='font-size: 18px;font-weight: normal; color: #4D458E;'> ¿Qué quiere decir “escritura de imágenes”?
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> Habitualmente las imágenes en el arte funcionan
        como símbolo y el hecho de que unas determinadas imágenes vayan al lado de
        otras no es casualidad. La imagen de la Virgen María, por ejemplo, pisando un
        dragón o una serpiente es habitual en la iconografía cristiana y significa el
        triunfo del bien sobre el mal, el de la virtud sobre el pecado y puede
        interpretarse como una imagen de la redención: en el origen la humanidad a
        través de Eva fue corrompida por la serpiente, pero María, otra mujer, ha
        vencido a la serpiente. Relaciones regulares, como la mencionada, son
        habituales y conocidas, y hasta cierto punto obvias. Sin embargo, podrían
        existir otra clase de correlaciones menos evidentes u ocultas, algunas de ellas
        propias de una época, otras de un determinado tema, otras terceras
        permanentes en las representaciones del arte, la mayoría de ellas inaccesibles
        para el gran público. En resumen, la iconografía se refiere a una colección de
        tipos particulares de imágenes utilizadas por los artistas para comunicar significados más profundos en sus obras de arte. El análisis iconográfico
        incluye la lectura crítica de las imágenes en relación con los valores sociales y
        culturales relevantes.
        </h6>
    </div>
    """, 
    unsafe_allow_html=True)

st.markdown("---")

        
st.text('   ')

st.image(floreros, caption='Floreros; Nuzzi, Mario', use_column_width=True)
        
st.text('   ')

st.markdown("---")
st.markdown("## Líneas generales y objetivos del proyecto. ¿Qué se pretende conseguir?")
st.markdown(
    f"""
    <div style='text-align: justify;'>
        <h6 style='font-size: 16px; color: #545458;'> El presente trabajo pretende trasladar el conjunto de métodos analíticos
        utilizados para dotar de inteligencia a los negocios al terreno de la museografía.
        Para ello necesita datos iconográficos. El Museo del Prado es probablemente
        el único museo del mundo que dispone de un registro iconográfico de su
        colección que incluye objetos, lugares, personajes, flora y fauna. ¿Cuántas
        veces aparece la virgen con rosas en los cuadros del siglo XVII? 21, pero sólo
        3 en el XVIII, siglo del que el Prado dispone de 156 vírgenes, frente a las 221
        del anterior.
        </h6>
        <h6 style='font-size: 18px;font-weight: normal; color: #4D458E;'> ¿Por qué razón se empezó a dejar de pintar a la Virgen con rosas
en el   siglo XVIII?”?
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> Esto lo tendrán que responder los historiadores del arte u
        otros estudiosos, pero el caso es que esto es así, al menos en la colección del
        Prado, probablemente la mejor colección del mundo en los siglos XVI, XVII y
        XVIII. Otro ejemplo, el cuadro dispone de 12 pinturas que representan a
        Deméter o a Ceres, ciruelas, alcachofas y calabazas aparecen en tres veces,
        en tres de ellos. Son los frutos más repetidos. Pues bien, en los tres cuadros en
        los que aparecen los tres frutos, lo hacen los tres juntos. ¿Qué puede significar
        eso? No es nuestro cometido decirlo, pero si podemos identificar esa
        correlación que parece significativa. Ceres, como es sabido, es la diosa de la
        agricultura. La palabra cereal se deriva de su nombre. Uno esperaría verla más
        veces representada con trigo, cebada u otros cereales. Pues bien, solo en uno
        de los cuadros aparece con cebada. Curioso, ¿no?
        </h6>
    </div>
    """, 
    unsafe_allow_html=True)
st.markdown("---")


st.markdown(
    f"""
    <div style='text-align: justify;'>
        <h6 style='font-size: 16px; color: #545458;'> El presente trabajo pretende trasladar el conjunto de métodos analíticos
        utilizados para dotar de inteligencia a los negocios al terreno de la museografía.
        Para ello necesita datos iconográficos. El Museo del Prado es probablemente
        el único museo del mundo que dispone de un registro iconográfico de su
        colección que incluye objetos, lugares, personajes, flora y fauna. ¿Cuántas
        veces aparece la virgen con rosas en los cuadros del siglo XVII? 21, pero sólo
        3 en el XVIII, siglo del que el Prado dispone de 156 vírgenes, frente a las 221
        del anterior.
        </h6>
        <h6 style='font-size: 18px;font-weight: normal; color: #4D458E;'> ¿Por qué razón se empezó a dejar de pintar a la Virgen con rosas
en el   siglo XVIII?”?
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> Esto lo tendrán que responder los historiadores del arte u
        otros estudiosos, pero el caso es que esto es así, al menos en la colección del
        Prado, probablemente la mejor colección del mundo en los siglos XVI, XVII y
        XVIII. Otro ejemplo, el cuadro dispone de 12 pinturas que representan a
        Deméter o a Ceres, ciruelas, alcachofas y calabazas aparecen en tres veces,
        en tres de ellos. Son los frutos más repetidos. Pues bien, en los tres cuadros en
        los que aparecen los tres frutos, lo hacen los tres juntos. ¿Qué puede significar
        eso? No es nuestro cometido decirlo, pero si podemos identificar esa
        correlación que parece significativa. Ceres, como es sabido, es la diosa de la
        agricultura. La palabra cereal se deriva de su nombre. Uno esperaría verla más
        veces representada con trigo, cebada u otros cereales. Pues bien, solo en uno
        de los cuadros aparece con cebada. Curioso, ¿no?
        </h6>
    </div>
    """, 
    unsafe_allow_html=True)   
    