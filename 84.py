# fibonacci

# using for loop
def print_fibonacci(n):
    a = 0  # First Fibonacci number
    b = 1  # Second Fibonacci number

    for i in range(n):
        print(a, end=" ")  # Print current number
        a, b = b, a + b    # Update values

# Example usage
print_fibonacci(10)

"""
Start with 0 and 1

Print the first number

Update:

a becomes b

b becomes a + b

Repeat n times
"""


# using while loop
def print_fibonacci_while(n):
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

print_fibonacci_while(10)
