# 1> Write a program which accepts one number and prints reverse of that number

# input :123: output :321

def pallindrom(ivalue):   
   Digit = 0
   rev = 0
   iNo = ivalue
   while(ivalue != 0):
      Digit = ivalue % 10
      rev = (rev * 10) + Digit
      ivalue = ivalue//10
      
   print(rev)
   print("what is value",ivalue)
   
   if( rev == iNo):
      return True
   else:
      return False
   
def main():
   iNo  = int(input("Enter the number : "))
   bRet = False
   
   bRet = pallindrom(iNo)
   
   if(bRet == True):
      print("palindrom ")
   else:
      print("Not pallindrom")

if __name__ == "__main__":
   main()
   
