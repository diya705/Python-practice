class Programmer:
    company = "Employee"
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"name: {name}, salary: {salary}, age: {age}")

p = Programmer("Diya", 21, 12000000)
print(p.salary, p.name, p.age, p.company)