# Write a program which contains one function named as ChkNum() which accept one
# parameter as number. if number is even then it should display "Even number" otherwise
#display "odd number " on console.

def ChkNum(No):
   if((No % 2) == 0):
      print("Even Number")
   else:
      print("Odd Number")
   
def main():
   No = int(input("Enter The number "))
   
   ChkNum(No)
 
if __name__== "__main__":
   main()
