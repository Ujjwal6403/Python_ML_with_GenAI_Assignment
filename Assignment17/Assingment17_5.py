
# Write a program which accept one number from user and addition of its factors.

def PrimeNo(No):
   
   for i in range(2,No+1):
      if(No % i == 0):
         break
      
   if(No == i):
      return True
def main():
   No = int(input("Enter the number :"))
   
   Ret = PrimeNo(No)
   
   if(Ret == True):
      print("prime")
   else:
      print("Not prime")
   
if __name__=="__main__":
   main()