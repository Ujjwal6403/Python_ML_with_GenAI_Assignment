#Write a progrm which accept name from user and display lenght of its name.


def Display(Name):  
   count = 0 
   for i in Name:
      count = count + 1
   print(count)     
   
def main():
   Name = (input("Enter the number : "))
   
   Display(Name)

if __name__== "__main__":
   main()
