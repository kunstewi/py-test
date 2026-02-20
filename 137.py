# - [ ] 137. **[Practice]** Check parentheses balance in a string.

"""
we will check if brackets like - ()  {}  [] are properly open and closed

"({[]})"  → ✅ Balanced  
"({[})"   → ❌ Not Balanced
"""

# method 1 using stack
def is_balanced(text):
    stack = []  # Stack to store opening brackets
    
    # Mapping of closing → opening brackets
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in text:
        # If opening bracket → push to stack
        if char in "({[":
            stack.append(char)
        
        # If closing bracket → check top of stack
        elif char in ")}]":
            if not stack:  # Nothing to match with
                return False
            
            top = stack.pop()
            if pairs[char] != top:
                return False

    # If stack empty → balanced
    return len(stack) == 0


# Example
print(is_balanced("({[]})"))  # True
print(is_balanced("({[})"))   # False

"""
Use a stack - Because brackets follow LIFO (Last In First Out) logic.

Push opening brackets

When closing bracket appears:

Check top of stack

If matches → pop

Else → not balanced

At the end:

Stack must be empty
"""

