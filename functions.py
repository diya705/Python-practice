def avg():  # this create an fuction (Function Definition)
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    avg = int(a+b+c)/3
    print(f"average is: {avg}")

avg() # This is call the function to perform (Function Call)
print("Thanks")


# Functions with Arguments
def goodday(name):  # name is the argument
    print("Good Day "+ name)

goodday("Diya")  # we call function with passing argument value

# Function with more than 1 arguments
def goodday(name, ending): 
    print("Good day " + name )
    print(ending)

goodday("Diya", "Thanks") # in function call we can pass values for more than one arguments together

# Function with return value 
def goodday(name, ending):
    print("Good day " + name )
    print(ending)
    return "Ok"   # return is used to take  and go with some value from the function and return/give to the variable which one call that function

a = goodday("Diya", "Thanks")
print (a)

# Also we give any method or formula or any operation value to the return 
def avg():  # this create an fuction (Function Definition)
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    avg = int(a+b+c)/3
    return avg 

a = avg() # This is call the function to perform (Function Call)
print("average by return is: ", a)

# Default Parameter value in function 
def goodday(name, ending = "Done"):
    print("Good day " + name )
    print(ending)

goodday("Diya") # if ending argument value is not pass then take by defalut value Done
goodday("Hii", "Pass ending value") # and if we pass the ending argument value then it not take by default value take pass value

