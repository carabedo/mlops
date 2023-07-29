import streamlit as st
import pandas as pd

df=pd.DataFrame([[1,2],[3,5]])

st.text('hola, como estan?')

st.checkbox('Opcion 1')

st.dataframe(df)

st.file_uploader('Adjunte sus datos')

st.text('Saludos!')