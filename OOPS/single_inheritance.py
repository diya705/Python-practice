class Employee:
    name = "Diya"
    salary = 50000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):  #inheritance from parent class Employee
    pass

e = Employee()
p = Programmer()
e.show()
p.show() # also use show function of parent class because of inheritance and give same answer as parent class because we have not change any value in child class