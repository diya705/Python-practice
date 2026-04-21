s = {} # this {} creates a dictionary, not a set
print(type(s))

a = set() # this set() creates a set, not a dictionary, and it is empty
print(type(a))

b = set("Diya") # this creates a set of unique characters from the string "Diya"
print(b, type(b))

c = {1, 2, 3, 2, 5, 6, 7, 6}
print(c, type(c)) #this create a set of unique numbers, duplicates are removed and the order is not guaranted

d = {1, 2, 3, 1, "Diya", "yes"}
print(d, type(d))

d.add("No")
print(d, type(d)) # this add the element "No" to the set d 

f = {1, 2, 3, 4, 5}
print(len(f)) # this prints the length of the set f, which is 5 
f.remove(3)
print(f) # this removes the element 3 from the set f and prints the remaining elements
s.clear() # this clears all the elements from the set s, making it an empty set
print(s) # this prints the empty set s, which is set()

x1 = {1, 2, 4, 5}
x2 = {4, 5, 6, 7}
print(x1.union(x2)) # this prints the union of sets x1 and x2, which is {1, 2, 4, 5, 6, 7}
print(x1. intersection(x2)) # this prints the intersection of sets x1 and x2, which is {4, 5}
print(x1. difference(x2)) # this prints the difference of sets x1 and x2, which is {1, 2}
print(x1. symmetric_difference(x2)) # this prints the symmetric difference of sets x1 and x2, which is {1, 2, 6, 7}