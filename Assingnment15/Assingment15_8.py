# 8> write a lambda function using filter() which accepts a list of number and return
# list of numbers divisible by both 3 and 5.


# num = [10,20,30,15,25]

# divisible =  list(filter(lambda No: No if(No % 5 == 0)and (No % 3 == 0)else 0,num))

# print(divisible)




Divisible_3and5 = lambda No: No if (No % 5 == 0)and(No % 3 == 0)else 0

def main():
   num = [1,2,3,4,15,30]
   
   dibisible = list(filter(Divisible_3and5,num))
   print(dibisible)
   
if(__name__ =="__main__"):
   main()
   
   