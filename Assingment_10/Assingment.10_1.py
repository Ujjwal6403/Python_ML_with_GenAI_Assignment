# 1> Write a program which accepts one number and prints multiplcationo table of that number.


# input :4 : output : 4,8,12,16,20,24,28,32,36,40

def MultiplicationTable(ivalue):
   print("Multiplication table :")
   for i in range(1,10+1):
    
      print( ivalue * i)
   
 
def main():
   iNo = int(input("Enter the number : "))
   
   MultiplicationTable(iNo)
   
if __name__== "__main__":
   main()