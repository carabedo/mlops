
from joblib import load
import pandas as pd

#Carga del modelo
Modelo, Preprocesador = load('modelo_prepro.joblib') 

def pipeline(tipo,barrio,sup,habs):
    X_pred=pd.DataFrame(columns=['tipo','barrio','sup','habs'])
    X_pred.loc[0,:]=[tipo,barrio,sup,habs]
    X_pred_dummies=Preprocesador.transform(X_pred)    
    return Modelo.predict(X_pred_dummies)[0]


# creamos la lista de opciones
lista_features=list(Preprocesador.get_feature_names_out())

lista_tipos=[x.split('tipo_')[1] for x in lista_features if 'tipo' in x]
lista_barrios=[x.split('barrio_')[1] for x in lista_features if 'barrio' in x]





# el modelo ya esta importado y listo
# generamos la web 
import streamlit as st


st.header('Elija las variables de la propiedad que quiere predecir:')

tipo = st.selectbox(
     'Tipo de inmueble?',lista_tipos)

barrio= st.selectbox(
     'Barrio del inmueble?',lista_barrios)

sup = st.slider('Superficie del inmueble?', 9, 400, 2)


habs= st.slider('Cantidad de habitaciones?', 1, 10, 1)



pred=pipeline(tipo,barrio,sup,habs)

st.write('El precio aproximado por m2 es: ', pred)
