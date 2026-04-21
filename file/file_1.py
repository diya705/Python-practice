# read() function 

f = open("C:\\python practice\\file\\first.txt") # open function is used to open the txt or jpg/png file in open function "r" (read) is taking as default argument
data = f.read() # read function is used to read the content of the file and store it in a variable
print(data) # print the content of the file
f.close() # close function is used to close the file after reading it

# write() function 
st = "This file is created by python code for practice write function in file handling"
f = open("C:\\python practice\\file\\second.txt", "w") # open function is used to open the txt or jpg/png file and "w" is used to write in the file
f.write(st) # write function is used to write the content in the file
print("Content written in the file successfully in file second.txt")
f.close() # close function is used to close the file after writing in it

# readlines() function read line by line
f = open("C:\\python practice\\file\\first.txt") # open function is used to open the txt or jpg/png file in open function "r" (read) is taking as default argument
lines = f.readlines() # readlines function is used to read the content of the file line by line and store it in a list
print(lines, type(lines)) # print the content of the file and its type
f.close() # close function is used to close the file after reading it

# also write this using while loop
f = open("C:\\python practice\\file\\first.txt") # open function is used to open the txt or jpg/png file in open function "r" (read) is taking as default argument 
lines = f.readline() # readline function is used to read the content of the file line by line and store it in a variable
while(lines != ""):
    print(lines)
    lines = f.readline() # readline function is used to read the content of the file line by line and store it in a variable
f.close() # close function is used to close the file after reading it

# "a" append mode is used to add content in the file without overwriting the existing content in the file
string = "This content is added by python code for practice append function in file handling"
f = open("C:\\python practice\\file\\second.txt", "a") # open function is used to open the txt or jpg/png file and "a" is used to append in the file
f.write(string) # write function is used to write the content in the file
print("Content appended in the file successfully in file second.txt")
f.close() # close function is used to close the file after appending in it

# "w+" mode is used to update the content in the file if it is already present otherwise it will create a new file and write the content in it
string = "This content is added by python code for practice update function in file handling"
f = open("C:\\python practice\\file\\second.txt", "w+") # open function is used to open the txt or jpg/png file and "w+" is used to update in the file
f.write(string) # write function is used to write the content in the file
print("Content updated in the file successfully in file second.txt")
f.close() # close function is used to close the file after updating in it

# "rb" mode is used to read the content of the file in binary format
f = open("C:\\python practice\\file\\first.txt", "rb") # open function is used to open the txt or jpg/png file and "rb" is used to read in binary format
d = f.read() # read function is used to read the content of the file and store it in a variable
print(d) # print the content of the file in binary format
f.close() # close function is used to close the file after reading it


# using with statement is write without write again close command
with open("C:\\python practice\\file\\second.txt") as f: # with statement is used to open the file and it will automatically close the file after the block of code is executed
    print(f.read()) # read function is used to read the content of the file and print it
# when yiu out from the statement the file will automatically closed and you don't need to write f.close() command