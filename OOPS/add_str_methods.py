class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2): #  add dunder method used to add the parameters 
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self): # string dunder method used to convert add value into readable string
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)