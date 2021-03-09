![imagen](https://user-images.githubusercontent.com/74833588/110534107-fdae6980-811e-11eb-9b19-b2bc04d7ebd1.png)

# Proyecto BigData

Proyecto Curso Instituto Tecnológico de Telefónica

El presente proyecto tiene como objetivo analizar la calidad del aire en dos ciudades españolas en función de la meteorología y del tráfico.  
Se obtiene un modelo de predicción listo para aplicar sobre nuevos datos actuales.

## Contenido

El repositorio del proyecto consta de las siguientes carpetas:

- **Contaminación**: Análisis de los datos de calidad del aire en Madrid y Barcelona. Contiene dos subcarpetas para Madrid y Barcelona con:
	- los ficheros con las fuentes de datos (CSVs), 
	- los Notebooks con el análisis de los datos para 2018-2019 y para 2020 
	- los ficheros CSV de salida para la siguiente fase del proyecto.
	- ficheros CSV con las estaciones de medida para ser usado por el software de visualización Qlik Sense.

- **Meteorología**: Análisis de los datos de meteorología en Madrid y Barcelona. Contiene:
	- los ficheros con las fuentes de datos (CSVs), 
	- los Notebooks con el análisis de los datos para 2018-2019 y para 2020
	- los ficheros CSV de salida para la siguiente fase del proyecto.
	- ficheros CSV con las estaciones de medida para ser usado por el software de visualización Qlik Sense.

- **Tráfico**: Análisis de los datos de tráfico en Madrid y Barcelona. Contiene dos subcarpetas para Madrid y Barcelona con:
	- los ficheros con las fuentes de datos (CSVs), 
	- los Notebooks con el análisis de los datos para 2018-2019 y para 2020
	- los ficheros CSV de salida para la siguiente fase del proyecto.
	- fichero CSV con los puntos de medida para ser usado por el software de visualización Qlik Sense.

- **Datos_Mergeados**: Unión de los datos anteriores y análisis conjunto en Madrid y Barcelona. Contiene dos subcarpetas para Madrid y Barcelona con:
	- el Notebook de análisis conjunto, 
	- los ficheros CSV de salida para el modelado.
	- los Notebooks con los modelados
	- ficheros SAV con los modelos entrenados.

- **Predicciones_sobre_2020**: Aplicación de los modelos obtenidos en la predicción sobre datos del 2020. Contiene:
	- los Notebooks con las predicciones


## Instalación

Para el desarrollo del proyecto se ha usado **Python 3.8** sobre Anaconda 3

Puede usar el gestor de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las librerías necesarias.

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install scipy
pip install scikit-learn
pip install joblib
```

## Uso

Para el desarrollo del proyecto deberán ejecutarse los Notebooks en el orden especificado en el apartado de Contenido. 

Puede ejecutarse de forma independiente todo lo relacionado con Madrid y todo lo relacionado con Barcelona.

## Visualizaciones
App AirQ diseñada con Qlik Sense desktop September 2020.
Algunos botones del dashboard de introducción necesitan objetos de esta versión, alternativamente se puede desplegar en una versión anterior y utilizar los botones incluidos como extensión en el qlik sense dashboard bundle. 
![imagen](https://user-images.githubusercontent.com/74833588/110533306-208c4e00-811e-11eb-9d79-839e0e3e5342.png)
Los 4 botones de navegación a substituir 
	-Analisis conjunto = id hoja = 54fd9c26-c153-4ba6-97db-ac2dfe4ffb62
	-Mapa = id hoja = c6f9e8a4-7a1f-412d-98e7-d6bf55fd5034
	-Estado actual por ciudad = id hoja = 994185d4-a366-467a-80b3-2cd4b7bc5ebe
	-Analisis conjunto = id hoja = 1d685140-b35d-499f-b212-aa077df844fe


Es necesario importar los zips incluidos en la carpeta del repositorio ProyectoBigData\visualizaciones qlik\Extensions\ en el apartado extensions del servidor qlik o bien guardarlos en la carpeta extensions de la instalación de Qlik Sense desktop. 
Habitualmente C:\Users\[usuario]\Documents\Qlik\Sense\Extensions

Es necesario importar la aplicación (AirQ - Madrid y Barcelona Ciudad.qvf) que encontraran en la carpeta de repositorio ProyectoBigData\visualizaciones qlik\ en el apartado en Apps del servidor Qlik o bien guardarlos en la carpeta Apps de la instalación de Qlik sense desktop. 
Habitualmente C:\Users\[usuario]\Documents\Qlik\Sense\Apps


