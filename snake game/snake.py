import random 

'''
1 for snake
-1 for water
0 for gun

'''
computer = random.choice(["s", "w", "g"])  # random.choice method is used to select a random element from a list.
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]
com = youDict[computer]
print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[com]}")

if(computer == you):
    print("It's a draw")
else:
    if(you == 1 and com == -1):
        print("You win")
    elif(you == 1 and com == 0):
        print("You Lose")
    elif(you == -1 and com == 1):
        print("You Lose")
    elif(you == -1 and com == 0):
        print("You win")
    elif(you == 0 and com == 1):
        print("You win")
    elif(you == 0 and com == -1):
        print("You Lose")
    else:
        print("Invalid input")