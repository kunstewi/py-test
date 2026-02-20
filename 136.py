# - [ ] 136. **[Practice]** Convert Snake_case to CamelCase.

# snake_case_example  →  SnakeCaseExample

# using split + loop
def snake_to_camel(text):
    words = text.split("_")   # Split at underscores
    result = ""

    for word in words:
        if word:  # Avoid empty strings
            result += word[0].upper() + word[1:].lower()

    return result


# Example
print(snake_to_camel("snake_case_example"))

"""
split("_") → break string into words

Capitalize first letter of each word

Join them together

Avoid empty strings (__example case)
"""

# pythonic method
def snake_to_camel(text):
    return "".join(word.capitalize() for word in text.split("_") if word)


print(snake_to_camel("snake_case_example"))


# lower camelcase version - snake_case_example → snakeCaseExample
def snake_to_lower_camel(text):
    words = text.split("_")
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


print(snake_to_lower_camel("snake_case_example"))