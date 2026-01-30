# 1: Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.
import time
import threading

def prime(Data):
   i = 0
   for No in Data:
      for i in range(2,No+1):
         if(No % i == 0):
            break
      if(No == i):
         print("Prime No is : ",No)
         
def NonPrime(Data):
   icnt = 0
   for No in Data:
      for i in range(1,No+1):
         if(No % i == 0):
            icnt = icnt + 1
      if(icnt > 2):
         print("Non_Prime No is : ",No)
      icnt = 0
         
   
def main():
   
   Data = [1, 2, 4, 3, 6, 7, 8, 9,19, 23] 
   
   t1 = threading.Thread(target=prime,args = (Data,))
   t2 = threading.Thread(target=NonPrime,args = (Data,))
   
   t1.start()
   t2.start()
   t1.join()
   t2.join()
   
   
   
      
if __name__=="__main__":
   main()
      
   
   