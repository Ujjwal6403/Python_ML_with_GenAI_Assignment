# 5. Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers.
# Map function will multiply each number by 2.
# Reduce will return Maximum number from that numbers.
# (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62]

# Output of reduce = 62

from functools import reduce

def PrimeNo(Arr):
   i = 2
   for i in range(2,Arr+1):
      if((Arr % i) == 0):
         break
      i = i + 1
   
   if(Arr == i):
      return Arr
     
def Multiply(Arr):
   return Arr*2
   
def Max(X , Max):
   if(X > Max):
      Max= X
   return Max

def main():
   Size = int(input("Enter the size of  List : "))
  
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   print(Data)
   
   # Data = [2, 70, 11, 10, 17, 23, 31, 77]
   
   FData = list(filter(PrimeNo,Data))
   print(" Data after filter is ",FData)
   
   MData = list(map(Multiply,FData))
   print("Data after mapping is :",MData)
   
   RData = reduce(Max,MData)
   
   print("After reduce ",RData)
   
if __name__=="__main__":
   main()