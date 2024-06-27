import pandas as pd
import pickle

def run(X_pre: pd.Series):

    preprocessor = pickle.load(open("./Models/preprocessor.pkl", "rb"))

    X_transformed = preprocessor.transform(X_pre)

    model_rf = pickle.load(open("./Models/model_rf.pkl", "rb"))

    # y_pred_proba = model_rf.predict_proba(X_transformed)
    y_probs = model_rf.predict_proba(X_transformed)[:, 1]
    y_pred_proba = (y_probs >= 0.3).astype(int)
    y_pred_proba = y_pred_proba[0]

    return y_pred_proba