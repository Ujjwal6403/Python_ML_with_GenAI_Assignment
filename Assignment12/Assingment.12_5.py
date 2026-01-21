# Write a program which accepts one number and prints that many numbers in reverse order

# input : 5
# output : 54321

def Display(ivalue):
   
    for i in range(ivalue,0,-1):
       print(i)
       
def main():
   
   iNo = int(input("Enter First number : "))
  
  
   Display(iNo)
if __name__ == "__main__":
   main()