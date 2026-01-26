
# Write a program which accept one number and display below pattern.
#input : 5 
# Output:         # * * * * *
                  # * * * *
                  # * * *
                  # * *
                  # *

def Display(No):
   for i in range(No+1):
      for j in range(No+1):
         if(i < j):
            print("*",end=" ")
            
      print("")
         
def main():
   No = int(input("Enter the Row :"))
   
   
   Display(No)

if __name__=="__main__":
   main()