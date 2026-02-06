#Please follow below rules while designing automation script as 

# * Accept input through command line or through file.
# * Display any message in log file instead of console.
# * For separete task defin separate function.
# * For robustness handle evey expected exception.
# * perform validations before takign any action.
# * Create user defind module to store the functionality

# Q1>.Design automation script which accept directory name and file extention from user.
# Display all files with that extention.

# Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is name directory and .txt is the extension that we want to search.

import os 
import sys

def CreateLogfile():
   try:
      
      Log = open("LogFile.Log","w")
      return Log
   except Exception as e:
      return None

def ValidateDirectory(DirectoryName,Log):
   
   Ret = os.path.exists(DirectoryName)
   if(Ret == False):
      Log.write("There is such Directory Name\n")
      return
      
   Ret = os.path.isdir(DirectoryName)
   if(Ret == False):
      Log.write("It is not a Directory\n")
      return
      
def DisplayAllFileGivenExtention(DirectoryName,Extention,Log):
   try:
    
      for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
         for Fname in FileName:
            if(Fname.endswith(Extention)): 
               Log.write(Fname+"\n")
   except Exception as e:
      Log.write("Exception occured while scanning directory \n")
            
def main():
   
   Log = CreateLogfile()
   try: 
      if(len(sys.argv) != 3):
         Log.write("Invalid Input : ")
         Log.write("Enter the valid input : ")
         return
   except Exception as e:
      Log.write("Unexpected error occurred\n")
   finally : 
      Log.close()
      
   ValidateDirectory(sys.argv[1],Log)
   DisplayAllFileGivenExtention(sys.argv[1],sys.argv[2],Log)
   
   
if __name__ == "__main__":
   main()