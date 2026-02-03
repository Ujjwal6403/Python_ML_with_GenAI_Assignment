# Q2 > Display File Line by Line

# Problem Statement : 
# Write a program which accepts a file name from user 
# and displays the contents of the file line by line on the screen.


# Input :  Demo.txt  
 
# Expected Output:Display each line of Demo.txt one by one.
###################################################################

import os 
def DisplayFileLineByLine(File):
   
   ret = os.path.exists(File)
   
   if(ret == False):
      print("There is no such file in a program \n")
      return
   
   fobj = open(File,"r")
   count = 0
   Data = fobj.read()
   line = Data.splitlines()
   for i in line:
      print(i)

   fobj.close()
   return count

def main():
   
   File = input("Enter the File name : ")
   
   DisplayFileLineByLine(File)
   
   
if __name__ == "__main__":
   main()