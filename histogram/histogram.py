import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the height data
df = pd.read_csv('height_data.csv')

# Extract the height in inches
heights = df['Height (in)']

# Define bin settings
bin_configs = {
    '1 ft increments (12 in)': 12,
    '1/2 ft increments (6 in)': 6,
    '4 inch increments': 4,
    '1 inch increments': 1
}

# Plot histograms with varying bin sizes
for title, bin_width in bin_configs.items():
    min_height = np.floor(heights.min())
    max_height = np.ceil(heights.max())
    bins = np.arange(min_height, max_height + bin_width, bin_width)
    
    plt.figure(figsize=(8, 5))
    plt.hist(heights, bins=bins, color='lightgreen', edgecolor='black')
    plt.title(f'Histogram of Heights: {title}')
    plt.xlabel('Height (inches)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
