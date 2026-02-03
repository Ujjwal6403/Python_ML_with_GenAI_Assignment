# Q1 > Compare Two File (command Line)

# Problem Statement : 
# Write a program which accept two file names through commnd line argumets and compares the contents of both files.
# * if both files contain the same contents . Display Success .
# otherwise display failure

# Input :  (Command Line):
 #  Demo.txt Hello.txt
 
# Expected Output : sucess or Failure

import os
import sys

def CompareTwoFile(File1,File2):
   
   Fobj = os.path.exists(File1)
   Sobj = os.path.exists(File2)
   
   if(Fobj == False)and(Sobj == False):
      print("There is no such file on that place :")
      return
   
   Fobj = open(File1,"r")
   Sobj = open(File2,"r")
    
   read1 = Fobj.read()
   read2 = Sobj.read()
   
   if(read1 == read2):
      print("Success\n")
   else:
      print("Failure\n")

   Fobj.close()
   Sobj.close()
   

def main():
   
   if(len(sys.argv) != 3):
      print("Invalid number of argument :")
      print("Please specify the name of directory")
      return
   
   CompareTwoFile(sys.argv[1],sys.argv[2])
   
if __name__ == "__main__":
   main()


   