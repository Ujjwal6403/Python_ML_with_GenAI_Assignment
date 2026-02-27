# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)

Border = "-"*100
print(Border)

sns.scatterplot(x=df["SleepHours"], y = df["FinalResult"],hue=df["FinalResult"])
plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.legend()
plt.show()