import pandas as pd
import matplotlib.pyplot as plt


fp = pd.read_csv("fraud_patterns.csv")
# fp_sorted = fp.sort_values("fraud_share_pct", ascending=True)
#
# plt.barh(fp_sorted["fraud_pattern"], fp_sorted["fraud_share_pct"],
#          color="crimson")
# plt.title("Udio svake vrste prevare (%)")
# plt.xlabel("Procenat (%)")
# plt.tight_layout()
# plt.show()

#scatter plot
 # 50,000 tačaka je previše — uzimamo uzorak
# sample = df.sample(5000, random_state=42)
#
# plt.scatter(sample["risk_score"], sample["fraud_rate"],
#             alpha=0.3, s=10, color="steelblue")
# plt.title("Risk Score vs Fraud Rate")
# plt.xlabel("Risk Score")
# plt.ylabel("Fraud Rate")
# plt.tight_layout()
# plt.show()

# bpnus- rename
df_bs = fp.rename(columns={
    "account_type":  "tip_racuna",
    "risk_score":    "ocjena_rizika",
    "fraud_count":   "broj_prevara",
    "is_fraudster":  "je_prevarant"
})
print(df_bs.columns)