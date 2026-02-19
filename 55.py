# match case
def check_number(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Unknown number"

print(check_number(2))  # Output: Two


# multiple cases
def check_day(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(check_day("Sunday"))  # Weekend


# match with condition
def number_type(num):
    match num:
        case n if n > 0:
            return "Positive"
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"

print(number_type(-5))  # Negative


# match with data structures
def process_data(data):
    match data:
        case [x, y]:
            return f"List with two elements: {x}, {y}"
        case {"name": name, "age": age}:
            return f"{name} is {age} years old"
        case _:
            return "Unknown structure"

print(process_data([10, 20]))
print(process_data({"name": "Kan", "age": 21}))
