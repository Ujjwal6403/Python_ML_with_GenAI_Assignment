
# Write a program which accept one number from user and addition of its factors.

def FactorialAdd(No):
   
   fact = 0
   temp = No//2
   
   for i in range(1,temp+1):
      if(No % i == 0):
         fact = fact + i
   return fact
def main():
   No = int(input("Enter the number :"))
   
   Ret = FactorialAdd(No)
   
   print("Factorial of Addition is : ",Ret)
   

if __name__=="__main__":
   main()