"""Dictionary related utility functions."""

__author__ = "730658017"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and turns its string values into keys, and keys into values."""
    new_dict: dict[str, str] = {}
    for key in given_dict:
        if given_dict[key] in new_dict:
            raise KeyError
        else:
            new_dict[given_dict[key]] = key
    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Takes a dictionary of people's names as keys and their favorite color as values, and returns the most favorited color."""
    if not colors:
        return "None"
    colors_by_vote: dict[str, int] = {}
    for person in colors:
        if colors[person] in colors_by_vote:
            colors_by_vote[colors[person]] += 1
        else:
            colors_by_vote[colors[person]] = 1
    colors_2: list[str] = []
    votes: list[int] = []
    for color in colors_by_vote:
        colors_2.append(color)
        votes.append(colors_by_vote[color])
    max_idx = 0
    for i in range(len(votes)):
        if votes[i] > votes[max_idx]:
            max_idx = i
    return colors_2[max_idx]


def count(given: list[str]) -> dict[str, int]:
    """Takes a list of strings and returns a dictionary containing each string as a key and the number of the same string in a list as a integer."""
    new_dict: dict[str, int] = {}
    for item in given:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(given: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary of each starting letter from a given list of words, mapping each letter key to a value of the word whose starting letter is the key."""
    new_dict: dict[str, list[str]] = {}
    for item in given:
        if item[0].lower() in new_dict:
            new_dict[item[0].lower()] += [item]
        else:
            new_dict[item[0].lower()] = [item]
    return new_dict


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Takes in a dictionary of weekdays as string keys and students present that day as a list of string values, and adds a student to the list associated with the weekday. If the day is not in the dictionary, then a new day string key is created and the student associated to that key."""
    if day not in log:
        log[day] = [student]
    elif student not in log[day]:
        log[day] += [student]
    temp_list = []
    for day in log:
        for item in log[day]:
            if item not in temp_list:
                temp_list.append(item)
                log[day] = temp_list
        temp_list = []
    return log