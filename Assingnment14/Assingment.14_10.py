#8>. Write a lambda function which accepts Three number and return Largest number .



# def largestNo(No1,No2,No3):
#    if(No1 > No2)and(No1 > No3):
#       return No1
#    elif ((No2 > No1) and (No2 > No3)):
#       return No2
#    else:
#       return No3

largestNo = lambda No1,No2,No3: (No1 if ( No1 > No2 and No1>No3) else No2 if (No2 > No1 and No2 > No3) else No3)

def main():
   No1 = int(input("Enter the First number : "))
   No2 = int(input("Enter the Second number : "))
   No3 = int(input("Enter the third numumber : "))
   
   
   
   ret = largestNo(No1,No2,No3)
   
   print("Multiplication is : ",ret)
  
   
if __name__ == "__main__":
   main()