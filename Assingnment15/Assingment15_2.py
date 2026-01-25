# 1> write a lambda function using filter() which accepts a list of number and return a list of of even number .

# num = [5,20,30,40]

# data = list(filter(lambda x: x % 2 == 0,num))

# print(data)
Even_No = lambda x:x % 2 == 0

def main():
   num = [1,2,3,4,5]
   
   Even = list(filter(Even_No,num))
   print(Even)
   
if(__name__ =="__main__"):
   main()
   
   