# .8.> write a program which accept one number and display below pattern.
# input = 5
# output = 1 
#          1 2 
#          1 2 3 
#          1 2 3 4 
#          1 2 3 4 5


def Display(No):
   for i in range(1,5+1):
      for j in range(1,5+1):
         if(i >= j):
            print(j,end=" ")
            
      print("")
         
def main():
   No = int(input("Enter the Row :"))
   
   
   Display(No)

if __name__=="__main__":
   main()