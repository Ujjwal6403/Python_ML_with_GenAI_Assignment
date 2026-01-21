# 1> Write a program which accepts one number and prints square of that number.

# input : 5 : output : 25

def PrintSquare(ivalue):

   Square = ivalue*ivalue
   
   print("The Square is :",Square)

def main():
   iNo = int(input("Enter  Number : "))
  
   PrintSquare(iNo)  

if __name__== "__main__":
   main()