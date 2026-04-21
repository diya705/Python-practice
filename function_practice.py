# find greatest of three numbers using function
def greatest(a, b, c):
    if (a>b and a>c):
        print(f"{a} is greatest")
    elif(b>a and b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

a = 1
b =3
c= 2
greatest(a, b, c)

# convert celcius to fahrenheit using function
def temp(cel):
    farh = (cel * 9/5) + 32
    return farh

cel = 37
cfh = temp(cel)
round(cfh, 2) # this is used to round the value of fahrenheit upto 2 decimal point
print(f"{cel} degree celcius is equal to {round(cfh, 2)} degree fahrenheit")


# sum of first n natural numbers using recursive function 
def natural(n):
    if n ==1:
        return 1
    return n + natural(n-1)

sum = natural(5)
print(f"Sum of first 5 natural numbers is: {sum}")

# print reverse star pattern using recursive function 
def star(n):
    if n == 0:
        return   # return is used to stop/exist from the function if it has any value then at exist it give that value to function call variable otherwise it just exist from the function and not give any value to function call variable
    print("*"*n)
    star(n-1)

star(3)


# remove the word and strip the word from list
def rem(lst, word):
    n = [] #this is empty list to store the value which we are remove and strip from the list
    for i in lst:
        if not(i == word): #not condition is write as 'not'
            n.append(i.strip(word)) # this is used to strip the word from the list and store in n list
    return n

lst = ["Diya", "Hii", "Di", "Hello"]
print(rem(lst, "Di")) # this is used to remove the word "Di" from the list and store in n list and print that list