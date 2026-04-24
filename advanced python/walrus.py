# using walrus operator  :=  use to assign value to a  variable with condition in the conditional statement in one attempt
if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected < =3)")   # output: list is too long 