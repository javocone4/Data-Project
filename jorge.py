import requests
import pandas as pd

URL= 'https://valencia.opendatasoft.com/explore/dataset/centros-educativos-en-valencia/download/?format=json&timezone=Europe/Berlin&lang=es'

respuesta = requests.get(url=URL)

colegios_json = respuesta.json()

colegios_csv = pd.DataFrame(colegios_json)
colegios_csv.to_csv('colegios1.csv')
