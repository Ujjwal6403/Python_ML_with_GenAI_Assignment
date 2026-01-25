#1>. Write a lambda function which accepts one number and return True if divisible by 5.


DivisibleBy5 = lambda iValue : True if iValue % 5 == 0 else False

def main():
   No = int(input("Enter the First number : "))

   
   ret = DivisibleBy5(No)
   if(ret == True):
      print("Divisible by 5 ")
   else:
      print("Not Divisible by 5 ")
   
if __name__ == "__main__":
   main()