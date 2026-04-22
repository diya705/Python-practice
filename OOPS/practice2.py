
import math

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    def square_root(self):
        print(f"The square root of {self.n} is {self.n**0.5}")
        print(f"The square root of {self.n} is {math.sqrt(self.n)}")  # write the square root using sqrt() method from math module 


c = Calculator(3)
c.square()
c.cube()
c.square_root()