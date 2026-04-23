import random # random  module is used to take the random number 
n = random.randint(1, 100)  # randint is used to take random number range from min range to max range
a = -1  # this variable is user input in intialization we take -1 
guesses = 0  # this is the no. of counting in which turn guess correct number 
while(a != n):
    guesses +=1
    a = int(input("Guess the number: "))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("Higher number please")
    elif(a==n):
        print(f"You have guessed the number correctly in {guesses} attempt")


