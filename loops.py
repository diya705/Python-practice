# while loop 
i = 1
while(i<=50):
    print(i)
    i = i+1  # we have to update the value of i otherwise it will run infinite loop

# printing list in the while loop 
l = ["Diya", "Riya", "Priya", "Miya", "Tiya"]
i = 0
while(i<len(l)):
    print(l[i])
    i = i+1

# for loop
i = 1
for i in range(1, 51): # range(start, end) function generates a sequence of numbers from start to end-1
    print(i)

i = 0 
for i in range(4): # if we write only one argument in range() function then it will consider it as end and start will be 0 by default
    print(i)

# continue statement
for i in range(10):
    if(i==5):
        continue  # skip this iteration and continue with next one
    print(i)

for i in range(10):
    if(i==5): # break the teration or code when condition match
        break
    print(i)


# write 'pass' for skip that loop  so it does not give any error 

for a in range(5):
    pass