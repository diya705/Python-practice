from random import randint # write from random because now we directly call randint() methoud without using random module name
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, start, end):
        print(f"Your ticket is booked from {start} to {end} in train number {self.trainNo}")

    def status(self):
        print(f"train number {self.trainNo} is on time")

    def fare(self):
        print(f"The fare of train number {self.trainNo} is {randint(100, 1000)}")  # directly call randint() method to generate a random fare between 100 and 1000

t = Train(12435)
t.book("Delhi", "Mumbai")
t.status()
t.fare()
