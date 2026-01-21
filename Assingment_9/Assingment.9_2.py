# 1> Write a program which contains one function CheckGreater() that 
# that accepts two number and print the greater number.

# input : No1 = 10, No2 = 20, output : 20:

def CheckGreater(ivalue1, ivalue2):
   if (ivalue1 > ivalue2):
      
         print("The greater number is ",ivalue1)
   else:
         print("The Greater number is :",ivalue2)
   
def main():
   iNo1 = int(input("Enter First Number : "))
   iNo2 = int(input("Enter the second number : "))
   
   CheckGreater(iNo1,iNo2)  

if __name__== "__main__":
   main()