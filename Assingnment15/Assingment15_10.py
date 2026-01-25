# 10> write a lambda function using filter() which accepts a list of number and return
# count of even nummber


# num = [1,2,3,4,5]

# counteven = len(list(filter(lambda No1: No1 % 2 == 0,num)))

# print(counteven)


CountEvenNo =  lambda No : No % 2 == 0

def main():
   Num = [1,2,3,4,5,6,8,10]
   
   CountEven = list(filter(CountEvenNo,Num))
   
   print(len(CountEven))
   
if __name__=="__main__":
   main()