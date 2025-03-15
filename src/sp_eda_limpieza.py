
#Fmportaciones
import pandas as pd

#Función para crear el eda preeliminar que muestra 5 filas, la info, nulos, duplicados y el distinct de objects
def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar (EDA) de un DataFrame.

    Esta función proporciona una vista general del DataFrame, mostrando:
    - Una muestra aleatoria de 5 registros.
    - Información sobre las columnas (tipos de datos, memoria, etc.).
    - El porcentaje de valores nulos por columna.
    - El número de registros duplicados.
    - La distribución de valores para las columnas categóricas.
    - Estadísticas descriptivas para las columnas numéricas.

    Args:
        df (pd.DataFrame): DataFrame que será analizado.

    Returns:
        None: La función imprime y muestra los resultados del análisis exploratorio sin devolver nada.
    """
    display(df.sample(5))
    print('--------------------')

    print('INFO')
    display(df.info())
    print('--------------------')

    print('NULOS')
    display(round(df.isnull().sum() / df.shape[0] * 100, 2))
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
    """
    Elimina la columna 'Unnamed: 0' de un DataFrame si existe.

    Esta función verifica si existe una columna llamada 'Unnamed: 0' en el DataFrame y, si es así, la elimina.
    Luego, imprime los nombres originales de las columnas, muestra un mensaje si la columna no se encuentra 
    y finalmente muestra una muestra del DataFrame después de la eliminación.

    Args:
        df (pd.DataFrame): DataFrame del cual se eliminará la columna 'Unnamed: 0', si existe.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
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
    """
    Convierte los nombres de las columnas de un DataFrame a mayúsculas.

    Esta función toma los nombres de las columnas del DataFrame y los convierte a mayúsculas (capitaliza la primera
    letra de cada nombre de columna). Luego, imprime un mensaje indicando que las columnas han sido modificadas
    y muestra una muestra del DataFrame actualizado.

    Args:
        df (pd.DataFrame): DataFrame cuyas columnas serán convertidas a mayúsculas.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    df.columns = df.columns.str.capitalize()
    print('Columnas pasadas a mayúsculas')
    display(df.sample())


#Función para detectar booleanos y cambiarlos por yes o no
def transformar_booleanos(df):
    """
    Transforma columnas booleanas de un DataFrame, cambiando valores 1 por 'yes' y 0 por 'no'.

    La función detecta las columnas que contienen solo valores 1 y 0 (excluyendo los nulos), las identifica como
    columnas booleanas y transforma los valores:
    - 1 se convierte en 'yes'.
    - 0 se convierte en 'no'.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas booleanas a transformar.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
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
    """
    Convierte las columnas de tipo 'object' en un DataFrame a tipo float.

    La función verifica todas las columnas del DataFrame que son de tipo 'object', intenta reemplazar las comas por
    puntos en los valores de cada columna y luego convierte esos valores a tipo float. Si alguna columna no puede ser
    convertida (por ejemplo, si contiene texto no numérico), se ignora. Al final, se imprime una lista de las columnas
    que fueron modificadas y muestra una muestra del DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas a convertir.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Iterar sobre todas las columnas del DataFrame
    columnas_modificadas = []
    for col in df.columns:
        # Verificar si la columna es de tipo object
        if df[col].dtype == 'object':
            try:
                # Reemplazar comas por puntos y convertir los valores a float
                df[col] = df[col].str.replace(',', '.', regex=False).astype(float)
                columnas_modificadas.append(col)
            except ValueError:
                continue
    print(f"Se han modificado las siguientes columnas: {columnas_modificadas}")
    display(df.sample())


#Función para convertir datos float a int redondeando sus decimales
def float_a_int(df, col):
    """
    Convierte una columna de tipo float64 a tipo int, redondeando sus valores.

    La función verifica si la columna especificada en el DataFrame es de tipo 'float64'. Si lo es, redondea los valores
    de esa columna y cambia su tipo de dato a entero ('int'). Después, muestra información sobre el DataFrame y una
    muestra aleatoria de los primeros registros.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna a modificar.
        col (str): El nombre de la columna que se desea convertir de float a int.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Verificar si el tipo de dato es float64
    if df[col].dtype == 'float64':
        # Redondear los valores de la columna y modificar el tipo de dato a int
        df[col] = df[col].round().astype(int)
        print(f"La columna {col} ha sido cambiada a número entero y redondeada")
        display(df.info())
        display(df.sample())


