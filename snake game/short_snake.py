import random

'''
1 for rock
-1 for paper
0 for scissors
'''
youstr = input("Enter your choice: ")
computer = random.choice(["r", "p", "s"])  # random.choice method is used to select a random element from a list.
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissors"}
you = youDict[youstr]
com = youDict[computer]
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[com]}")

if(com == you):
    print("it is a draw")
else:
    if(com-you == 2 or com-you == -1):
        print("You Win")
    elif(com-you == 1 or com-you == -2):
        print("You Lose")
    else:
        print("Invalid input")




'''
com-you 
a. 1(r) - -1(p) = 2 (Y win)
b. 1(r) - 0(s) = 1 (Y lose)
c. -1(p) - 1(r) = -2 (Y lose)
d. -1(p) - 0(s) = -1 (Y win)
e. 0(s) - 1(r) = -1 (Y win)
f. 0(s) - -1(p) = 1 (Y lose)
'''