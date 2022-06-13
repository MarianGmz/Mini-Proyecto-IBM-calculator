import streamlit as st

st.title("Bienvenido a la Calculadora IMC")

peso = st.number_input("Ingrese su peso(kgs)")

formato = st.radio("Seleccionar formato de altura ",("Mts","Cm","Ft"))

try:
    if formato ==  "Mts":
        altura = st.number_input("Metros")
        imc = peso/(altura**2)
    elif formato == "Cm":
        altura = st.number_input("Centimetros")
        altura = altura/100
        imc = peso/(altura**2)
    elif formato == "Ft":
        altura = st.number_input("Pies")
        imc = peso / (((altura/3.28))**2)
except Exception as e:
    st.info("Coloque los datos correspondientes")
calcular = st.button("Calcular")
if calcular:
    st.text(f"Tu indice de masa corporal es {imc}")
    if imc < 18.5:
        st.warning("Peso Bajo")

    elif imc >=1.85 and imc <=24.9:
        st.success("Peso Saludable")

    elif imc >= 25.0 and imc <= 29.9:
        st.info("Sobre Peso")
    elif imc >= 30.0 and imc <=39.9:
        st.warning("Obesidad")
    elif imc >= 40:
        st.error("Obesidad Extrema")

