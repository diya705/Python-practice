from functools import reduce

# Map Example 
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)  # map(function name, list var )
print(list(sqList))

# Filter Example

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even, l)  # filter used to filter the things which are matchgh with our condition and print only that things filter(fun name, list var)
print(list(onlyEven))

# Reduce Example 
sum = lambda a,b: a+b

print(reduce(sum, l))  # works like 1+2=3 3+3=6 6+4=10 10+5 = 15
