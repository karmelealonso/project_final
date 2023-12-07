import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import options as opts
from pyecharts.charts import Line
import plotly.express as px
from pyecharts.globals import ThemeType
import numpy as np
import random



# Cargar los nuevos DataFrames
obras_completo = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/obras_completo.csv")
personajes_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/personajes_streamlit.csv")
objetos_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/objetos_streamlit.csv")
fauna_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/fauna_streamlit.csv")
flora_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/flora_streamlit.csv")
lugar_streamlit = pd.read_csv("/Users/karmelealonsoaia/Desktop/ironhack_labs/PROYECTOS/project_final/data/data_clean/data_streamlit/lugar_streamlit.csv")

# Función para obtener los top 10 elementos según la categoría seleccionada
def get_top_10_elements(category_df):
    return category_df.iloc[:, 0].value_counts().head(10).index.tolist()


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


# Crear el menú lateral
page = st.sidebar.radio("Selecciona un elemento iconográfico", ["¿Qué podemos encontrar?", "Objetos", "Personajes", "Fauna", "Flora", "Lugar"])


st.title("Análisis sobre la iconografía del Museo del Prado")

if page == "¿Qué podemos encontrar?":


    # Selector de rango de años
    selector_año_rango = st.slider("Selecciona Rango de Años", min_value=obras_completo["Año"].min(), max_value=obras_completo["Año"].max(), value=(obras_completo["Año"].min(), obras_completo["Año"].max()))

    # Selector de Títulos
    selector_titulos = st.multiselect("Título", titulos_list)

    # Selector de Autores
    selector_autores = st.multiselect("Autores", autores_list)

    # Selector de Objetos
    selector_objetos = st.multiselect("Objetos", objetos_list)

    # Selector de Personajes
    selector_personajes = st.multiselect("Personajes", personajes_list)

    # Selector de Fauna
    selector_fauna = st.multiselect("Fauna", fauna_list)

    # Selector de Escuelas
    selector_flora = st.multiselect("Flora", flora_list)
    
    # Selector de Lugares
    selector_lugar = st.multiselect("Lugares", lugar_list)

    # Selector de Escuelas
    selector_escuelas = st.multiselect("Escuelas", escuelas_list)
    
    # Botón de sin_nulos
    boton_sin_nulos = st.button("Filtrar")

    # Aplicar el sin_nulos cuando se presiona el botón
    if boton_sin_nulos:
        # Filtrar el DataFrame basado en los sin_nuloss seleccionados
        obras_completo_sin_nulos = obras_completo[
            (obras_completo["Título"].isin(selector_titulos) if selector_titulos else True) &
            (obras_completo["Autor"].isin(selector_autores) if selector_autores else True) &
            (obras_completo["Objetos"].isin(selector_objetos) if selector_objetos else True) &
            (obras_completo["Personajes"].isin(selector_personajes) if selector_personajes else True) &
            (obras_completo["Escuela"].isin(selector_escuelas) if selector_escuelas else True) &
            (obras_completo["Fauna"].isin(selector_fauna) if selector_fauna else True) &
            (obras_completo["Lugar"].isin(selector_lugar) if selector_lugar else True) &
            (obras_completo["Año"].between(selector_año_rango[0], selector_año_rango[1]))
        ]

        # Reemplazar valores nulos con una cadena vacía
        obras_completo_sin_nulos = obras_completo_sin_nulos.fillna("Desconocido")

        # Convertir la columna "Año" a enteros para quitar la coma
        obras_completo_sin_nulos["Año"] = obras_completo_sin_nulos["Año"].astype(int)
        
        # Mostrar la tabla filtrada
        st.title("Tabla Filtrada")
    
        # Seleccionar las columnas específicas que deseas mostrar
        columnas_mostrar = ["Título", "Autor", "Objetos", "Personajes", "Escuela", "Fauna", "Lugar", "Año"]
        st.dataframe(obras_completo_sin_nulos[columnas_mostrar])


