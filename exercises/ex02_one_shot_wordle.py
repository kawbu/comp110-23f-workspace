"""EX01: One Shot Wordle."""

__author__ = "730658017"

secret_word = "python"
user_guess = input(f"What is your {len(secret_word)}-letter guess?    ")

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again:  ")

index_counter = 0
out_string = ""
while index_counter < len(secret_word):
    if user_guess[index_counter] == secret_word[index_counter]:
        out_string += "\U0001F7E9"
    else:
        char_in_word = False
        alt_index_counter = 0
        while not char_in_word and alt_index_counter < len(secret_word):
            if user_guess[index_counter] == secret_word[alt_index_counter]:
                char_in_word = True
            else:
                alt_index_counter += 1
        if char_in_word:
            out_string += "\U0001F7E8"
        else:
            out_string += "\U00002B1C"
    index_counter += 1

print(out_string)

if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")