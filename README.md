# MLOps

Introduccion al deploy de modelos.

## Persistencia

Luego de entrenar el modelo en la notebook `ModeloMLOps` guardamos el modelo y el transformador en un pickle usando la libreria joblib.


## Deploy Streamlit Local

Usando la libreria `streamlit` creamos una interfaz web muy simple, que permite al usuario ingresar los datos de su inmueble.

`streamlit_test.py`


Para ver la pagina usamos el comando:

`streamlit run streamlit_test.py`

Podemos agregar un grafico de fuerza generado con shap.

`streamlit run streamlit_test_shap.py`


## Deploy StreamlitCloud

Si queremos disponibilizar nuestro modelo en la nube, podemos usar el servicio gratuito de la streamlitcloud.

Necesitamos crear un repositorio con nuestra webapp y vincular nuestra cuenta de github con streamlitcloud.

No olvidemos generar una lista de todas las librerias utilziadas en nuestro proyecto:

`pip3 freeze > requirements.txt`

Este archivo contiene la lista de librerias y versiones para evitar cualquier problema de incompatibilidades.


Nuestro repositorio deberia verse asi:

```
modelo_prepro.joblib
requirements.txt
st_modelo_shap.py
```

Luego de crear el repositorio vamos a streamlitcloud, seleccionamos `new app` y deberiamos ver el nombre del repo con al app. No olvidar elegir la version de python que utilizaron (en mi caso `python 3.11`)

## Deploy AWS EC2

Podemos usar una maquina virtual para hostear nuestra webapp.

## Deploy AWS Lambdas

Podemos crear una API que reciba solo los datos del inmueble en un json y que devuelva la prediccion.

Para eso vamos a tener que crear una funcion lambda y usar layers para las librerias que usamos en el proyecto.