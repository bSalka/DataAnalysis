# import pandas as pd
#
# edges=pd.read_csv("network_edges.csv")
#
# print(edges.isnull().sum())
#
# edges_clean = edges.dropna(subset=["ring_id"])
# print(edges_clean.shape)
# print(edges_clean.head())
# print(edges_clean["shared_type"].value_counts())
#
# print(edges_clean["ring_id"].value_counts().head(5))


#2
import pandas as pd

df = pd.read_csv("network_edges.csv")

# duplikati = df.duplicated().sum()
# print("Broj potpuno identičnih redova:", duplikati)
#
# #3
# duplikati_shared = df["shared_type"].duplicated().sum()
# print("Broj duplikata u shared_type:", duplikati_shared)
#
# #4
# print("Broj jedinstvenih account_a:", df["account_a"].nunique())
# unique_accounts = df.drop_duplicates(subset=["account_a"])
#
# print(unique_accounts.head())

# Pitanje: Da li računi bez 2FA imaju veći fraud_rate?
# bez_2fa = df[df["has_2fa"] == 0]
# sa_2fa  = df[df["has_2fa"] == 1]
# print(f"Bez 2FA: {bez_2fa['fraud_rate'].mean():.4f}")
# print(f"Sa 2FA:  {sa_2fa['fraud_rate'].mean():.4f}")
#
# # Pitanje: Koji tip računa ima najviše prevaranta?
# print(df.groupby("account_type")["is_fraudster"].mean())
#
# # Pitanje: Koji tip prevare ima najveći prosječni iznos?
# print(df.sort_values("avg_amount", ascending=False)[["fraud_pattern", "avg_amount"]])