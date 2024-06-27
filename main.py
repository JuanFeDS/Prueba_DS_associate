import pandas as pd
import streamlit as st

from src import make_prediction

# st.title('Hello World!')
edad = st.slider(
    "Edad",
    18, 80, (45))

col1, col2, col3 = st.columns(3)

salario_final = col1.number_input("Salario Final", 0)
score_clear = col2.number_input("Score", 0)

mantiene_nom = col3.selectbox(
    "Cliente con nomina",
    ("Si", "No"))

tasa_ofertada = col1.number_input("Tasa Ofertada", 0)

cliente_digital = col2.selectbox(
    "Cliente Digital",
    ("Si", "No"))

sum_op_digital = col3.number_input("Operaciones digitales", 0)

max_con = col1.number_input("max_con", 0)
mean_importe = col2.number_input("mean_importe", 0)
m_consultas = col3.number_input("m_consultas", 0)
m_monetarias = col1.number_input("m_monetarias", 0)
m_nomonetarias = col2.number_input("m_nomonetarias", 0)
cross_sell = col3.number_input("cross_sell", 0)
activo = col1.number_input("activo", 0)
pasivo = col2.number_input("pasivo", 0)
cross_sell_ahor = col3.number_input("cross_sell_ahor", 0)


    # st.write(data)

# clicked = st.button('Click me')



@st.experimental_dialog("Predicción")
def vote(prediction):
    # @st.experimental_dialog("Cast your vote")
    if prediction == 1:
        resultado = 'acepta'
    elif prediction == 0:
        resultado = 'no acepta'

    st.write(f"El usario {resultado}")

if "vote" not in st.session_state:
    if st.button('Hacer predicción'):

        data = pd.DataFrame({
            'EDAD': [edad],
            'Salario_final': [salario_final],
            'SCORE_CLEAR': [score_clear],
            'MANTIENE_NOM': [mantiene_nom],
            'max_con': [max_con],
            'tasa_ofertada': [tasa_ofertada],
            'cliente digital': [cliente_digital],
            'sum_op_digital': [sum_op_digital],
            'mean_importe': [mean_importe],
            'm_consultas': [m_consultas],
            'm_monetarias': [m_monetarias],
            'm_nomonetarias': [m_nomonetarias],
            'CROSS_SELL': [cross_sell],
            'ACTIVO': [activo],
            'PASIVO': [pasivo],
            'cross_sell_ahor': [cross_sell_ahor]
        })

        prediction = make_prediction.run(data)

        vote(prediction)