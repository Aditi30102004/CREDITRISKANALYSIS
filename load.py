import pandas as pd  

# Load dataset
df = pd.read_csv("germancredit.csv", delimiter=" ", header=None)

# Display first few rows
print(df.head())
print(df.info())  # Check column types
print(df.describe())  # Summary statistics
