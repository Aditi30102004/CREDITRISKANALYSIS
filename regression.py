import pandas as pd

# ✅ Load dataset
df = pd.read_csv("germancredit.csv", delimiter=",")

# ✅ Assign column names (agar required ho)
df.columns = ["status_checking", "duration", "credit_history", "purpose", "credit_amount",
              "savings_account", "employment_since", "installment_rate", "personal_status",
              "other_debtors", "residence_since", "property", "age", "other_installment_plans",
              "housing", "existing_credits", "job", "liable_people", "telephone",
              "foreign_worker", "target"]
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ✅ Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Model Performance
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n✅ Classification Report:\n", classification_report(y_test, y_pred))
print("\n✅ Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
