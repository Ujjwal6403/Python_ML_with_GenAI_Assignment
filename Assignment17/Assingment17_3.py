
# Write a program which accept one number from user and return it's factorial.

def Factorial(No):
   fact = 1
   for i in range(1,No+1):
      fact = fact * i
   return fact   
def main():
   No = int(input("Enter the number :"))
   
   Ret = Factorial(No)
   
   print("Factorial is : ",Ret)
   

if __name__=="__main__":
   main()