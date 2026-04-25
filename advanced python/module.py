# we can create our own module by creating an function and then import in any other file

def myFunc():
    print("hello world!")


if __name__ == "__main__":
    print("This code is run from the main file")
    myFunc()
    print(__name__)   # this is used to print the function type
    # if you run the module file and use this name then it print main means it is main type function


