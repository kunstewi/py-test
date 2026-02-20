# factorial

# using for loop
n = 5

factorial = 1   # Start with 1 (important!)

for i in range(1, n + 1):
    factorial *= i   # Same as: factorial = factorial * i

print(factorial)


# using while loop
w = 5
factorialw = 1

while w > 0:
    factorialw *= w
    w -= 1

print(factorialw)


# user input
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)