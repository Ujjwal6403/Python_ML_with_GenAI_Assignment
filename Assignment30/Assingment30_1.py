# Q1 > Count lines in a File

# Problem Statement : 
# Write a program which accepts a file name from user 
# and counts how many lines are present in the file

# Input :  Demo.txt  
 
# Expected Output: Total number of lines in Demo.txt.
###################################################################

import os 
def CountLinesInAFile(File):
   
   ret = os.path.exists(File)
   
   if(ret == False):
      print("There is no such file in a program \n")
      return
   
   fobj = open(File,"r")
   count = 0
   Data = fobj.read()
   line = Data.splitlines(Data)
   for i in line:
      count = count + 1

   fobj.close()
   return count

def main():
   
   File = input("Enter the File name : ")
   
   Ret = CountLinesInAFile(File)
   print("Number of line in a file: ",Ret)
   
if __name__ == "__main__":
   main()