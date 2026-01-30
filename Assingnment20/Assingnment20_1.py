# 1: Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module
# Ensure proper thread creation and execution.


import threading
import time

def Even(number):
   for i in range(1 , number+1):
      print(i * 2)
   print("Even Thread Name : ",threading.current_thread().name)
   print("Even Thread id :",threading.current_thread().ident)

def Odd(number):
   for i in range(1,number+number):
      if(i % 2 != 0):
         print(i)
         
   print("Old Thread Name :",threading.current_thread().name)
   print("Odd Thread id :",threading.current_thread().ident)
         

def main():
   No = int(input("Enter the number : "))
   
   print("Main thread Name : ",threading.current_thread().name)
   print("Main Thread id :",threading.current_thread().ident)
   
   t1 = threading.Thread(target=Even,args=(No,))
   t2 = threading.Thread(target=Odd,args=(No,))
   
   t1.start()
   t2.start()
   
   # t1.join()
   # t2.join()
   print("End of main thread")

if __name__ == "__main__":
   main()