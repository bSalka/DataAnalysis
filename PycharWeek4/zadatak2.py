import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleep.csv")

avg_sleep_by_age = df.groupby('Age')['Sleep Duration'].mean()

avg_quality_by_stress=df.groupby("Stress Level")["Quality of Sleep"].mean()

fig,axes=plt.subplots(1,2, figsize=(16, 6))

#Age vs Sleep duration
axes[0].bar(avg_sleep_by_age.index, avg_sleep_by_age.values, color='blue')
axes[0].set_title('Prosječna dužina sna po godinama', fontsize=14)
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Sleep Duration (hours)')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].tick_params(axis='x')

#Stress level vs Quality of sleep
axes[1].bar(avg_quality_by_stress.index, avg_quality_by_stress.values, color='blue')
axes[1].set_title('Kvaliteta sna po nivou stresa', fontsize=14)
axes[1].set_xlabel('Stress Level')
axes[1].set_ylabel('Quality of Sleep')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)
axes[1].tick_params(axis='x')

plt.tight_layout()
plt.show()