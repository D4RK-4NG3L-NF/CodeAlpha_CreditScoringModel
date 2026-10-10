
import pandas as pd

data = {
    "income": [30000, 50000, 70000, 25000, 90000],
    "debt": [10000, 15000, 20000, 18000, 10000],
    "payment_history": [1, 1, 1, 0, 1],
    "credit_history_years": [1, 3, 5, 2, 7],
    "creditworthy": [1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("credit_data.csv", index=False)
print("Data saved Succesfully!")
print("\nLoading the saved dataset...")
df = pd.read_csv("credit_data.csv")
print(df.head())