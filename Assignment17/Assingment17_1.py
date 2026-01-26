# Create on module named as arithmatic which contain 4 fuctions as
# add() from addtion, sub() fro substaction, Mult() for Multiplication and div()division.
# All functions accepts two parameters as number and perform the operation. write on python program 
# which call all the function from arithmetic module by accepting the parameters from user.
import Arithmatic

iNo1 = int(input("Enter the First Number"))
iNo2 = int(input("Enter the second Number"))

Result = 0

Result = Arithmatic.Add(iNo1,iNo2)
print("Addition is : ",Result)
Result = Arithmatic.Div(iNo1,iNo2)
print("Division is : ",Result)
Result = Arithmatic.Mul(iNo1,iNo2)
print("Multiplication is : ",Result)
Result = Arithmatic.Sub(iNo1,iNo2)
print("substaction is : ",Result)
