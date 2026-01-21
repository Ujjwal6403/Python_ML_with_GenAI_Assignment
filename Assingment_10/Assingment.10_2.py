# 1> Write a program which accepts one number and prints sum of First N natural number

# input :5 : output :15

def SumOfNaturalNo(ivalue):
   Sum = 0
   for i in range(ivalue+1):
      Sum = Sum + i
   return Sum
      
def main():
   iNo = int(input("Ente the number "))
   
   Sret = SumOfNaturalNo(iNo)
   print("The sum of natural no is ",Sret)
   
if __name__== "__main__":
   main()