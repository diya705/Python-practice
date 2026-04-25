a = 89  # this global varibale 

def fun():
    global a  # using global we change local var into global var
    a = 3  # this is local variable
    print(a)

fun()
print(a)  # now we print var 'a' without using object reference of fun() then we take output value of local variable because we change that local into global