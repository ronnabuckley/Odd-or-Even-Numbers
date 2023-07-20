#Ronna Buckley
#Program to check evn or odd number

#program title
print("Check If Even or Odd Number Program")

#Ask user to enter a number
num1 = int(input("Enter a number to check if it is even or odd: "))

#Use modulus operator to check if remainder is even or odd
remainder = num1 % 2

#if remainder = 0 then it is even, else the value determines it is odd
if(remainder == 0):
  print(num1, " is an even number.")
else:
  print(num1, " is an odd number.")