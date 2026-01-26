# write a program which accept number from user and return number of digits in that number.
# Input : 5187934  output : 7

def DigitCount(No):
   i = 0
   while(No != 0):
      i = i + 1
      No = No // 10
   return i 
def main():
   No = int(input("Enter the Row :"))
   
   Ret = DigitCount(No)
   print("Count of digit : ",Ret)
   
if __name__=="__main__":
   main()