# write a program which accept number from user and print that number of * on scrren.


def Display(No):
   for i in range(No):
      print("*",end=" ")
  
def main():
   No = int(input("Enter the number : "))
   
   Display(No)

if __name__== "__main__":
   main()
