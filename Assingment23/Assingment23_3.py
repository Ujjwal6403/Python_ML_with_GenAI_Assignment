
# 3: Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:Value
# Define a constructor (init) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime() returns True if the number is prime, otherwise returns False
# ChkPerfect()returns True if the number is perfect, otherwise returns False
# Factors()-displays all factors of the number
# SumFactors()-returns the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.
#########################################################################################################

class Number:
   
   def __init__(self):
      self.Value = self.Number = int(input("Enter the number:"))
      
   def CheckPrime(self):
      for i in range(2,self.Value+1):
         if((self.Value % i) == 0):
            break
      if self.Value == i:
         return True
      else:
         return False
      
   def ChkPerfect(self):
      sum= 0
      self.temp = self.Value//2
      for i in range(1,self.temp+1):
         if(self.Value % i == 0):
            sum = sum + i
         
      if(sum == self.Value):
         return True
      else:
         return False
   
   def Factor(self):
      for i in range(1,self.Value+1):
         if(self.Value % i == 0):
            print("Factor of sum is : ",i)
   
   def SumFactor(self):
      sum = 0
      for i in range(1,self.Value+1):
         if(self.Value % i == 0):
            sum = sum + i
      return sum
   
   
obj1 = Number()
ret = 0
ret = obj1.CheckPrime()
if(ret == True):
   print("it is a prime number : ",obj1.Value)
else:
   print("it is not prime number : ",obj1.Value)

ret = obj1.ChkPerfect()
if(ret == True):
   print("It is a perfect number : ",obj1.Value)
else:
   print("It is not perfect number : ",obj1.Value)
   
obj1.Factor()

ret = obj1.SumFactor()
print("Summation of factor : ",ret)
