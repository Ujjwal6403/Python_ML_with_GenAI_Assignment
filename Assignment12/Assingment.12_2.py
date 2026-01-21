# Write a program which accepts one number and prints its factors.

#input : 12
#output : 1,2,3,4,5,6,12

def Factors(ivalue):
   
   for i in range(1,ivalue+1):
      
      if((ivalue % i) == 0):
         
         print(i)
         
def main():
   
   iNo = int(input("Enter the character : "))
   
   Factors(iNo)

if __name__ == "__main__":
   main()