
import reverse_geocoder as rg  # Librería para realizar la geocodificación inversa
import pandas as pd           # Librería para manejar DataFrame


def geolocalizar(df, latcol, loncol, batch_size=100):
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

