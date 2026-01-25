#1>. Write a lambda function which accepts one number and return cube of that number.

Cube = lambda iValue : iValue * iValue * iValue

def main():
   No = int(input("Enter the number : "))
   
   ret = Cube(No)
   print("Cube of no :",ret)
   
if __name__ == "__main__":
   main()