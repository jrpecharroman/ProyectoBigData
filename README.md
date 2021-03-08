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
	- los Notebooks con el análisis de los datos para 2018-2019 y para 2020
	- ficheros SAV con los modelos entrenados.

- **Predicciones_sobre_2020**: Unión de los datos anteriores y análisis conjunto en Madrid y Barcelona. Contiene dos subcarpetas para Madrid y Barcelona con:
	- el Notebook de análisis conjunto, 
	- los ficheros CSV de salida para el modelado.
	- los Notebooks con los modelados
	- los Notebooks con el análisis de los datos para 2018-2019 y para 2020
	- ficheros SAV con los modelos entrenados.
	
	
	
Area meteo: 
conectarse a la Api de AEMET para tratar los datos de metereologia relevantes para el proyecto
Se utiliza la siguiente libreria python https://github.com/pablo-moreno/python-aemet
 
