# 1> Write a program which accepts one number and prints sum of digit.

# input :7521: output :4

def SumDigit(ivalue):   
   Digit = 0
   Sum  = 0
   while(ivalue != 0):
      Digit = ivalue % 10
      Sum = Sum + Digit
      ivalue = ivalue//10
   return Sum
def main():
   iNo  = int(input("Enter the number : "))
   
   Ret = SumDigit(iNo)
   print("The Sum of digit is : ",Ret)

if __name__ == "__main__":
   main()
   
   
