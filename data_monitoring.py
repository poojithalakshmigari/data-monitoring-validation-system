 import pandas as pd

data = pd.read_csv("dataset.csv")

print("Total records:", len(data))

missing_values = data.isnull().sum()
print("Missing values:")
print(missing_values)

duplicates = data.duplicated().sum()
print("Duplicate records:", duplicates)

print("Data monitoring completed")
