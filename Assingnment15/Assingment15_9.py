# 9> write a lambda function using reduce() which accepts a list of number and return
# Product of all element
# from functools import reduce

# num = [1,2,3,4,5]

# product =  reduce(lambda No1 ,No2: No1 * No2,num)

# print(product)

from functools import reduce

productOfAllElement =  lambda x,y : x * y

def main():
   Num = [1,2,3,4,5]
   
   product = reduce(productOfAllElement,Num)
   
   print(product)
   
if __name__=="__main__":
   main()