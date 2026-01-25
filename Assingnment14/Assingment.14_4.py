#1>. Write a lambda function which accepts two  number and return Maximum number .

Minimum = lambda iValue1,iValue2 : iValue1 if iValue1 < iValue2 else iValue2

def main():
   No1 = int(input("Enter the First number : "))
   No2 = int(input("Enter the Second number : "))
   
   ret = Minimum(No1,No2)
   
   print("Manimum number is  :",ret)
   
if __name__ == "__main__":
   main()