# Write a program which accepts one number and prints binary equivalent.


def BinaryEquivalent(ivalue):
   R = 0
   rev = 0
   while(ivalue != 0):
      R = ivalue % 2 
      print(R)
      ivalue = ivalue //2
      
     
    
def main():
   
   iNo = int(input("Enter the number : "))
 
   BinaryEquivalent(iNo)

  
if __name__ == "__main__":
   main()