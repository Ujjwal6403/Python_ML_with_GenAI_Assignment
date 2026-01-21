# 1> Write a program which accepts one number and prints all odd number till that number.

# input :10 : output :1,3,5,7,9

def EvenNumber(ivalue):
   
   for i in range(1,ivalue+1):
      if((i % 2)!= 0):
         print(i)
  
def main():
   
   iNo = int(input("Enter the number : "))
   EvenNumber(iNo)
   
if __name__== "__main__":
   main()