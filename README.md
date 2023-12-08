# project_final
Proyecto final
# ArtEye: El Ojo de Halcón del Arte (un viaje infinito por los paisajes del arte)

# UN ANÁLISIS ICONOGRÁFICO DE LA COLECCIÓN DEL MUSEO DEL PRADO

PERSONAJES, LUGARES, OBJETOS, FAUNA Y FLORA



![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/Mecanismo_fisiopatologico_de_RI.png)

# 1. Introducción.
La Resistencia a la Insulina (RI) es un problema de salud de creciente importancia en la sociedad actual. Su impacto se hace evidente en la salud y el bienestar de las personas, ya que está estrechamente relacionado con enfermedades crónicas, como la diabetes tipo 2, que afecta a un número significativo de individuos en todo el mundo. El estudio de la RI y sus factores desencadenantes se ha vuelto esencial, ya que puede desempeñar un papel crucial tanto en la prevención como en el tratamiento de estas enfermedades.
Entre los factores de riesgo que destacan en la aparición de la Resistencia a la Insulina se encuentran la obesidad, el sedentarismo, la falta de sueño, antecedentes familiares de diabetes tipo 2, el síndrome de ovario poliquístico y la edad, especialmente a partir de los 45 años. Estos factores representan desafíos significativos para la salud pública, lo que resalta la importancia de investigar y comprender más a fondo la RI. En este contexto, este estudio busca arrojar luz sobre estos aspectos y sus implicaciones en la salud de la población.

# 2. Hipótesis inicial.
Como hipótesis inicial del estudio, planteo que:
"La Resistencia a la Insulina (RI) está asociada con diversas variables sociodemográficas, como la edad, el sexo, la clase social y el nivel de educación. Además, que existe una correlación significativa entre la RI y ciertos hábitos de salud, incluyendo la práctica de ejercicio físico, la adhesión a una dieta mediterránea y el tabaquismo. Y por último, que también se relaciona con el sobrepeso y la obesidad".

# 3. Pasos a seguir: 

- # Paso 1: Extración de los datos. Materiales y métodos utilizados.

**3.1. DataFrame 1:**
El primer DataFrame utilizado en el estudio consiste en un archivo CSV que contiene datos de 258,931 trabajadores (103,427 mujeres y 155,504 hombres) de diversas regiones de España, incluyendo Baleares, Andalucía, Canarias, Comunidad Valenciana, Cataluña, Madrid, Castilla La Mancha, Castilla León y País Vasco. Estos trabajadores pertenecen a una amplia variedad de sectores laborales, como hostelería, construcción, comercio, sanidad, administración pública, transporte, educación, industria y limpieza.

-El estudio se realizó entre enero de 2004 y junio de 2006 y se basó en datos clínicos y personales recopilados de una base de datos anonimizada de trabajadores mantenida por la Escuela Universitaria ADEMA-UIB (Universidad de las Islas Baleares). Todos los parámetros se expresan en miligramos por decilitro.

-En cuanto a la definición de fumadores, se consideró a alguien fumador si había consumido al menos un cigarrillo diariamente (o su equivalente en otras formas de consumo) en los últimos treinta días o si había dejado de fumar hace menos de 12 meses.

-La clasificación de la clase social se dividió en tres categorías, siguiendo los datos de la Clasificación Nacional de Ocupaciones 2011 (CNO-11) y aplicando los criterios establecidos por la Sociedad Española de Epidemiología:

- Clase I: Incluye a personal directivo, profesionales universitarios, deportistas y artistas.

- Clase II: Engloba a trabajadores con cualificación en ocupaciones intermedias y autónomos.

- Clase III: Comprende a trabajadores no cualificados.

![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/df_clean_imagenes/df_clean.png)


**3.2. DataFrame 2:**

El segundo DataFrame se originó a partir de un archivo CSV descargado del INE. Contiene información acerca de la población total española, diferenciando por edades y sexo.

El objetivo final que se pretende con esta tabla, en la que contamos con la información sobre la población total en España, es el de, combinando los valores de esta con los de la tabla anterior y posterior, poder estimar el número real de personas afectadas en España, y no tan solo un porcentaje, del cual no obtenemos un numero concreto. 
Es decir, tras obtener un resultado porcentual, ajustarlo al número concreto que equivaldría con respecto a la población total española.

![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/df_clean_imagenes/df2_clean.png)


**3.3. DataFrames 3, 4 y 5:**

Los DataFrames 3, 4 y 5 han sido obtenidos a través del scrapeo, por Beautiful Soup, de un artículo publicado por "Elsevier". Las tres tablas tienen un denominador común, a saber: el estudio de la resistencia a la insulina en la población española.

![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/df_clean_imagenes/df3_clean.png)

![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/df_clean_imagenes/df4_clean.png)

![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/df_clean_imagenes/df5_clean.png)


- # Paso 2: Transformación de los datos. Exploración y Limpieza.

En el segundo paso de nuestro proyecto, nos sumergimos en la transformación de los datos, in cluyendo exploración y limpieza de los mimso también. A lo largo de esta fase, analizaremos los datos e identificaremos posibles inconsistencias para asegurarnos que los datos sean coherentes y estén listos para su posterior uso. 

Partimos de los 5 archivos mencionados en el apartado anterior. Estos archivos abarcaban información enfocada al estudio del RI en la población española.

Nuestra primera tarea consiste en realizar una exploración exhaustiva de estos archivos utilizando el módulo Pandas de Python. Este proceso nos permite conocer la naturaleza de los datos, detectar posibles errores o inconsistencias en los datos y eliminar información redundante o no relevante en nuestro estudio.

En resumen, el enfoque de esta fase es explorar los datos contenidos en los archivos con el fin de garantizar que estén preparados para ser transformados y a continuación cargados en una base de datos sólida y lista para su uso en la toma de decisiones y análisis posteriores.

- # Paso 3: Carga de los datos en MongoDB.Construcción de la Base de Datos

Una vez que los datos han sido limpiados y transformados, pasamos a la construcción de la base de datos mediante MongoDB. Este proceso es esencial para garantizar la organización y accesibilidad de los datos.

![](https://github.com/karmelealonso/3.-project_etl/blob/main/imagenes/colecciones_MongoDB.png)

# Contenido del repositorio. 

- notebook: contiene tres archivos jupyter notebook.
    1. main.ipynb: contiene la extracción y posterior limpieza y transformación de los diferentes archivos. 
    2. Desarrollo.ipynb:: contiene el desarrollo del proyecto de forma explicativa y algún cambio añadido para tener las diferentes tablas listas para su posterior estudio.
    3. Carga de los datos a MongoDB.ipynb: contiene la carga de los datos a MongoDB.
- data: contiene tres archivos con las tablas. 
    1. data_raw: contiene los archivos recién extraídos, en crudo.
    2. data_clean: contiene los archivos limpios.
    3. data_def: contiene los archivos con algunas modificaciones que se hicieron más adelante de cara al estudio planteado al comienzo.
- imágenes: contienen las imágenes utilizadas a lo largo del proyecto.



**Para obtener información más detallada sobre el procedimiento y los pasos que se han seguido, te invito a consultar los documentos disponibles en el repositorio.**

