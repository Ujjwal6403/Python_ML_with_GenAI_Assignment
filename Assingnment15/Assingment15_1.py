# 1> write a lambda function using map() which accepts a list of number and return a list of square of each number .
Square = lambda x:x * x
 
def main():
   num = [10,20,30,40]

   SquareNo =list(map(Square,num))

   print(SquareNo)

if __name__ =="__main__":
   main()
