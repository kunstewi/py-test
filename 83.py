# count vowels case insensitive

def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():   # convert to lowercase
        if char in vowels:
            count += 1

    return count


print(count_vowels("Hello World"))


# using sum
def count_vowels_sum(text):
    vowels = "aeiou" # vowels = "aeiouAEIOU" if uppercase needed
    return sum(1 for char in text.lower() if char in vowels)



# to count vowel and consonants not number or spaces
def count_vowels_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():  # check if it is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


v, c = count_vowels_consonants("Hello World 123!")
print("Vowels:", v)
print("Consonants:", c)
