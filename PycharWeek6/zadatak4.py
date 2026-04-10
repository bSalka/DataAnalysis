import pandas as pd
from pandas.conftest import ascending

df = pd.read_csv("account_profiles.csv")

# df["rizik_kategorija"] = df["risk_score"].apply(
#     lambda x: "Visok" if x > 50 else ("Srednji" if x > 25 else "Nizak")
# )
#
# print(df[["risk_score", "rizik_kategorija"]].head())


#2
# bez_2fa = df[df["has_2fa"] == 0]["fraud_rate"].mean()
# sa_2fa = df[df["has_2fa"] == 1]["fraud_rate"].mean()
#
# print("Prosječan fraud_rate bez 2FA:", bez_2fa)
# print("Prosječan fraud_rate sa 2FA:", sa_2fa)
#
# #3
# print(df.groupby("account_type")["is_fraudster"].mean())
#
# print(df.sort_values("avg_amount",ascending=False)[["fraud_pattern", "avg_amount"]])

