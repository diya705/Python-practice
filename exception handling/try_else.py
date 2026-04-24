# in try and else if try block is successfuly run then the code moves to else block 
# if exception block run and error comes then else block is not work

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("now i am run beacuse try block successfully run")