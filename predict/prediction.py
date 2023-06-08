import joblib
from preprocessing.cleaning_data import preprocess

lr_from_joblib = joblib.load('My_model.pkl')
encod = joblib.load("Encoded.pkl")

def predict(data_input: dict):
    df = preprocess(data_input)
    data_encoded = encod.transform(df)
    prediction = lr_from_joblib.predict(data_encoded)
    return round(prediction[0], 2)