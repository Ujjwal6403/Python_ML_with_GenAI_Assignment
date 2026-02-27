# 9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)
Border = "-"*100

sns.scatterplot(x=df["AssignmentsCompleted"], y = df["FinalResult"],hue=df["FinalResult"])
plt.title("relationship between AssignmentsCompleted and FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.legend()
plt.show()
