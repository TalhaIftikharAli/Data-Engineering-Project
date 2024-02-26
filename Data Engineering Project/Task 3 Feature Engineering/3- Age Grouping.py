# Importing relevent library
import pandas as pd

# Reading CSV
file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 3 Feature Engineering\Output-1 Titanic_cleaned_dataset.csv'
df = pd.read_csv(file_path)

# Categorizing the age data
age_boundaries = [0, 12, 18, 60, float('inf')]
categories = ['child', 'teen', 'adult', 'senior']
df['age_group'] = pd.cut(df['age'], bins=age_boundaries, labels=categories, right=False)

# Checking the total count against each category
print(df['age_group'].value_counts())

# Data to CSV
df.to_csv('Titanic_age_group_categorized.csv', index=False)