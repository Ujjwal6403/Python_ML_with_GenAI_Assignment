# 1> Write a program which accepts one number and prints reverse of that number

# input :123: output :321

# def Reverse(ivalue):   
#    Digit = 0
#    rev = []
#    while(ivalue != 0):
#       Digit = ivalue % 10
#       rev.append(Digit)
#       ivalue = ivalue//10
#    print(rev)
# def main():
#    iNo  = int(input("Enter the number : "))
   
#    Reverse(iNo)

# if __name__ == "__main__":
#    main()
   
   
def Reverse(ivalue):   
   Digit = 0
   rev = 0
   while(ivalue != 0):
      Digit = ivalue % 10
      rev = (rev * 10) + Digit
      ivalue = ivalue//10
   print(rev)
def main():
   iNo  = int(input("Enter the number : "))
   
   Reverse(iNo)

if __name__ == "__main__":
   main()
   
   