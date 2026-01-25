#8>. Write a lambda function which accepts Two number and return Addition


Addition = lambda iValue1,iValue2: (iValue1 + iValue2)

def main():
   No1 = int(input("Enter the First number : "))
   No2 = int(input("Enter the Second number : "))
   
   
   ret = Addition(No1,No2)
   
   print("Addition is : ",ret)
  
   
if __name__ == "__main__":
   main()