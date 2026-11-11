
# Q54. Generator Function to Extract Vowels

def getvowels(name):
    vowels = "aeiouAEIOU"

    for ch in name:
        if ch in vowels:
            yield ch


# Sample input
name = input("Enter name: ")

# Display vowels
for vowel in getvowels(name):
    print(vowel)
