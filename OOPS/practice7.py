class Emoployee:
    salary = 234
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ( (salary/self.salary) -1) * 100
        print(f"the increment percentage is {self.increment}%")

e = Emoployee()
e.salaryAfterIncrement = 257
print(e.salaryAfterIncrement)