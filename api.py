from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # ✅ Import CORS Middleware

# ✅ Load the model correctly
model_path = "random_forest_credit.pkl"  
try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"❌ Model loading failed: {e}")

# ✅ FastAPI App
app = FastAPI(title="Credit Risk API", version="1.0")

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change to frontend URL if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Define Input Schema
class CreditRiskInput(BaseModel):
    status_checking: int
    duration: int
    credit_history: int
    purpose: int
    credit_amount: int
    savings_account: int
    employment_since: int
    installment_rate: int
    personal_status: int
    other_debtors: int
    residence_since: int
    property: int
    age: int
    other_installment_plans: int
    housing: int
    existing_credits: int
    job: int
    liable_people: int
    telephone: int
    foreign_worker: int

# ✅ Root API Check
@app.get("/")
def home():
    return {"message": "Credit Risk API is running 🚀"}

# ✅ Loan Prediction API
@app.post("/predict")
def predict_risk(data: CreditRiskInput):
    try:
        input_data = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
        print("Received Data:", input_data)  # Debugging print

        # ✅ Make Prediction
        prediction = model.predict(input_data)[0]  # Get the predicted class
        print("Prediction Output:", prediction)  # Debugging print

        # ✅ Return Response
        return {"credit_risk": "✅ Loan Approved!" if prediction == 1 else "❌ Loan Rejected!"}
    
    except Exception as e:
        print("❌ Prediction Error:", str(e))  # Print error details
        return {"error": "Prediction failed"}
