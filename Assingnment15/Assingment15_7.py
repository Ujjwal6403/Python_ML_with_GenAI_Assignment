# 6> write a lambda function using filter() which accepts a list of Strings and return list of strings
# having lenght greater than 5.

# num = ["ujjwal","dipak","Rushikes","shubham"]

# String =  list(filter(lambda s: s if(len(s) > 5)else 0,num))

# print(String)


StringLenGreterThan5 = lambda s : s if(len(s) > 5)else 0

def main():
   num =  num = ["ujjwal","dipak","Rushikes","shubham"]
   
   strx = list(filter(StringLenGreterThan5,num))
   print(strx)
   
if(__name__ =="__main__"):
   main()