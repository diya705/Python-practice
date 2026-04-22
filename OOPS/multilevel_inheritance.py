class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

e = Employee()
p = Programmer()
m = Manager()
print(e.a) # access variable a of class Employee
print(p.a, p.b) # access variable a of class Employee and variable b of class Programmer
print(m.a, m.b, m.c) # access variable a of class Employee and variable b of class Programmer and variable c of class Manager