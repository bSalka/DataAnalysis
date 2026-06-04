import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


sns.set_theme(style="whitegrid")
df=sns.load_dataset("penguins")

print(df.head(10))
print(df.info())

#provjera nedostajucih podataka
print(df.isnull().sum())

print(f"Oblik skupa: {df.shape}")
print(df["species"].value_counts())
df=df.dropna()

#vjezba 2
# najteza=df.groupby("species")["body_mass_g"].mean()
# print(najteza.describe())
#
# #grupiranje po vrsti
# cols=["body_mass_g","bill_length_mm","bill_depth_mm","flipper_length_mm"]
# summary=df.groupby("species")[cols].agg(["mean","median","std"]).round(2)
# print(summary)
#
# cv=df.groupby("species")["body_mass_g"].agg(lambda x:(x.std()/x.mean()*100).round(2))
# print("KV (%):", cv)

#zadatak3
# sns.histplot(df["flipper_length_mm"],bins=20,kde=True)
# plt.show()
#
# #Mreza violinskih grafikona 2x2
# fig,axes= plt.subplots(2,2,figsize=(12,8))
# mjere=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]
#
# for ax,col in zip(axes.flat,mjere):
#     sns.violinplot(data=df, x="species", y=col, ax=ax)
#     ax.set_title(col.replace("_",""))
#
# plt.suptitle("Mjere pingivina po vrsti")
# plt.tight_layout()
# plt.show()

#vjezba4
# r,p=stats.pearsonr(df["flipper_length_mm"], df["body_mass_g"])
# print(f"r={r:.3f},p={p:.4f}")
#
# fig, ax = plt.subplots(figsize=(7,5))
# sns.regplot(data=df, x="flipper_length_mm", y="body_mass_g", ax=ax, scatter=False,color="gray")
# sns.scatterplot(data=df, x="flipper_length_mm",
# y="body_mass_g", hue="species", ax=ax)
#
# # Toplinska karta korelacija
# corr = df.corr(numeric_only=True)
#
# sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
#
# # Pair plot
# sns.pairplot(df, hue="species", diag_kind="kde")

#popravit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Pearsonova korelacija
# r, p = stats.pearsonr(
# df["flipper_length_mm"], df["body_mass_g"])
#
# print(f"r = {r:.3f}, p = {p:.4f}")
#
# # Scatter s regresijskim pravcem
# fig, ax = plt.subplots(figsize=(7, 5))
#
# sns.regplot(data=df, x="flipper_length_mm",
# y="body_mass_g", ax=ax, scatter=False, color="gray")
#
# sns.scatterplot(data=df, x="flipper_length_mm",
# y="body_mass_g", hue="species", ax=ax)
#
# # Toplinska karta korelacija
# corr = df.corr(numeric_only=True)
#
# sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
#
# # Pair plot
# sns.pairplot(df, hue="species", diag_kind="kde")


#zadatak5
adelie=df[df["species"]=="Adelie"]["flipper_length_mm"]
chinstrap=df[df["species"]=="Chinstrap"]["flipper_length_mm"]


#t-test
t,p=stats.ttest_ind(adelie,chinstrap)
print(f"t={t:3f},p={p:.4f}")

zajednicki=np.sqrt((adelie.std()**2+chinstrap.std()**2)/2)
d=(adelie.mean()-chinstrap.mean())/zajednicki
print(f"Cohenov d={d:3f}")

#stupičasti grafikon
sns.barplot(data=df,x="species",y="flipper_length_mm",capsize=0.1)
plt.title("Srednja duljina peraje po vrsti (95%)")
plt.show()