import requests
import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
url='http://ergast.com/api/f1/2022/22/results.json'
response=requests.get(url)
print(json.loads(response.content))
content=json.loads(response.content)
print(content['MRData'].keys())
print(pd.DataFrame(content['MRData']['RaceTable']['Races'][0]['Results']))

#RESULTADOS TEMPORADA 2022

df_results_2022=pd.DataFrame()
for race in list(range(1,23)):
    url = 'http://ergast.com/api/f1/2022/{}/results.json'
    response = requests.get(url.format(race))
    content=json.loads(response.content)

    df_results_2022=df_results_2022.append(pd.DataFrame(content['MRData']['RaceTable']['Races'][0]['Results']))

print(df_results_2022)

#Tabla de Puntuaciones
#Conductores

df_results_2022['Driver']=df_results_2022['Driver'].apply(lambda x: x['driverId']) #Asignamos una funcion para extraer el nombre del conductor del diccionario y asignarlo a nuestra columna Driver.
print(df_results_2022['Driver'])
df_results_2022['points']=df_results_2022['points']
print(df_results_2022['points'])
df_results_2022['points']=df_results_2022['points'].astype(int) #Convertimos los valores a tipo entero para poder realizar su suma.
print(df_results_2022.groupby(['Driver']).sum())
print(df_results_2022.groupby(['Driver']).sum().sort_values(by='points', ascending=False)) #Acomodamos los datos de manera descendente.
df_results_2022['position']=df_results_2022['position'].astype(int)
print(df_results_2022.groupby(['Driver']).agg({'points':'sum','position':'min'}).sort_values(by='points', ascending=False)) #Con agg() agregamos nuvas columnas de los valores seleccionados junto con una funcion a aplicar a los valores.

#Constructors

df_results_2022['Constructor']=df_results_2022['Constructor'].apply(lambda x: x['constructorId'])
print(df_results_2022.groupby(['Constructor']).agg({'points':'sum'}).sort_values(by='points', ascending=False))
