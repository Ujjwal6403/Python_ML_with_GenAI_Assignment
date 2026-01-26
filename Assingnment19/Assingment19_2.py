# 1> Writet a program which contains one lambda function which accepts two  parameter and return its mulitplicattion.

#input : 4    3 Output : 12
#input : 6    3 Output : 18

Multiplication = lambda x , y : x * y

def main():
   No1 = int(input("Enter the First number : "))
   No2 = int(input("Enter the seocnd number"))
   
   Ret =Multiplication(No1,No2)
   
   print("Multiplication : ",Ret)
if __name__=="__main__":
   main()