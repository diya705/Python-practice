# . Python Lists (Most Common)
# What most people call an "array" in Python is actually a list.
# Does it have .sort()? Yes.
# How it works: It sorts the list in-place (changes the original list) and returns None.
# python

my_list = [3, 1, 2]
my_list.sort()
print(my_list) # Output: [1, 2, 3]

# The array module (Standard Library)
# Python has a built-in array.array type for storing purely numerical data efficiently.
# Does it have .sort()? No.
# How to sort it: You must use the built-in sorted() function, which returns a new list, or convert it to a list, sort it, and convert it back.
# python

import array
my_arr = array.array('i', [3, 1, 2])
# Option 1: returns a new list
sorted_list = sorted(my_arr)
# Option 2: sort and update original
sorted_arr = array.array('i', sorted(my_arr))

# 3. NumPy Arrays (numpy.ndarray)
# If you are doing data science or heavy math, you are likely using NumPy.
# Does it have .sort()? Yes.
# How it works: Similar to lists, arr.sort() modifies the NumPy array in-place.
# python

import numpy as np
arr = np.array([3, 1, 2])
arr.sort()
print(arr) # Output: [1 2 3]

# . Python Lists (Standard Arrays)
# If you're using a standard list like my_list = [1, 2, 3], len() is the most efficient and standard method.
# Replit
# Replit
# Syntax: len(my_list)
# Performance: It is an O(1) constant-time operation because Python stores the size of the list internally and doesn't need to count the items one by one.
#  The array Module
# If you are using the built-in array module for homogeneous data, len() works exactly the same as it does for lists.

# Example:
    # python

import array
my_arr = array.array('i', [1, 2, 3, 4])
print(len(my_arr)) # Output: 4


# Map objects don't have a .sort() method and they don't have a length (len()).
# To fix this, you must convert the map into a list first.

if __name__ == '__main__':
    n = int(input())
    # Convert the map object into a list so you can sort and use len()
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    # Using negative indexing is cleaner in Python: 
    # arr[-1] is the last element, arr[-2] is second to last
    if arr[len(arr)-1] != arr[len(arr)-2]:
        print(arr[len(arr)-2]) # This logic needs a small tweak for the "Runner-Up"
    else:
        # Instead of hardcoding -3, we should find the first unique value 
        # that is smaller than the maximum.
        pass