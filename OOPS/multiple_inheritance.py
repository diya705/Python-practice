class Employee:
    name = "Diya"
    salary = 50000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def lang(self):
        print(f"The language is {self.language}")

# inherit from multiple parent class Employee and Cod er
class Programmer(Employee, Coder):  #inheritance from parent class Employee
    pass

class language(Employee, Coder):
    def multiple_inherit(self):
        print(f"The name is {self.name} and the salary is {self.salary} and the language is {self.language}")

e = Employee()
p = Programmer()
l = language()
e.show()
p.show() # also use show function of parent class because of inheritance and give same answer as parent class because we have not change any value in child class
p.lang() # use lang function of parent class Coder
l.multiple_inherit() # use multiple_inherit function of parent class language and take value from parent class Employee and Coder because of inheritance