# 3. Consider below task
# 1. Train linear regression model.
# 2. Predict salary for 6 years of experience.
# 3. Plot regression line using matplotlib.
# Dataset
# Experience Salary
# 1         20000
# 2         25000
# 3         30000
# 4         35000
# 5         40000

# Expected Output
# Predicted Salary for 6 Years Experience: ₹45000
# Graph should display:
# • Data points
# • Regression line

import numpy as np
import matplotlib.pyplot as plt

def LinearRegrassionSalary():
   
   X = [1,2,3,4,5]
   Y = [20000,25000,30000,35000,40000]
   
   print("Experience : ",X)
   print("Salary : ",Y)
   
   mean_x = np.mean(X)
   mean_y = np.mean(Y)
   
   n = len(X)
   
   numerator = 0
   denominator = 0
   
   for i in range(n):
      numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
      denominator = denominator + ((X[i] - mean_x)**2)
      
   m = numerator/denominator
   c = mean_y - m*mean_x
   
   print("Slop m = ",m)
   print("Intercept c = ",c)
   
   # Prediction
   
   x = 6
   predicted_salary = m*x + c
   
   print("Predicted salary for 6 year Experience : ",predicted_salary)
   
   # Regression line
   Y_pred = []
   for i in X:
      Y_pred.append(m*i+c)
      
      #plotting
   plt.scatter(X,Y,label= "Data Points")
   plt.plot(X,Y_pred,label = "Regression line")
   
   plt.xlabel("Experience (Years)")
   plt.ylabel("Salary")
   plt.title("Salary prediction using linear Regression")
   
   plt.legend()
   plt.show()
   
   
   
   
def main():
   LinearRegrassionSalary()
   
if __name__ == "__main__":
   main()
