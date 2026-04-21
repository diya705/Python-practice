a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))

if(a1>a2 and a1>a3):   # in python we write and condition as 'and' and not '&&' like in c++ and java
    print("a1 is greatest: ", a1)
elif(a2>a1 and a2>a3):
    print("a2 is greatest: ", a2)
elif(a3>a1 and a3>a2):
    print("a3 is greatest: ", a3)
else:
    print("All numbers are equal")


# writing spame code for practice
p1 = "Make a lot of Money"
p2 = "buy now"
p3 = "subscribe this channel"
p4 = "click this link"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam message")
else:
    print("This is not a spam message")


# find string in a list 
l = ["Diya", "Riya", "Priya", "Miya", "Tiya"]
name = input("Enter name to search: ")
if(name in l):
    print("Name is present in the list")
else:
    print("Name is not present in the list")


# find out marks of a student and print grade
marks = int(input("Enter marks: "))

if(marks<=100 and marks>=90):
    print("Grade: A")
elif(marks<90 and marks>=80):
    print("Grade: B")
elif(marks<80 and marks>=70):
    print("Grade: C")
elif(marks<70 and marks>=60):
    print("Grade: D")
elif(marks<60 and marks>=0):
    print("Grade: F")
else:
    print("Invalid marks")


# find substring from a string in writing anytype of case 
post = input("Enter the post: ")
# 'in' is a keyword in python which is used to check if a substring is present in a string or not. It returns True if the substring is present and False if it is not present.
if("Diya".lower() in post.lower()):  # lower() function conver string into lowercase and we can compare two strings in any case 
    print("This post is about Diya")
else:
    print("This post is not about Diya")