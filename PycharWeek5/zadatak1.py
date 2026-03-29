import pandas as pd
df=pd.read_csv("imdb_top_1000.csv")

print(df.shape)
print(df.columns)
print(df.head())

print(df.info())
print(df.describe())