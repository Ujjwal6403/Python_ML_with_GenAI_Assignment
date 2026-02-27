# 8. Draw a boxplot for Attendance.
# Identify if any outliers are present.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)
Border = "-"*100


plt.boxplot(x=df["Attendance"])
plt.show()



