import pandas as pd

# Load dataset
mall = pd.read_csv("Mall_Customers.csv")

# Dataset shape
print("Shape:")
print(mall.shape)

# Column names
print("\nColumns:")
print(mall.columns)

# First 5 rows
print("\nFirst 5 Rows:")
print(mall.head())

# Dataset information
print("\nDataset Information:")
mall.info()

# Missing values
print("\nMissing Values:")
print(mall.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(mall.describe())