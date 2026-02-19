# Validate user input until it matches a specific condition (while loop).

# Keep asking until the user enters a positive number

while True:
    num = int(input("Enter a positive number: "))  # take input and convert to int
    
    if num > 0:   # check condition
        break     # exit loop if condition is satisfied
    
    print("Invalid input. Please try again.")
    
print("Valid input received:", num)


# validate input range 1 - 10

while True:
    num = int(input("Enter a number between 1 and 10: "))
    
    if 1 <= num <= 10:
        break
    
    print("Number must be between 1 and 10.")
    
print("Thank you! You entered:", num)


# validate string input

while True:
    name = input("Enter your name: ")
    
    if name.isalpha():   # checks if only letters
        break
    
    print("Name should contain only letters.")
    
print("Welcome,", name)


# handles invalid integers

while True:
    try:
        num = int(input("Enter a positive number: "))
        
        if num > 0:
            break
        else:
            print("Number must be positive.")
    
    except ValueError:
        print("Please enter a valid integer.")

print("Valid input:", num)

