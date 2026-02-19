# using range

# Loop from 1 to 100 (inclusive)
for i in range(1, 101):
    
    # If number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    # If number is divisible by only 3
    elif i % 3 == 0:
        print("Fizz")
    
    # If number is divisible by only 5
    elif i % 5 == 0:
        print("Buzz")
    
    # If number is not divisible by 3 or 5
    else:
        print(i)


# using while

i = 1  # Start from 1

while i <= 100:
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
    i += 1  # Increment i
