#Please follow below rules while designing automation script as 

# * Accept input through command line or through file.
# * Display any message in log file instead of console.
# * For separete task defin separate function.
# * For robustness handle evey expected exception.
# * perform validations before takign any action.
# * Create user defind module to store the functionality

# Q2>.Desing automation script which accept directory name and two file extensions from user.
# Rename all files with first File extention with the second file extention.

# Usage : DirectoryFileSearch.py "Demo" ".txt" ".doc"
# Demo is name directory and .txt is the extension that we want to search.

import os 
import sys

def CreateLog():
   fobj = open("Marvellous.Log","w")
   return fobj

def ValidateDirectory(DiracotoryName ,Log):
      obj  = os.path.exists(DiracotoryName)
      
      if(obj == False):
         Log .write("There is no Directory name :")
         return
      
      obj = os.path.isdir(DiracotoryName)
      
      if(obj == False):
         Log.write("Ther is no such directory ")
         return

def DirectoryfileRenamewithExtention(DirectoryName,Ext1,Ext2,Log):

   for FolderName, SubFolder,FileName in os.walk(DirectoryName):
      for Fname in FileName:
         OldFile = os.path.join(FolderName, Fname)
         NewName = Fname.replace(Ext1,Ext2)
         NewFile = os.path.join(FolderName, NewName)
         os.rename(OldFile,NewFile)
         
         Log.write(f"Renamed : {Fname} to {NewFile}\n")
   
def main():
   
   
   Log = CreateLog()
   # DirectoryName = input("Enter the Directory name :")
   
   # Ext1 = input("Enter the Extention1 : ")
   # Ext2 = input("Enter the Extention2  :  ")
   
   if(len(sys.argv) != 4):
      Log.write("Invalid Input : ")
      Log.write("Enter the valid input : ")
      
   
   
   ValidateDirectory(sys.argv[1],Log)
   
   
   DirectoryfileRenamewithExtention(sys.argv[1],sys.argv[2],sys.argv[3] ,Log)
   
   
if __name__ =="__main__":
   main()