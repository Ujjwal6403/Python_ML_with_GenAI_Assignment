# 6. Plot a histogram of StudyHours.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)
Border = "-"*100

plt.title("Student Study Hours")
plt.hist(df["StudyHours"])
plt.show()
print(Border)
