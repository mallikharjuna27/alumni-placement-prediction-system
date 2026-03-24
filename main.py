import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("placement_data.csv")

print("\n--- Dataset Preview ---")
print(data.head())

# Basic Analysis
print("\n--- Placement Count ---")
placement_count = data['Placed'].value_counts()
print(placement_count)

# Average CGPA of placed vs not placed
print("\n--- Average CGPA ---")
avg_cgpa = data.groupby('Placed')['CGPA'].mean()
print(avg_cgpa)

# Placement percentage
total_students = len(data)
placed_students = len(data[data['Placed'] == 'Yes'])
placement_percentage = (placed_students / total_students) * 100

print(f"\nPlacement Percentage: {placement_percentage:.2f}%")

# Visualization
placement_count.plot(kind='bar', title="Placement Distribution")
plt.xlabel("Placed")
plt.ylabel("Count")
plt.show()
