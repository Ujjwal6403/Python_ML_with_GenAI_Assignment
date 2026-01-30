# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Valuel and Value2.
# Define a constructor (init) that initializes all instance variables to 0.
# Implement the following instance methods:
# Accept()-accepts values for Value1 and Value2 from the user.
# Addition()returns the addition of Valuel and Value2.
# Subtraction() returns the subtraction of Valuel and Value2.
# Multiplication() returns the multiplication of Valuel and Value2.
# Division()-returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.


class Arithmetic:
   
   def __init__(self):
      self.Value1 = 0
      self.Value2 = 0
      
   def Accept(self):
      self.Value1 = int(input("Enter the Value1 "))
      self.Value2 = int(input("Enter the Value2  "))
      
   def Addition(self):
      
      return (self.Value1 + self.Value2)
   
   def Substaction(self):
      sub = self.Value1 - self.Value2
      return sub
   
   def Multiplication(self):
      return (self.Value1 * self.Value2)
   
   def Division(self):
      
      try:
         
         return (self.Value1 // self.Value2)
      
      except(ZeroDivisionError):
         print("Inside zero devision Error : ")
        
   
obj1 = Arithmetic()
Ret = 0
obj1.Accept()

Ret = obj1.Addition()
print("Addition is : ",Ret)

Ret = obj1.Substaction()
print("Substaction is : ",Ret)

Ret = obj1.Multiplication()
print("Multiplication is ",Ret)

Ret = obj1.Division()
print("Division is : ",Ret)

   
   
   
      
      
   
      