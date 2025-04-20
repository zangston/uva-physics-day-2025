import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the bedroom data
df_bedrooms = pd.read_csv('bedroom_data.csv')

# Number of bedrooms data
bedroom_counts = df_bedrooms['Bedrooms']

# 1. Initial histogram: no space between bars (quantized data, discrete peaks)
plt.figure(figsize=(8, 5))
plt.hist(bedroom_counts, bins=np.arange(min(bedroom_counts), max(bedroom_counts) + 1, 1), color='lightblue', edgecolor='black')
plt.title('Histogram of Number of Bedrooms (No Space Between Bars)')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2. Modified histogram: space between bars (x-axis in increments of 0.5)
# Create bins with a 0.5 increment for artificial gaps
bin_edges = np.arange(min(bedroom_counts) - 0.5, max(bedroom_counts) + 1.5, 0.5)

plt.figure(figsize=(8, 5))
plt.hist(bedroom_counts, bins=bin_edges, color='lightgreen', edgecolor='black')
plt.title('Histogram of Number of Bedrooms (With Gaps Between Bars)')
plt.xlabel('Number of Bedrooms (with gaps)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
