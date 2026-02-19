# In Python, or stops evaluating as soon as it finds something True.

# It does not check the remaining conditions once the result is already decided.

# basic only the first one runs
def first():
    print("First function called")
    return True

def second():
    print("Second function called")
    return True

result = first() or second()

print("Result:", result)


# if first function returns false python has to run the second function


# with variables
x = 10

if x > 5 or x / 0 == 2:
    print("Condition is True")
