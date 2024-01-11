import requests
import json
import urllib3

# disable warning url
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def validar(x):
    total = list(map(lambda item: item['cantidad'], x['empleo']['vacantes']))    
    
    if sum(total) > 100 :
        print(f"Cantidad de registros: {(total)} Sumatoria: {sum(total)} ")
        return True
    else:
        return False

def buscar_empleo(url):
    # Realizar una solicitud HTTP GET al endpoint JSON de ejemplo
    response = requests.get(url, verify=False)

    # Obtener los datos de la respuesta como JSON
    datos_json = json.loads(response.text)

    # Imprimir los datos en la consola y la cantidad
    # print(datos_json)
    # print(len(datos_json))

 
    # object is a list or not
    if type(datos_json) is list:
  

        #productos_filtrados = list(filter(lambda producto: len(producto['empleo']['vacantes']) > 50, datos_json))
        productos_filtrados = list(filter(validar, datos_json))

        for producto in productos_filtrados:
            print(producto['id'])
     
    else:
        print("your object is not a list")

i = 0
while i < 27:
    url = f"https://simo.cnsc.gov.co/empleos/ofertaPublica/?search_palabraClave=&search_nivel=3&search_convocatoria=678784991&search_departamento=&search_municipio=&search_salario=&search_entidad=&search_numeroOPEC=&page={i}&size=10"
    buscar_empleo(url)
    i += 1
