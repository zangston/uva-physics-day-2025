import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_samples = 500
mean_height_in = 68  # 5'8"
std_dev = 3

# Generate normally distributed heights in inches
heights_in = np.random.normal(loc=mean_height_in, scale=std_dev, size=n_samples)

# Convert to feet and inches (keeping fractional inches)
def format_height(inches):
    feet = int(inches // 12)
    remaining_inches = round(inches % 12, 1)
    return f"{feet}'{remaining_inches}\""

# Create DataFrame
df = pd.DataFrame({
    'Height (in)': heights_in,
    'Height (ft & in)': [format_height(h) for h in heights_in]
})

# Save to CSV
df.to_csv('height_data.csv', index=False)

print("CSV generated: 'height_data.csv'")