elif page == "Objectos":
    st.title("Objetos")
    

    # Definir una clave única para el sin_nulos de personajes
    key_objetos_filter = "objetos_filter"

    # Filtro para seleccionar personajes
    selector_objetos = st.sidebar.multiselect(
        f"Seleccionar Objetos", top_10_objetos, default=top_10_objetos, key=key_objetos_filter
    )

    # Ordenar las edades de manera lógica
    orden_objetos = ['Enseres domésticos', 'Florero', 'Cestería', 'Objetos artísticos', 'Pintura', 'Cuadro dentro de cuadro', 'Jardín', 'Elementos de arquitectura', 'Objeto de adorno o servicio de mesa', 'Objeto uso individual']

    # Elegimos los colores:
    color = ['#117A65  ', '#f26722', '#cd2027', '#139b48', '#04B4A2', '#f1eb1f', '#4c2600', '#0a3452', '#259E04',
             '#4554a5']
   


    # Filtrar el DataFrame solo para los elementos más comunes
    df_objetos_comunes = objetos_streamlit[objetos_streamlit['Objetos'].isin(top_10_objetos)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_objetos_comunes['Frecuencia'] = df_objetos_comunes.groupby('Objetos')['Objetos'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_objetos = df_objetos_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel con Plotly Express
    pie_chart_objetos = px.pie(
        df_objetos_comunes,
        names='Objetos',
        values='Frecuencia',
        title='Distribución de Frecuencia de Objetos',
        hover_data=['Objetos', 'Frecuencia'],
        labels={'Frecuencia': 'Porcentaje'},
        category_orders={'Objetos': orden_objetos},
        color_discrete_sequence=color,
        hole=0.4
    )

    # Establecer dimensiones del gráfico
    pie_chart_objetos.update_layout(width=1000, height=600)

    # Mostrar el gráfico de pastel en Streamlit
    st.plotly_chart(pie_chart_objetos)

    
            
    # Convertir la columna 'Año' a tipo datetime
    objetos_streamlit['Año'] = pd.to_datetime(objetos_streamlit['Año'], format='%Y', errors='coerce', infer_datetime_format=True, yearfirst=True)

    # Crear una nueva columna 'Década'
    objetos_streamlit['Década'] = objetos_streamlit['Año'].dt.year // 10 * 10

    # Filtro deslizable para seleccionar rango de décadas
    decadas_range_objetos = st.sidebar.slider(
        "Seleccionar Rango de Décadas",
        min_value=objetos_streamlit['Década'].min(),
        max_value=objetos_streamlit['Década'].max(),
        value=(objetos_streamlit['Década'].min(), objetos_streamlit['Década'].max())
    )

    # Filtrar el DataFrame para los objetos seleccionados y rango de décadas
    df_filtrado_decadas_objetos = objetos_streamlit[
        (objetos_streamlit['Objetos'].isin(selector_objetos)) &
        (objetos_streamlit['Década'].between(*decadas_range_objetos))
    ]

    # Calcular la frecuencia de objetos por década
    df_frecuencia_decadas_objetos = df_filtrado_decadas_objetos.groupby(['Década', 'Objetos']).size().reset_index(name='Frecuencia')

    # Crear el gráfico de líneas con Plotly Express
    line_chart_objetos = px.line(df_frecuencia_decadas_objetos, 
                                 x='Década', 
                                 y='Frecuencia', 
                                 color='Objetos',
                                 category_orders={'Objetos': orden_objetos},
                                 color_discrete_sequence=color,
                                 labels={'Frecuencia': 'Número de Apariciones'}, 
                                 title='Desarrollo de Objetos a lo largo del Tiempo')
    
    # Ocultar la leyenda
    line_chart_objetos.update_layout(width=1000, height=600)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line_chart_objetos)



    # Obtener valores únicos de la columna 'Escuela'
    unique_escuelas = objetos_streamlit['Escuela'].unique()

    # Filtro para seleccionar escuelas
    selector_escuelas = st.sidebar.multiselect(
        "Seleccionar Escuelas", unique_escuelas, default=unique_escuelas, key="escuelas_filter"
    )

    # Obtener los 10 elementos más comunes de la columna 'Objetos'
    top10_objetos = objetos_streamlit['Objetos'].value_counts().nlargest(10).index

    # Filtrar el DataFrame para incluir solo los 10 elementos más comunes
    objetos_top10 = objetos_streamlit[objetos_streamlit['Objetos'].isin(top10_objetos)]

    # Calcular la frecuencia de los top 10 elementos de la columna 'Objetos' por 'Escuela'
    top10_objetos_by_escuela = objetos_top10.groupby('Escuela')['Objetos'].value_counts().groupby(level=0, group_keys=False).nlargest(10).reset_index(name='Frecuencia')

    # Crear el gráfico de barras con Plotly Express
    bar_chart_objetos_by_escuela = px.bar(top10_objetos_by_escuela, x='Escuela', y='Frecuencia', color='Objetos',
                                        labels={'Frecuencia': 'Número de Apariciones'}, title='Top 10 Objetos por Escuela',
                                        category_orders={'Objetos': orden_objetos},
                                        color_discrete_sequence=color,
                                        width=1000, height=600, 
                                        )

    # Mostrar el gráfico de barras en Streamlit
    st.plotly_chart(bar_chart_objetos_by_escuela)

    


    # Calculo cuántos objetos tiene cada obra:
    titulo_objetos_frecuencia = objetos_streamlit.groupby(['Título', 'Objetos']).size().reset_index(name='Frecuencia')

    # Agrupo por el título para obtener la lista de objetos representados en cada una de las obras:
    titulo_objetos = titulo_objetos_frecuencia.groupby('Título')['Objetos'].unique().reset_index(name='Objetos_en_obra')

    # Filtrar por objetos seleccionados
    titulo_objetos['Objetos_en_obra'] = titulo_objetos['Objetos_en_obra'].apply(lambda x: [o for o in x if o in selector_objetos])

    # Creamos la matriz de correlaciones
    correlation_matrix_objetos = pd.DataFrame(0, index=selector_objetos, columns=selector_objetos)

    for objetos_en_obra in titulo_objetos['Objetos_en_obra']:
        for i in range(len(objetos_en_obra)):
            for j in range(i + 1, len(objetos_en_obra)):
                objeto1 = objetos_en_obra[i]
                objeto2 = objetos_en_obra[j]

                correlation_matrix_objetos.at[objeto1, objeto2] += 1
                correlation_matrix_objetos.at[objeto2, objeto1] += 1

    # Convertimos la matriz a un formato adecuado para Plotly
    correlation_matrix_objetos_plotly = correlation_matrix_objetos.unstack().reset_index()
    correlation_matrix_objetos_plotly.columns = ['Objeto1', 'Objeto2', 'Frecuencia']

    # Pivot the DataFrame to create a 2D matrix
    correlation_matrix_objetos_2d = correlation_matrix_objetos_plotly.pivot(index='Objeto1', columns='Objeto2', values='Frecuencia').fillna(0)

    # Convert to NumPy array
    correlation_matrix_objetos_array = correlation_matrix_objetos_2d.values
    
    
    
    # Creamos el heatmap interactivo con Plotly Express
    fig_objetos = px.imshow(correlation_matrix_objetos_array,
                            x=correlation_matrix_objetos_2d.columns, 
                            y=correlation_matrix_objetos_2d.index,
                            labels=dict(color="Frecuencia"),
                            title='Relaciones regulares entre los objetos representados en el Museo del Prado',
                            color_continuous_scale = 'viridis',
                            range_color = [0, 40],
                        
                            
                            width=800, height=600)

    # Añadimos el texto de frecuencia a la matriz de correlaciones
    annotations_objetos = []
    for i, objeto1 in enumerate(correlation_matrix_objetos_2d.index):
        for j, objeto2 in enumerate(correlation_matrix_objetos_2d.columns):
            value = correlation_matrix_objetos_2d.at[objeto1, objeto2]
            annotations_objetos.append(dict(text=str(value), x=objeto2, y=objeto1,
                                            xref='x1', yref='y1', showarrow=False, font=dict(color='white')))

    fig_objetos.update_layout(annotations=annotations_objetos, width=1000, height=600 )

    st.plotly_chart(fig_objetos)





# Crear la subpágina "Personajes"
elif page == "Personajes":
    st.title("Personajes")
    

    # Definir una clave única para el sin_nulos de personajes
    key_personajes_filter = "personajes_filter"

    # Filtro para seleccionar personajes
    selector_personajes = st.sidebar.multiselect(
        f"Seleccionar Personajes", top_10_personajes, default=top_10_personajes, key=key_personajes_filter
    )

    # Ordenar los personajes de manera lógica
    orden_personajes = ['Afrodita/Venus', 'Deméter/Ceres', 'Dionisio/Baco', 'Flora', 'Hera/Juno', 'Jesús', 'San José', 'San Juan Bautista', 'Virgen María', 'Ángel/ángeles']

    # Elegimos los colores:
    color = ['#117A65  ', '#f26722', '#cd2027', '#139b48', '#04B4A2', '#f1eb1f', '#4c2600', '#0a3452', '#259E04',
             '#4554a5']

    

    # Filtrar el DataFrame solo para los elementos más comunes
    df_personajes_comunes = personajes_streamlit[personajes_streamlit['Personajes'].isin(top_10_personajes)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_personajes_comunes['Frecuencia'] = df_personajes_comunes.groupby('Personajes')['Personajes'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_personajes = df_personajes_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel con Plotly Express
    pie_chart_personajes = px.pie(
        df_personajes_comunes,
        names='Personajes',
        values='Frecuencia',
        title='Distribución de Frecuencia de Personajes',
        hover_data=['Personajes', 'Frecuencia'],
        labels={'Frecuencia': 'Porcentaje'},
        category_orders={'Personajes': orden_personajes},
        color_discrete_sequence=color,
        hole=0.4
    )

    # Establecer dimensiones del gráfico
    pie_chart_personajes.update_layout(width=1000, height=600)

    # Mostrar el gráfico de pastel en Streamlit
    st.plotly_chart(pie_chart_personajes)

    
    
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
        (personajes_streamlit['Personajes'].isin(selector_personajes)) &
        (personajes_streamlit['Década'].between(*decadas_range))
    ]

    # Calcular la frecuencia de personajes por década
    df_frecuencia_decadas = df_filtrado_decadas.groupby(['Década', 'Personajes']).size().reset_index(name='Frecuencia')

    # Crear el gráfico de líneas con Plotly Express
    line_chart = px.line(df_frecuencia_decadas, 
                         x='Década', 
                         y='Frecuencia', 
                         color='Personajes',
                        labels={'Frecuencia': 'Número de Apariciones'}, 
                        category_orders={'Objetos': orden_personajes},
                        color_discrete_sequence=color,
                        title='Desarrollo de Personajes a lo largo del Tiempo')

    # Ocultar la leyenda
    line_chart.update_layout(width=1000, height=600)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line_chart)


    
    # Obtener valores únicos de la columna 'Escuela'
    unique_escuelas_personajes = personajes_streamlit['Escuela'].unique()

    # Filtro para seleccionar escuelas
    selector_escuelas_personajes = st.sidebar.multiselect(
        "Seleccionar Escuelas", unique_escuelas_personajes, default=unique_escuelas_personajes, key="escuelas_filter_personajes"
    )

    # Obtener los 10 elementos más comunes de la columna 'Personajes'
    top10_personajes = personajes_streamlit['Personajes'].value_counts().nlargest(10).index

    # Filtrar el DataFrame para incluir solo los 10 elementos más comunes
    personajes_top10 = personajes_streamlit[personajes_streamlit['Personajes'].isin(top10_personajes)]

    # Calcular la frecuencia de los top 10 elementos de la columna 'Personajes' por 'Escuela'
    top10_personajes_by_escuela = personajes_top10.groupby('Escuela')['Personajes'].value_counts().groupby(level=0, group_keys=False).nlargest(10).reset_index(name='Frecuencia')

    # Crear el gráfico de barras con Plotly Express
    bar_chart_personajes_by_escuela = px.bar(top10_personajes_by_escuela, x='Escuela', y='Frecuencia', color='Personajes',
                                        labels={'Frecuencia': 'Número de Apariciones'}, title='Top 10 Personajes por Escuela',
                                        color_discrete_sequence=color,
                                        width=1000, height=600,
                                        )

    # Mostrar el gráfico de barras en Streamlit
    st.plotly_chart(bar_chart_personajes_by_escuela)

    


    # Calculo cuantos personajes tiene cada obra:
    titulo_personajes_frecuencia = personajes_streamlit.groupby(['Título', 'Personajes']).size().reset_index(name='Frecuencia')

    # Agrupo por el título para obtener la lista de los personajes representados en cada una de las obras:
    titulo_personajes = titulo_personajes_frecuencia.groupby('Título')['Personajes'].unique().reset_index(name='Personajes_en_obra')
    
    # Filtrar por personajes seleccionados
    titulo_personajes['Personajes_en_obra'] = titulo_personajes['Personajes_en_obra'].apply(lambda x: [p for p in x if p in selector_personajes])

    # Creamos la matriz de correlaciones
    correlation_matrix = pd.DataFrame(0, index=selector_personajes, columns=selector_personajes)

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
                    labels=dict(color="Frecuencia"),
                    title='Relaciones regulares entre los personajes representados en el Museo del Prado',
                    color_continuous_scale="Viridis",
                    width=800, height=600)

    # Añadimos el texto de frecuencia a la matriz de correlaciones
    annotations = []
    for i, personaje1 in enumerate(correlation_matrix_2d.index):
        for j, personaje2 in enumerate(correlation_matrix_2d.columns):
            value = correlation_matrix_2d.at[personaje1, personaje2]
            annotations.append(dict(text=str(value), x=personaje2, y=personaje1,
                                    xref='x1', yref='y1', showarrow=False, font=dict(color='white')))

    fig.update_layout(annotations=annotations, width=1000, height=600)

    st.plotly_chart(fig)

    



