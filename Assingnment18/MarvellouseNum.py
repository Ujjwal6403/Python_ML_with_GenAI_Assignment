def chkprime(Arr):
   
   for i in range(2,Arr):
      if(Arr % i == 0):
         break
   if(Arr == i):
      sum = sum + Arr
      
def main():
   print("Enter the No of element : ")
   Size = int(input())
   
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   
   print(Data)
   
   Ret = chkprime(Data)
   
   print("addition is prime number :  ",Ret)

if __name__=="__main__":
   main()
