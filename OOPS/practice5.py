class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j) # call constructor of parent class TwoDVector
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j  + {self.k}k")

v1 = TwoDVector(2, 3)
v1.show()
v2 = ThreeDVector(2, 3, 4)
v2.show()