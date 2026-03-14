import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("ufo_sightings.csv", low_memory=False)
top_countries = df["country"].value_counts().head(5).index

filtered=df[df["country"].isin(top_countries)]

country_shape=filtered.groupby(["country", "shape"]).size().unstack()

country_shape.plot(kind="bar",stacked=True, figsize=(10,7))

plt.title("UFO Shapes by Coutry")
plt.xlabel("country")
plt.ylabel("Number of Sightings")
plt.legend(title="Shape",bbox_to_anchor=(1,1.2), loc="upper left")
plt.tight_layout(rect=[0, 0, 0.85, 1])


plt.show()