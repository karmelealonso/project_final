import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import options as opts
from pyecharts.charts import Line
import plotly.express as px
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
import numpy as np


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


 # Obtener valores únicos para cada selector
titulos_list = obras_completo["Título"].unique().tolist()
autores_list = obras_completo["Autor"].unique().tolist()
objetos_list = obras_completo["Objetos"].unique().tolist()
personajes_list = obras_completo["Personajes"].unique().tolist()
escuelas_list = obras_completo["Escuela"].unique().tolist()
fauna_list = obras_completo["Fauna"].unique().tolist()
lugar_list = obras_completo["Lugar"].unique().tolist()
flora_list = obras_completo["Flora"].unique().tolist()


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


# Crear el menú lateral
page = st.sidebar.radio("Selecciona un elemento iconográfico", ["¿Qué podemos encontrar?", "Objectos", "Personajes", "Fauna", "Flora", "Lugar"])


st.title("Análisis sobre la iconografía del Museo del Prado")

if page == "¿Qué podemos encontrar?":
    st.markdown("Breve introducción del proyecto")

    # Selector de rango de años
    selected_year_range = st.slider("Selecciona Rango de Años", min_value=obras_completo["Año"].min(), max_value=obras_completo["Año"].max(), value=(obras_completo["Año"].min(), obras_completo["Año"].max()))

    # Selector de Títulos
    selected_titulos = st.multiselect("Título", titulos_list)

    # Selector de Autores
    selected_autores = st.multiselect("Autores", autores_list)

    # Selector de Objetos
    selected_objetos = st.multiselect("Objetos", objetos_list)

    # Selector de Personajes
    selected_personajes = st.multiselect("Personajes", personajes_list)

    # Selector de Fauna
    selected_fauna = st.multiselect("Fauna", fauna_list)

    # Selector de Escuelas
    selected_flora = st.multiselect("Flora", flora_list)
    
    # Selector de Lugares
    selected_lugar = st.multiselect("Lugares", lugar_list)

    # Selector de Escuelas
    selected_escuelas = st.multiselect("Escuelas", escuelas_list)
    
    # Botón de filtro
    filter_button = st.button("Filtrar")

    # Aplicar el filtro cuando se presiona el botón
    if filter_button:
        # Filtrar el DataFrame basado en los filtros seleccionados
        filtered_df = obras_completo[
            (obras_completo["Título"].isin(selected_titulos) if selected_titulos else True) &
            (obras_completo["Autor"].isin(selected_autores) if selected_autores else True) &
            (obras_completo["Objetos"].isin(selected_objetos) if selected_objetos else True) &
            (obras_completo["Personajes"].isin(selected_personajes) if selected_personajes else True) &
            (obras_completo["Escuela"].isin(selected_escuelas) if selected_escuelas else True) &
            (obras_completo["Fauna"].isin(selected_fauna) if selected_fauna else True) &
            (obras_completo["Lugar"].isin(selected_lugar) if selected_lugar else True) &
            (obras_completo["Año"].between(selected_year_range[0], selected_year_range[1]))
        ]

        # Mostrar la tabla filtrada
        st.title("Tabla Filtrada")
        st.write(filtered_df)


