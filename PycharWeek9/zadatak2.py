import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")
#df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

# top10 = df["PrviZanr"].value_counts().head(10).index
# df_top10 = df[df["PrviZanr"].isin(top10)]
#
# plt.figure(figsize=(10, 6))
# sns.countplot(data=df_top10, y="PrviZanr",
#               order=top10, palette="viridis")
# plt.title("Top 10 žanrova — IMDB Top 1000")
# plt.xlabel("Broj filmova")
# plt.tight_layout()
# plt.show()

#zadatak2
top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]
#
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.boxplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
#             ax=ax, palette="Set2", order=top5_zanrovi)
# sns.stripplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
#               ax=ax, color="black", alpha=0.4, size=4,
#               order=top5_zanrovi)
# plt.title("IMDB ocjene po žanru — boxplot + strip")
# plt.tight_layout()
# plt.show()

#zadatak3
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decenija"] = (df["Released_Year"] // 10) * 10

pivot = pd.pivot_table(df_top5, values="IMDB_Rating",
                       index="Decenija", columns="PrviZanr",
                       aggfunc="mean")
pivot = pivot.loc[pivot.index >= 1950]

plt.figure(figsize=(10, 8))
sns.heatmap(pivot, annot=True, cmap="YlOrRd", fmt=".1f",
            linewidths=0.5)
plt.title("Prosječna IMDB ocjena — Decenija vs Žanr")
plt.tight_layout()
plt.show()