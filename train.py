import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ✅ Load dataset
df = pd.read_csv("germancredit.csv", delimiter=",")

# ✅ Assign column names
df.columns = ["status_checking", "duration", "credit_history", "purpose", "credit_amount",
              "savings_account", "employment_since", "installment_rate", "personal_status",
              "other_debtors", "residence_since", "property", "age", "other_installment_plans",
              "housing", "existing_credits", "job", "liable_people", "telephone",
              "foreign_worker", "target"]

# ✅ Features & Target split
X = df.drop(columns=["target"])
y = df["target"]

# ✅ Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Normalize numerical columns
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("✅ Data Preprocessing Done!")
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ✅ Train Logistic Regression Model
model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Model Performance
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n✅ Classification Report:\n", classification_report(y_test, y_pred))
print("\n✅ Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Model Performance
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n✅ Classification Report:\n", classification_report(y_test, y_pred))
print("\n✅ Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

