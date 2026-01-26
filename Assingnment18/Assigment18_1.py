#1> write a program which accept N number from user and store it into list. 
# return addition of all elements from the list.

# input : Number of elements : 6
# input elements : 13 5 45 7 4 56
# output : 130

def Addition(Arr):
   Sum = 0
   for i in range(len(Arr)):
      Sum = Sum + Arr[i]
   return Sum

def main():
   print("Enter the No of element : ")
   Size = int(input())
   
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   print(Data)
   
   Ret = Addition(Data)
   print("Addition of list of element : ",Ret)

if __name__=="__main__":
   main()