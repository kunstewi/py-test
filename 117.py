# Encode a string to bytes `.encode('utf-8')`.

# In Python, .encode('utf-8') converts a string (str) into bytes using UTF-8 encoding.

text = "Hello"

encoded_text = text.encode("utf-8")

print(encoded_text)
print(type(encoded_text)) 

"""
Output

b'Hello'
<class 'bytes'>

The b before 'Hello' means it is a bytes object, not a normal string.
"""

# example with unicode characters
text = "नमस्ते"

encoded_text = text.encode("utf-8")

print(encoded_text)

# b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87' ( output )


# convert back to string
text = "Hello"

encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")

print(decoded)