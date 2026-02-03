# Q2 > Copy File Contents into Another File

# Problem Statement : 
# Write a program which accepts a Two file name from user 

# * Fist file is and extisting File
# * Second file is a new file


# Input :  abc.txt Demo.txt
 
# Expected Output:Contents of ABC.txt copied into Demo.txt.
###################################################################

import os 
def CopyFileContentsIntoAnotherFile(File1,File2):
   
   ret1 = os.path.exists(File1)
   ret2 = os.path.exists(File2)
   
   if(ret1 == False)and(ret2 == False):
      print("There is no such file in a program \n")
      return
   
   fobj = open(File1,"r")
   
   hobj = open(File2,"w")
   
   Data1 = fobj.read()
   
   hobj.write(Data1)
   
   fobj.close()
   hobj.close()
  
def main():
   
   File1 = input("Enter the First File name : ")
   File2 = input("Enter the Second File name : ")
   CopyFileContentsIntoAnotherFile(File1,File2)
   
   
if __name__ == "__main__":
   main()