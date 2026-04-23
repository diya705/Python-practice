class Employee:
    a = 1 # class atttribute of Employee class

    @classmethod  # to access class attribute value we need to use class method
    def show(cls): # for class method we need to use cls as parameter not self
        print(f"The class attribute of Employee class is: {cls.a}") # access class attribute a of Employee class using cls

e = Employee()
e.a = 10  # instance attribute of Employee class
e.show() # access class attribute a