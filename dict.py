# dictionary write in curly braces and in this write Key and Value together left side is Key and write side is Value 
# we also change the dictionary it is mutable
marks = {
    "Diya": "I'm World Biggest & Successfull Engineer",
    "No.": 1,
    "Success": "Yes"

}
print(marks) #this print whole dictionary
print(marks.items()) # this also  print the whole dictionary but write like a tuple
print(marks.keys()) # this prints the keys that are on the left side 
print(marks.values()) # this prints the va;lues that are on the left side
marks.update({"Success": "Always Yes", "Happy": "Yes Forever and ever"})  # this update/change the already existing key values in original dictionary and also add new keys and values in the dictionary 
print(marks)
print(marks["Diya"]) # this prints the value of the key "Diya" and if this key is not exist then it give me KeyError
print(marks.get("Diya")) # this also prints the value of the key "Diya" and if not exist then it give None