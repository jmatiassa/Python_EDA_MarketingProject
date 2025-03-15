
import reverse_geocoder as rg  # Librería para realizar la geocodificación inversa
import pandas as pd           # Librería para manejar DataFrame


def geolocalizar(df, latcol, loncol, batch_size=100):
    """
    Realiza la geolocalización de coordenadas (latitud y longitud) a nombre de ciudad, país y región.

    Esta función toma un DataFrame con columnas de latitud y longitud, y utiliza una API de geolocalización (como 
    geopy o similar) para obtener información sobre la ubicación correspondiente. Los resultados, que incluyen el 
    nombre de la ciudad, el país y la región, se agregan como nuevas columnas en el DataFrame. El procesamiento se 
    realiza en lotes para evitar problemas con las solicitudes a la API.

    Args:
        df (pd.DataFrame): DataFrame que contiene las coordenadas geográficas (latitud y longitud).
        latcol (str): El nombre de la columna que contiene las coordenadas de latitud.
        loncol (str): El nombre de la columna que contiene las coordenadas de longitud.
        batch_size (int, optional): El tamaño del lote para procesar las coordenadas en grupos. El valor predeterminado es 100.

    Returns:
        pd.DataFrame: El DataFrame original con las nuevas columnas 'City', 'Country', y 'Region' añadidas con los resultados de la geolocalización.
    """
    # Crear lista de coordenadas y resultados
    coordenadas_lotes = []
    resultados = []

    # Iterar sobre el DataFrame fila por fila
    for index, row in df.iterrows():
        lat = row.get(latcol, None)
        lon = row.get(loncol, None)

        # Validar coordenadas: si falta una, asignar resultado nulo
        if pd.isna(lat) or pd.isna(lon):
            resultados.append((None, None, None))
        else:
            coordenadas_lotes.append((lat, lon))

    # Procesar en lotes las coordenadas válidas
    for i in range(0, len(coordenadas_lotes), batch_size):
        lote = coordenadas_lotes[i:i + batch_size]
        try:
            lote_resultados = rg.search(lote)
            resultados.extend([(r.get('name', None), r.get('cc', None), r.get('admin1', None)) for r in lote_resultados])
        except Exception as e:
            print(f"Error al procesar lote {lote}: {e}")
            resultados.extend([(None, None, None)] * len(lote))  # Rellenar con None en caso de error

    # Agregar resultados al DataFrame original
    ciudades, paises, regiones = zip(*resultados)
    df['City'] = ciudades
    df['Country'] = paises
    df['Region'] = regiones

    return df


