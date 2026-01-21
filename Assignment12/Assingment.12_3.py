# Write a program which accepts two number and prints addition,substaction,multiplication and division.

def ASMD(ivalue1,ivalue2):
   
   Addition = ivalue1 + ivalue2
   Substaction = ivalue1 - ivalue2
   Multiplication = ivalue1 * ivalue2
   Division = ivalue1 / ivalue2
   
   return Addition,Substaction,Multiplication,Division
   
         
def main():
   
   iNo1 = int(input("Enter First number : "))
   iNo2 = int(input("Enter second number : "))
   
   ARet,SRet,MRet,DRet= ASMD(iNo1,iNo2)
   
   print("Addition  : ",ARet, "substaction : ", SRet ," Multiplication : ",MRet, "Division is : ",DRet)
   


if __name__ == "__main__":
   main()