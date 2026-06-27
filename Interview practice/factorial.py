
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n  = int(input("Enter a number to find factorial: "))
print(f"The factorial of {n} is {factorial(n)}")

# Another approach to find factorial is using memoization technique. We can store the previously calculated factorials in a dictionary to avoid redundant calculations.
memo = {}
def factorial_memo(n):
    if n ==0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memo(n-1)
    return memo[n]

n = int(input("Enter a number to find factorial: "))
print(f"The factorial of {n} is {factorial_memo(n)}")
