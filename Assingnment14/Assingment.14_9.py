#8>. Write a lambda function which accepts Two number and return multiplication


Multiplication = lambda iValue1,iValue2: (iValue1 * iValue2)

def main():
   No1 = int(input("Enter the First number : "))
   No2 = int(input("Enter the Second number : "))
   
   
   ret = Multiplication(No1,No2)
   
   print("Multiplication is : ",ret)
  
   
if __name__ == "__main__":
   main()