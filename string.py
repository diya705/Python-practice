# use replace method into string take is taken from user 
a = input("Enter a string: ")
print(a.replace(a, "yes")) # input is using to take the input from the user and store it in a variable

# use f string to print any variable in between the line without use concetatination
b = input("Enter your name:")
print(f"This is my name {b} \n Hello!")

# .replace() method chaining
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''
name = input("Enter your name: ")
print(letter.replace("<|NAME|>", name).replace("<|DATE|>", "13/03/2026"))

# find whitespace in string
x = " "
print(x.isspace()) 

# find double space index in string
y = "hello  world"
print(y.find("  "))
# replace double space with single space
print(y.replace("  ", " "))
# string is immutable and we can not change the string but we can create a new string by using the replace method.
print(y) # original string is not changed because string is immutable

# escape sequence in string
letter = "Dear Diya, Enjoy your day! \nThis is a new line. \tThis is a tab space."
print(letter)

v = "first"
v = "second"
print(v) # string is immutable but we can reassign the variable to a new string.

# Another approach is to slice the string and join it back.
# Example
string = "abracadabra"
string = string[:5] + "k" + string[6:]
print(string)
# abrackdabra

# String .startswith()You can iterate through the main string and check if the current slice starts with your target substring. This removes the need to manually compute the ending index slice.python
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        # Check if the string starting at index i begins with sub_string
        if string[i:].startswith(sub_string):
            count += 1
    return count
            