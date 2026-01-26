#3> write a program which accept N number from user and store it into list. 
# return Maximum number from the list.

# input : Number of elements : 7
# input elements : 13 5 45 7 4 56 34
# output : 56

def Maximum(Arr):
   Min = 0
   for i in range(len(Arr)):
      if(Arr[i] > Min):
         Min = Arr[i]
   return Min

def main():
   print("Enter the No of element : ")
   Size = int(input())
   
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   print(Data)
   
   Ret = Maximum(Data)
   print("Maximum No  of list of element : ",Ret)

if __name__=="__main__":
   main()