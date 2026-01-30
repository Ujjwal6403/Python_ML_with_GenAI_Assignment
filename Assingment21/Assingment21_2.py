# 2: Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.import time

import threading
import time
def MaxiMum(Data):
   Max = 0
   for No in Data:
      if(No > Max):
         Max = No
   print("Maximum Element is : ",Max)
         
def MiniMum(Data):
   Min = Data[1]
   for No in Data:
      if(No < Min):
         Min = No
   
   print("Minimum Element in : ",Min)
   
def main():
   
   print("Enter the size of List: ")
   No = int(input())
   
   Data = []
   
   for i in range(No):
      Element = int(input("Enter Element in List : "))
      Data.append(Element)
      
   print(Data)
   
   start_time  = time.time()
      
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
      
   
   