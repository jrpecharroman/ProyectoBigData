from logging import exception

import pandas as panda
from datetime import datetime
import matplotlib.pyplot as pyplt
import seaborn as sns
from seaborn import pairplot

from sklearn.impute import SimpleImputer
import numpy as numpy
from sklearn.preprocessing import normalize
import sklearn.preprocessing as sklPreprocesing


URL_DESCARGA = "/home/carlos/Proyectos/Python/datosContaminacionMadrid/madrid-air-quality.csv"
try:
    dfContaminacion = panda.read_csv(URL_DESCARGA)
except Exception as error:
    print(error, "--> No se ha podido descargar el fichero")


columnNames = ['date', 'pm25', 'pm10','o3','no2','so2','co']
dfContaminacion.columns = columnNames

dfContaminacion ['date'] = panda.to_datetime(dfContaminacion['date'], format='%Y-%m-%d', errors='coerce')
dfContaminacion ['pm25'] = panda.to_numeric(dfContaminacion['pm25'], errors='coerce')
dfContaminacion ['pm10'] = panda.to_numeric(dfContaminacion['pm10'], errors='coerce')
dfContaminacion ['o3'] = panda.to_numeric(dfContaminacion['o3'], errors='coerce')
dfContaminacion ['no2'] = panda.to_numeric(dfContaminacion['no2'], errors='coerce')
dfContaminacion ['so2'] = panda.to_numeric(dfContaminacion['so2'], errors='coerce')
dfContaminacion ['co'] = panda.to_numeric(dfContaminacion['co'], errors='coerce')

print(dfContaminacion.dtypes)


df2018 = dfContaminacion[(dfContaminacion['date'] > '2018-01-01') & (dfContaminacion['date'] < '2019-01-01')]
#Mirar más adelante porque no funciona y lanza error
#dfPrueba = dfContaminacion.loc[datetime(2018 - 0o1 - 0o1):datetime(2019 - 0o1 - 0o1)]
#datos2018 = dfContaminacion['date'].loc[datetime(2016,1,1,0,0,1):datetime(2016,1,1,0,0,3)]
#datos2018 = dfContaminacion.loc[dfContaminacion['date'] > datetime(2018,1,1)]
print(df2018.shape)



