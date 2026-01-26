# write a program which accept number from user and 
# check whether that number is positive or negative or zero.

def ChkPosornegorzero(No):
   if(No > 0):
     print("positive No")
   elif(No < 0 ):
      print("negative no")
   else:
      print("Zero")
   
def main():
   
   No = int(input("Enter the number : "))
   
   ret = ChkPosornegorzero(No)
 
if __name__== "__main__":
   main()
