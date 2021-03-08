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