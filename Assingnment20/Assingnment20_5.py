# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronizatio

import threading

def Assending(No):
      for i in range(1,No+1):
         print("Number in Assending order is",i)
      
    
def Desending(No):
      for i in range(No,0,-1):
         print("Desendig is : ",i)
      

def main():
   print("Inside a main Thread : ")
   
   no = int(input("Enter the Number of elemeent : "))

   # Assending(no)
   # Desending(no)
   t1 = threading.Thread(target=Assending,args=(no,))
   t2 = threading.Thread(target=Desending,args=(no,))

   t1.start()
   t1.join()
   
   t2.start()
   t2.join()
  
   print("End of main thread")

if __name__ == "__main__":
   main()