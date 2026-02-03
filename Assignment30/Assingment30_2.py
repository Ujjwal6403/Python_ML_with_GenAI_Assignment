# Q2 > Count Words in a File

# Problem Statement : 
# Write a program which accepts a file name from user 
# and counts the total number of words in that file.

# Input :  Demo.txt  
 
# Expected Output: Total number of words in Demo.txt.
###################################################################

import os 
def CountWordsInAFile(File):
   
   ret = os.path.exists(File)
   
   if(ret == False):
      print("There is no such file in a program \n")
      return
   
   fobj = open(File,"r")
   count = 0
   Data = fobj.read()
   word = Data.split()
   for i in word:
         count = count + 1

   fobj.close()
   return count

def main():
   
   File = input("Enter the File name : ")
   
   Ret = CountWordsInAFile(File)
   print("Number of word in a file: ",Ret)
   
if __name__ == "__main__":
   main()