import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the height data
df = pd.read_csv('height_data.csv')

# Extract the height in inches
heights = df['Height (in)']

# Define bin settings for 1 inch increments
bin_width = 1
min_height = np.floor(heights.min())
max_height = np.ceil(heights.max())
bins = np.arange(min_height, max_height + bin_width, bin_width)

# Plot histogram with 1-inch bins
plt.figure(figsize=(8, 5))
plt.hist(heights, bins=bins, color='lightgreen', edgecolor='black', density=True)

# Overlay a kernel density estimate (smooth line on top)
sns.kdeplot(heights, color='blue', linewidth=2)

# Customize plot
plt.title('Histogram of Heights with KDE Curve')
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
