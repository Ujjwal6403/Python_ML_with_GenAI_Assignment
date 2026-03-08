# 2. Using the same dataset from above question, calculate model performance.
# Tasks
# 1. Predict all Y values using regression equation.
# 2. Calculate:
# • Mean Squared Error (MSE)
# • R2 Score
# Show all intermediate calculations.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def LinearRegreassionAlgorithm():
   X = [1,2,3,4,5]
   Y = [3,4,2,4,5]

   print("Values of Independent variable : X -",X)
   print("Values of Dependent variable : Y -",Y)
   
   mean_x = np.mean(X)
   mean_y = np.mean(Y)
   
   print("X_mean is : ",mean_x)
   print("Y_mean is :",mean_y)
   
   n = len(X)
   
   numerator = 0
   denominator = 0
   
   for i in range(n):
      numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
      denominator = denominator + ((X[i] - mean_x)**2)
      
   m = numerator / denominator
   
   print("slope of line is ",m) # 0.4
   
   C = mean_y - (m * mean_x)
   
   print("Y intercept of line is C : ",C)
   
   # x = 6
   
   # y = C + m * x
   
   # print("Predicted y for x = 6 :", y)
   
   Y_pred =[]
   for x in X:
      y = C + m * x
      Y_pred.append(y)
      print("X = ",x," Predicted Y =",y)
   
   # MSE calculation
   mse = 0
   
   for i in range(n):
      error = (Y[i] - Y_pred[i])**2
      mse +=error
      print("Actual:",Y[i], "Predicted : ",Y_pred[i]," Error^2:",error)
   
   mse - mse/2
   print("mean squaer error(mse) = ",mse)
   
   
   r2 = r2_score(Y,Y_pred)
   
   print("Acutal values : Y",Y)
   print("predicted values Yp",Y_pred)
   print("R square value : ",r2)
   
def main():
   
   LinearRegreassionAlgorithm()
if __name__ == "__main__":
   main()