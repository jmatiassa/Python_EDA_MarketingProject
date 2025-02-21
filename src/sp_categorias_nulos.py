import pandas as pd
import numpy as np
import sys
sys.path.append("..")

#Función que muestra el porcentaje de nulos
def calcular_nulos(df):
    numero_nulos=(((df.isnull().sum())/df.shape[0])*100)
    display(numero_nulos)

#Función que muestra el porcentaje de nulos de una columna
def calcular_nulos_columna(df,col):
    numero_nulos=(((df[col].isna().sum())/df[col].shape[0])*100).round(decimals=2)
    return numero_nulos



#Analisis general categoricas
def analisis_general_categoricas(df):
    col_cat= df.select_dtypes(include='O').columns
    if len(col_cat)==0:
        print("No hay columnas")
    else:
        for col in col_cat: 
            print(f"{col} tiene {len(df[col].unique())} valores únicos")
            print(f"Valores unicos:{df[col].unique()}")
            print(f"Nulos:{calcular_nulos_columna(df,col)}%")
            display((df[col].value_counts(normalize=True)))
            print("-----------------------------------------")

#Reemplazar los nulos de df_limpio
def rellenar_nulos(df):
    for col in df.select_dtypes(include='O').columns:
        if col == 'Default':
            df[col]=df[col].fillna('no')
        elif col:
            df[col]=df[col].fillna('unknown')