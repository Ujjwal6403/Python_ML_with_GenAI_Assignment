# 1. Write a Python program to load the le student_performance_ml.csv using pandas.
# Display:
# First 5 records
# Last 5 records
# Total number of rows and columns
# List of column names
# Data types of each column

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)

Border = "-"*100
print(Border)

# Display First Five Record used head() to show first five records
print("First Five Rows Data is : \n",df.head())

# Display Last Five Record. tail() method used to show by default last five row.
print("Last Five Rows Data is : \n",df.tail())

# Total number of rows and columns dataframe.shape[0] indicate total rows side and shape[1] show column size.
print(f"Total number of rows is : {df.shape[0]} and columns are : ",df.shape[1])

# List of column names
print("List of Column Names is : \n",list(df.columns))

# Data types of each column
print("Show Data Types of each column :\n",df.dtypes)

print(Border)