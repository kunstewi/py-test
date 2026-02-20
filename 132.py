#  [ ] 132. **[Practice]** Implement Caesar Cipher.

# A Caesar Cipher shifts each letter in a message by a fixed number of positions in the alphabet.

"""
A → D
B → E
X → A  (wrap around)
"""

# basic lower case only
def caesar_cipher(text, shift):
    result = ""  # Store encrypted text
    
    for char in text:
        if char.isalpha():  # Check if character is a letter
            
            # Convert letter to ASCII number (a=97)
            shifted = ord(char) - ord('a')
            
            # Apply shift with wrap-around using modulo
            shifted = (shifted + shift) % 26
            
            # Convert back to character
            result += chr(shifted + ord('a'))
        else:
            result += char  # Keep spaces or symbols unchanged
    
    return result


# Example
print(caesar_cipher("hello", 3))   # khoor


# handle upper case and lowercase
def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26
            result += chr(shifted + ord('a'))
            
        elif char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted + ord('A'))
            
        else:
            result += char   # Keep punctuation unchanged
            
    return result


# Example
print(caesar_cipher("Hello World!", 3))
# Khoor Zruog!


# decryption version
def decrypt_caesar(text, shift):
    return caesar_cipher(text, -shift)


print(decrypt_caesar("Khoor Zruog!", 3))
# Hello World!


"""
ord(char) → converts character to ASCII number

chr(number) → converts ASCII back to character

% 26 → keeps shift within alphabet range (wrap-around)
"""