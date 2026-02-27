# 7. Create a scatter plot of:
# StudyHours vs PreviousScore
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)
Border = "-"*100


plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
sns.scatterplot(x = df["StudyHours"],y = df["PreviousScore"],hue=df["FinalResult"])
plt.legend() # show status window which color show on which type of result.
plt.show()
