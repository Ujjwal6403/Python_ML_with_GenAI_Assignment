
# 2. The value of K plays an important role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.
# Dataset
# Use the same dataset as Assignment 1.
# Tasks
# Predict the class of the same new point using:
# • K = 1
# • K = 3
# • K = 5
# Expected Output
# Prediction Results
# K = 1 → Red
# K = 3 → Red
# K = 5 → Blue
# Explain why the prediction changes when K increases.

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
   
   x = int(input("Enter X coordinate : "))
   y = int(input("Enter Y coordinate : "))
   
   new_point = {"X":x, "Y":y}
   
   # Calculate distance
   for data in dataset:
      data['distance'] = EucDistance(data, new_point)
      
   print(border)
   print("calculated distances are : ")
   print(border)
   
   for data in dataset:
      print(data)
   
   # Sort distances
   sorted_data = sorted(dataset, key = lambda item : item["distance"])
   
   print(border)
   print("sorted data is : ")
   print(border)
   
   for d in sorted_data:
      print(d)
   
   print(border)
   
   ##################################################################
   # # K = 3
   print(border)
   K = 3
   nearest = sorted_data[:K]
   
   print(border)
   print("nearest 3 element are : ")
   print(border)
   
   for d in nearest:
      print(d)
   
   # Voting
   votes = {}
   
   for neighbour in nearest:
      label = neighbour['Label']
      votes[label] = votes.get(label,0) + 1
      
   print(border)
   print("voting result is : ")
   print(border)
   
   for d in votes:
      print("name : ",d," value : ",votes[d])
      
   prediction3 = max(votes, key = votes.get)
   
   print(border)
   print("predicted class K = 3 :", prediction3)
   print(border)
   
################################################################################

   print(border)
   # K = 5
   print(border)
   K = 5
   nearest = sorted_data[:K]
   
   print(border)
   print("nearest 5 element are : ")
   print(border)
   
   for d in nearest:
      print(d)
   
   # Voting
   votes = {}
   
   for neighbour in nearest:
      label = neighbour['Label']
      votes[label] = votes.get(label,0) + 1
      
   print(border)
   print("voting result is : ")
   print(border)
   
   for d in votes:
      print("name : ",d," value : ",votes[d])
      
   prediction5 = max(votes, key = votes.get)
   
   print(border)
   print("predicted class K = 5->  :", prediction5)
   print(border)
   
   
   ###################################################################
   
   
   print(border)
   # K = 1
   print(border)
   K = 1
   nearest = sorted_data[:K]
   
   print(border)
   print("nearest 5 element are : ")
   print(border)
   
   for d in nearest:
      print(d)
   
   # Voting
   votes = {}
   
   for neighbour in nearest:
      label = neighbour['Label']
      votes[label] = votes.get(label,0) + 1
      
   print(border)
   print("voting result is : ")
   print(border)
   
   for d in votes:
      print("name : ",d," value : ",votes[d])
      
   prediction1 = max(votes, key = votes.get)
   
   print(border)
   print("predicted class K = 1->  :", prediction1)
   print(border)
   
   
def main():
   KNeighborsClassifier()

if __name__ == "__main__":
   main()
   
# Explain why the prediction changes when K increases.

# KNN algorithm madhe prediction he nearest neighbors cha majority voting var depend aste.

# K = 1 asel tar algorithm fakt sarvat javalcha point consider karto, tyamule prediction tya eka point cha class var tharate.

# K = 3 asel tar algorithm 3 nearest neighbors select karto ani jya class che voting jast aste toch class predict karto.

# K = 5 asel tar algorithm 5 nearest neighbors consider karto. Pan aaplya dataset madhe fakt 4 records ahet, mhanun algorithm available points 
# consider karto ani tyavarun prediction karto.pahile class predict karto