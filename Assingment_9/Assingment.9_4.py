# 1> Write a program which accepts one number and print cube of that number.

# input : 5 : output : 125

def Printcube(ivalue):

   cube = ivalue*ivalue*ivalue
   
   print("The cube is :",cube)

def main():
   iNo = int(input("Enter  Number : "))
  
   Printcube(iNo)  

if __name__== "__main__":
   main()