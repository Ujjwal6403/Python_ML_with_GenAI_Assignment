# 5> write a lambda function using reduce() which accepts a list of number and return maximum element.

# from functools import reduce

      
# num = [1,32,3,4]

# maximum = reduce(lambda No1 ,No2: No1 if(No1 > No2)else No2,num)


# print(maximum)

from functools import reduce

Maximum_No = lambda x ,y:x if x > y else y

def main():
   num = [1,32,3,4,5]
   
   Max = reduce(Maximum_No,num)
   print(Max)
   
if(__name__ =="__main__"):
   main()