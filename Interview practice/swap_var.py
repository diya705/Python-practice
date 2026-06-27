# Traditional method for swap
x = input("Enter X number: ")
y = input("Enter Y number: ")

temp = x
x = y
y = temp
print(f"After Swapping: X = {x}, Y = {y} ")

# Using tuple unpacking for swap
x = input("Enter X number: ")
y = input("Enter Y number: ")
x, y = y, x
print(f"After Swapping using tuple unpacking: X = {x}, Y = {y}")

