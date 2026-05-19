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


# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

print('ab123'.isalnum())
# True
print('ab123#'.isalnum())
# False
str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).

print('abcD'.isalpha())
# True
print('abcd1'.isalpha())
# False
str.isdigit()
# This method checks if all the characters of a string are digits (0-9).

print('1234'.isdigit())
# True
print('123edsd'.isdigit())
# False
str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).

print('abcd123#'.islower())
# True
print('Abcd123#'.islower())
# False
str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).

print('ABCD123#'.isupper())
# True
print('Abcd123#'.isupper())
# False


# use string slicing with the syntax text[0:5].
# In Python, the stop index is exclusive, so 0:5 will extract indexes 0, 1, 2, 3, and 4.
# Example Code
# python
text = "HackerRank"

# One-line code to extract and print index 0 to 4
print(text[0:5])  # Output: Hacke

# using the imported textwrap module:
#     Since the challenge already imports textwrap for you, you can also solve it using the built-in module directly in one line:
#         python
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)