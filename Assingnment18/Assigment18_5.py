#3> write a program which accept N number from user and store it into list. 
# return addition of all prime number form that list. 
# main Python file accepts N numbers from user and pass 
# each number to chkPrime() function which id part of our user defined module named as marvellousNum.
# name of the function from main python file should be listPrime().


# input : Number of elements : 11
# input elements : 13 5 45 7 4 56 10 34 2 5 8

# output : 54(13 + 5 + 7 + 2 + 5)

import MarvellouseNum

def main():
   print("Enter the No of element : ")
   Size = int(input())
   
   Data = list()
   print("Enter the elements :")
   
   for i in range(Size):
      value = int(input())
      Data.append(value)
   
   print(Data)
   
   Ret = MarvellouseNum.chkprime(Data)
   
   print("addition is prime number :  ",Ret)

if __name__=="__main__":
   main()