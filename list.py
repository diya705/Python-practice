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