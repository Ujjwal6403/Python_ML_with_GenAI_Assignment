# 1> Write a program which accepts one number and prints Factorial of that number.

# input :5 : output :120

def Factorial(ivalue):
   fact = 1
   for i in range(1,ivalue+1):
      
      fact = fact * i
   print("The factorial is :",fact)
  
def main():
   
   iNo = int(input("Enter the number "))
   Factorial(iNo)
   
if __name__== "__main__":
   main()