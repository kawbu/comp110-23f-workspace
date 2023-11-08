"""Test my zip function."""

__author__ = "730658017"

# Tests Below
from lessons.lessons2.zip import zip


def test_different_length_lists() -> None:
    """zip(["Monday", "Tuesday", "Wednesday], [1, 2, 3, 4] should return {})."""
    test_list_1: list[str] = ["Monday", "Tuesday", "Wednesday"]
    test_list_2 = list[int] = [1, 2, 3, 4]
    assert zip(test_list_1, test_list_2) == {}


def test_order_of_keys_and_values() -> None:
    """zip(["One", "Two", "Three", "Four"], [1, 2, 3, 4] should return {"One": 1, "Two": 2, "Three": 3, "Four": 4})."""
    test_list_1: list[str] = ["One", "Two", "Three", "Four"]
    test_list_2: list[int] = [1, 2, 3, 4]
    assert zip(test_list_1, test_list_2) == {"One": 1, "Two": 2, "Three": 3, "Four": 4}


def test_empty_list() -> None:
    """zip([], []) should return {}."""
    assert zip([], []) == {}