# walrus operator := 
# it lets you assign a value to a variable inside an expression

# 1. inside if
if (n := len("Hello")) > 3:
    print(f"Length is {n}")

# without walrus
n = len("Hello")
if n > 3:
    print(f"Length is {n}")


# 2. in a while loop
while (user_input := input("Enter something (type 'quit' to stop): ")) != "quit":
    print("You typed:", user_input)


#3 list comprehension
numbers = [1, 2, 3, 4]
squares = [y for x in numbers if (y := x * x) > 5]

print(squares) # [9, 16]


