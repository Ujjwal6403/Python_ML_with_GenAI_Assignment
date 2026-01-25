# 1> write a lambda function using reduce() which accepts a list of number and return a list of  addition of all element .
# from functools import reduce
# num = [1,2,3,4]

# add = reduce(lambda x,y: x + y, num)

# print(add)

from functools import reduce

Addition = lambda x ,y: x + y

def main():
   num = [1,2,3,4,5]
   
   Add = reduce(Addition,num)
   print(Add)
   
if(__name__ =="__main__"):
   main()