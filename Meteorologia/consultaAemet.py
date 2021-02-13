
import requests
import pandas as pd

def ejemploPythonRequest():
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/2017-01-01/aniofin/2018-01-01/estacion/3195/"

    querystring = {"api_key":'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqYXVtZUBncmVlbmZvb2RpYmVyaWNhLmVzIiwianRpIjoiMWFmMmM5ZDMtMDBhZS00YWMwLTk2ZjctZTYzODZiYzQ3NDRjIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MDIwMDcyNjEsInVzZXJJZCI6IjFhZjJjOWQzLTAwYWUtNGFjMC05NmY3LWU2Mzg2YmM0NzQ0YyIsInJvbGUiOiIifQ.R9v0ZXsF3sN-_p87RjELY91YYTVWqx_DqellRX9xCD4'}

    headers = {
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    urlDatos = response.json().get('datos')
    print(urlDatos)
    import urllib.request, json
    with urllib.request.urlopen(urlDatos) as url:
        datos = json.loads(url.read().decode('utf-8'))

    import pandas as pd

    df_estacion_datos_diarios = pd.DataFrame(datos)

    print(df_estacion_datos_diarios.head())

def ejemploHttpCliente():
    import http.client

    conn = http.client.HTTPSConnection("opendata.aemet.es")

    headers = {
        'cache-control': "no-cache"
    }

    conn.request("GET",
                 "/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqYXVtZUBncmVlbmZvb2RpYmVyaWNhLmVzIiwianRpIjoiMWFmMmM5ZDMtMDBhZS00YWMwLTk2ZjctZTYzODZiYzQ3NDRjIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MDIwMDcyNjEsInVzZXJJZCI6IjFhZjJjOWQzLTAwYWUtNGFjMC05NmY3LWU2Mzg2YmM0NzQ0YyIsInJvbGUiOiIifQ.R9v0ZXsF3sN-_p87RjELY91YYTVWqx_DqellRX9xCD4",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


ejemploPythonRequest()