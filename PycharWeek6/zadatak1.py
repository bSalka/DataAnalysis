import pandas as pd

# primjer 4a replace()
# fp=pd.read_csv("fraud_patterns.csv")
# print(fp[["fraud_pattern", "transaction_count"]])
#
# fp["fraud_pattern"]=fp["fraud_pattern"].replace({
#     "card_not_present": "CPN prevara",
#     "account_takeover": "Preuzimanje računa",
#     "card_present_stolen": "Ukradena kartica",
#     "friendly_fraud": "Lažna reklamacija",
#     "atm_fraud": "ATM prevara",
#     "money_laundering": "Pranje novca",
#     "identity_theft": "Krađa identiteta",
# })
#
# print(fp[["fraud_pattern", "transaction_count"]])

#2primjer- 4b map()
df = pd.read_csv("account_profiles.csv")

tip_prevod = {
    "personal": "Lični",
    "business": "Poslovni",
    "premium": "Premium",
}

df["tip_racuna"] = df["account_type"].map(tip_prevod)
print(df[["account_id", "account_type", "tip_racuna"]].head())

#1koliko racuna ima fraud_count>0
#2kakav je prosječan risk_score prevaranata vs.neprevaranata
#3koliki procenat prevaranata nema 2FA (has_2fa==0)

#1
broj_fraud = df[df["fraud_count"] > 0].shape[0]
print("broj frauda",broj_fraud)

#2
prevaranti = df[df["fraud_count"] > 0]["risk_score"].mean()
neprevaranti = df[df["fraud_count"] == 0]["risk_score"].mean()

print("Prosječan risk_score (prevaranti):", prevaranti)
print("Prosječan risk_score (neprevaranti):", neprevaranti)

#3
prevaranti = df[df["fraud_count"] > 0]

bez_2fa = prevaranti[prevaranti["has_2fa"] == 0]

procenat = (bez_2fa.shape[0] / prevaranti.shape[0]) * 100

print("Procenat prevaranata bez 2FA:", procenat)

