import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleep.csv")

avg_sleep_by_age = df.groupby('Age')['Sleep Duration'].mean()

plt.figure(figsize=(10,6))
avg_sleep_by_age.plot(kind='bar', color='skyblue')
plt.title('Prosječna dužina sna po godinama')
plt.xlabel('Godine')
plt.ylabel('Sleep Duration (hours)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()