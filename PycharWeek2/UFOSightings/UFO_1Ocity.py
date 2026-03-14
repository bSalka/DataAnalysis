import pandas as pd
import matplotlib.pyplot as plt
from fontTools.subset import subset

df=pd.read_csv("ufo_sightings.csv", low_memory=False)

df=df.dropna(subset=["city"])

city_counts=df["city"].value_counts()

top10_cities=city_counts.head(10)

print("Top 10 cities with most UFO Sightings")
print(top10_cities)

plt.figure(figsize=(10,10))
top10_cities.plot(kind="bar")

plt.title("Top 10 Cities with Most UFO Sightings")
plt.xlabel("City")
plt.ylabel("Number of UFO Sightings")
plt.show()