elif page == "Fauna":
    st.markdown("Analytical study of Fauna")
        
    # Definir una clave única para el sin_nulos de fauna
    key_fauna_filter = "fauna_filter"

    # Filtro para seleccionar personajes
    selector_fauna = st.sidebar.multiselect(
        f"Seleccionar Fauna", top_10_fauna, default=top_10_fauna, key=key_fauna_filter
    )

    # Ordenar loa fauna de manera lógica
    orden_fauna = ['Antrópodos', 'Perro', 'Paloma', 'Oveja', 'Cobaya Común', 'Caballo', 'Mono', 'Jilguero', 'Pavo Real', 'Conejo']

    # Elegimos los colores:
    color = ['#117A65  ', '#f26722', '#cd2027', '#139b48', '#04B4A2', '#f1eb1f', '#4c2600', '#0a3452', '#259E04',
             '#4554a5']

        # Filtrar el DataFrame solo para los elementos más comunes
    df_fauna_comunes = fauna_streamlit[fauna_streamlit['Fauna'].isin(top_10_fauna)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_fauna_comunes['Frecuencia'] = df_fauna_comunes.groupby('Fauna')['Fauna'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_fauna = df_fauna_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel con Plotly Express
    pie_chart_fauna = px.pie(
        df_fauna_comunes,
        names='Fauna',
        values='Frecuencia',
        title='Distribución de Frecuencia de Fauna',
        hover_data=['Fauna', 'Frecuencia'],
        labels={'Frecuencia': 'Porcentaje'},
        category_orders={'Fauna': orden_fauna},
        color_discrete_sequence=color,
        hole=0.4
    )

    # Establecer dimensiones del gráfico
    pie_chart_fauna.update_layout(width=1000, height=600)

    # Mostrar el gráfico de pastel en Streamlit
    st.plotly_chart(pie_chart_fauna)


    # Convertir la columna 'Año' a tipo datetime
    fauna_streamlit['Año'] = pd.to_datetime(fauna_streamlit['Año'], format='%Y', errors='coerce', infer_datetime_format=True, yearfirst=True)

    # Crear una nueva columna 'Década'
    fauna_streamlit['Década'] = fauna_streamlit['Año'].dt.year // 10 * 10

    # Filtro deslizable para seleccionar rango de décadas
    decadas_range_fauna = st.sidebar.slider(
        "Seleccionar Rango de Décadas",
        min_value=fauna_streamlit['Década'].min(),
        max_value=fauna_streamlit['Década'].max(),
        value=(fauna_streamlit['Década'].min(), fauna_streamlit['Década'].max())
    )



    # Filtrar el DataFrame para la fauna seleccionada y rango de décadas
    df_filtrado_decadas_fauna = fauna_streamlit[
        (fauna_streamlit['Fauna'].isin(selector_fauna)) &
        (fauna_streamlit['Década'].between(*decadas_range_fauna))
    ]

    # Calcular la frecuencia de fauna por década
    df_frecuencia_decadas_fauna = df_filtrado_decadas_fauna.groupby(['Década', 'Fauna']).size().reset_index(name='Frecuencia')

    # Crear el gráfico de líneas con Plotly Express
    line_chart_fauna = px.line(df_frecuencia_decadas_fauna, 
                               x='Década', 
                               y='Frecuencia', 
                               color='Fauna',
                                labels={'Frecuencia': 'Número de Apariciones'},
                                category_orders={'Objetos': orden_fauna},
                                color_discrete_sequence=color, 
                                title='Desarrollo de Fauna a lo largo del Tiempo')

    # Ocultar la leyenda
    line_chart_fauna.update_layout(width=1000, height=600)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line_chart_fauna)
   
   
   # Obtener valores únicos de la columna 'Escuela'
    unique_escuelas = flora_streamlit['Escuela'].unique()

    # Filtro para seleccionar escuelas
    selector_escuelas = st.sidebar.multiselect(
        "Seleccionar Escuelas", unique_escuelas, default=unique_escuelas, key="escuelas_filter"
    )
    
    

    # Obtener los 10 elementos más comunes de la columna 'Fauna'
    top10_fauna = fauna_streamlit['Fauna'].value_counts().nlargest(10).index

    # Filtrar el DataFrame para incluir solo los 10 elementos más comunes
    fauna_top10 = fauna_streamlit[fauna_streamlit['Fauna'].isin(top10_fauna)]

    # Calcular la frecuencia de los top 10 elementos de la columna 'Fauna' por 'Escuela'
    top10_fauna_by_escuela = fauna_top10.groupby('Escuela')['Fauna'].value_counts().groupby(level=0, group_keys=False).nlargest(10).reset_index(name='Frecuencia')

    # Crear el gráfico de barras con Plotly Express
    bar_chart_fauna_by_escuela = px.bar(top10_fauna_by_escuela, x='Escuela', y='Frecuencia', color='Fauna',
                                        labels={'Frecuencia': 'Número de Apariciones'}, title='Top 10 Fauna por Escuela',
                                        color_discrete_sequence=color,
                                        width=1000, height=600, 
                                        )

    # Mostrar el gráfico de barras en Streamlit
    st.plotly_chart(bar_chart_fauna_by_escuela)

 



    # Calculo cuánta fauna aparece en cada obra:
    titulo_fauna_frecuencia = fauna_streamlit.groupby(['Título', 'Fauna']).size().reset_index(name='Frecuencia')

    # Agrupo por el título para obtener la lista de fauna representada en cada una de las obras:
    titulo_fauna = titulo_fauna_frecuencia.groupby('Título')['Fauna'].unique().reset_index(name='Fauna_en_obra')

    # Filtrar por fauna seleccionada
    titulo_fauna['Fauna_en_obra'] = titulo_fauna['Fauna_en_obra'].apply(lambda x: [f for f in x if f in selector_fauna])

    # Creamos la matriz de correlaciones
    correlation_matrix_fauna = pd.DataFrame(0, index=selector_fauna, columns=selector_fauna)

    for fauna_en_obra in titulo_fauna['Fauna_en_obra']:
        for i in range(len(fauna_en_obra)):
            for j in range(i + 1, len(fauna_en_obra)):
                fauna1 = fauna_en_obra[i]
                fauna2 = fauna_en_obra[j]

                correlation_matrix_fauna.at[fauna1, fauna2] += 1
                correlation_matrix_fauna.at[fauna2, fauna1] += 1

    # Convertimos la matriz a un formato adecuado para Plotly
    correlation_matrix_plotly_fauna = correlation_matrix_fauna.unstack().reset_index()
    correlation_matrix_plotly_fauna.columns = ['Fauna1', 'Fauna2', 'Frecuencia']

    # Pivot the DataFrame to create a 2D matrix
    correlation_matrix_2d_fauna = correlation_matrix_plotly_fauna.pivot(index='Fauna1', columns='Fauna2', values='Frecuencia').fillna(0)

    # Convert to NumPy array
    correlation_matrix_array_fauna = correlation_matrix_2d_fauna.values

    # Creamos el heatmap interactivo con Plotly Express
    fig_fauna = px.imshow(correlation_matrix_array_fauna,
                        x=correlation_matrix_2d_fauna.columns, 
                        y=correlation_matrix_2d_fauna.index,
                        labels=dict(color="Frecuencia"),
                        title='Relaciones regulares entre la fauna representada en el Museo del Prado',
                        color_continuous_scale="Viridis",
                        width=800, height=600)

    # Añadimos el texto de frecuencia a la matriz de correlaciones
    annotations_fauna = []
    for i, fauna1 in enumerate(correlation_matrix_2d_fauna.index):
        for j, fauna2 in enumerate(correlation_matrix_2d_fauna.columns):
            value = correlation_matrix_2d_fauna.at[fauna1, fauna2]
            annotations_fauna.append(dict(text=str(value), x=fauna2, y=fauna1,
                                        xref='x1', yref='y1', showarrow=False, font=dict(color='white')))

    fig_fauna.update_layout(annotations=annotations_fauna, width=1000, height=600)

    st.plotly_chart(fig_fauna)





elif page == "Flora":
    st.markdown("Analytical study of Flora")
        
    # Definir una clave única para el sin_nulos de fauna
    key_flora_filter = "flora_filter"

    # Filtro para seleccionar personajes
    selector_flora = st.sidebar.multiselect(
        f"Seleccionar Flora", top_10_flora, default=top_10_flora, key=key_flora_filter
    )

    # Crear un diccionario con colores RGB aleatorios para los top 10 elementos de flora
    color_dict_flora = {flora: f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for flora in top_10_flora}

    # Filtrar el DataFrame solo para los elementos más comunes
    df_flora_comunes = flora_streamlit[flora_streamlit['Flora'].isin(top_10_flora)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_flora_comunes['Frecuencia'] = df_flora_comunes.groupby('Flora')['Flora'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_flora = df_flora_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel con Plotly Express
    pie_chart_flora = px.pie(
        df_flora_comunes,
        names='Flora',
        values='Frecuencia',
        title='Distribución de Frecuencia de Flora',
        hover_data=['Flora', 'Frecuencia'],
        labels={'Frecuencia': 'Porcentaje'},
        color_discrete_map=color_dict_flora,
        hole=0.4
    )

    # Establecer dimensiones del gráfico
    pie_chart_flora.update_layout(width=1000, height=600)

    # Mostrar el gráfico de pastel en Streamlit
    st.plotly_chart(pie_chart_flora)

        
# Convertir la columna 'Año' a tipo datetime
    flora_streamlit['Año'] = pd.to_datetime(flora_streamlit['Año'], format='%Y', errors='coerce', infer_datetime_format=True, yearfirst=True)

    # Crear una nueva columna 'Década'
    flora_streamlit['Década'] = flora_streamlit['Año'].dt.year // 10 * 10

    # Filtro deslizable para seleccionar rango de décadas
    decadas_range_flora = st.sidebar.slider(
        "Seleccionar Rango de Décadas",
        min_value=flora_streamlit['Década'].min(),
        max_value=flora_streamlit['Década'].max(),
        value=(flora_streamlit['Década'].min(), flora_streamlit['Década'].max())
    )

    # Filtrar el DataFrame para la flora seleccionada y rango de décadas
    df_filtrado_decadas_flora = flora_streamlit[
        (flora_streamlit['Flora'].isin(selector_flora)) &
        (flora_streamlit['Década'].between(*decadas_range_flora))
    ]

    # Calcular la frecuencia de flora por década
    df_frecuencia_decadas_flora = df_filtrado_decadas_flora.groupby(['Década', 'Flora']).size().reset_index(name='Frecuencia')

    # Crear el gráfico de líneas con Plotly Express
    line_chart_flora = px.line(df_frecuencia_decadas_flora, x='Década', y='Frecuencia', color='Flora',
                                labels={'Frecuencia': 'Número de Apariciones'}, title='Desarrollo de Flora a lo largo del Tiempo',
                                color_discrete_map=color_dict_flora
    )

    # Ocultar la leyenda
    line_chart_flora.update_layout(width=1000, height=600)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line_chart_flora)

    
    
    # Obtener valores únicos de la columna 'Escuela'
    unique_escuelas = flora_streamlit['Escuela'].unique()

    # Filtro para seleccionar escuelas
    selector_escuelas = st.sidebar.multiselect(
        "Seleccionar Escuelas", unique_escuelas, default=unique_escuelas, key="escuelas_filter"
    )
    
    
    
    # Obtener los 10 elementos más comunes de la columna 'Flora'
    top10_flora = flora_streamlit['Flora'].value_counts().nlargest(10).index

    # Filtrar el DataFrame para incluir solo los 10 elementos más comunes
    flora_top10 = flora_streamlit[flora_streamlit['Flora'].isin(top10_flora)]

    # Calcular la frecuencia de los top 10 elementos de la columna 'Flora' por 'Escuela'
    top10_flora_by_escuela = flora_top10.groupby('Escuela')['Flora'].value_counts().groupby(level=0, group_keys=False).nlargest(10).reset_index(name='Frecuencia')

    # Crear el gráfico de barras con Plotly Express
    bar_chart_flora_by_escuela = px.bar(top10_flora_by_escuela, x='Escuela', y='Frecuencia', color='Flora',
                                        labels={'Frecuencia': 'Número de Apariciones'}, title='Top 10 Flora por Escuela',
                                        color_discrete_sequence=px.colors.qualitative.Set3,
                                        width=1000, height=600, 
                                        )

    # Mostrar el gráfico de barras en Streamlit
    st.plotly_chart(bar_chart_flora_by_escuela)





    # Calculo cuánta flora aparece en cada obra:
    titulo_flora_frecuencia = flora_streamlit.groupby(['Título', 'Flora']).size().reset_index(name='Frecuencia')

    # Agrupo por el título para obtener la lista de flora representada en cada una de las obras:
    titulo_flora = titulo_flora_frecuencia.groupby('Título')['Flora'].unique().reset_index(name='Flora_en_obra')

    # Filtrar por flora seleccionada
    titulo_flora['Flora_en_obra'] = titulo_flora['Flora_en_obra'].apply(lambda x: [f for f in x if f in selector_flora])

    # Creamos la matriz de correlaciones
    correlation_matrix_flora = pd.DataFrame(0, index=selector_flora, columns=selector_flora)

    for flora_en_obra in titulo_flora['Flora_en_obra']:
        for i in range(len(flora_en_obra)):
            for j in range(i + 1, len(flora_en_obra)):
                flora1 = flora_en_obra[i]
                flora2 = flora_en_obra[j]

                correlation_matrix_flora.at[flora1, flora2] += 1
                correlation_matrix_flora.at[flora2, flora1] += 1

    # Convertimos la matriz a un formato adecuado para Plotly
    correlation_matrix_plotly_flora = correlation_matrix_flora.unstack().reset_index()
    correlation_matrix_plotly_flora.columns = ['Flora1', 'Flora2', 'Frecuencia']

    # Pivot the DataFrame to create a 2D matrix
    correlation_matrix_2d_flora = correlation_matrix_plotly_flora.pivot(index='Flora1', columns='Flora2', values='Frecuencia').fillna(0)

    # Convert to NumPy array
    correlation_matrix_array_flora = correlation_matrix_2d_flora.values

    # Creamos el heatmap interactivo con Plotly Express
    fig_flora = px.imshow(correlation_matrix_array_flora,
                        x=correlation_matrix_2d_flora.columns, 
                        y=correlation_matrix_2d_flora.index,
                        labels=dict(color="Frecuencia"),
                        title='Relaciones regulares entre la flora representada en el Museo del Prado',
                        color_continuous_scale="Viridis",
                        width=800, height=600)

    # Añadimos el texto de frecuencia a la matriz de correlaciones
    annotations_flora = []
    for i, flora1 in enumerate(correlation_matrix_2d_flora.index):
        for j, flora2 in enumerate(correlation_matrix_2d_flora.columns):
            value = correlation_matrix_2d_flora.at[flora1, flora2]
            annotations_flora.append(dict(text=str(value), x=flora2, y=flora1,
                                        xref='x1', yref='y1', showarrow=False, font=dict(color='white')))

    fig_flora.update_layout(annotations=annotations_flora, width=1000, height=600)

    st.plotly_chart(fig_flora)




elif page == "Lugar":
    st.markdown("Estudio Analítico de Lugares")

    # Definir una clave única para el sin_nulos de lugares
    key_lugar_filter = "lugar_filter"

    # Filtro para seleccionar lugares
    selector_lugar = st.sidebar.multiselect(
        f"Seleccionar Lugares", top_10_lugar, default=top_10_lugar, key=key_lugar_filter
    )

    # Crear un diccionario con colores RGB aleatorios para los top 10 elementos de lugar
    color_dict_lugar = {lugar: f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for lugar in top_10_lugar}

    # Filtrar el DataFrame solo para los elementos más comunes
    df_lugar_comunes = lugar_streamlit[lugar_streamlit['Lugar'].isin(top_10_lugar)]

    # Calcular la frecuencia y agregarla al DataFrame
    df_lugar_comunes['Frecuencia'] = df_lugar_comunes.groupby('Lugar')['Lugar'].transform('count')

    # Calcular la frecuencia total
    frecuencia_total_lugar = df_lugar_comunes['Frecuencia'].sum()

    # Crear el gráfico de pastel con Plotly Express
    pie_chart_lugar = px.pie(
        df_lugar_comunes,
        names='Lugar',
        values='Frecuencia',
        title='Distribución de Frecuencia de Lugares',
        hover_data=['Lugar', 'Frecuencia'],
        labels={'Frecuencia': 'Porcentaje'},
        color_discrete_map=color_dict_lugar,
        hole=0.4
    )

    # Establecer dimensiones del gráfico
    pie_chart_lugar.update_layout(width=1000, height=600)

    # Mostrar el gráfico de pastel en Streamlit
    st.plotly_chart(pie_chart_lugar)



    # Convertir la columna 'Año' a tipo datetime
    lugar_streamlit['Año'] = pd.to_datetime(lugar_streamlit['Año'], format='%Y', errors='coerce', infer_datetime_format=True, yearfirst=True)

    # Crear una nueva columna 'Década'
    lugar_streamlit['Década'] = lugar_streamlit['Año'].dt.year // 10 * 10

    # Filtro deslizable para seleccionar rango de décadas
    decadas_range_lugar = st.sidebar.slider(
        "Seleccionar Rango de Décadas",
        min_value=lugar_streamlit['Década'].min(),
        max_value=lugar_streamlit['Década'].max(),
        value=(lugar_streamlit['Década'].min(), lugar_streamlit['Década'].max())
    )

    # Filtrar el DataFrame para el lugar seleccionado y rango de décadas
    df_filtrado_decadas_lugar = lugar_streamlit[
        (lugar_streamlit['Lugar'].isin(selector_lugar)) &
        (lugar_streamlit['Década'].between(*decadas_range_lugar))
    ]

    # Calcular la frecuencia de lugares por década
    df_frecuencia_decadas_lugar = df_filtrado_decadas_lugar.groupby(['Década', 'Lugar']).size().reset_index(name='Frecuencia')

    # Crear el gráfico de líneas con Plotly Express
    line_chart_lugar = px.line(df_frecuencia_decadas_lugar, x='Década', y='Frecuencia', color='Lugar',
                                labels={'Frecuencia': 'Número de Apariciones'}, title='Desarrollo de Lugares a lo largo del Tiempo',
                                color_discrete_map=color_dict_lugar
    )

    # Ocultar la leyenda
    line_chart_lugar.update_layout(width=1000, height=600)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line_chart_lugar)

    
    
