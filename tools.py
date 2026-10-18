import pandas as pd
from langchain.tools import tool
import pickle

@tool
def kyphosis_predict(age:int, number:int, start:int)->int:
    """Tool used for predicting whether kyphosis is absent or present in a patient.
    age: Age of the patient.
    number: Number of vertebrae involved in the operation.
    start: number of the first vertebra operated on.
    """
    preprocessor = pickle.load(open("preprocessing.pkl","rb"))
    model = pickle.load(open("model.pkl", "rb"))

    patient = pd.DataFrame({"Age":[age], "Number":[number], "Start":[start]})
    patient[["Age"]] = preprocessor["age_scaler"].transform(patient[["Age"]])
    prediction = model.predict(patient)
    return "Kyphosis Prediction: " + preprocessor["label_encoder"].inverse_transform(prediction) 