import requests
import csv
import os
import geojson
import psycopg2
URL= 'https://valencia.opendatasoft.com/explore/dataset/centros-educativos-en-valencia/download/?format=json&timezone=Europe/Berlin&lang=es'
  
#Obtenemos el paquete/caja que nos viene de ahi con el get'
respuesta = requests.get(url=URL)
   
#extraemos los datos en formato JSON
#datos = respuesta.json()
#os.mkdir("C:\\Users\\sragg\\Downloads\\docker\\prueba_python\\General")

#EXTRAER CSV COLEGIOS
with open('colegios.csv', 'a', newline='') as csvfile:
  spamwriter = csv.writer(csvfile)
  spamwriter.writerow(respuesta)


'''
URL1 = 'https://valencia.opendatasoft.com/explore/dataset/barris-barrios/download/?format=json&timezone=Europe/Berlin&lang=es'

respuesta1 = requests.get(url=URL1)

with open('barrios.geojson', 'w', newline='') as f:
  spamwriter = geojson.dump(f)
  spamwriter.writerow(respuesta1)
'''
#hola

#CONEXION A POSTGREESQL
conn = psycopg2.connect(database='colegios',host='postgres',user='postgres',password='Welcome01',)
conn.autocommit = True
cursor = conn.cursor()

sql = "CREATE TABLE COLEGIOS(geo_point_2d geography NOT NULL,dgenerica char(20),geo_shape geography NOT NULL);"
  
cursor.execute(sql)
  
sql2 = '''COPY details(geo_point_2d,dgenerica,geo_shape)
FROM 'C:\\Users\\sragg\\Downloads\\docker\\prueba_python\\colegios.csv'
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)