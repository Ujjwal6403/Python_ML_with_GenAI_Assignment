# Q2 > Search a Word in File

# Problem Statement : 
# Write a program which accepts a File Name and a word from 
# the User and checks whetherr that word is present in the file or not.

# Input :  Demo.txt  Marvellous
 
# Expected Output:Display whether the word Marvellous is found in Demo.txt or no
#####################################################################################

import os 
def SearchAWordInFile(File,word):
   
   ret = os.path.exists(File)

   if(ret == False):
      print("There is no such file in a program \n")
      return
   
   fobj = open(File,"r")
   
   Data = fobj.read()
   
   print(Data)
   temp = Data.split()
   
   for i in temp:
      if(i == word):
         print("Present in a file")
         break
   
   fobj.close()
  
def main():
   
   File = input("Enter the File name : ")
   
   word = input("Enter the word : ")
   
   SearchAWordInFile(File,word)
   
   
if __name__ == "__main__":
   main()