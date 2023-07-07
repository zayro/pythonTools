import requests

import json

import pandas as pd

# leer datos json desde un archivo
# datos_json = pd.read_json('datos.json')


# URL del JSON remoto
url_phone = "http://country.io/phone.json"

url_names = "http://country.io/names.json"

# Realizamos la petición a la url
response_phone = requests.get(url_phone)
response_names = requests.get(url_names)

# Comprobamos que la petición nos devuelve un Status Code N= 200
status_code = response_phone.status_code
if status_code == 200:
    # Pasamos el contenido JSON de la respuesta a una variable
    jsonResponsePhone = response_phone.json()
    jsonResponseName = response_names.json()

    json_string_phone = json.dumps(jsonResponsePhone)
    json_string_name = json.dumps(jsonResponseName)

    df_phone = pd.read_json(json_string_phone, typ='series')
    df_name = pd.read_json(json_string_name, typ='series')
     
    
    df1 = pd.DataFrame([df_phone])
    df2 = pd.DataFrame([df_name])
       
    
    df = pd.concat([df1, df2], ignore_index=True)
    
    print(df.head())
    
    dataframe1 = df.transpose()
    
    dataframe1.reset_index(inplace=True )
    
    # set index column name
    df.index.name = 'code'
    # add name of colums to dataFrame
    dataframe1.rename({0:'phone',1:'name'  }, axis=1, inplace=True)
    
    print("----------- \n")    
    print(dataframe1.head())    
    print("----------- \n")
    

    
    
    print("----------- \n")
    for index, row in dataframe1.iterrows():        
        print(index,row["index"], row["phone"], row["name"])        
    print("----------- \n")
 
else:
    print("Error al obtener los datos")
