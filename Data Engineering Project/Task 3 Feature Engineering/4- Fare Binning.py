# Importing relevent libraries
import pandas as pd
import numpy as np

# Reading CSV
file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 3 Feature Engineering\Output-1 Titanic_cleaned_dataset.csv'
df = pd.read_csv(file_path)

#Checking Unique fares
unique_fares = np.sort(df['fare'].unique())
print(unique_fares)

# Categorizing the fare data
fare_bins = [0, 50, 100, float('inf')]
fare_labels = ['low', 'medium', 'high']
df['fare_range'] = pd.cut(df['fare'], bins=fare_bins, labels=fare_labels, right=False)

# Checking the total count against each category
print(df['fare_range'].value_counts())

# Data to CSV
df.to_csv('Titanic_fare_binning.csv', index=False)