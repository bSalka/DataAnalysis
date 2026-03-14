import pandas as pd

from matplotlib import pyplot as plt

df =pd.read_csv("ufo_sightings.csv", low_memory=False)

# pretvori datum
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

# napravi hour kolonu
df["hour"] = df["datetime"].dt.hour

# broj viđenja po satu
hour_counts = df["hour"].value_counts().sort_index()

hour_counts.plot(kind="bar")

plt.title("UFO Sightings by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Sightings")

plt.show()