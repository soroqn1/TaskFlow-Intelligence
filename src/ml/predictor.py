import joblib
import os

MODEL_PATH = "data/model.joblib"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully")
else:
    model = None
    print("Model not found")

def predict_priority(description: str) -> str:
    if model is None:
        return "Model not found. Please train the model first."
    prediction = model.predict([description])[0]
    return prediction