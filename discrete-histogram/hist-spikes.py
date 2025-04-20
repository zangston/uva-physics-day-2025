import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the bedroom data
df_bedrooms = pd.read_csv('bedroom_data.csv')

# Extract the number of bedrooms
bedroom_counts = df_bedrooms['Bedrooms']

# Bin edges with 0.5 increments for visible gaps
bin_edges = np.arange(min(bedroom_counts) - 0.5, max(bedroom_counts) + 1.5, 0.5)

# Create histogram with visible gaps
plt.figure(figsize=(8, 5))
plt.hist(bedroom_counts, bins=bin_edges, color='lightgreen', edgecolor='black')

# Count occurrences of each integer bedroom count
value_counts = bedroom_counts.value_counts().sort_index()

# Build x and y with zero in between real counts to show discrete spikes
x_spike = []
y_spike = []

for val, count in zip(value_counts.index, value_counts.values):
    # Insert a zero before and after the actual data point
    x_spike.extend([val - 0.5, val, val + 0.5])
    y_spike.extend([0, count, 0])

# Plot the spiky line
plt.plot(x_spike, y_spike, color='red', linewidth=2, label='Discrete Peaks')

# Labels and formatting
plt.title('Histogram of Bedrooms with Discrete Peaks')
plt.xlabel('Number of Bedrooms (with gaps)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
