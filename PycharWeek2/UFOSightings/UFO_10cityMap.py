import pandas as pd
import plotly.express as px
from fontTools.subset import subset

df=pd.read_csv("ufo_sightings.csv",low_memory=False)

df=df.dropna(subset=["city"])
df["latitude"]=pd.to_numeric(df["latitude"],errors="coerce")
df["longitude"]=pd.to_numeric(df["longitude"],errors="coerce")

df=df.dropna(subset=["latitude","longitude"])

city_counts=df["city"].value_counts()

top10_cities=city_counts.head(10)

top10_city_names=top10_cities.index
map_data=df[df["city"].isin(top10_city_names)]

fig=(px.scatter_geo(
    map_data,
    lat="latitude",
    lon="longitude",
    hover_data="city",
    projection="natural earth",
    title="Top 10 Cities with Most UFO Sightings",))

fig.show()