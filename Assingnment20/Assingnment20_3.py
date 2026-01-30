# 3: Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
# Extract all even elements from the list.
# Calculate and display their sum.
# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum.
# Threads should run concurrently.

import threading

def EvenList(number):
   Sum = 0
   for i in number:
      if(i % 2 == 0):
         Sum = Sum + i
   print("Summation of Even Factor : ",Sum)

def OddList(number):
   Sum = 0
   for i in number:
      if(i % 2 != 0):
         Sum = Sum + i
   print("Summation of Odd Factor : ",Sum)
   
def main():
   print("Inside a main Thread : ")
   list = []
   No = int(input("Enter the Number of elemeent : "))
   for _ in range(No):
      n = int(input("Enter the element of list : "))
      list.append(n)


   t1 = threading.Thread(target=EvenList,args=(list,))
   t2 = threading.Thread(target=OddList,args=(list,))
      
   
   t1.start()
   t2.start()
   
   t1.join()
   t2.join()
   print("End of main thread")

if __name__ == "__main__":
   main()