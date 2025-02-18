import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns  

# ✅ Load dataset
df = pd.read_csv("germancredit.csv", delimiter=",")

# ✅ Assign column names
df.columns = ["status_checking", "duration", "credit_history", "purpose", "credit_amount",
              "savings_account", "employment_since", "installment_rate", "personal_status",
              "other_debtors", "residence_since", "property", "age", "other_installment_plans",
              "housing", "existing_credits", "job", "liable_people", "telephone",
              "foreign_worker", "target"]

# ✅ Plot Correlation Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
