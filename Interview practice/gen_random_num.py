import random
# print any random number
num = random.random()
print(num)
# print int type random number in specific range 
num_int = random.randint(1, 100)
print(num_int)
# print float type random number in specific range 
num_float = random.uniform(1, 100)
print(num_float)
# print random num in range with incremental step
num_step = random.randrange(1, 100, 5)
print(num_step)
# print series of random numbers
numlist = random.sample(range(1, 100), 5)
print(numlist)