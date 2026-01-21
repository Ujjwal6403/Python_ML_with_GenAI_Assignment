# Write a program which accepts marks and display greade.


def DisplayGrade(ivalue):
   if(ivalue >= 75):
      print("Distictin")
      
   elif(ivalue >= 60):
      print("First class")
      
   elif(ivalue >= 50):
      print("Second class")
   elif(ivalue < 50):
      print("Fail")
      
def main():
   
   iNo = int(input("Enter the number : "))
 
   DisplayGrade(iNo)

  
if __name__ == "__main__":
   main()