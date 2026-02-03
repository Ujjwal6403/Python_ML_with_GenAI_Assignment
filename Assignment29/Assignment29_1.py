# Q1 > Check File Exits in Current Directory

# Problem Statement : 
# Write a program which accepts a file name from user and 
# Checks wheterh that file exists in the current directory or not.

# Input : 
 #  Demo.txt
 
# Expected Output : 
#Display whether Demo.txt exists or not.

import os 

def Check(File):
   Ret  = False
   Ret = os.path.exists(File)
   
   if(Ret == False):
      print("There is no such Directory ")
   else:
      print(File ," the Exists in the current Directory")
      

def main():
   File = input("Enter the File Name :")
   
   Check(File)
   
if __name__ == "__main__":
   main()