#3> write a program which accept N number from user and store it into list. 
# return Minimum number from the list.

# input : Number of elements : 7
# input elements : 13 5 45 7 4 56 34
# output : 4

def Minimum(Arr):
   Min = Arr[1]
   for i in range(len(Arr)):
      if(Arr[i] < Min):
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
   
   Ret = Minimum(Data)
   print("Minimum No  of list of element : ",Ret)

if __name__=="__main__":
   main()