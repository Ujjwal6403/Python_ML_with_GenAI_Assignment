# Q5 > Frequency of a String in File

# Problem Statement : 
# Write a program which accept a File name and one String from the user and return the frequency(count of occurences ) of that String in the file.


# Input :  
 #  Demo.txt  Marvellous
 
# Expected Output: Count how many times "Marvellous" appears in Demo.txt.
import os
# import sys

def FrequencyOfAStrigInFile(String):
   
   Ret  = os.path.exists("Demo.txt")
   if(Ret == False):
      print("There is no such File")
      return
   Fobj = open("Demo.txt","r")
   Data = Fobj.read()
   Count = Data.count(String)
         
   Fobj.close()
   return Count

def main():
   String = input("Enter the String : ")
   Ret = FrequencyOfAStrigInFile(String)
   
   print("Marvellous Count in a String is :",Ret)
   
if __name__ == "__main__":
   main()


   