#Función para convertir datos float a int en una lista de columnas
def float_int_lista(df, lista_floatint):
    """
    Convierte varias columnas de tipo float64 a tipo int, redondeando sus valores.

    La función recorre una lista de columnas especificadas y, si el tipo de dato de la columna es 'float64',
    redondea los valores y cambia su tipo de dato a 'int'. Después, muestra información sobre las columnas modificadas,
    estadísticas descriptivas y una muestra aleatoria de los registros de esas columnas.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas a modificar.
        lista_floatint (list): Lista de nombres de columnas que se desean convertir de float a int.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    for col in lista_floatint:
        if df[col].dtype == 'float64':
            # Redondear los valores de la columna y modificar el tipo de dato a int
            df[col] = df[col].round().astype(int)
            print(f"La columna {col} ha sido cambiada a número entero y redondeada")
    
    display(df[lista_floatint].info())
    display(df[lista_floatint].describe().T)
    display(df[lista_floatint].sample())



#Función par eliminar la columna seleccionada de un dataframe

def eliminar_columna(df, col):
    """
    Elimina una columna específica de un DataFrame.

    Esta función elimina la columna indicada en el DataFrame usando el nombre de la columna proporcionado. 
    Después de eliminar la columna, muestra una muestra aleatoria del DataFrame actualizado.

    Args:
        df (pd.DataFrame): DataFrame del cual se eliminará la columna.
        col (str): El nombre de la columna que se desea eliminar.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Se elimina la columna
    df.drop(col, axis=1, inplace=True)
    print(f"Se ha eliminado la columna {col}")
    display(df.sample())


#Función para convertir la fecha a datetime

def convertir_fecha(df, col, fmat):
    """
    Convierte una columna de un DataFrame a tipo datetime usando un formato personalizado.

    Esta función reemplaza los nombres de los meses en español en una columna por su equivalente numérico (por ejemplo, 
    "enero" se convierte en "01") y luego convierte los valores de esa columna al formato de fecha especificado por 
    el parámetro `fmat`.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna a convertir.
        col (str): El nombre de la columna que contiene las fechas a convertir.
        fmat (str): El formato de fecha a aplicar durante la conversión (por ejemplo, "%d-%m-%Y").

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Generar un diccionario de conversiones
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
    
    # Reemplazar los valores
    df.replace({col: meses}, regex=True, inplace=True)
    df[col] = pd.to_datetime(df[col], format=fmat)

    print(f"Se ha convertido la columna {col} a fecha")
    print(df.info())
    display(df.sample())


#Función que pasa los valores de una columna a minúsculas

def convertir_minusculas(df, col):
    """
    Convierte los valores de una columna a minúsculas.

    Esta función convierte todos los valores de la columna especificada a minúsculas utilizando el método `str.lower()`.
    Después de la conversión, muestra una muestra aleatoria del DataFrame actualizado.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna a convertir.
        col (str): El nombre de la columna cuyos valores serán convertidos a minúsculas.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Conversión a minúsculas
    df[col] = df[col].str.lower()
    display(df.sample())


#Función que convierte el . en _ en los valores de una columna
def convertir_minusculas(df, col):
    """
    Convierte los valores de una columna a minúsculas.

    Esta función convierte todos los valores de la columna especificada a minúsculas utilizando el método `str.lower()`.
    Después de la conversión, muestra una muestra aleatoria del DataFrame actualizado.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna a convertir.
        col (str): El nombre de la columna cuyos valores serán convertidos a minúsculas.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Conversión a minúsculas
    df[col] = df[col].str.lower()
    display(df.sample())


#Función que convierte el - en _ en los valores de una columna

def guion_barrabaja(df, col):
    """
    Reemplaza los guiones ('-') por guiones bajos ('_') en los valores de una columna.

    Esta función toma la columna especificada del DataFrame, convierte los valores a cadenas de texto si es necesario,
    y reemplaza todos los guiones ('-') por guiones bajos ('_'). Luego, muestra la frecuencia de los valores únicos
    de la columna.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna a modificar.
        col (str): El nombre de la columna en la que se deben reemplazar los guiones por guiones bajos.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    # Reemplazar los valores - por _
    df[col] = df[col].astype(str).str.replace('-', '_', regex=False)
    print(f"Se ha cambiado '-' por '_' en la columna {col}")
    display(df[col].value_counts())




#Función que cambia el nombre de una columna por otro

def cambiar_columna(df, col, col1):
    """
    Cambia el nombre de una columna en un DataFrame.

    Esta función renombra una columna en el DataFrame, cambiando su nombre de `col` a `col1`. Luego, muestra una muestra
    aleatoria del DataFrame con el nombre de la columna actualizado.

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna a renombrar.
        col (str): El nombre actual de la columna que se desea cambiar.
        col1 (str): El nuevo nombre que se asignará a la columna.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    df.rename(columns={col: col1}, inplace=True)
    print(f'Se ha cambiado el nombre de la columna {col} por {col1}')
    display(df.sample())



#Función que pasa a minúsculas todos los valores del dataframe

def convertir_valores_minusculas(df):
    """
    Convierte los valores de las columnas de tipo 'object' a minúsculas, excepto la columna 'ID'.

    Esta función recorre todas las columnas del DataFrame que son de tipo 'object' (cadenas de texto), y convierte
    sus valores a minúsculas, a excepción de la columna 'ID'. Luego, muestra una muestra aleatoria del DataFrame actualizado.

    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas a convertir.

    Returns:
        None: La función modifica el DataFrame in situ y no retorna ningún valor.
    """
    columnas_df = df.select_dtypes(include='O').columns
    for col in columnas_df:
        if col != 'ID':
            df[col] = df[col].str.lower()
    display(df.sample())

