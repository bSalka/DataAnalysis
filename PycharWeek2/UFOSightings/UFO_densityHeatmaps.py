import pandas as pd
import plotly.express as px


from PycharWeek2.UFOSightings.ufo_worldMap import fig

df = pd.read_csv('ufo_sightings.csv')

df["latitude"] = pd.to_numeric(df["latitude"], errors='coerce')
df["longitude"] = pd.to_numeric(df["longitude"], errors='coerce')
df=df.dropna(subset=['latitude','longitude'])

fig=px.density_mapbox(df,
                       lat="latitude",
                       lon="longitude",
                       radius=5,
                       zoom=1,
                       mapbox_style="open-street-map",
                       title="UFO sightings Density Map")
fig.show()