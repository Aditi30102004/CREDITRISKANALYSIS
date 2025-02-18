import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import TomekLinks
from sklearn.metrics import roc_auc_score, precision_recall_curve, auc

# ✅ Load dataset with no header
df = pd.read_csv("C:/Users/Aditi/Downloads/germancredit.csv", header=None)

# ✅ Assign column names manually
df.columns = ["status_checking", "duration", "credit_history", "purpose", "credit_amount",
              "savings_account", "employment_since", "installment_rate", "personal_status",
              "other_debtors", "residence_since", "property", "age", "other_installment_plans",
              "housing", "existing_credits", "job", "liable_people", "telephone",
              "foreign_worker", "target"]

# ✅ Features & Target split
X = df.drop(columns=["target"])
y = df["target"]

# ✅ Train-Test Split (Stratified)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Apply SMOTE + Tomek Links for better balance
smote = SMOTE(random_state=42)
tomek = TomekLinks()
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
X_resampled, y_resampled = tomek.fit_resample(X_resampled, y_resampled)  # Under-sampling step

# ✅ Train Random Forest Classifier (Tweaked)
model = RandomForestClassifier(
    n_estimators=300,              
    max_depth=25,                  
    min_samples_split=3,           
    min_samples_leaf=2,            
    class_weight={1: 1, 2: 4},  # More weight to minority class
    random_state=42
)
model.fit(X_resampled, y_resampled)

# ✅ Get Probability Scores
y_scores = model.predict_proba(X_test)[:, 1]

# ✅ Optimize Threshold using Precision-Recall Curve
precision, recall, thresholds = precision_recall_curve(np.where(y_test == 2, 1, 0), y_scores)
optimal_idx = np.argmax(2 * (precision * recall) / (precision + recall + 1e-10))  # F1-score max
optimal_threshold = thresholds[optimal_idx]

# ✅ Apply New Threshold
y_pred = (y_scores >= optimal_threshold).astype(int)
y_pred = np.where(y_pred == 1, 2, 1)  # Convert back to original labels

# ✅ Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy:.3f}\n")

print("✅ Classification Report:")
print(classification_report(y_test, y_pred))

print("✅ Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ✅ Compute AUC-PR and AUC-ROC Scores
auc_score = auc(recall, precision)
roc_score = roc_auc_score(np.where(y_test == 2, 1, 0), y_scores)

print(f"✅ AUC-PR Score: {auc_score:.3f}")
print(f"✅ AUC-ROC Score: {roc_score:.3f}")


import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Feature Importance Plot
feature_importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_names, hue=feature_names, palette="viridis", legend=False)
plt.xlabel("Feature Importance")
plt.ylabel("Feature Names")
plt.title("Feature Importance in Random Forest")
plt.show()


import joblib
joblib.dump(model, "random_forest_credit.pkl")

model = joblib.load("random_forest_credit.pkl")
