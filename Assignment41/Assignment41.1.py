# 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.
# The program should:
# • Calculate Euclidean distance
# • Sort distances
# • Select K nearest neighbors
# • Predict the class based on majority voting
# Dataset
# Point X Y Label
# A     1 2 Red
# B     2 3 Red
# C     3 1 Blue
# D     6 5 Blue

# Tasks
# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.
# Input Format
# Enter X coordinate: 2
# Enter Y coordinate: 2
# Expected Output
# Nearest Neighbors:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41
# Predicted Class: Red

import math
def EucDistance(p1,p2):
   Ans  = math.sqrt((p1['X'] - p2['X'])**2 + (p1['Y'] - p2['Y'])**2)
   return Ans

def KNeighborsClassifier():
   border = "_"*40
   
   dataset = [
            {'point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
            {'point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
            {'point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
            {'point' : 'D', 'X' : 6, 'Y' : 5, 'Label' : 'Blue'},
            
            ]
   print(border)
   print("User Define KNN Algorithm")
   print(border)
   print(border)
   # step1 : Take input from user
   print(border)
   
   x = int(input("Enter X coordinate : "))
   y = int(input("Enter Y coordinate : "))
   
   new_point = {"X":x, "Y":y}
   
   for data in dataset:
      data['distance'] = EucDistance(data, new_point)
      
   print(border)
   print("calculated distances are : ")
   print(border)
   
   for data in dataset:
      print(data)
   
   sorted_data = sorted(dataset, key = lambda item : item["distance"])
   print(border)
   print("sorted data is : ")
   print(border)
   
   for d in sorted_data:
      print(d)
      
   
   K = 3
   nearest = sorted_data[:K]
   print(border)
   print("nearest 3 element are : ")
   print(border)
   
   for d in nearest:
      print(d)
      
   
   votes = {}
   
   for neighbour in nearest:
      label = neighbour['Label']
      votes[label] = votes.get(label,0) + 1
      
   print(border)
   print("voting result is : ")
   print(border)
   
   for d in votes:
      print("name : ",d, "value : ",votes[d])
      
   prediction = max(votes, key = votes.get)
   
   print(border)
   print("predicted class :", prediction)
   print(border)

def main():
     
   KNeighborsClassifier()
if __name__ == "__main__":
   main()