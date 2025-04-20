import numpy as np
import pandas as pd

# Seed for reproducibility
np.random.seed(42)

# Custom bedroom distribution probabilities
# Bedrooms:     1    2    3     4     5     6     7
# Probabilities: 5%  25%  40%   20%   7%    2%    1%
bedroom_options = [1, 2, 3, 4, 5, 6, 7]
probabilities = [0.05, 0.25, 0.4, 0.2, 0.07, 0.02, 0.01]

# Generate bedroom counts for 500 houses
bedroom_counts = np.random.choice(bedroom_options, size=500, p=probabilities)

# Create DataFrame
df_bedrooms = pd.DataFrame({'Bedrooms': bedroom_counts})

# Save to CSV
df_bedrooms.to_csv('bedroom_data.csv', index=False)

print("Generated 'bedroom_data.csv' with 500 entries.")
