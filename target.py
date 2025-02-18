import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  

# ✅ Load dataset
df = pd.read_csv("germancredit.csv", delimiter=",")

# ✅ Assign proper column names
df.columns = ["status_checking", "duration", "credit_history", "purpose", "credit_amount",
              "savings_account", "employment_since", "installment_rate", "personal_status",
              "other_debtors", "residence_since", "property", "age", "other_installment_plans",
              "housing", "existing_credits", "job", "liable_people", "telephone",
              "foreign_worker", "target"]

# ✅ Now run the seaborn plot
plt.figure(figsize=(6, 4))
sns.countplot(x=df["target"], palette="viridis")
plt.title("Target Variable Distribution")
plt.xlabel("Credit Risk (1 = Good, 2 = Bad)")
plt.ylabel("Count")
plt.show()
