#1>. Write a lambda function which accept one number and returns square of that number.

 
square = lambda iNo : iNo * iNo

def main():
   iNo = int(input("Enter the number : "))
  
   Ret = square(iNo)
   print("Square of no ",Ret)
   
if __name__ == "__main__":
   main()
