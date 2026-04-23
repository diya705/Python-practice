class Animals:
    def __init__(self, type):
        self.type = type
class Pets(Animals):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
    def show(self):
        print(f"the pet name is {self.name} and it is a {self.type} Animals")

class Dogs(Pets):
    def __init__(self, name, type):
        super().__init__(name, type)
    def bark(self):
        print(f"{self.name} is barking")

a = Animals("Mammal")
p = Pets("Tommy", "mammal")
p.show()
d = Dogs("Tommy", "mammal")
d.bark()
