# EDA_MARKETING

## Contenido:
1. Objetivo del proyecto
2. Documentación inicial del proyecto
3. Cració del entorno de desarrollo para el centro de control de las versiones.
4. Procesado de datos
5. Visualización de datos

## Objetivo del proyecto
Mediante este proyecto se pretende obtener conclusiones relevantes para la toma de decisiones sobre los resultados de las campañas de marketing de una empresa. Para ello se requiere que se utilicen los conocimientos adquiridos en el bloque de python y de análisis de datos en python del curso. En concreto, los requisitos son:
- Transformación y limpieza de datos.
- Análisis descriptivo de los datos.
- Visualización de los datos.
- Informe explicativo del análisis.
  
## Documentación inicial del proyecto
Para realizar el trabajo se nos presenta la siguiente información:
- Un documento word llamado DataProject_Proyecto EDA con Python que tiene la información de contexto del proyecto así como enunciado y definición de los campos que hay en los ficheros. También instrucciones para la entrega, consejos y criterios de evaluación.
- Documento csv 'bank-additional': este documento contiene la ifnormación sobre los registros de las campañas de marketing directo
- Documento csv 'customer-details.xlsx: es un archivo excel con información sobre los clientes del banco

## Creación del entorno de desarrollo para el control de las versiones:
### Mediante la consola del sistema se hacen las siguientes acciones:
- Creación de una carpeta llamada EDA_MAKETING en el escritorio, clonada de la ya creada en github
- Se añade la carpeta venv que almacenará los distintos programas utilizados en el entorno y sus históricos de versiones
- Se activa el entorno mediante la llamada a Activate por consola
- Se instala una nueva versión disponible de pip
- Se crea el documento requiremens.txt que documentará el histórico de versiones
- Se sube el entorno a github:
(venv) C:\Users\matis\Desktop\EDA_MARKETING>git add .

(venv) C:\Users\matis\Desktop\EDA_MARKETING> git commit -m "Creación del sistema de carpetas y entorno"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

(venv) C:\Users\matis\Desktop\EDA_MARKETING> git push
Everything up-to-date

(venv) C:\Users\matis\Desktop\EDA_MARKETING>

## Procesado de datos
El análisis de los datos proporcionados requiere ser transformado. De esa forma se puede obtener información relevante para el objetivo del proyecto. Para se han seguido los siguientes pasos:

1. Eda preeliminar de limpieza de datos
    Se utiliza el jupyter notebook eda_limpieza y el documento de soporte src sp_eda_limpieza para: importar las fuentes de datos bank-additional y customer-details;poner iniciales en mayusculas en las columnas; convertir los datos a su formato int, float espacífico;eliminar columnas con datos no relevantes; cambiar carácteres; unir los dataframes 
2. Transformación de las coordenadas mediante geolocalización
    Se utiliza el csv eda_mk_ok.csv para aplicar una función de geocoding creada en el src sp_geocode en el notebook geocode_bank.ipynb. Como output se crea el csv bankadditional_geocoded.csv
3. Análisis de las columnas categóricas
    Se estudian los valores de las distintas columnas categóricas y se transforman los valores de los países geocodificados de sus siglas a valores completos
    Se rellenan los nulos con unknown o con la moda dependiendo de su volumetría. Para ello se importa el csv vankadditional_geocoded.csv y se trabaja en el notebook nulos_categorias.ipynb. Se crea el src sp_categorias_nulos.py para crear formulas que den soporte al código y sp_vusualizacion para los paquetes de visualización. Como output se exporta a csv el documento df_gestion_nulos_ok
4. Análisis de las columnas numéricas
    Se realiza un análisis del dataframe df_gestion_nulos_ok.csv en el notebook columnas_numericas.ipynb. Se utiliza como soporte el src sp_columnas_numericas.py. Se extrae como output el csv df_nulos_numericos_ok.csv
5. Visualización y análisis de la información
    Se realiza un análisis del dataframe df_nulos_numericos_ok.csv en el notebook analisis_subscripciones.ipynb, se extraen conclusiones y se utiliza el sp_analisis_subscripciones para guardar las fórmulas. 
    Durante este documento de trabajo se extrae la información necesaria que se utilizará para comunicar las conclusiones

El informe de resultados sobre la campaña de márketing se presenta en el documento PDF Informe_EDA_Marketing_directo.v1. En este ifnorme se puede tener una visión clara sobre las conclusiones obtenidas durante el análisis y las estrategias propuestas que permitan acercar futuras estrategias a un mayor número de ventas. A continuación se presentan las imágenes del informe

