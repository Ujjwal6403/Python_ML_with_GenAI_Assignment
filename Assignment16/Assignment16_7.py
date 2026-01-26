# write a program which contains one function that accept one number
# form user and returns true if number is divisible by 5 otherwise return false.

def DivisibleBy5(No):
   
   if((No % 5)==0):
      return True
   else:
      return False
def main():
   No = int(input("Enter the number : "))
   
   Ret = DivisibleBy5(No)
   
   if(Ret == True):
      print(True)
   else:
      print(False)
   
if __name__== "__main__":
   main()
