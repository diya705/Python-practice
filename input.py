import math
a = input("Enter number 1: ") # input is using to take the input from the user and store it in a variable
b = input("Enter number 2: ") # input is using to take the input from the user and store it in a variable
print("Number a or 1 is:", a)
print("Number b or 2 is:", b)

# Typecasting the input to integers
a = int(a)
b = int(b)

print("The sum is:", a+b) 

# another way to add the numbers taking input from the user 
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print("The sum is:", a+b)

# e = int(input("Enter number e: ")) # this will give an error because we cannot specify the type of variable while taking input from the user

x = int(input("Enter x: "))
y = math.pow(x, 2)
print("The square of x is: ", y)