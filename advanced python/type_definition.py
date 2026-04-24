# variable type hint  
# use : semicolon for this
#  in this we assign value and type of variable in one time 
age: int = 25

#Function type hints
def sum(a: int, b: int) -> int:
    return a+b

# variable type hint
name: str = "Diya"

#Function type hints
def greeting(name: str) -> str:
    return f"hello, {name}"


print(greeting("Alice")) #Output: hello, alice