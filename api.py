from fastapi import FastAPI
import joblib
import pandas as pd
import requests
from pydantic import BaseModel
from io import BytesIO

# ✅ Hugging Face Se Model Direct Memory Me Load Karo
model_url = "https://huggingface.co/Aditi30102004/credit-risk-model/resolve/main/random_forest_credit.pkl"
response = requests.get(model_url)
model = joblib.load(BytesIO(response.content))  # ✅ Directly Load Model

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
