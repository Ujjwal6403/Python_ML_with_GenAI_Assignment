# 1> Write a program which accepts one number and prints all even number till that number.

# input :10 : output :2,4,6,8,10

def EvenNumber(ivalue):
   
   for i in range(1,ivalue+1):
      if((i % 2)== 0):
         print(i)
  
  
def main():
   
   iNo = int(input("Enter the number : "))
   EvenNumber(iNo)
   
if __name__== "__main__":
   main()