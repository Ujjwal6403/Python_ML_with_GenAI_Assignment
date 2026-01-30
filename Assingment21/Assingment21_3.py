# 3: Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.
# 10: Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.


import threading
import time
def SumOfList(Data):
   for no in Data:
      Sum = Sum + no
   
   return Sum
         
def ProductOfList(Data):
   for No in Data:
      Product = Product * No
   return Product   
def main():
   
   Data = [10,20,30,40,50,60]
      
   t1 = threading.Thread(target=MaxiMum,args = (Data,))
   t2 = threading.Thread(target=MiniMum,args = (Data,))
  
   t1.start()
   t1.join()
   t2.start()
   t2.join()
   
   end_time = time.time()
   print("Time Required : ",end_time - start_time)
   print("End of main Thread : ")
   
      
if __name__=="__main__":
   main()
      
   
   