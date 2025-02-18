from fastapi import FastAPI
import joblib
import pandas as pd
import requests
from pydantic import BaseModel
import os

# ✅ Hugging Face Se Model Download (Best Solution)
model_url = "https://huggingface.co/aditi2722/creditriskmodel/resolve/main/random_forest_credit.pkl"
model_path = "random_forest_credit.pkl"

if not os.path.exists(model_path):  # ✅ Agar model nahi hai to download karo
    response = requests.get(model_url)
    with open(model_path, "wb") as f:
        f.write(response.content)

# ✅ Load trained model
model = joblib.load(model_path)

# ✅ FastAPI app instance
app = FastAPI(title="Credit Risk API", version="1.0")

# ✅ Define request schema (expected input format)
class CreditRiskInput(BaseModel):
    status_checking: float
    duration: float
    credit_history: float
    purpose: float
    credit_amount: float
    savings_account: float
    employment_since: float
    installment_rate: float
    personal_status: float
    other_debtors: float
    residence_since: float
    property: float
    age: float
    other_installment_plans: float
    housing: float
    existing_credits: float
    job: float
    liable_people: float
    telephone: float
    foreign_worker: float

# ✅ Root endpoint
@app.get("/")
def home():
    return {"message": "Credit Risk API is running 🚀"}

# ✅ Prediction endpoint
@app.post("/predict")
def predict_risk(data: CreditRiskInput):
    input_data = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
    prediction = model.predict(input_data)[0]  # Predict class
    return {"credit_risk": int(prediction)}



