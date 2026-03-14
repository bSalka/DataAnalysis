import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure

# Load dataset
df = pd.read_csv("ufo_sightings.csv", low_memory=False)
# Clean coordinates
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])
# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
# Extract year
df["year"] = df["datetime"].dt.year
# Optional: reduce dataset for smoother animation
df = df.sample(15000)
fig= px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    animation_frame="year",
    projection="orthographic",
    color_discrete_sequence=["cyan"])

fig.update_layout(
        title="UFO signal activity over time",
        template="plotly_dark",
        geo=dict(
        showland=True,
        landcolor="rgb(40,40,40)",
        showcountries=True,
        showocean=True,
        oceancolor="rgb(10,10,30)",
        bgcolor="black",
        )
    )

fig.show()