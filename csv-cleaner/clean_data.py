import pandas as pd

df = pd.read_csv('messy.csv')

df.columns = df.columns.str.strip().str.lower()

df = df.drop_duplicates()

df['amount'] = pd.to_numeric(df['amount'], errors="coerce")
df = df.dropna(subset=["amount"])

df["date"] = pd.to_datetime(df["date"], errors="coerce", format="mixed")
df["date"] = df["date"].dt.strftime("%Y-%m-%d")

df.to_csv("clean.csv", index=False)
print(df.head())