# we write tuple in the paranthesis/brackets and we write list in the square brackets. tuple is immutable and list is mutable 
a = (1, 2, 3, "hii", True)
print(a)
print(type(a))

# count method is used to count the number of occurrences of a specific element in the tuple.
print(a.count(2))

# index method is used to find the index of the specific element in the tuple 
print(a.index("hii"))

# index method also used to find the specific element  by giving index number as an argument. if the index number is out of range then it will give an error.
print(a[1])