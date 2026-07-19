def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m - 1)
m = int(input("Enter a number to calculate its factorial: "))
result = factorial(m)
print(f"The factorial of {m} is {result}.")
