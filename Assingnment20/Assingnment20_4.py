# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# Thread Name

import threading

def Small(name):
   icnt = 0
   for char in name:
      if char >= 'a' and char <= 'z':
         icnt = icnt +1
   print("Small character count is : ",icnt)
   
   print("Even Thread Name : ",threading.current_thread().name)
   print("Even Thread id :",threading.current_thread().ident)

def Capital(name):
   icnt = 0
   for char in name:
      if char >= 'A' and char <= 'Z':
         icnt = icnt +1
   print("Capital character count is : ",icnt)
   
   print("Even Thread Name : ",threading.current_thread().name)
   print("Even Thread id :",threading.current_thread().ident)
 
def Digit(name):
   icnt = 0
   for char in name:
      if char >= '0' and char <= '9':
         icnt = icnt +1
   print("digit character count is : ",icnt)
   
   print("Even Thread Name : ",threading.current_thread().name)
   print("Even Thread id :",threading.current_thread().ident)
   
def main():
   print("Inside a main Thread : ")
   
   print("Even Thread Name : ",threading.current_thread().name)
   print("Even Thread id :",threading.current_thread().ident)
   
   # no = int(input("Enter the Number of elemeent : "))
   
   Data = "UjjWAL Narkhede123"

   t1 = threading.Thread(target=Small,args=(Data,))
   t2 = threading.Thread(target=Capital,args=(Data,))
   t3 = threading.Thread(target=Digit,args=(Data,))
   
      
   
   t1.start()
   t2.start()
   t3.start()
   
   t1.join()
   t2.join()
   t3.join()
   print("End of main thread")

if __name__ == "__main__":
   main()