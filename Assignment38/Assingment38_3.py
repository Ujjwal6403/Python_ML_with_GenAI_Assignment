
# 3. Using pandas functions, calculate and display:
# Average StudyHours
# Average Attendance
# Maximum PreviousScore
# Minimum SleepHours
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)

Border = "-"*100
print(Border)
print(Border)
print("Average StudyHours : ",df["StudyHours"].mean())
print("Average Attendance : ",df["Attendance"].mean())
print("Average PreviousScore : ",df["PreviousScore"].mean())
print("Average SleepHours : ",df["SleepHours"].mean())

print(Border)