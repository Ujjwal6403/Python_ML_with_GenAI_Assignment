# Q1 > Display File Contents

# Problem Statement : 
# Write a program which accepts a file name form the user, open
# that File and Display the entire contents on the console

# Input : 
 #  Demo.txt
 
# Expected Output : 
#Display content of Demo.txt on console
import os
def DisplayFileContents(File):
   hobj = False
   hobj = os.path.exists(File)
   
   if(hobj == False):
      print("There is no name file on this path")
      return
   
   fobj = open(File,"r")
   
   data = fobj.read()
   
   print("File contents are : \n")
   print(data)
   fobj.close()
   

def main():
   File = input("Enter the File Name :")
   
   DisplayFileContents(File)
   
if __name__ == "__main__":
   main()


   