elif page == "Objectos":
    st.markdown("Analytical study of Objects")
        
    # Filtrar el DataFrame solo para los objetos más comunes
    df_objetos_comunes = objetos_streamlit[objetos_streamlit['Objetos'].isin(top_10_objetos)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_objetos_comunes['Frecuencia'] = df_objetos_comunes.groupby('Objetos')['Objetos'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_objetos = df_objetos_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel para objetos
    pie_chart_objetos = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            series_name="Objetos",
            data_pair=[(objeto, objeto_total['Frecuencia'].sum() / frecuencia_total_objetos * 100) 
                        for objeto, objeto_total in df_objetos_comunes.groupby('Objetos')],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Distribución de Frecuencia de Objetos"),
            legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
        )
    )

    # Guardar el gráfico PyEcharts para objetos como un archivo HTML
    pie_chart_objetos.render("pie_chart_objetos.html")

    # Mostrar el gráfico en Streamlit
    st.components.v1.html(open("pie_chart_objetos.html", "r").read(), height=600)
        
    # Agrupar por año y calcular la suma acumulativa de las apariciones de cada objeto
    df_objetos_comunes_grouped = df_objetos_comunes.groupby(['Año', 'Objetos']).agg({'Frecuencia': 'sum'}).reset_index()
    df_objetos_comunes_grouped['Frecuencia_cumsum'] = df_objetos_comunes_grouped.groupby('Objetos')['Frecuencia'].cumsum()

    
    
    # Crear el gráfico de líneas
    line_chart_objetos = (
        Line()
        .add_xaxis(xaxis_data=df_objetos_comunes_grouped['Año'].tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Evolución de Aparición de Top 10 Objetos a lo largo del Tiempo"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            legend_opts=opts.LegendOpts(pos_right="10%", pos_top="5%"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
    )

    # Agregar líneas al gráfico con la suma acumulativa
    for objeto in top_10_objetos:
        data = df_objetos_comunes_grouped[df_objetos_comunes_grouped['Objetos'] == objeto]
        line_chart_objetos.add_yaxis(
            series_name=objeto,
            y_axis=data['Frecuencia_cumsum'].tolist(),
            is_smooth=True
        )

    # Renderizar el gráfico
    chart_html_objetos = line_chart_objetos.render("line_chart_objetos.html")

    # Mostrar el gráfico en Streamlit
    st.components.v1.html(chart_html_objetos, height=600)


# Crear la subpágina "Personajes"
elif page == "Personajes":
    st.title("Personajes")
    st.markdown("Estudio analítico de los Personajes")

    # Definir una clave única para el filtro de personajes
    key_personajes_filter = "personajes_filter"

    # Filtro para seleccionar personajes
    selected_personajes = st.sidebar.multiselect(
        f"Seleccionar Personajes", top_10_personajes, default=top_10_personajes, key=key_personajes_filter
    )

    # Filtrar el DataFrame para los personajes seleccionados
    df_personajes_comunes = personajes_streamlit[personajes_streamlit['Personajes'].isin(selected_personajes)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_personajes_comunes['Frecuencia'] = df_personajes_comunes.groupby('Personajes')['Personajes'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total = df_personajes_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel
    pie_chart = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND))
        .add(
            series_name="Personajes",
            data_pair=[(personaje, personaje_total['Frecuencia'].sum() / frecuencia_total * 100) 
                    for personaje, personaje_total in df_personajes_comunes.groupby('Personajes')],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Distribución de Frecuencia de Personajes"),
            
            legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
        )
    )

            



    # Guardar el gráfico PyEcharts como un archivo HTML
    pie_chart.render("pie_chart.html")


    # Mostrar el gráfico en Streamlit
    st.components.v1.html(open("pie_chart.html", "r").read(), height=600)


    # Calculo cuantos personajes tiene cada obra:
    titulo_personajes_frecuencia = personajes_streamlit.groupby(['Título', 'Personajes']).size().reset_index(name='Frecuencia')

    # Agrupo por el título para obtener la lista de los personajes representados en cada una de las obras:
    titulo_personajes = titulo_personajes_frecuencia.groupby('Título')['Personajes'].unique().reset_index(name='Personajes_en_obra')
    
    # Filtrar por personajes seleccionados
    titulo_personajes['Personajes_en_obra'] = titulo_personajes['Personajes_en_obra'].apply(lambda x: [p for p in x if p in selected_personajes])

    # Creamos la matriz de correlaciones
    correlation_matrix = pd.DataFrame(0, index=selected_personajes, columns=selected_personajes)

    for personajes_en_obra in titulo_personajes['Personajes_en_obra']:
        for i in range(len(personajes_en_obra)):
            for j in range(i + 1, len(personajes_en_obra)):
                personaje1 = personajes_en_obra[i]
                personaje2 = personajes_en_obra[j]

                correlation_matrix.at[personaje1, personaje2] += 1
                correlation_matrix.at[personaje2, personaje1] += 1

    # Convertimos la matriz a un formato adecuado para Plotly
    correlation_matrix_plotly = correlation_matrix.unstack().reset_index()
    correlation_matrix_plotly.columns = ['Personaje1', 'Personaje2', 'Frecuencia']

    # Pivot the DataFrame to create a 2D matrix
    correlation_matrix_2d = correlation_matrix_plotly.pivot(index='Personaje1', columns='Personaje2', values='Frecuencia').fillna(0)

    # Convert to NumPy array
    correlation_matrix_array = correlation_matrix_2d.values

    # Creamos el heatmap interactivo con Plotly Express
    fig = px.imshow(correlation_matrix_array,
                    x=correlation_matrix_2d.columns, 
                    y=correlation_matrix_2d.index,
                    labels=dict(x="Personaje 1", y="Personaje 2", color="Frecuencia"),
                    title='Mapa de Correlaciones entre los Personajes Seleccionados',
                    color_continuous_scale="Viridis",
                    width=800, height=600)

    # Añadimos el texto de frecuencia a la matriz de correlaciones
    annotations = []
    for i, personaje1 in enumerate(correlation_matrix_2d.index):
        for j, personaje2 in enumerate(correlation_matrix_2d.columns):
            value = correlation_matrix_2d.at[personaje1, personaje2]
            annotations.append(dict(text=str(value), x=personaje2, y=personaje1,
                                    xref='x1', yref='y1', showarrow=False, font=dict(color='white')))

    fig.update_layout(annotations=annotations)

    st.plotly_chart(fig)

    
    
        # Convertir la columna 'Año' a tipo datetime
    personajes_streamlit['Año'] = pd.to_datetime(personajes_streamlit['Año'], format='%Y', errors='coerce', infer_datetime_format=True, yearfirst=True)

    # Crear una nueva columna 'Década'
    personajes_streamlit['Década'] = personajes_streamlit['Año'].dt.year // 10 * 10

    # Filtro deslizable para seleccionar rango de décadas
    decadas_range = st.sidebar.slider(
        "Seleccionar Rango de Décadas",
        min_value=personajes_streamlit['Década'].min(),
        max_value=personajes_streamlit['Década'].max(),
        value=(personajes_streamlit['Década'].min(), personajes_streamlit['Década'].max())
    )


    # Filtrar el DataFrame para los personajes seleccionados y rango de décadas
    df_filtrado_decadas = personajes_streamlit[
        (personajes_streamlit['Personajes'].isin(selected_personajes)) &
        (personajes_streamlit['Década'].between(*decadas_range))
    ]

    # Calcular la frecuencia de personajes por década
    df_frecuencia_decadas = df_filtrado_decadas.groupby(['Década', 'Personajes']).size().reset_index(name='Frecuencia')

    # Crear el gráfico de líneas con Plotly Express
    line_chart = px.line(df_frecuencia_decadas, x='Década', y='Frecuencia', color='Personajes',
                        labels={'Frecuencia': 'Número de Apariciones'}, title='Desarrollo de Personajes a lo largo del Tiempo')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line_chart)








