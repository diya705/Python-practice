class Employee:
    a = 1 # class atttribute of Employee class

    @classmethod  # to access class attribute value we need to use class method
    def show(cls): # for class method we need to use cls as parameter not self
        print(f"The class attribute of Employee class is: {cls.a}") # access class attribute a of Employee class using cls

    @property # to access method as attribute we need to use property decorator
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter # to set value to method we need to use setter decorator
    def name(self, name):
        self.fname = name.split(" ")[0] # split the name into first name and last name and assign to fname and lname
        self.lname = name.split(" ")[1]

e = Employee()
e.a = 10  # instance attribute of Employee class
e.show() # access class attribute a

e.name = "Diya Agarwal" # set value to name method using setter decorator
print(e.name) # access name method as attribute using property decorator