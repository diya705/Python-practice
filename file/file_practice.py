with open("C:\\python practice\\file\\poem.txt") as f: # with statement is used to open the file and it will automatically close the file after the block of code is executed
    print(f.read()) # read function is used to read the content of the file and print it
    f.seek(0) # move the file pointer to the beginning of the file
    if("twinkle" in f.read()):
        print("twinkle is present in the file")
    else:
        print("twinkle is not present in the file")
# when you out from the statement the file will automatically closed and you don't need to write

# Ques 2 
import os
import random 

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)  # gnerate a randome score between 1 and 62 using random.randint()function which takes two arguments the lower and upper limit of the range and returns a random integer between them
    # fetch the hiscore
    with open("C:\\python practice\\file\\hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score: {score}")
    if(score>hiscore):
        print("Congratulations! you have made new high score")
        with open("C:\\python practice\\file\\hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()    


def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"C:\\python practice\\file\\table\\table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)



# ques replace 
word = "twinkle"
with open("C:\\python practice\\file\\poem.txt") as f:
    content = f.read()
    content_new = content.replace(word, "Diya")

with open("C:\\python practice\\file\\poem.txt", "w") as f:
    f.write(content_new)
          

# change  different multiple words in one time 
words = ["Diya", "star"]
with open("C:\\python practice\\file\\poem.txt") as f:
          content = f.read()
for i in words:
          content = content.replace(i, "t" * len(words))

with open("C:\\python practice\\file\\poem.txt", "w") as f:
    f.write(content)


# readline at specifice line which we define
line = 1
with open("C:\\python practice\\file\\first.txt") as f:
     lines = f.readline()
lineno = 1
for line in lines:
     if("This" in lines):
          print(f"Which is present in the file Line no: {lineno}")
          break
     lineno += 1
else: 
    print("this is not present in the file")


# clear the text in the File
with open("C:\\python practice\\file\\first.txt", "w") as f:
     f.write("")   

# copy content from one file to another by rename the file and also delete the old file 
import shutil
with open("C:\\python practice\\file\\poem.txt") as f:
     content = f.read()
os.remove("C:\\python practice\\file\\poem.txt")
with open("C:\\python practice\\file\\first.txt", "w") as f:
        f.write(content)