try:
    a = int(input("Enter a number: "))
    print(a)

except ZeroDivisionError as y:  # we can also specify any specific type error
    print(f"Zero Division Error {y}")

except TypeError as e:
    print((f"Type  Error {e}"))

except ValueError as z:
    print(f"Value Error {z}")

except Exception as e:  # this is common exception case we can write this in any type of error
    print(e)
print("thank you")

