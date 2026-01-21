# 1> Write a program which accepts one number and check whether it is divisible by 3 and 5

# input : 15 : output : Divisible by 3 and 5

def Checkwhether(ivalue):
   
   if((ivalue % 3) == 0)&((ivalue % 5) == 0):
      return True
   else: 
      return False
def main():
   iNo = int(input("Enter  Number : "))
   bret = False
  
   bret = Checkwhether(iNo) 
   if(bret == True):
     print("The number is Divisible by 3 and 5")
   else:
      print("The number is not divisible by 3 and 5")
 
if __name__== "__main__":
   main()