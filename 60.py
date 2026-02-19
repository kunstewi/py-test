number = 29

if number < 2:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        # This else runs only if the loop did NOT break
        print(f"{number} is a prime number")

"""
How for-else Works

The for loop checks if any number divides number.

If a divisor is found → break executes → else block is skipped.

If no divisor is found → loop completes normally → else block runs.
"""

# optimized version using root

if number < 2:
    print(f"{number} is not prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")
