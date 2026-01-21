# Write a program which accepts radius of circle and prints area of circle.


def AreaOfCircle(radius):
   pi = 3.14
   Area = pi * (radius*radius)
   print(Area)
def main():
   
   radius = int(input("Enter lenght number : "))
   
   
   AreaOfCircle(radius)
  
if __name__ == "__main__":
   main()