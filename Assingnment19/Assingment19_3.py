# 3. Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user.

# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
from functools import reduce

def GreaterThanOrEqual(Arr):
   if (Arr >= 70)and(Arr <= 90):
      return Arr
     
def IncreaseEachNo(Arr):
   return Arr+10
   
def Add(X,Y):
   return X*Y

def main():
   # Size = int(input("Enter the size of  List : "))
  
   # Data = list()
   # print("Enter the elements :")
   
   # for i in range(Size):
   #    value = int(input())
   #    Data.append(value)
   # print(Data)
   
   Data =  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
   
   FData = list(filter(GreaterThanOrEqual,Data))
   print(" Data after filter is ",FData)
   
   MData = list(map(IncreaseEachNo,FData))
   print("Data after mapping is :",MData)
   
   RData = reduce(Add,MData)
   
   print("After reduce ",RData)
   
if __name__=="__main__":
   main()