"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730658017"

given_word = input("Enter a 5-character word: ")
if len(given_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
    
given_char = input("Enter a single character: ")
if len(given_char) != 1:
    print("Error: Character must be a single character.")

print("Searching for " + given_char + " in " + given_word)
instances = 0

if given_word[0] == given_char:
    index = 0
    print(given_char + " found at index " + str(index))
    instances += 1
if given_word[1] == given_char:
    index = 1
    print(given_char + " found at index " + str(index))
    instances += 1
if given_word[2] == given_char:
    index = 2
    print(given_char + " found at index " + str(index))
    instances += 1
if given_word[3] == given_char:
    index = 3
    print(given_char + " found at index " + str(index))
    instances += 1
if given_word[4] == given_char:
    index = 4
    print(given_char + " found at index " + str(index))
    instances += 1

if instances != 0:
    if instances == 1:
        print(str(instances) + " instance of " + given_char + " found in " + given_word)
    else:
        print(str(instances) + " instances of " + given_char + " found in " + given_word)
else:
    print("No instances of " + given_char + " found in " + given_word)

