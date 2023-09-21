"""EX03: Structured Wordle."""

__author__ = "730658017"


def contains_char(given_string: str, expected_char: str) -> bool:
    """Checks if a given string contains a given character.
    
    Takes a given string.
    Then, loops through each index of the string to check if the expected character is in the string.
    Return true if any of the indexes contain the expected char,
    return false otherwise.
    """
    assert len(expected_char) == 1
    counter = 0
    while counter <= len(given_string) - 1:
        if given_string[counter] == expected_char:
            return True
        counter += 1
    return False


def emojified(given_guess: str, given_secret: str) -> str:
    """Returns a string with box emojis depending on the equivalency of two strings.
    
    Takes two given strings of the same length.
    Checks each index of the first string and determines
    if it is equal to the same index of the second string.
    If so, it appends a green emoji box to a result string
    which will be returned. If the string does not match, then
    it checks if the character at the index of the first string
    is contained in the second string using an external function.
    If so, then a yellow box emoji is appended to the result string.
    If neither of the conditions are met, then a white box is appended
    to the resulting string. After each index has been checked, the resulting
    string is returned.
    """
    assert len(given_guess) == len(given_secret)
    counter = 0
    result = ""
    while counter <= len(given_guess) - 1:
        if given_guess[counter] == given_secret[counter]:
            result += "\U0001F7E9"
        elif contains_char(given_secret, given_guess[counter]):
            result += "\U0001F7E8"
        else:
            result += "\U00002B1C"
        counter += 1
    return result


def input_guess(expected_length: int) -> str:
    """Returns a user given string of expected length parameter.
    
    Takes a given length integer, and asks a user for an input. 
    While the input string length does not equal the
    given expected length, the user is continually asked
    to provide a new input until an equal length string is
    given. Then, that string is returned.
    """
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    current_turn = 1
    secret_word = "codes"
    game_won = False
    while current_turn <= 6 and not game_won:
        print(f"=== Turn {current_turn}/6 ===")
        current_guess = input_guess(5)
        print(emojified(current_guess, secret_word))
        if current_guess == secret_word:
            game_won = True
        else:
            current_turn += 1
    
    if game_won:
        print(f"You won in {current_turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()