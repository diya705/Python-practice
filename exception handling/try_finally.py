# finally always runs in any condition if try block run  or if except block run
def main():
    try:
        a = int(input("enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:   # finally is main use in the functions because when we return in the function then below code is not excecuted but finally overwrite this it works also after the return in any condition
        print("Hey I am inside of finally")

main()