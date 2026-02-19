# checking for if password is of 8 length and contains a digit

# Take password input from user
password = input("Enter your password: ")

# Condition 1: Check length
if len(password) <= 8:
    print("Password must be longer than 8 characters.")

else:
    has_number = False   # Flag to check if password contains a digit

    # Loop through each character in password
    for char in password:
        # Check if character is a digit
        if char.isdigit():
            has_number = True
            break   # Stop loop once we find a number

    # Final validation
    if has_number:
        print("Valid Password")
    else:
        print("Password must contain at least one number.")



# while loop
if len(password) <= 8:
    print("Password must be longer than 8 characters.")
else:
    has_number = False
    i = 0   # index counter

    # Loop using while
    while i < len(password):
        if password[i].isdigit():
            has_number = True
            break
        i += 1   # move to next character

    if has_number:
        print("Valid Password")
    else:
        print("Password must contain at least one number.")



# without using .isdigit()
if len(password) <= 8:
    print("Password must be longer than 8 characters.")
else:
    has_number = False

    for char in password:
        if char >= '0' and char <= '9':
            has_number = True
            break

    if has_number:
        print("Valid Password ✅")
    else:
        print("Password must contain at least one number.")



# Advanced Version 
password = input("Enter your password: ")

if len(password) <= 8:
    print("Password must be longer than 8 characters.")
else:
    has_number = False
    has_upper = False
    has_lower = False
    has_special = False

    for char in password:
        if char >= '0' and char <= '9':
            has_number = True
        elif char >= 'A' and char <= 'Z':
            has_upper = True
        elif char >= 'a' and char <= 'z':
            has_lower = True
        else:
            has_special = True

    if has_number and has_upper and has_lower and has_special:
        print("Strong Password")
    else:
        print("Weak Password")
