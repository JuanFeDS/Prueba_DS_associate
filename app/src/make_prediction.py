import pandas as pd
import pickle

from Utils.functions import adjust_decimal_format

def run(df: pd.DataFrame):
    df['tasa_ofertada'] = adjust_decimal_format(df['tasa_ofertada'])
    df['sum_op_digital'] = adjust_decimal_format(df['sum_op_digital'])
    df['mean_importe'] = adjust_decimal_format(df['mean_importe'])
    df['m_consultas'] = adjust_decimal_format(df['m_consultas'])
    df['m_monetarias'] = adjust_decimal_format(df['m_monetarias'])
    df['m_nomonetarias'] = adjust_decimal_format(df['m_monetarias'])
    df['Salario_final'] = adjust_decimal_format(df['Salario_final'])

    df['EDAD'] = df['EDAD'].apply(lambda x: int(x))

    preprocessor = pickle.load(open("./Models/preprocessor.pkl", "rb"))

    df = df[['EDAD', 'Salario_final', 'SCORE_CLEAR', 'MANTIENE_NOM', 'max_con',
       'tasa_ofertada', 'cliente digital', 'sum_op_digital', 'mean_importe',
       'm_consultas', 'm_monetarias', 'm_nomonetarias', 'CROSS_SELL', 'ACTIVO',
       'PASIVO', 'cross_sell_ahor']]

    X_transformed = preprocessor.transform(df)

    model_rf = pickle.load(open("./Models/model_rf.pkl", "rb"))

    # y_pred_proba = model_rf.predict_proba(X_transformed)
    y_probs = model_rf.predict_proba(X_transformed)[:, 1]
    y_pred_proba = (y_probs >= 0.3).astype(int)
    # y_pred_proba = y_pred_proba[0]

    return y_pred_proba