# 3. Use KNN to predict whether a student passes or fails based on study hours and attendance.
# Dataset
# Study Hours Attendance Result
# 2            60        Fail
# 5            80        Pass
# 6            85        Pass
# 1            50        Fail

# Tasks
# 1. Accept input from user:
# ◦ Study hours
# ◦ Attendance percentage
# 2. Apply KNN algorithm
# 3. Predict whether the student Passes or Fails
# Input Example
# Enter Study Hours: 4
# Enter Attendance: 70
# Expected Output
# Predicted Result: Pass


   
import math

def EcuDistance(p1,p2):
   Ans = math.sqrt((p1['StudyHours'] - p2['StudyHours'])**2 +(p1['Attendance'] - p2['Attendance'])**2)
   return Ans
def  KNNAlgorith():
   border = "_"*40
   
   dataset = [
      {'StudyHours':2,'Attendance':60,'Result':'Fail'},
      {'StudyHours':5,'Attendance':80,'Result':'Pass'},
      {'StudyHours':6,'Attendance':85,'Result':'Pass'},
      {'StudyHours':1,'Attendance':50,'Result':'Fail'}
   ]
   
   print(border)
   print("Knn student result prediction")
   print(border)
   
   StudyHours = int(input("Enter study hours : "))
   Attendance = int(input("Enter attendecen : "))
   
   new_point = {'StudyHours':StudyHours,'Attendance':Attendance}
   
   
   for data in dataset:
      data['distance'] = EcuDistance(data,new_point)
      
   print(border)
   print("calculated distances")
   print(border)
   
   for d in dataset:
      print(d)
      
   sorted_data = sorted(dataset,key = lambda item: item['distance'])
   
   print(border)
   print("sorted data")
   print(border)
   
   for d in sorted_data:
      print(d)
      
   # k = 3
   K = 3
   nearest = sorted_data[:K]
   
   print(border)
   print("Nearest neighbors ")
   print(border)
   
   for d in nearest:
      print(d)
      
   
   votes = {}
   
   for n in nearest:
      label = n['Result']
      votes[label] = votes.get(label,0)+1
      
   prediction = max(votes,key=votes.get)

   print(border)
   print("predicted result:",prediction)
   print(border)
      
      
def main():
  
   KNNAlgorith()
if __name__ == "__main__":
   main()