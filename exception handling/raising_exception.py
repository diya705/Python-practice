# using 'raise' word we can raise any type of error 

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b ==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"the divisio a/b is {a/b}")