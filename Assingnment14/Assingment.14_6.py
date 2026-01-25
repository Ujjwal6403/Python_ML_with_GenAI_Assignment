#1>. Write a lambda function which accepts one number and return True if number is odd otherwise False.

CheckOddNo = lambda iValue : True if iValue % 2 != 0 else False

def main():
   No = int(input("Enter the First number : "))

   
   ret = CheckOddNo(No)
   if(ret == False):
      print("Not odd")
   else:
      print("odd ")
   
if __name__ == "__main__":
   main()