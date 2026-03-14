import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("ufo_sightings.csv", low_memory=False)

df["dateTime"] = pd.to_datetime(df["datetime"], errors="coerce")

df["year"] = df["dateTime"].dt.year

year_counts=df["year"].value_counts().sort_index()

plt.figure()
year_counts.plot()
plt.title("UFO Sightings per Year")
plt.xlabel("Year")
plt.ylabel("Number of Sightings")
plt.show()