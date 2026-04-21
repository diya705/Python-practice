class Employee:  # define name of class
    name = "Diya"  # assign the value to variable (class attribute)
    age = 22

    #dunder method _init_ method call automatically without calling this method
    def __init__(self):
        print("I am creating an object and this function calls automatically")


    # we create a function in the class
    def getInfo(self):  # pass 'self' agrument/object and take reference of function object when call class attributes
        print(f"The name is {self.name}. The salary is {self.salary}. The age is {self.age}")

    # staticmethod is only used when we don't call any class attributes in that function
    @staticmethod  # write static method because we don't want to create an object of this function like getInfo method
    def greet(): # we don't pass self object because we don't call any class attribute
        print("Good morning")

    

    

e = Employee()  # create an object of class Employee
e.salary = 50000  # assign the value to variable (object attribute/instance attribute)
print(e.name, e.age, e.salary) # access the class attribute by using object name and dot operator
e.getInfo() # call the function using the object reference of class Employee 
e.greet() # call the static method function without self object so it not give any error

a = Employee()  # create different another object of the same class
a.salary = 1000000 
print(a.name, a.age, a.salary)
# Here salary is an instance attribute and name and age are class attributes as thet directly belong to the class

# instance attributes have high preference than class attributes
b = Employee()
b.age = 21  # instance attributes have high preference than class attributes 
print(b.name, b.age)
