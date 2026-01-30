# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (init) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display()-displays account holder name and current balance
# Deposit()-accepts an amount from the user and adds it to balance
# Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest()-calculates and returns interest using formula: Interest (Amount ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccout:
   ROI = 10.5
   def __init__(self):
      self.name = input("Enter the name ")
      self.Amount = 0
      
   def Display(self):
      print("Accout holder name : ",self.Amount)
      print("Current balance ",self.Amount)
   
   def Deposit(self):
      self.Amount = float(input("Enter the amount "))
      
      self.Balance = self.Balance + self.Amount
      
   
   def Withdrow(self):
      self.Amount = float(input("Enter the ammount"))
      if(self.Balance > self.Amount):
         self.Balance = self.Balance - self.Amount
      
   def CalculateInterest(self):
      return (self.Amount * self.ROI) / 100

obj1 = BankAccout()

obj1.Display()
obj1.Deposit()
obj1.Withdrow()
obj1.CalculateInterest()


     

