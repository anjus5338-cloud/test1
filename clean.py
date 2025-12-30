import pandas as pd

df = pd.read_csv("clean_data.csv")
df.fillna(df.mean(numeric_only=True),inplace=True)
print(df.isnull().sum())



