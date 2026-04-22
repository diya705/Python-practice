class Employee:
    a = 1
    def __init__(self):
        print("This is constructor of Employee class")
class Programmer(Employee):
    b = 2
    def __init__(self):
        super().__init__() # call constructor of parent class Employee
        print("This is constructor of Programmer class")
class Manager(Programmer):
    c = 3
    def __init__(self):
        print("This is constructor of Manager class")

e = Employee()
p = Programmer()
m = Manager()
print(e.a) # access variable a of class Employee
print(p.a, p.b) # access variable a of class Employee and variable b of class Programmer
print(m.a, m.b, m.c) # access variable a of class Employee and variable b of class Programmer and variable c of class Manager