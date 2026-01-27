#3> write a program which accept N number from user and store it into list. 
# return addition of all prime number form that list. 
# main Python file accepts N numbers from user and pass 
# each number to chkPrime() function which id part of our user defined module named as marvellousNum.
# name of the function from main python file should be listPrime().

def chkprime(Arr):
   sum = 0
   print(Arr)
   i = 2
   for num in Arr:
      for i in range(2,num+1):
         if(num % i == 0):
            break
      if(num == i):
         sum = sum + num
        
         
   return sum     

