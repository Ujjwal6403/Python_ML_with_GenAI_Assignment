import threading
import time

def Assending(No):
   for i in range(1,No+1):
      print("Number in Assending order is",i)
      
      
def Desending(No):
   for i in range(No+1,0,-1):
      print("Desendig is : ",i)
      

t1 = threading.Thread(target=Assending,args=(50,))
t2 = threading.Thread(target=Desending,args=(50,))

t1.start()
t2.start()