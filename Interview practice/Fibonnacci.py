def print_fibonnaci(n):
    a, b = 0, 1
    if n <1:
        print("Please enter a positive integer")
    elif n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    elif n >2:
        print(a)
        print(b)
        # genearte next num in the series
        for i in range(2, n):
            c = a + b
            a, b = b, c
            print(c)

print_fibonnaci(int(input("Enter a number to generate fibonnaci series:")))
