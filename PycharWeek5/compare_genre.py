import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

drame = df[df["Genre"].str.contains("Drama")]
akcije=df[df["Genre"].str.contains("Action")]

print(f"Broj drama: {len(drame)} od {len(df)}")
print(f"Broj akcija: {len(akcije)} od {len(df)}")

top_drame = drame.sort_values("IMDB_Rating", ascending=False).head(10)
print("\nTop 10 drama:")
print(top_drame[["Series_Title", "Released_Year", "IMDB_Rating"]])

top_akcije = akcije.sort_values("IMDB_Rating", ascending=False).head(10)
print("\nTop 10 akcija:")
print(top_akcije[["Series_Title", "Released_Year", "IMDB_Rating"]])