# Write a program which accepts one number and check wheterh its is perfect number of not.

#input = 6
#output = perfect number


def CheckPerfect(ivalue):
   
   i = 1
   Sum = 0
   while (i < ivalue/2):
      if((ivalue % i) == 0):
         Sum = Sum + 1
   
      print("...",ivalue)
   # print("...sum",Sum)
   
   if(Sum == ivalue):
      return True
   else:
      return False
   
def main():
   
   iNo = int(input("Enter the number : "))
   iRet = 0
   iRet = CheckPerfect(iNo)
   
   if(iRet == True):
      print("Its perfect number")
   else:
      print("Its not perfect number")
   
  
if __name__ == "__main__":
   main()

