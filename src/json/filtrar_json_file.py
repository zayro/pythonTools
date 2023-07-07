import os
import json

# Ruta Absoluta
# c:/ruta/descarga.json'

with open(os.getcwd() + './src/assets/descarga.json') as archivo:
    contenido = json.load(archivo)
    
# object is a list or not
if type(contenido) is list:
    print("your object is a list")
else:
    print("your object is not a list")
    
print(len(contenido))
    
productos_filtrados = list(filter(lambda producto: producto['empleo']['vacantes'][0]['cantidad'] > 1, contenido))

for producto in productos_filtrados:
    print(producto['id'])
    
    
