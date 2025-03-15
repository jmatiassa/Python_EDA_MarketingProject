import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#Función para detectar variables continuas
def detectar_continuas(df):
    """
    Detecta y devuelve una lista de las variables continuas en un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de Pandas del cual se extraerán las variables continuas.

    Returns:
        list: Lista de nombres de columnas que contienen variables continuas (float64 o int64).
    """
    variables_continuas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    return variables_continuas


#Función para detectar variables categoricas
def detectar_categoricas(df):
    """
    Detecta y devuelve una lista de las variables categóricas en un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de Pandas del cual se extraerán las variables categóricas.

    Returns:
        list: Lista de nombres de columnas que contienen variables categóricas (excluyendo float64 e int64).
    """
    variables_categoricas = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    return variables_categoricas




#Funciíon que representa la tasa de subscripción según la categoría

def plot_subscription_rate(df, variables_categoricas, target_variable):
    """
    Genera gráficos de barras para analizar la tasa de suscripción (proporción de suscripciones)
    en variables categóricas, añadiendo una línea con la tasa promedio de suscripción y etiquetas en las barras.

    :param df: DataFrame con los datos a analizar.
    :param variables_categoricas: Lista de variables categóricas.
    :param target_variable: Nombre de la variable objetivo (0/1).
    """

    # Calcular la tasa de suscripción promedio
    avg_conversion_rate = df[target_variable].mean()

    for col in variables_categoricas:
        # Calcular el número total de registros y el número de suscripciones por categoría
        total_counts = df.groupby(col)[target_variable].count()  # Total de ofertas por categoría
        subscription_counts = df.groupby(col)[target_variable].sum()  # Total de suscripciones por categoría

        # Calcular la tasa de suscripción por categoría
        subscription_rate = (subscription_counts / total_counts).sort_values(ascending=False)

        # Crear el gráfico de barras
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x=subscription_rate.index, y=subscription_rate.values, palette="viridis")
        
        # Añadir etiquetas encima de las barras
        for i, rate in enumerate(subscription_rate.values):
            ax.text(i, rate, f'{rate:.2%}', ha='center', va='bottom', fontsize=10, color='black')
        
        # Añadir línea con la tasa promedio de suscripción
        plt.axhline(avg_conversion_rate, color='red', linestyle='--', label=f'Tasa Promedio: {avg_conversion_rate:.2%}')
        
        # Personalizar el gráfico
        plt.xticks(rotation=45)
        plt.title(f"Tasa de subscripción por categoría: {col}")
        plt.ylabel("Tasa de subscripción")
        plt.xlabel(col)
        plt.legend()  # Mostrar la leyenda con la tasa promedio
        plt.show()


#calcular kpi de tasa de conversión global

def calcular_tasa_conversion(df, Columna_conversion):
    """
    Calcula la tasa de conversión en un DataFrame.

    La tasa de conversión se define como el porcentaje de registros donde 
    la columna de conversión tiene el valor 1, respecto al total de registros.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        Columna_conversion (str): Nombre de la columna que indica la conversión (valor 1 significa conversión).

    Returns:
        float: Tasa de conversión expresada como un porcentaje con dos decimales.
    """
    ventas = df[df[Columna_conversion] == 1].shape[0]
    total_registros = df.shape[0]
    tasa_conversion = round(((ventas / total_registros) * 100), 2)
    return tasa_conversion


#Función para crear una distribucióni temporal ordenada por tiempo
def plot_subscription_by_month(df, date_column, target_variable):
    """
    Genera un gráfico de barras para analizar la tasa de suscripción por mes y año,
    ordenando las barras en orden ascendente por fecha.

    :param df: DataFrame con los datos a analizar.
    :param date_column: Nombre de la columna de fecha.
    :param target_variable: Nombre de la variable objetivo (0/1).
    """

    # Asegurarse de que la columna de fecha esté en formato datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # Crear una nueva columna para el mes y año
    df['month_year'] = df[date_column].dt.to_period('M')

    # Calcular el número total de registros y suscripciones por mes y año
    total_counts = df.groupby('month_year')[target_variable].count()  # Total de registros por mes/año
    subscription_counts = df.groupby('month_year')[target_variable].sum()  # Total de suscripciones por mes/año

    # Calcular la tasa de suscripción por mes y año
    subscription_rate = (subscription_counts / total_counts).sort_index()  # Ordenar por fecha ascendente

    # Crear el gráfico de barras
    plt.figure(figsize=(15, 8))
    ax = sns.barplot(x=subscription_rate.index.astype(str), y=subscription_rate.values, palette="coolwarm")
    ax.set_title("Tasa de Suscripción por Mes y Año", fontsize=16)
    ax.set_xlabel("Mes y Año", fontsize=14)
    ax.set_ylabel("Tasa de Suscripción", fontsize=14)
    plt.xticks(rotation=45)
    plt.show()

#Función qque calcula la duración de la campaña
def calcular_duración_campaña(df, fecha):
    """
    Calcula la duración de una campaña en años a partir de una columna de fechas en un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        fecha (str): Nombre de la columna que contiene las fechas de la campaña.

    Returns:
        float: Duración de la campaña en años (considerando años bisiestos con un promedio de 365.25 días por año).
    """
    fecha_min = df[fecha].min()
    fecha_max = df[fecha].max()
    duracion_campaña = (fecha_max - fecha_min).days / 365.25
    return duracion_campaña
   

#Función que muestra las volumetrías de nº leads y nº conversiones por columna categórica
def tabla_volumetrias_subscripciones(df, variables_categoricas, target_variable):
    """
    Genera tablas de volumen de suscripciones por cada variable categórica en el DataFrame.

    Para cada variable categórica proporcionada, esta función calcula y muestra:
    - El número total de registros por categoría.
    - El número total de suscripciones (sumatorio de la variable objetivo) por categoría.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        variables_categoricas (list): Lista de nombres de las columnas categóricas que se analizarán.
        target_variable (str): Nombre de la columna que representa las suscripciones (variable objetivo).
    
    Returns:
        None: La función imprime las tablas, pero no devuelve ningún valor.
    """
    for col in variables_categoricas:
        total_counts = df.groupby(col)[target_variable].count() 
        subscription_counts = df.groupby(col)[target_variable].sum() 
        print(total_counts)
        print("-----------------------------")
        print(subscription_counts)
        print("-----------------------------")


#Función que muestra las volumetrías de leads y conversiones distribuidas por meses
def tabla_fechas(df, date_column, target_variable):
    """
    Genera una tabla de total de registros y suscripciones por mes y año.

    La función agrupa los datos por mes y año, y luego calcula y muestra:
    - El número total de registros por mes/año.
    - El número total de suscripciones (sumatorio de la variable objetivo) por mes/año.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        date_column (str): Nombre de la columna que contiene las fechas para agrupar por mes/año.
        target_variable (str): Nombre de la columna que representa las suscripciones (variable objetivo).
    
    Returns:
        None: La función imprime las tablas, pero no devuelve ningún valor.
    """
    df['month_year'] = df[date_column].dt.to_period('M')
    total_counts = df.groupby('month_year')[target_variable].count()  # Total de registros por mes/año
    subscription_counts = df.groupby('month_year')[target_variable].sum()  # Total de suscripciones por mes/año
    print(total_counts)
    print("-----------------------------")
    print(subscription_counts)
    print("-----------------------------")
