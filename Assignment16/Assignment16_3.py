# Write a program which contains one function named as Add() which
# accepts two number from user and return addition of that two numbers.

def Add(No1,No2):
   return No1 + No2
   
def main():
   No1 = int(input("Enter The First number "))
   No2 = int(input("Enter The Second number "))
   
   ret = Add(No1,No2)
   print("Addition is :",ret)
 
if __name__== "__main__":
   main()
