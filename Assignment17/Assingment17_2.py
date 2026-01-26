# 2 write a program which accept one number and display below pattan.
# input = 5
# output :  # * * * * *
            # * * * * *
            # * * * * *
            # * * * * *
            # * * * * *

def Display(No):
   for i in range(No):
      for j in range(No):
         print("*",end=" ")
      print("")
         
def main():
   No = int(input("Enter the Row :"))
   
   
   Display(No)

if __name__=="__main__":
   main()