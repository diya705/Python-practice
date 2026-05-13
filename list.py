# in list we can store multiple types of data and we can change the data in list because list is mutable.
friends = ["Rolf", "Bob", "Jen", 123, True]
print(friends[0]) # Rolf

# append method is used to add an element at the end of the list.
friends.append("yes")
print(friends)

# sort method is used to arrange the list in the ascending order.
num = [5, 2, 9, 1]
num.sort()
print(num)

a = [3, 1, 9, 2, 8, 4]
a.reverse()
print(a)

# insert method is used to add an element at a specific index.
a.insert(2, 10) 
print(a)

# pop method is used to remove an element from the list. By default it removes the last element, but we can also specify the index of the element to be removed.
x = a.pop()
print(x)
print(a)

y = a.pop(1)
print(y)
print(a)

# remove method is used to remove the first occurrence of a specific element from the list.
a.remove(9)
print(a)

# list comprehension
# The Python Solution (List Comprehension)
# To solve this in one line (which is the point of the exercise), you use a nested loop inside brackets:
x = 1
y = 1
z = 1
n = 2

# List comprehension syntax
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]