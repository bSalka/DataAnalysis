import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

all_actors = pd.concat([
    df["Star1"],
    df["Star2"],
    df["Star3"],
    df["Star4"]
])

top_actor = all_actors.value_counts()

print("Glumac koji se najviše pojavljuje:")
print(top_actor.head(1))

all_stars=pd.concat([df["Star1"], df["Star2"], df["Star3"],df["Star4"]] )

print(all_stars.value_counts().head(10))