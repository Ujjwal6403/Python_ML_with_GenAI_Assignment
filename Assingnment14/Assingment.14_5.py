#1>. Write a lambda function which accepts one number and return True if number is even otherwise False.

CheckEvenNo = lambda iValue : True if iValue % 2 == 0 else False

def main():
   No = int(input("Enter the First number : "))

   
   ret = CheckEvenNo(No)
   if(ret == False):
      print("Not Even")
   else:
      print("Even ")
   
if __name__ == "__main__":
   main()