class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): # operator overloading for + operator
        return self.n + num.n # add the value of n of both the objects and return the result
    
n = Number(5)
m = Number(10)
print(n + m) # add the value of n of both the objects using + operator