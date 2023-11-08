"""Unit Tests for dictionary."""

__author__ = "730658017"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance 
import pytest


def test_regular_dict() -> None:
    """Should return an inverted dictionary with the number strings as values and names as keys."""
    test_dict = {"18": "tim", "12": "jeff", "19": "john"}
    assert invert(test_dict) == {"tim": "18", "jeff": "12", "john": "19"}


def test_dict_order() -> None:
    """Should return an inverted dictionary with a number key string corresponding to its name as a value."""
    test_dict = {"one": "1", "two": "2", "three": "3", "four": "4"}
    assert invert(test_dict) == {"1": "one", "2": "two", "3": "three", "4": "four"}


def test_duplicate_values() -> None:
    """Should return a KeyError due to duplicate values in the original dictionary, which cannot be inverted."""
    test_dict = {"john": "18", "jeff": "12", "jim": "18", "tom": "16"}
    with pytest.raises(KeyError):
        invert(test_dict)


def test_same_frequency() -> None:
    """Should return a dict with all list items as keys corresponding to values of 1."""
    test_list = ["hello", "hi", "how", "are", "you?"]
    assert count(test_list) == {"hello": 1, "hi": 1, "how": 1, "are": 1, "you?": 1}


def test_empty_dictionary() -> None:
    """Should return an empty dictionary."""
    test_list = []
    assert count(test_list) == {}


def test_different_frequencies() -> None:
    """Should return a dictionary with 'needle' as 1 and 'hay' as 10."""
    test_list = ["hay", "hay", "hay", "hay", "hay", "needle", "hay", "hay", "hay", "hay", "hay"]
    assert count(test_list) == {"hay": 10, "needle": 1}


def test_same_colors() -> None:
    """Should return 'blue', as all persons chose blue as their favorite color."""
    test_dict = {"jeff": "blue", "tim": "blue", "john": "blue", "timothy": "blue", "jonathan": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_max_color() -> None:
    """Should return 'yellow', the most common favorite color among the data."""
    test_dict = {"jeff": "yellow", "tim": "green", "john": "purple", "timothy": "yellow", "jonathan": "grey"}
    assert favorite_color(test_dict) == "yellow"


def test_empty_dict() -> None:
    """Should return a string 'None' since there is no favorite color."""
    test_dict = {}
    assert favorite_color(test_dict) == "None"


def test_same_letter_words() -> None:
    """Should return a dictionary with one key with its value being a list which contains all items in the given list."""
    test_list = ["hello", "hi", "hay", "haha", "house"]
    assert alphabetizer(test_list) == {'h': ["hello", "hi", "hay", "haha", "house"]}


def test_empty_list() -> None:
    """Should return an empty dictionary."""
    test_list = []
    assert alphabetizer(test_list) == {}


def test_sentence() -> None:
    """Should return a dictionary with multiple values corresponding to the first letter of each word."""
    test_list = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
    assert alphabetizer(test_list) == {'t': ['the', 'the'], 'q': ['quick'], 'b': ['brown'], 'f': ['fox'], 'j': ['jumped'], 'o': ['over'], 'l': ['lazy'], 'd': ['dog']}


def test_add_student_existng_day() -> None:
    """Should return a dictionary with the same keys but an added value to the corresponding weekday."""
    test_dict = {"Monday": ["sarah", "clarisse", "chris", "trevor"], "Tuesday": ["sarah", "clarisse", "trevor"], "Wednesday": ["sarah", "clarisse", "chris", "trevor"]}
    assert update_attendance(test_dict, "Tuesday", "chris") == {"Monday": ["sarah", "clarisse", "chris", "trevor"], "Tuesday": ["sarah", "clarisse", "trevor", "chris"], "Wednesday": ["sarah", "clarisse", "chris", "trevor"]}


def test_add_new_day() -> None:
    """Should return a dictionary with unchanged previous key-value pairs, but with a new key-value pair appended."""
    test_dict = {"Monday": ["sarah", "clarisse", "chris", "trevor"], "Tuesday": ["sarah", "clarisse", "trevor"], "Wednesday": ["sarah", "clarisse", "chris", "trevor"]}
    assert update_attendance(test_dict, "Thursday", "sarah") == {"Monday": ["sarah", "clarisse", "chris", "trevor"], "Tuesday": ["sarah", "clarisse", "trevor"], "Wednesday": ["sarah", "clarisse", "chris", "trevor"], "Thursday": ["sarah"]}


def test_empty_log() -> None:
    """Should return a dictionary containing one weekday key and a name value."""
    test_dict = {}
    assert update_attendance(test_dict, "Monday", "sarah") == {"Monday": ["sarah"]}