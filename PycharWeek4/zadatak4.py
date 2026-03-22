import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleep.csv")

min_sleep_index = df['Sleep Duration'].idxmin()
min_sleep_person = df.loc[min_sleep_index]
print("Osoba koja najmanje spava:")
print(min_sleep_person)

max_sleep_index = df['Sleep Duration'].idxmax()
max_sleep_person = df.loc[max_sleep_index]
print("Osoba koja najviše spava:")
print(max_sleep_person)

max_heart_index = df['Heart Rate'].idxmax()
max_heart_person = df.loc[max_heart_index]
print("Osoba sa najvišim heart rate :")
print(max_heart_person)

min_steps_index = df['Daily Steps'].idxmin()
min_steps_person = df.loc[min_steps_index]
print("Osoba sa najmanjim daily steps :")
print(min_steps_person)

names=[f"Min Sleep\nID{min_sleep_person["Person ID"]}",
       f"Max Sleep\nID{max_sleep_person["Person ID"]}",
       f"Max Heart Rate\nID{max_heart_person["Person ID"]}",
       f"Min Steps\nID{min_steps_person["Person ID"]}",]

sleep_values = [min_sleep_person['Sleep Duration'], max_sleep_person['Sleep Duration'], 0, 0]
heart_values = [min_sleep_person['Heart Rate'], max_sleep_person['Heart Rate'], max_heart_person['Heart Rate'], 0]
steps_values = [0, 0, 0, min_steps_person['Daily Steps']]

x=range(len(names))

plt.figure(figsize=(12,6))
plt.bar(x, sleep_values, label="Sleep Duration (h)", color="blue")
plt.bar(x, heart_values, label="Heart Rate (bpm)", color="red")
plt.bar(x, steps_values, label="Daily Steps", color="green")
plt.xticks(x, names)
plt.ylabel("Vrijednosti")
plt.title("Ekstremne vrijednosti u podacima")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
