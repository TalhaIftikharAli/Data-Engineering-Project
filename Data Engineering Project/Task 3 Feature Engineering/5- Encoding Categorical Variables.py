#Importing relevent library
import pandas as pd

# Reading the CSV
file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 3 Feature Engineering\Output-1 Titanic_cleaned_dataset.csv'

df = pd.read_csv(file_path)

# Binary encoding on 'sex'
df['sex_into_binary'] = df['sex'].map({'male': 0, 'female': 1})

# Perform one-hot encoding on 'embarked'   
df = pd.get_dummies(df, columns=['embarked'], drop_first=True)

# Data to CSV
df.to_csv('Titanic_encoding_categorical_variables.csv', index=False)