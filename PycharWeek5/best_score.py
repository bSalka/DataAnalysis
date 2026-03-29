import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

drame = df[df["Genre"].str.contains("Drama")]
print(f"Broj drama: {len(drame)} od {len(df)}")

top_drame = drame.sort_values("IMDB_Rating", ascending=False).head(10)

print(top_drame[["Series_Title", "Released_Year", "IMDB_Rating"]])