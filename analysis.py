"""
Aravali Forest Cover Analysis (Dynamic Version).
Author: Rishabh
Purpose: Automatic multi-year statistical analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ===============================
# 1️. Load Data
# ===============================

data_path = "data/aravali_forest_data.csv"
df = pd.read_csv(data_path)

print(" Data loaded successfully.")
print("Shape:", df.shape)

# ===============================
# 2️. Prepare Data
# ===============================

# Set district as index
df.set_index("District", inplace=True)

# Extract year columns dynamically
years = sorted([int(col) for col in df.columns])
print("\n Years detected:", years)

# Convert columns to numeric (safety)
df = df.apply(pd.to_numeric)

# ===============================
# 3️. Display Table
# ===============================

print("\n Forest % by district and year:")
print(df)

# ===============================
# 4️. Mean Comparison
# ===============================

first_year = years[0]
last_year = years[-1]

mean_first = df[str(first_year)].mean()
mean_last = df[str(last_year)].mean()

print(f"\n Mean forest % in {first_year}: {mean_first:.2f}%")
print(f" Mean forest % in {last_year}: {mean_last:.2f}%")
print(f" Change: {mean_last - mean_first:.2f}%")

# ===============================
# 5️. Paired T-Test
# ===============================

t_stat, p_value = stats.ttest_rel(df[str(first_year)], df[str(last_year)])

print(f"\n Paired t-test p-value: {p_value:.4f}")

if p_value < 0.05:
    print(" Statistically significant change detected.")
else:
    print(" No statistically significant change detected.")

# ===============================
# 6️. Effect Size (Cohen's d)
# ===============================

diff = df[str(last_year)] - df[str(first_year)]
cohen_d = diff.mean() / diff.std()

print(f" Cohen's d (effect size): {cohen_d:.2f}")

if abs(cohen_d) < 0.2:
    interpretation = "Small effect"
elif abs(cohen_d) < 0.5:
    interpretation = "Medium effect"
elif abs(cohen_d) < 0.8:
    interpretation = "Large effect"
else:
    interpretation = "Very large effect"

print(f"   {interpretation}")

# ===============================
# 7️. Plot Trends
# ===============================

plt.figure(figsize=(12,6))

for district in df.index:
    plt.plot(years, df.loc[district], marker='o', label=district)

plt.title("Forest Cover Trends in Aravali Districts")
plt.xlabel("Year")
plt.ylabel("Forest Cover (%)")

# Legend OUTSIDE the graph
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    fontsize=9
)

plt.grid(True)

# This makes space for legend
plt.tight_layout()
plt.show()