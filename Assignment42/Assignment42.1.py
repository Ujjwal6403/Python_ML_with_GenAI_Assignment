# 1. Implement Simple Linear Regression manually without using any ML library.
# Dataset
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]

# Tasks
# Calculate:
# 1. Mean of X (X̄ )
# 2. Mean of Y (Ȳ)
# 3. Slope (m)
# 4. Intercept (c)
# Expected Output Example
# Mean of X = 3
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4
# Regression Equation:
# Y = 0.4X + 2.4
# Predicted Y for X = 6 : 4.8

#######################################################################3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
   
   x = 6
   
   y = C + m * x
   
   print("Predicted y for x = 6 :", y)
   
def main():
   
   LinearRegreassionAlgorithm()
if __name__ == "__main__":
   main()