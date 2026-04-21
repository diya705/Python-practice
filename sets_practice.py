words = {
    "one": 1,
    "two": 2,
    "three": 3
}
word = input("Enter the word you want meaning of: ")
print(words.get(word, "word not founs in dictionary")) # this prints the value of the key entered by user and if not exist then it give "word not found in dictionary"
print(words[word]) # this also prints the value of the key entered by user and if not exist then it give KeyError


# problem 2
s = set()
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
n = input("Enter number: ")
s.add(int(n)) # this add the number entered by user to the set s
print(s) # this prints the set s, which contains the unique numbers entered by user, duplicates are removed and the order is not guaranted


# problem 3
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s) # this prints the set s, which contains the unique elements 20, 20.0 and "20". Note that 20 and 20.0 are considered the same in Python, so only one of them will be stored in the set.
print(len(s)) # this prints the length of the set s, which is 2, because 20 and 20.0 are considered the same element in the set, so only one of them is counted.


# problem 4 dictionary
a = {}
name = input("Enter friend's name: ")
lang = input("Enter  language name: ")
a. update({name: lang}) # this updates the dictionary a with the key as friend's name and value as language name entered by user
name = input("Enter friend's name: ")
lang = input("Enter  language name: ")
a. update({name: lang}) # this updates the dictionary a with the key as friend's name and value as language name entered by user
name = input("Enter friend's name: ")
lang = input("Enter  language name: ")
a. update({name: lang}) # this updates the dictionary a with the key as friend's name and value as language name entered by user
name = input("Enter friend's name: ")
lang = input("Enter  language name: ")
a. update({name: lang}) # this updates the dictionary a with the key as friend's name and value as language name entered by user

print (a) # this prints the dictionary a, which contains the friends' names as keys and their favorite programming languages as values entered by user
