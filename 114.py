# Pad a string with zeros using `.zfill()`.

# The .zfill(width) method pads a string on the left side with zeros (0) until it reaches the specified total length.

number = "42"

padded = number.zfill(5)

print(padded) # 00042

# Since "42" has length 2 and we want length 5, Python adds 3 zeros to the left.


# another one
code = "7"
print(code.zfill(3)) # 007


# if string is already long enough
text = "12345"
print(text.zfill(3)) # 12345 no change


# work with signs
num = "-42"
print(num.zfill(5)) # -0042



