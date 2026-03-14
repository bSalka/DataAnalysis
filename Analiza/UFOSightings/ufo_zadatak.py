import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ufo_sightings.csv", low_memory=False)

top_states = df["state"].value_counts().head(5).index

filtered = df[df["state"].isin(top_states)]

state_shape = filtered.groupby(["state", "shape"]).size().unstack()

state_shape.plot(kind="bar", stacked=True, figsize=(10,6))

plt.title("UFO Shapes by State")
plt.xlabel("State")
plt.ylabel("Number of Sightings")
plt.legend(title="Shape")
plt.show()