import pandas as pd
from langchain.tools import tool
from rag import search
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

@tool
def search_private_documents(query: str) -> str:
    """Use this tool to search through the user's private documents, PDFs, text files, and images.
    Always use this tool if the user asks a question about their files, documents, or data.
    Input should be a clear search query."""

    try:
        #RETRIEVAL
        # Call the search function from rag.py
        results = search(query, k=4)

        if not results:
            return "No relevant information found in the documents."

        #AUGMENTATION
        # Format the retrieved chunks into a single string for the LLM to read
        formatted_results = []
        for i, doc in enumerate(results):
            source = doc.metadata.get("source", "Unknown file")
            content = doc.page_content
            formatted_results.append(f"--- Document {i+1} (Source: {source}) ---\n{content}")

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"An error occurred while searching the documents: {str(e)}"