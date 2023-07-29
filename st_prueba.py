import streamlit as st


st.header('Elija las variables de la propiedad que quiere predecir:')

tipo = st.selectbox(
     'Tipo de inmueble?',['ph','departamento'])

barrio= st.selectbox(
     'Barrio del inmueble?',['Gerli','Burzaco','Belgrano'])

sup = st.slider('Superficie del inmueble?', 9, 400, 2)


habs= st.slider('Cantidad de habitaciones?', 1, 10, 1)


st.write('El precio aproximado por m2 es: ', 34)