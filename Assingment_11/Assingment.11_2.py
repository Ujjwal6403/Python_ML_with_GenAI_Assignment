# 1> Write a program which accepts one number and prints count of digits in that number.

# input :7521: output :4

def CountDigit(ivalue):   
   Digit = 0
   count = 0
   while(ivalue != 0):
      count = count + 1
      ivalue = ivalue//10
   return count
def main():
   iNo  = int(input("Enter the number : "))
   
   Ret = CountDigit(iNo)
   print("The count of digit is : ",Ret)

if __name__ == "__main__":
   main()
   
   
