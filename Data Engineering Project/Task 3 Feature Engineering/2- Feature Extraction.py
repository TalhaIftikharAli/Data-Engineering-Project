# Import relevant library
import pandas as pd

# Loading the cleaned dataset
file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 3 Feature Engineering\Titanic_cleaned_dataset.csv'

df = pd.read_csv(file_path)

# Extracting Titles from Name Column
df['title'] = df['name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# New Feature Creation
df['travel_alone'] = (df['sibsp'] + df['parch'] == 0).astype(int)

# Data to CSV
df.to_csv('Titanic_with_new_feature.csv', index=False)