import streamlit as st

st.title("Bienvenido a la Calculadora BMI")

peso = st.number_input("Ingrese su peso(kgs)")

formato = st.radio("Seleccionar formato de altura ",("Mts","Cms","Fts"))

if formato ==  "Mts":
    altura = st.number_input("Metros")
    IBM = peso/(altura**2)
elif formato == "Cms":
     altura = st.number_input("Centimetros")
     altura = altura/100
     IBM = peso/(altura**2)
elif formato == "Fts":
    altura = st.number_input("Pies")
    altura = altura*0.3048
    BM = peso/(altura**2)

