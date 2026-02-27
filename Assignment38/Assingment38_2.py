
# 2. Write a program to:
# Display total number of students in the dataset
# Count how many students Passed (FinalResult = 1)
# Count how many students Failed (FinalResult = 0)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)

Border = "-"*100
print(Border)

print("Display total number of students in the dataset : ",df.shape[0])

print("Count how many students Passed (FinalResult = 1) : ",list(df["FinalResult"]).count(1))

print("Count how many students Failed (FinalResult = 0) : ",list(df["FinalResult"]).count(0))

print(Border)