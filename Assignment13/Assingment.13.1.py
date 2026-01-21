# Write a program which accepts lenght and width of rectagle and print area


def Area(length,width):
   
    Area = length * width
    print(Area)
def main():
   
   length = int(input("Enter lenght number : "))
   
   width = int(input("Enter width number : "))
   
   Area(length,width)
  
if __name__ == "__main__":
   main()