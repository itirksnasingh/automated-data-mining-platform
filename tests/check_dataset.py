import pandas as pd

df = pd.read_csv("data/raw/Online Retail.csv", encoding="utf-8")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())