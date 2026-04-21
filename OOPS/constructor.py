import os
class Employee:
    name = "Diya" 
    age = 22
    
    def __init__(self, name, age, salary, language):
        self.name = name
        self.age = age
        self.salary = salary
        self.language = language
        print(f"name: {name}, salary: {salary}, age: {age}, language: {language}")

e = Employee("Diya", 21, 12000000, "Python")
print(e.salary, e.name, e.age, e.language)
