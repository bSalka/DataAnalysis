import pandas as pd

izvjestaj =pd.read_csv("policijski_izvjestaj.csv")
osumnjiceni = pd.read_csv("osumnjiceni.csv")
kartice=pd.read_csv("pristupne_kartice.csv")
svjedoci=pd.read_csv("izjave_svjedoka.csv")
telefoni=pd.read_csv("telefonski_zapisi.csv")
finansije=pd.read_csv("finansijski_zapisi.csv")

print(f"Osumnjičenenih:{len(osumnjiceni)}")
print(f"Pristupnih zapisa :{len(kartice)}")
print("Telefonskih zapisa :{len(telefoni)}")
print("Finansijski zapisa :{len(finansije)}")

ubistvo=izvjestaj[izvjestaj["tip"]=="ubistvo"]
print(ubistvo[["datum", "vrijeme", "lokacija", "opis"]].to_string(index=False))

tech_hub_15=kartice[(kartice["zgrada"]=="Tech Hub")&
                    (kartice ["datum"]=="2026-03-15")]

u_zgradi=tech_hub_15.merge(osumnjiceni, on="ime_prezime")
print(f"Ukupno ulazaka: {len(tech_hub_15)}")
print(f"od toga osumnjičenih: {len(u_zgradi)}")
print(u_zgradi[["ime_prezime", "vrijeme_ulaza", "vrijeme_izlaza", "veza_sa_zrtvom"]].to_string(index=False))

tech_hub_sve=kartice[(kartice["zgrada"]=="Tech Hub")]
sve=tech_hub_sve.merge(osumnjiceni, on="ime_prezime")
print(sve.groupby("ime_prezime")["datum"].nunique().sort_values(ascending=False).to_string())

print(u_zgradi["ime_prezime"].value_counts().to_string())


#vrijeme ko je u hubu od 19i 30 do 20 30
kartice["vrijeme_ulaza"] = pd.to_datetime(kartice["vrijeme_ulaza"])
kartice["vrijeme_izlaza"] = pd.to_datetime(kartice["vrijeme_izlaza"])

# filtriraj interval
u_intervalu = kartice[
    (kartice["zgrada"] == "Tech Hub") &
    (kartice["datum"] == "2026-03-15") &
    (kartice["vrijeme_ulaza"].dt.time <= pd.to_datetime("20:30").time()) &
    (kartice["vrijeme_izlaza"].dt.time >= pd.to_datetime("19:30").time())
]

print(u_intervalu[["ime_prezime", "vrijeme_ulaza", "vrijeme_izlaza"]].to_string(index=False))


#izjave
# koliko izjava ukupno postoji
print(f"Ukupno izjava: {len(svjedoci)}")


# koje izjave spominju Emira Begovića
emir_izjave = svjedoci[
    svjedoci["opis"].str.contains("Emir Begović", case=False, na=False)
]
print("\nIzjave koje spominju Emira Begovića:")
print(emir_izjave.to_string(index=False))


#dino
# koje izjave spominju Dinu Delića
dino_izjave = svjedoci[
    svjedoci["svjedok"].str.contains("Dino Delić", case=False, na=False)
]

print("\nIzjave koje spominju Dinu Delića:")
print(dino_izjave.to_string(index=False))


# postoje li izjave koje ne spominju nikoga po imenu
nepoznati=svjedoci[svjedoci["spominje_osumnjicenog"].isna() |
                   (svjedoci)["spominje_osumnjicenog"] == ""]
print(nepoznati[["izjava_id", "vrijeme", "opis"]].to_string(index=False))

#osumnjiceni=pd.read_csv("osumnjiceni.csv")
visoki_crni = osumnjiceni[
    (osumnjiceni["visina_cm"] > 180) &
    (osumnjiceni["boja_kose"] == "crna")
]

print(visoki_crni[["ime_prezime", "visina_cm", "boja_kose"]].to_string(index=False))

sa_imenima=telefoni.merge(
    osumnjiceni[["ime_prezime", "telefon"]],
    left_on="telefon_pozivatelja",
    right_on="telefon", how="left")
sa_imenima=sa_imenima.rename(columns={"ime_prezime": "pozivatelj"})

sa_imenima=sa_imenima.merge(
    osumnjiceni[["ime_prezime", "telefon"]],
    left_on="telefon_primaoca",
    right_on="telefon", how="left",
suffixes=("", "primalaca"))
sa_imenima=sa_imenima.rename(columns={"ime_prezime": "primaoc"})

# emir_kasno=sa_imenima[
#     (sa_imenima["pozivatelj"]=="Emir Begović") &
# ]

print(finansije.groupby("ime_prezime")["iznos_KM"].sum())


























