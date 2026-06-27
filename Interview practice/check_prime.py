num = int(input("Enter a number: "))
if num > 1:
    if num ==2:
        print(num, "is a prime number")
    else:
          for i in range(2, num):
            if (num % i) ==0:
                print(num, 'is not a prime number')
                break
            else:
                print(num, 'is a prime number')
else:
    print(num, "is not a prime number")


# By creating a function to check if a number is prime, we can make the code more reusable and organized. Here's an improved version of the code:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True
    
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")