# palindrome

# string slicing
def is_palindrome_slice(s):
    return s == s[::-1]

# Example
print(is_palindrome_slice("madam"))   # True
print(is_palindrome_slice("hello"))   # False


# using loop
def is_palindrome_loop(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

print(is_palindrome_loop("racecar"))  # True


# ignore space and case
def is_palindrome_ignore(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome_ignore("Race Car"))  # True


# punctuation handling
import re # obviously the import won't work here

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True


