# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors.
# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message: "Exit from main"

import threading

def EvenFactor(number):
   Sum = 0
   for i in range(1 , number+1):
      if(i % 2 == 0):
         Sum = Sum + i
   print("Summation of Even Factor : ",Sum)

def OddFactor(number):
   Sum = 0
   for i in range(1,number+1):
      if(i % 2 != 0):
         Sum = Sum + i
   print("Summation of Odd Factor : ",Sum)
   
def main():
   print("Inside a main Thread : ")
   No = int(input("Enter the number : "))
   
   t1 = threading.Thread(target=EvenFactor,args=(No,))
   t2 = threading.Thread(target=OddFactor,args=(No,))
   
   t1.start()
   t2.start()
   
   t1.join()
   t2.join()
   print("End of main thread")

if __name__ == "__main__":
   main()