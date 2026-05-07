import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# sns.set_theme(style="whitegrid", palette="muted")

#UCITAVANJE PODATAKA
df = pd.read_csv("imdb_top_1000.csv")
#
# sns.scatterplot(data=df, x="IMDB_Rating", y="Meta_score", alpha=0.5)
# plt.title("IMDB Rating vs Metascore")
# plt.show()

#2 ZADATAK
# df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()
#
# top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
# df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]
#
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df_top5, x="IMDB_Rating", y="Meta_score",
#                 hue="PrviZanr", style="PrviZanr", alpha=0.7)
# plt.title("Rating vs Metascore — po žanru")
# plt.show()

# Primjer 3 — Distribucije: histplot i kdeplot
#
# fig, axes = plt.subplots(1, 3, figsize=(16, 5))
#
# sns.histplot(data=df, x="IMDB_Rating", bins=20, ax=axes[0],
#              color="steelblue")
# axes[0].set_title("Histogram")
#
# sns.kdeplot(data=df, x="IMDB_Rating", ax=axes[1],
#             color="coral", fill=True)
# axes[1].set_title("KDE plot")
#
# sns.histplot(data=df, x="IMDB_Rating", bins=20, ax=axes[2],
#              kde=True, color="teal")
# axes[2].set_title("Histogram + KDE")
#
# plt.tight_layout()
# plt.show()

# Primjer 4 — Distribucije po kategoriji
# ---------------------------------------------------------------
# top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
#
# plt.figure(figsize=(10, 5))
# sns.histplot(data=df_top5, x="IMDB_Rating", hue="PrviZanr",
#              bins=15, alpha=0.5)
# plt.title("Distribucija ocjena po žanru")
# plt.show()
#
# plt.figure(figsize=(10, 5))
# sns.kdeplot(data=df_top5, x="IMDB_Rating", hue="PrviZanr",
#             fill=True, alpha=0.4)
# plt.title("KDE po žanru")
# plt.show()

# zadazak5
# top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
#
# fig, axes = plt.subplots(1, 2, figsize=(14, 5))
#
# sns.boxplot(data=df, x="PrviZanr", y="IMDB_Rating",
#             ax=axes[0], palette="Set2")
# axes[0].set_title("Boxplot — Ocjene po žanru")
#
# sns.violinplot(data=df, x="PrviZanr", y="IMDB_Rating",
#                ax=axes[1], palette="Set2")
# axes[1].set_title("Violinplot — Ocjene po žanru")
#
# plt.tight_layout()
# plt.show()

#zadatak6
#num_cols = ["IMDB_Rating", "Meta_score", "No_of_Votes", "Runtime"]
# df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(float)
#
 #korelacija = df[num_cols].corr()
#
# plt.figure(figsize=(8, 6))
# sns.heatmap(korelacija, annot=True, cmap="coolwarm",
#             center=0, fmt=".2f", linewidths=1)
# plt.title("Korelacijska matrica — IMDB dataset")
# plt.tight_layout()
# plt.show()

#zadatak7
# sns.pairplot(df[num_cols + ["PrviZanr"]].dropna(),
#              hue="PrviZanr", palette="Set2",
#              plot_kws={"alpha": 0.5, "s": 20})
# plt.suptitle("Pairplot — IMDB Top 1000", y=1.02)
# plt.show()

#zadatak8
# top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
# df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]
# plt.figure(figsize=(10, 5))
# sns.barplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
#             palette="viridis", errorbar=("ci", 95))
# plt.title("Prosječna ocjena po žanru (s intervalom povjerenja)")
# plt.ylabel("Prosječna IMDB ocjena")
# plt.show()

