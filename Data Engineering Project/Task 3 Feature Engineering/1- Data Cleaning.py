# Import relevant libraries
import pandas as pd

# Loading the Dataset
file_path = r'Task 3 Feature Engineering/0- Dataset/titanic.csv'

df = pd.read_csv(file_path)

# Droppping unnecessary columns
drop_boat_column = df.drop('boat', axis=1, inplace=True)
drop_body_column = df.drop('body', axis=1, inplace=True)
drop_address_column = df.drop('home.dest', axis=1, inplace=True)

# Identifying missing values
missing_values = df.isnull().sum()
print('Missing values count : ')
print(missing_values)

# Handling missing values
# Cabin : Missing count = 1015
df.drop('cabin', axis=1, inplace=True)

# Age: Missing count = 264
df['age'].fillna(df['age'].median(), inplace=True)

# Fare: Missing count = 2
df['fare'].fillna(df['fare'].median(), inplace=True)

# Embarked: Missing count = 3
repeated_embarked = df['embarked'].mode()[0]
df['embarked'].fillna(repeated_embarked, inplace=True)

# For 'pclass', 'survived', 'name', 'sex', 'sibsp', 'parch', and 'ticket' missing count is 1
# drop the rows with missing values since they are very few compared to the dataset size
df.dropna(subset=['pclass','survived','name','sex','sibsp','parch','ticket'], inplace=True)

# Justifications
# 1- Cabin:
# It has a large number of missing values (>75%).
# Not a right approach to fill this column since we may introduce some bias.
# Therefore, it's better to drop this column.

# 2- Age and Fare:
# Both include numerical features. Using median to input missing values preserves the integrity
# of the data as oppossed to mean as it may include outliers which can have a heavy impact on
# the mean and hence the missing value.

# 3- Other Columns:
# 'pclass','survived','name','sex','sibsp','parch' and 'ticket'.
# All these missing rows can therefore be dropped.

# Verify if there are any missing values remaining
print('Missing values count : ')
print(df.isnull().sum())

# Saving the dataset
df.to_csv('Titanic_cleaned_dataset.csv', index=False)