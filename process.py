import pandas as pd  
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset (comma-separated)
df = pd.read_csv("germancredit.csv", delimiter=",")

# Assign proper column names
df.columns = ["status_checking", "duration", "credit_history", "purpose", "credit_amount",
              "savings_account", "employment_since", "installment_rate", "personal_status",
              "other_debtors", "residence_since", "property", "age", "other_installment_plans",
              "housing", "existing_credits", "job", "liable_people", "telephone",
              "foreign_worker", "target"]

# ✅ Encode categorical columns
categorical_cols = ["status_checking", "credit_history", "purpose", "savings_account",
                    "employment_since", "personal_status", "other_debtors", "property",
                    "other_installment_plans", "housing", "job", "telephone", "foreign_worker"]

encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

# ✅ Normalize numerical columns
numerical_cols = ["duration", "credit_amount", "installment_rate", "residence_since",
                  "age", "existing_credits", "liable_people"]

scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# ✅ Check if everything looks good
print(df.head())
print(df.info())
