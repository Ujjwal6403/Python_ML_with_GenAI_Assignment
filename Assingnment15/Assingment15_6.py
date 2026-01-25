# 6> write a lambda function using reduce() which accepts a list of number and return manimum element.

# from functools import reduce

      
# num = [1,32,3,4]

# minmum = reduce(lambda No1 ,No2: No1 if(No1 < No2)else No2,num)

# print(minmum)

from functools import reduce

Minimum_No = lambda x ,y:x if x < y else y

def main():
   num = [1,32,3,4,0]
   
   Min = reduce(Minimum_No,num)
   print(Min)
   
if(__name__ =="__main__"):
   main()