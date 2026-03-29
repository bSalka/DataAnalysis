import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

top_directors = df["Director"].value_counts().head(10)

print(top_directors)

print("\nProsječna ocjena filmova koje je režirao Christopher Nolan:")
nolan=df[df["Director"]=="Christopher Nolan"]
print(nolan["IMDB_Rating"].mean())