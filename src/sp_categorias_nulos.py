import pandas as pd
import numpy as np
import sys
sys.path.append("..")

#Función que muestra el porcentaje de nulos
def calcular_nulos(df):
    numero_nulos=(((df.isnull().sum())/df.shape[0])*100)
    display(numero_nulos)

#Función que muestra el porcentaje de nulos de una columna
def calcular_nulos(df):
    """
    Calcula el porcentaje de valores nulos por cada columna en un DataFrame.

    La función calcula el porcentaje de valores nulos en cada columna y los muestra.

    Args:
        df (pd.DataFrame): DataFrame del cual se calcularán los valores nulos por columna.
    
    Returns:
        None: La función muestra los porcentajes de valores nulos, pero no devuelve ningún valor.
    """
    numero_nulos = (((df.isnull().sum()) / df.shape[0]) * 100)
    display(numero_nulos)




#Analisis general categoricas
def analisis_general_categoricas(df):
    """
    Realiza un análisis general sobre las columnas categóricas de un DataFrame.

    Para cada columna categórica, la función muestra:
    - El número de valores únicos.
    - Los valores únicos de la columna.
    - El porcentaje de valores nulos.
    - La distribución de los valores en la columna (frecuencia relativa).

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos a analizar.
    
    Returns:
        None: La función imprime los resultados de los análisis, pero no devuelve ningún valor.
    """
    col_cat = df.select_dtypes(include='O').columns
    if len(col_cat) == 0:
        print("No hay columnas")
    else:
        for col in col_cat:
            print(f"{col} tiene {len(df[col].unique())} valores únicos")
            print(f"Valores unicos: {df[col].unique()}")
            print(f"Nulos: {calcular_nulos_columna(df, col)}%")
            display((df[col].value_counts(normalize=True)))
            print("-----------------------------------------")


#Reemplazar los nulos de df_limpio
def rellenar_nulos(df):
    """
    Rellena los valores nulos en las columnas categóricas de un DataFrame.

    La función rellena los valores nulos en las columnas de tipo objeto (categóricas) con los siguientes valores:
    - Para la columna 'Default', los nulos se rellenan con 'no'.
    - Para todas las demás columnas categóricas, los nulos se rellenan con 'unknown'.

    Args:
        df (pd.DataFrame): DataFrame con las columnas que contienen valores nulos.

    Returns:
        pd.DataFrame: DataFrame con los valores nulos rellenados en las columnas categóricas.
    """
    for col in df.select_dtypes(include='O').columns:
        if col == 'Default':
            df[col] = df[col].fillna('no')
        elif col:
            df[col] = df[col].fillna('unknown')
    return df
