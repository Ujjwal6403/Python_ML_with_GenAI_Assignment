# 1> Write a program which contains one lambda function which accepts one parameter and return power of two.

#input : 4     Output : 16
#input : 6     Output : 64

def PowerOfTwo(x):
   power = 1
   for i in range(1 ,x+1):
      power= power * 2
   return power
def main():
   No = int(input("Enter the number : "))
   
   Ret = PowerOfTwo(No)
   
   print("Power of two is : ",Ret)
if __name__=="__main__":
   main()