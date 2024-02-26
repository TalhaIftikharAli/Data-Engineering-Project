import pandas as pd

file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 3 Feature Engineering\Output-1 Titanic_cleaned_dataset.csv'

# Load the dataset
titanic_data = pd.read_csv(file_path)

# Exclude non-numeric columns
numeric_columns = titanic_data.select_dtypes(include=['int64', 'float64']).columns
numeric_data = titanic_data[numeric_columns]

# Compute the correlation matrix
correlation_matrix = numeric_data.corr()

correlation_matrix_round = correlation_matrix.round(2)

# Display correlation matrix
print(correlation_matrix_round)

# Data Set to CSV
correlation_matrix_round.to_csv('Correlation_Matrix.csv')