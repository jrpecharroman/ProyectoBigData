![imagen](https://user-images.githubusercontent.com/74833588/110534107-fdae6980-811e-11eb-9b19-b2bc04d7ebd1.png)

# Proyecto BigData

Proyecto Curso Instituto Tecnológico de Telefónica

El presente proyecto tiene como objetivo analizar la calidad del aire en dos ciudades españolas en función de la meteorología y del tráfico.  
- Usando datos de los años 2018 y 2019 se obtiene un modelo de predicción listo para aplicar sobre nuevos datos.
- Se aplica sobre los datos del 2020 y se compara con las mediciones reales.

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

- **AnalisisConjunto_Modelados**: Unión de los datos anteriores y análisis conjunto en Madrid y Barcelona. Obtención de modelos de predicción. Contiene dos subcarpetas para Madrid y Barcelona con:
	- el Notebook de análisis conjunto, 
	- los ficheros CSV de salida para el modelado.
	- los Notebooks con los modelados
	- ficheros SAV con los modelos entrenados.

- **Predicciones_sobre_2020**: Aplicación de los modelos obtenidos en la predicción sobre datos del 2020. Contiene:
	- los Notebooks con las predicciones
	
- **Visualizaciones Qlik**: Archivos necesarios para la poder instalar la aplicación de BI diseñada para el proyecto basada en Qlik Sense:
	- AirQ - Madrid y Barcelona Ciudad.qvf
	- Carpeta con las extensiones necesarias a instalar.
	- Scripts utilizados en la carga de datos para generar el modelo de análisis. 
	- Carpeta con imágenes fijas y gifs a modo de ejemplos visuales de los dashboards diseñados.
	- Carpeta con los datos de las Geolocalizaciones creadas para las estaciones AQI.
	- Carpeta otros con archivos de diseño para la escala de colores de AQI

- **Recursos**: Contiene algunos recursos externos utilizados en el proyecto:
	- Acceso a [diagrama de las fuentes y tecnologias utilizadas en el proyecto ](https://app.terrastruct.com/diagrams/780713555)
	- Copia [librería aemet para python](https://github.com/pablo-moreno/python-aemet)


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

Puede ubicar la carpeta ProyectoBigData en cualquier ruta de su equipo.

## Ejecución

Para el desarrollo del proyecto deberán ejecutarse los Notebooks en el siguiente orden: 
> Puede ejecutarse de forma independiente todo lo relacionado con Madrid y todo lo relacionado con Barcelona

### Madrid: modelado desde datos 2018-2019

1. ProyectoBigData \ Contaminacion \ datosContaminacionMadrid \ JupiterNoteBook \ **DatosCalidadMadrid-2018-2019.ipynb**

   > generará el fichero 'contaminacionMadrid2018_2019.csv' en la misma carpeta

2. ProyectoBigData \ Meteorologia \ **ConsultasAemet - mad 18-19.ipynb**

   > generará el fichero 'df_sinhoras_estacion_datos_diarios_mad.csv' en la misma carpeta

3. ProyectoBigData \ Tráfico \ Madrid \ **DatosTráficoMadrid_18_19.ipynb**

   > generará el fichero 'trafico_mad.csv' en la misma carpeta

4. ProyectoBigData \ AnalisisConjunto_Modelados \ Madrid \ **AnalisisConjunto_Mad.ipynb**

   > generará en la misma carpeta los ficheros:  
   > 'DatosMergeadosMadrid.csv'  
   > 'DatosMergeadosMadrid_ConSeleccionCaract.csv' y  
   > 'DatosMergeadosMadrid_ConSeleccionCaract_PCA.csv' 

5. ProyectoBigData \ AnalisisConjunto_Modelados \ Madrid \ **ModelosPredictivosMadrid_SinSeleccionCaract_PM10.ipynb**

   > generará el fichero 'Modelo_finalizado_MadridPM10.sav' en la misma carpeta
 
6. ProyectoBigData \ AnalisisConjunto_Modelados \ Madrid \ **ModelosPredictivosMadrid-ConSeleccionCaracterísticas_PCA_PM10.ipynb**

7. ProyectoBigData \ AnalisisConjunto_Modelados \ Madrid \ **ModelosPredictivosMadrid-ConSeleccionCaracterísticas_PM10.ipynb**

8. ProyectoBigData \ AnalisisConjunto_Modelados \ Madrid \ **ModelosPredictivosMadrid_SinSeleccionCaract_NO2.ipynb**

   > generará el fichero 'Modelo_finalizado_MadridNO2.sav' en la misma carpeta

### Madrid: aplicación predicciones sobre datos del 2020

9. ProyectoBigData \ Contaminacion \ datosContaminacionMadrid \ JupiterNoteBook \ **DatosCalidadMadrid-2020.ipynb**

   > generará el fichero 'contaminacionMadrid2020.csv' en la misma carpeta

10. ProyectoBigData \ Meteorologia \ **ConsultasAemet - mad 20.ipynb**

    > generará el fichero 'df_sinhoras_estacion_datos_diarios_mad_2020.csv' en la misma carpeta

11. ProyectoBigData \ Tráfico \ Madrid \ **DatosTráficoMadrid_2020.ipynb**

    > generará el fichero 'trafico_mad_2020.csv' en la misma carpeta

12. ProyectoBigData \ Predicciones_sobre_2020 \ **PrediccionesMadridPM10_2020.ipynb**

13. ProyectoBigData \ Predicciones_sobre_2020 \ **PrediccionesMadridNO2_2020.ipynb**


### Barcelona: modelado desde datos 2018-2019

1. ProyectoBigData \ Contaminacion \ datosContaminacionBarcelona \ JupiterNoteBook \ **DatosCalidadBarcelona.ipynb**

   > generará el fichero 'contaminacionBarcelona2018_2019.csv' en la misma carpeta

2. ProyectoBigData \ Meteorologia \ **ConsultasAemet - bcn 18-19-sin estacion fabra.ipynb**

   > generará el fichero 'df_sinhoras_estacion_datos_diarios_bcn.csv' en la misma carpeta

3. ProyectoBigData \ Tráfico \ Barcelona \ **DatosTráficoBarcelona_18_19.ipynb**

   > generará los ficheros 'DatosEstadoTraficoBarcelona.csv' y 'DatosEstadoTraficoBarcelona_SinMadrugadas.csv' en la misma carpeta

4. ProyectoBigData \ AnalisisConjunto_Modelados \ Barcelona \ **AnalisisConjuntoBarcelona.ipynb**

   > generará en la misma carpeta los ficheros:  
   > 'DatosMergeadosBarcelona.csv'  
   > 'DatosMergeadosBarcelona_ConSeleccionCaract_ParaPM10.csv'  
   > 'DatosMergeadosBarcelona_ConSeleccionCaract_ParaNO2.csv' y  
   > 'DatosMergeadosBarcelona_ConSeleccionCaract_PCA.csv' 

5. ProyectoBigData \ AnalisisConjunto_Modelados \ Barcelona \ **ModeloBarcelonaPM10.ipynb**

   > generará el fichero 'Modelo_finalizado_BarcelonaPM10.sav' en la misma carpeta
 
6. ProyectoBigData \ AnalisisConjunto_Modelados \ Barcelona \ **ModeloBarcelonaNO2.ipynb**

   > generará el fichero 'Modelo_finalizado_BarcelonaNO2.sav' en la misma carpeta

### Barcelona: aplicación predicciones sobre datos del 2020

7. ProyectoBigData \ Contaminacion \ datosContaminacionBarcelona \ JupiterNoteBook \ **DatosCalidadBarcelona-2020.ipynb**

   > generará el fichero 'contaminacionBarcelona2020.csv' en la misma carpeta

8. ProyectoBigData \ Meteorologia \ **ConsultasAemet - bcn-2020-sin estacion fabra.ipynb**

    > generará el fichero 'df_sinhoras_estacion_datos_diarios_bcn_2020.csv' en la misma carpeta

9. ProyectoBigData \ Tráfico \ Barcelona \ **DatosTraficoBarcelona_2020.ipynb**

   > generará los ficheros 'DatosEstadoTraficoBarcelona_2020.csv' y 'DatosEstadoTraficoBarcelona_SinMadrugadas_2020.csv' en la misma carpeta

10. ProyectoBigData \ Predicciones_sobre_2020 \ **PrediccionesBarcelonaPM10_2020.ipynb**

11. ProyectoBigData \ Predicciones_sobre_2020 \ **PrediccionesBarcelonaNO2_2020.ipynb**

## Visualizaciones

- Para el apartado de visualizaciones se ha desarrollado una aplicación en Qlik Sense. Para desplegar la aplicación AirQ - Madrid y Barcelona ciudad será es necesario:

**1.** Disponer de una instalacion Qlik Sense.

**2.** Importar los zips incluidos en la carpeta del repositorio ProyectoBigData\visualizaciones qlik\Extensions\ en el apartado extensions del servidor qlik o bien guardarlos en la carpeta "extension"s si se trata una instalación de Qlik Sense Desktop la cual habitualmente se ubica en la siguiente ruta:
		
		C:\Users\[usuario]\Documents\Qlik\Sense\Extensions

**3.** Es necesario importar la aplicación AirQ - Madrid y Barcelona Ciudad.qvf. Podran encontrar el archivo en la carpeta de repositorio 		ProyectoBigData\visualizaciones qlik\ en el apartado en Apps del servidor Qlik o bien guardarlo en la carpeta "Apps" si se dispone de una instalación de Qlik Sense Desktop Desktop la cual habitualmente se ubica en la siguiente ruta:. 

		C:\Users\[usuario]\Documents\Qlik\Sense\Apps

**4.** La App AirQ fue diseñada con Qlik Sense desktop September 2020 y es possible que algunos botones del dashboard de introducción necesitan objetos de esta versión, alternativamente se puede desplegar en una versión anterior y utilizar los botones incluidos como extensión en el "Qlik Sense Dashboard Bundle".

![imagen](https://user-images.githubusercontent.com/74833588/110533306-208c4e00-811e-11eb-9d79-839e0e3e5342.png)

   	>Si fuera el caso los 4 botones de navegación a sustituir son los siguientes: 

	   > Analisis conjunto = id hoja = 54fd9c26-c153-4ba6-97db-ac2dfe4ffb62
	   > Mapa = id hoja = c6f9e8a4-7a1f-412d-98e7-d6bf55fd5034
	   > Estado actual por ciudad = id hoja = 994185d4-a366-467a-80b3-2cd4b7bc5ebe
	   > Analisis conjunto = id hoja = 1d685140-b35d-499f-b212-aa077df844fe
