n = int(input("Enter a number: "))

print("By for loop")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


# through while loop 
j = 1
print("By While loop")
while(j<=10):
    print(f"{n} x {j} = {n*j}")
    j = j+1

# greet person which are in the list and name start with 'S'
l = ["Sita", "Gita", "Rita", "Mita", "Tita"]
for name  in l:
    if(name.startswith("S")):  # startswith() function checks if the string starts with the specified prefix and return True or False
        print(f"Hello {name}!")


# prime no. problem by for loop
for i in range(2, n):
    if(n%i==0):
        print(f"{n} is not a prime number")
        break
    else:
        print(f"{n} is a prime number")
        break

# sum of first n natural no. using while loop 
sum = 0
i = 1
while(i<=n):
    sum = sum + i
    i = i+1
print(f"The sum of first {n} natural numbers is: {sum}")

# factorial of a given number using for loop
f = 1
fact = 0
for f in range(f, n+1):
    if(f ==1):
        fact = int(f)
        print(f"{f} factorial is: {fact}")
        f = f+1
    else:
        fact = int(fact * int(f))
        print(f"{f} factorial is: {fact}")
        f = f+1

# another simplest way to find factorial of a given number using for loop
fact = 1
for f in range(1, n+1):
    fact = fact * f
    print(f"{f} factorial is: {fact}")


# print star pattern for num = 3 in the odd number
num = 7
for i in range(1, num+1):
    print(" "*(num - i)+"*"*(2*i-1))

# also write the same star pattern in another way using end parameter in print function
for i in range(1, num+1):
    print(" "*(num-i), end="")  # end parameter is used to specify what to print at the end of the output. By default, it is a newline character (\n) which means that after printing the output, it will move to the next line. 
    # But if we set it to an empty string (""), it will not move to the next line and will continue printing on the same line.
    print("*"*(2*i-1))

# print star pattern for num = 3 in as it is sequence
for i in range(1, num+1):
    print("*"*i)

'''
* * *
*   *
* * *
'''

for i in range(1, num+1):
    for j in range(1, num+1):
        if(i and j ==1 or i and j ==num):
            print("*"*(num), end="")
        elif(i==j):
            print(" ", end="")
    print()
        
# another way to solve this problem

for i in range(1, num+1):
    if(i==1 or i==num):
        print("*"*num, end="")
    else:
        print("*", end="")
        print(" "*(num-2), end="")
        print("*", end="")
    print(" ")

# print table in reverse order in for loop 
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}")
