"""HERE IS DOCSTRING."""

__author__ = "730658017"


def short_words(given_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for i in given_list:
        if len(i) >= 5:
            print(f"{i} is too long!")
        else:
            new_list.append(i)
    return new_list