# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)
Border = "-"*100

Resultstudent = df["FinalResult"].value_counts(True)

print("Pass Student Persentage :",Resultstudent[1])
print("Fail Student Persentage :",Resultstudent[0])
#print(failstudent)
print(Border)