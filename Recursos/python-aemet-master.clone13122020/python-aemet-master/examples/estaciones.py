from aemet import Aemet, Estacion
import json


aemet = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqYXVtZUBncmVlbmZvb2RpYmVyaWNhLmVzIiwianRpIjoiMWFmMmM5ZDMtMDBhZS00YWMwLTk2ZjctZTYzODZiYzQ3NDRjIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MDIwMDcyNjEsInVzZXJJZCI6IjFhZjJjOWQzLTAwYWUtNGFjMC05NmY3LWU2Mzg2YmM0NzQ0YyIsInJvbGUiOiIifQ.R9v0ZXsF3sN-_p87RjELY91YYTVWqx_DqellRX9xCD4')
estaciones = Estacion.get_estaciones('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqYXVtZUBncmVlbmZvb2RpYmVyaWNhLmVzIiwianRpIjoiMWFmMmM5ZDMtMDBhZS00YWMwLTk2ZjctZTYzODZiYzQ3NDRjIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MDIwMDcyNjEsInVzZXJJZCI6IjFhZjJjOWQzLTAwYWUtNGFjMC05NmY3LWU2Mzg2YmM0NzQ0YyIsInJvbGUiOiIifQ.R9v0ZXsF3sN-_p87RjELY91YYTVWqx_DqellRX9xCD4')[:3]
datos = []
anyo_inicio, anyo_fin = 2016, 2017 + 1


for estacion in estaciones:
    print('{}: {}'.format(estacion['indicativo'], estacion['nombre']))
    for anyo in range(anyo_inicio, anyo_fin):
        vcm = aemet.get_valores_climatologicos_mensuales(anyo, estacion['indicativo'])
        resultado = {
            'estacion': estacion,
            'valores_climatologicos': vcm,
            'anyo': anyo
        }
        datos.append(resultado)

print(json.dumps(datos, indent=2))
