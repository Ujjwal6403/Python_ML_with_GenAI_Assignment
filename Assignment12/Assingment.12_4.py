# Write a program which accepts one number and prints that many numbers starting from 1.

# input : 5
# output : 12345

def Display(ivalue):
   
    for i in range(1,ivalue+1):
       print(i)
       
def main():
   
   iNo = int(input("Enter First number : "))
  
  
   Display(iNo)
if __name__ == "__main__":
   main()