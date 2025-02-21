
#Fmportaciones
import pandas as pd

#Función para crear el eda preeliminar que muestra 5 filas, la info, nulos, duplicados y el distinct de objects
def eda_preliminar (df):
    display (df.sample(5))
    print('--------------------')

    print('INFO')

    display(df.info())
    print('--------------------')

    print('NULOS')
    display(round(df.isnull().sum()/df.shape[0]*100,2))
    print('--------------------')

    print('duplicados')

    print(df.duplicated().sum())

    print('VALUE COUNT')

    for col in df.select_dtypes(include='O').columns:
        display(df[col].value_counts())
        print('--------------------')

    print('VALORES NUMÉRICOS')
    display(df.describe().T)

#Función para borrar la columna Unnamed: 0
def borrar_unnamed(df):
    # Verifica los nombres de las columnas para asegurarse de que no haya problemas con el nombre
    print("Columnas originales:", df.columns)
    
    # Eliminar la columna 'Unnamed: 0' si existe
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis=1, inplace=True)  # Eliminar la columna directamente
        print("Columna 'Unnamed: 0' eliminada")
    else:
        print("La columna 'Unnamed: 0' no se encuentra en el DataFrame")
    
    # Muestra el DataFrame después de eliminar la columna
    display(df.sample())

# Función para pasar la primera letra de las columnas a mayúscula
def columnas_mayuscula(df):
    df.columns= df.columns.str.capitalize()
    print('Columnas pasadas a mayúscualas')
    display(df.sample())

#Función para detectar booleanos y cambiarlos por yes o no
def transformar_booleanos(df):
    # Detectar las columnas booleanas (que contienen solo 1 y 0, excluyendo nulos)
    columnas_booleanas = [col for col in df.columns if df[col].dropna().isin([0, 1]).all()]
    
    # Aplicar la transformación: cambiar 1 por 'yes' y 0 por 'no' en las columnas booleanas
    for col in columnas_booleanas:
        df[col] = df[col].map({1: 'yes', 0: 'no'})
    
    # Mostrar las columnas detectadas y una muestra del DataFrame
    print(f"Columnas booleanas detectadas: {columnas_booleanas}")
    print("\nMuestra del DataFrame:")
    display(df.sample(5))  # Muestra 5 filas aleatorias del DataFrame

#Función para convertir datos object a float que están separados por , en vez de por.
def convertir_a_float(df):
    # Iterar sobre todas las columnas del DataFrame
    columnas_modificadas=[]
    for col in df.columns:
        # Verificar si la columna es de tipo object
        if df[col].dtype == 'object':
            try:
                # Reemplazar comas por puntos y convertir los valores a float
                df[col] = df[col].str.replace(',', '.', regex=False).astype(float)
                columnas_modificadas.append(col)
            except ValueError:
                continue
    print(f"Se han modificado las siguientes columnas:{columnas_modificadas}")
    display(df.sample())

#Función para convertir datos float a int redondeando sus decimales
def float_a_int (df,col):
    # Verificar si el tipo de dato es float64
    if df[col].dtype=='float64':
        #Redondear los valores de la columna y modificar el tipo de dato a int
        df[col]=df[col].round().astype(int)
        print(f"La columna {col} ha sido cambiada a numero entero y redondeada")
        display(df.info())
        display(df.sample())   

#Función para convertir datos float a int en una lista de columnas
def float_int_lista(df, lista_floatint):
    for col in lista_floatint:
       if df[col].dtype=='float64':
        #Redondear los valores de la columna y modificar el tipo de dato a int
            df[col]=df[col].round().astype(int)
            print(f"La columna {col} ha sido cambiada a numero entero y redondeada")
    display(df[lista_floatint].info())
    display(df[lista_floatint].describe().T)
    display(df[lista_floatint].sample())  


#Función par eliminar la columna seleccionada de un dataframe

def eliminar_columna(df,col):
    #Se elimina la columna
    df.drop(col, axis=1, inplace=True)
    print(f"Se ha eliminado la columna {col}")
    display(df.sample()) 

#Función para convertir la fecha a datetime

def convertir_fecha (df,col,fmat):
    #Generar un diccionario de conversiones
    meses = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12"
    }
    
    #Reemplazar los valores
    df.replace({col:meses}, regex=True, inplace=True)
    df[col]=pd.to_datetime(df[col], format=fmat)

    print(f"Se ha convertido la columna {col} a fecha")
    print(df.info())
    display(df.sample())

#Función que pasa los valores de una columna a minúsculas

def convertir_minusculas(df,col):
    #conversión a minúsculas
    df[col]=df[col].str.lower()
    display(df.sample())

#Función que convierte el . en _ en los valores de una columna
def punto_barrabaja(df,col):
     #Reemplazar los valores . por _
     df[col] = df[col].astype(str).str.replace('.', '_', regex=False)
     print(f"Se ha cambiado '.' por '_' en la columna {col}")
     display(df.sample())

#Función que convierte el - en _ en los valores de una columna

def guion_barrabaja(df,col):
     #Reemplazar los valores - por _
     df[col] = df[col].astype(str).str.replace('-', '_', regex=False)
     print(f"Se ha cambiado '-' por '_' en la columna {col}")
     display(df[col].value_counts())



#Función que cambia el nombre de una columna por otro

def cambiar_columna (df,col,col1):
    df.rename(columns={col:col1}, inplace=True)
    print(f'Se ha cambiado el nombre de la columna {col} por {col1}')
    display(df.sample())


#Función que pasa a minúsculas todos los valores del dataframe

def convertir_valores_minusculas(df):
    columnas_df = df.select_dtypes(include='O').columns
    for col in columnas_df:
        if col != 'ID':
            df[col] = df[col].str.lower()
    display(df.sample())