elif page == "Fauna":
    st.markdown("Analytical study of Fauna")
        
    # Filtrar el DataFrame solo para los personajes más comunes
    df_fauna_comunes = fauna_streamlit[fauna_streamlit['Fauna'].isin(top_10_fauna)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_fauna_comunes['Frecuencia'] = df_fauna_comunes.groupby('Fauna')['Fauna'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_fauna = df_fauna_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel para objetos
    pie_chart_fauna = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            series_name="Fauna",
            data_pair=[(fauna, fauna_total['Frecuencia'].sum() / frecuencia_total_fauna * 100) 
                    for fauna, fauna_total in df_fauna_comunes.groupby('Fauna')],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Distribución de Frecuencia de Fauna"),
            legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
        )
    )

    # Guardar el gráfico PyEcharts para objetos como un archivo HTML
    pie_chart_fauna.render("pie_chart_fauna.html")

    # Mostrar el gráfico en Streamlit
    st.components.v1.html(open("pie_chart_fauna.html", "r").read(), height=600)
        


elif page == "Flora":
    st.markdown("Analytical study of Flora")
        
    # Filtrar el DataFrame solo para los personajes más comunes
    df_flora_comunes = flora_streamlit[flora_streamlit['Flora'].isin(top_10_flora)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_flora_comunes['Frecuencia'] = df_flora_comunes.groupby('Flora')['Flora'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_flora = df_flora_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel para objetos
    pie_chart_flora = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            series_name="Flora",
            data_pair=[(flora, flora_total['Frecuencia'].sum() / frecuencia_total_flora * 100) 
                    for flora, flora_total in df_flora_comunes.groupby('Flora')],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Distribución de Frecuencia de Flora"),
            legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
        )
    )

    # Guardar el gráfico PyEcharts para objetos como un archivo HTML
    pie_chart_flora.render("pie_chart_flora.html")

    # Mostrar el gráfico en Streamlit
    st.components.v1.html(open("pie_chart_flora.html", "r").read(), height=600)
        

elif page == "Lugar":
    st.markdown("Analytical study of Places")
        
    # Filtrar el DataFrame solo para los personajes más comunes
    df_lugar_comunes = lugar_streamlit[lugar_streamlit['Lugar'].isin(top_10_lugar)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_lugar_comunes['Frecuencia'] = df_lugar_comunes.groupby('Lugar')['Lugar'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_lugar = df_lugar_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel para objetos
    pie_chart_lugar = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            series_name="Lugar",
            data_pair=[(lugar, lugar_total['Frecuencia'].sum() / frecuencia_total_lugar * 100) 
                    for lugar, lugar_total in df_lugar_comunes.groupby('Lugar')],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Distribución de Frecuencia de Lugar"),
            legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
        )
    )

    # Guardar el gráfico PyEcharts para objetos como un archivo HTML
    pie_chart_lugar.render("pie_chart_lugar.html")

    # Mostrar el gráfico en Streamlit
    st.components.v1.html(open("pie_chart_lugar.html", "r").read(), height=600)

    print(personajes_comunes)
