import pandas as pd
import streamlit as st

from src import make_prediction

st.title('Hello World!')

# df = st.file_uploader("Carga tu archivo:")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep='|')
    st.write(df.head(3))

@st.experimental_dialog("Predicción")
def vote(prediction):
    # @st.experimental_dialog("Cast your vote")
    if prediction == 1:
        resultado = 'acepta'
    elif prediction == 0:
        resultado = 'no acepta'

    st.write(f"El usario {resultado}")

# if "vote" not in st.session_state:
if st.button('Hacer predicción'):
    prediction = make_prediction.run(df)

    df_final = pd.merge(
        df.reset_index(),
        pd.DataFrame(prediction, columns=['alta']).reset_index(), 
        how='left'
    )

    df_final.drop('index', axis=1, inplace=True)

    st.write(df_final.head(3))

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(df_final)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="large_df.csv",
        mime="text/csv",
    )