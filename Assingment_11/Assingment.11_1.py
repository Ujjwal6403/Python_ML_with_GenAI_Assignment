# 1> Write a program which accepts one number and checks whether it is prime or not.

# input :11 : output :prime number

def CheckPrime(ivalue):
   i = 2
   for i in range(2,ivalue+1):
      
      if((ivalue % i) == 0):
         
         break
      
   if(i == ivalue):
      print("prime no",ivalue)
   elif ivalue == 1:
      print("Not prime no",ivalue)
   else:
      print("Not prime",ivalue)
def main():
   iNo = int(input("Enter Number : "))
   
   CheckPrime(iNo)

if __name__ == "__main__":
   main()
   
   
#######################################################
# use bool
def CheckPrime(iValue):
   if(iValue == 1):
      return False
   bflag = True
   for i in range (2,iValue):
      if((iValue % i) == 0):
         bflag = False
         break
   return bflag

def main():
   iNo = int(input("Enter the number :"))
   Bret = False
   
   Bret = CheckPrime(iNo)
   
   if(Bret == False):
      print("Not prime No")
   else:
      print(" prime No")
      
if __name__ == "__main__":
   main()