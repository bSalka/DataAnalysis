import pandas as pd

#1. primjer
# df=pd.read_csv("account_profiles.csv")
#
# print(df.shape)
# print(df.columns)
# print(df.head())
# print(df.info())

#2 primjer
# edges=pd.read_csv("network_edges.csv")
# print(edges.shape)
# print(edges.head())
# print(edges.isnull().sum())

#3 primjer dropna()
edges=pd.read_csv("network_edges.csv")
edges_clean=edges.dropna()
print(edges_clean.shape)
edges_rings=edges.dropna(subset=["ring_id"])
print(edges_rings.shape)

#4 primjer- analiza nakon dropna
print(edges_rings["ring_id"].nunique())
print(edges_rings["ring_id"].value_counts().head(5))
print(edges_rings["shared_type"].value_counts())


#5 primjer fillna()
edges_filled=edges.fillna({"ring_id": "NEPOZNAT"})
print(edges_filled["ring_id"].value_counts().head(5))









