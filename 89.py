# Implement a primitive “Guess the Number” game.

# basic implementation

# Import random module to generate random numbers
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Infinite loop until correct guess
while True:
    # Take user input and convert it to integer
    guess = int(input("Enter your guess: "))
    
    # Compare guess with secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it correctly!")
        break  # Exit the loop when correct


"""
random.randint(1, 100) → generates a random number between 1 and 100.

while True: → keeps the game running until the correct guess.

int(input(...)) → converts user input from string to integer.

break → stops the loop when the guess is correct.
"""


# with attempt counter

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to Guess the Number!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break

