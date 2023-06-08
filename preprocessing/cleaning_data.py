import pandas as pd

def preprocess(data_input: dict):
    data = pd.DataFrame([data_input.dict()])
    data = data.replace({"Yes": 1, "No": 0})
    return data