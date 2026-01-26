# 4. Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even.
# Map function will calculate its square. 
# Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100]

# Output of reduce = 204
from functools import reduce

def EvenNo(Arr):
   return (Arr % 2 == 0)
     
def CalculateSqare(Arr):
   return Arr*Arr
   
def Add(X,Y):
   return X+Y

def main():
   Size = int(input("Enter the size of  List : "))
  
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   print(Data)
   
   # Data =  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
   
   FData = list(filter(EvenNo,Data))
   print(" Data after filter is ",FData)
   
   MData = list(map(CalculateSqare,FData))
   print("Data after mapping is :",MData)
   
   RData = reduce(Add,MData)
   
   print("After reduce ",RData)
   
   
   
   
   
   
   
   
   
   
if __name__=="__main__":
   main()