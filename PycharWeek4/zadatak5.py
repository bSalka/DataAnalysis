import pandas as pd
import matplotlib.pyplot as plt
from PIL.ImageChops import difference

df = pd.read_csv("sleep.csv")

high_stress = df[df["Stress Level"] > 7]
avg_sleep_high = high_stress["Sleep Duration"].mean()
print(f"High stress (>7)-Avarage sleep:{avg_sleep_high:.2f} hours")

low_stress = df[df["Stress Level"] <= 3]
avg_sleep_low = low_stress["Sleep Duration"].mean()
print(f"Low stress (>7)-Avarage sleep:{avg_sleep_low:.2f} hours")

difference=avg_sleep_low-avg_sleep_high
print(f"Difference: {difference:.2f} hours")


categories = ['High Stress (>7)', 'Low Stress (<=3)']
avg_sleep = [avg_sleep_high, avg_sleep_low]
colors = ['red', 'blue']

plt.figure(figsize=(8,6))
plt.bar(categories, avg_sleep, color=colors, edgecolor='black',linewidth=2)
plt.ylabel('Prosječna dužina sna (h)', fontsize=12)
plt.title('Utjecaj stresa na prosječnu dužinu sna', fontsize=14, fontweight='bold')
plt.ylim(0,max(avg_sleep)+2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(avg_sleep):
    plt.text(i, v + 0.1, f'{v:.2f}h', ha='center', fontweight='bold')
plt.show()

