#importaciones
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


#Función que representa los gráficos para analizar las columnas numéricas
def subplot_columnas_numericas(df,col):
    num_graph= len(col)
    num_rows=((num_graph)+2)//2

    fig,axes=plt.subplots(num_graph,2,figsize=(15,num_rows*5))

    for i,col in enumerate(col):
        sns.histplot(data=df, x=col, ax=axes[i,0])
        sns.boxplot(data=df, x=col, ax=axes[i,1])
    for j in range(i+1,len(axes)):
        fig.delaxes(axes[j])

#Función que analiza los nulos de las columnas numéricas
def analisis_columnas_numericas_null(df,umbral=10):
    columns_with_nulls=df.columns[df.isnull().any()]

    null_colums_info=pd.DataFrame(
        {"Column":columns_with_nulls,
         "Datatype":[df[col].dtype for col in columns_with_nulls],
         "Nullcount":[df[col].isnull().sum() for col in columns_with_nulls],
         "Null%": [((df[col].isnull().sum()/df.shape[0])*100)for col in columns_with_nulls ]}
    )
    display(null_colums_info)
    high_null_cols= null_colums_info[null_colums_info['Null%']>=umbral]['Column'].tolist()
    low_null_cols= null_colums_info[null_colums_info['Null%']< umbral]['Column'].tolist()
    return high_null_cols,low_null_cols

#rellenar nulos mediante predicción usando sklern
def imputar_iterative(df, lista_columnas):
    
    iter_imputer = IterativeImputer(max_iter=50, random_state=42)
    
    # Imputar valores en las columnas especificadas
    data_imputed = iter_imputer.fit_transform(df[lista_columnas])
    
    # Crear nombres para las nuevas columnas
    new_col = [col + "_iterative" for col in lista_columnas]
    
    # Asignar los valores imputados a nuevas columnas
    for i, col in enumerate(lista_columnas):
        # Si la columna original era de tipo entero, convertir los valores imputados a enteros
        if pd.api.types.is_integer_dtype(df[col]):
            df[new_col[i]] = data_imputed[:, i].round().astype(int)
        else:
            df[new_col[i]] = data_imputed[:, i]
    
    # Mostrar estadísticas descriptivas de las nuevas columnas
    display(df[new_col].describe().T)
    
    return df, new_col

