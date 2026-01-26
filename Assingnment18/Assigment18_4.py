#3> write a program which accept N number from user and store it into list. 
# accept one another number from user and return frequecy of that number from list.

# input : Number of elements : 11
# input elements : 13 5 45 7 4 56 5 34 2 5 65
# Element of search : 5
# output : 3

def Frequency(Arr,search):
   count = 0
   for i in range(len(Arr)):
      if(Arr[i]  == search):
         count = count + 1
   return count

def main():
   print("Enter the No of element : ")
   Size = int(input())
   
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   
   search = int(input("Enter the element you want to search "))
   
   print(Data,search)
   
   Ret = Frequency(Data,search)
   print("Frequency of serch element in  list of element : ",Ret)

if __name__=="__main__":
   main()