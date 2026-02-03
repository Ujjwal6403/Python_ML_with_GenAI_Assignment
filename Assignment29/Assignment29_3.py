# Q1 > Copy File content a new file (command Line)

# Problem Statement : 
# Write a program which accepts an existing file name through
# command line arguments, create a new file named Demo.txt,
# and copies all content from the given file into Demo.txt.

# Input : 
 #  Abc .txt
 
# Expected Output : 
# create Demo.txt and contents of abc.txt into Demo.txt

import os
import sys
def CopyFileContentANewFile(File = "Demo.txt"):
   hobj = False
   hobj = os.path.exists(File)
   
   if(hobj == False):
      print("There is no name file on this path")
      return
   
   fobj = open(File,"r")
   
   data = fobj.read()
   
   new = open("Abc.txt ","w")
   new.write(data)

   fobj.close()
   new.close()
   

def main():
   
   if(len(sys.argv) != 2):
      print("Invalid number of argument :")
      print("Please specify the name of directory")
      return
   
   CopyFileContentANewFile(sys.argv[1])
   
if __name__ == "__main__":
   main()


   