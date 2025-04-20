import pandas as pd
import matplotlib.pyplot as plt
import random

# Load the data
data = pd.DataFrame({
    'Brand': ['Nike', 'Adidas', 'Puma', 'Reebok', 'New Balance', 'Asics'],
    'Count': [15, 12, 7, 5, 9, 6]
})

# Plot function
def plot_bar(data, title):
    plt.figure(figsize=(8, 5))
    plt.bar(data['Brand'], data['Count'], color='skyblue')
    plt.xlabel('Shoe Brand')
    plt.ylabel('Count')
    plt.title(title)
    plt.tight_layout()
    plt.show()

# 1. Alphabetical order
alphabetical = data.sort_values(by='Brand')
plot_bar(alphabetical, 'Bar Chart: Alphabetical Order')

# 2. By number of letters in the brand name
data['Name Length'] = data['Brand'].apply(len)
by_length = data.sort_values(by='Name Length')
plot_bar(by_length.drop(columns='Name Length'), 'Bar Chart: By Number of Letters')

# 3. Random order
random_order = data.sample(frac=1, random_state=42)  # reproducible shuffle
plot_bar(random_order, 'Bar Chart: Random Order')
