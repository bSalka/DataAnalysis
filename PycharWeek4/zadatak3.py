import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleep.csv")

print("="*50)
print("Females older than 30:")
print("="*50)
for index, row in df.iterrows():
    if row["Gender"] == "Female" and row["Age"]>30:
        print(row)

print("\n" + "=" *50)
print("People with stress level >7:")
print("="*50)
for index, row in df.iterrows():
    if row["Stress Level"]>7:
        print(row)

females_30_plus_rows = []
for index, row in df.iterrows():
    if row['Gender'] == 'Female' and row['Age'] > 30:
        females_30_plus_rows.append(row)

females_30_plus = pd.DataFrame(females_30_plus_rows)
avg_stress_30_plus = females_30_plus.groupby('Age')['Stress Level'].mean()

plt.figure(figsize=(10,6))
avg_stress_30_plus.plot(kind='bar', color='lightcoral')
plt.title('Prosječni Stress Level po godinama (žene starije od 30)')
plt.xlabel('Godine')
plt.ylabel('Prosječni Stress Level')
plt.axhline(7, color='blue', linestyle='--', label='Stress Level = 7')
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle='--', alpha=0.7)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()