"""Combining twolists into a dictionary."""

__author__ = "730658017"


def zip(given_strs: list[str], given_ints: list[int]) -> dict[str, int]:
    """Takes two lists and turns them into a dictionary using subsequent index values from both lists."""
    if len(given_strs) != len(given_ints) or not given_strs or not given_ints:
        return {}
    new_dict: dict[str, int] = {}
    for i in range(0, len(given_ints)):
        new_dict[given_strs[i]] = given_ints[i]
    return new_dict