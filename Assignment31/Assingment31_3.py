#Please follow below rules while designing automation script as 

# * Accept input through command line or through file.
# * Display any message in log file instead of console.
# * For separete task defin separate function.
# * For robustness handle evey expected exception.
# * perform validations before takign any action.
# * Create user defind module to store the functionality

# Q2>.Desing automation script which accept Two directory names.
# Copy all files from First Directory into second Directory, 
# second Directory should be created at run time.


# Usage : Directorycopy.py "Demo" "Temp"
# Demo is name directory which is existing and contains files in it. we have to create new Directory as temp and copy all files from Demo to temp.

import os 
import sys
def CreateLogFile():
   Log = open("LogFile.Log","w")
   return Log
   
def ValidationCheck(Directory, Log):
   Fobj = False
   Fobj = os.path.exists(Directory)
   
   if(Fobj  == False):
      Log.write("There is no Direcotory....")
      return
   
   Fobj = os.path.isdir(Directory)
   
   if(Fobj == False):
      Log.write("There is no such Directory...")
      return
      
def DirectoryCopy(Direcotry ,Temp):
   fobj = None
   for FolderName , SubFolderName, FileName in os.walk(Direcotry):
      for Fname in FileName:
         
         os.mkdir(Temp)
            
         Temp = os.path.join(FolderName,Fname)
               
def main():
   
   Log = CreateLogFile()
   
   if(len(sys.argv) != 3):
      Log.write("Invalid Input... ")
      Log.write("Please Enter the Valid Input at The time of Execution")
      return
   ValidationCheck(sys.argv[1],Log)
   DirectoryCopy(sys.argv[1],sys.argv[2])
   
if __name__ == "__main__":
   main()