"""My First COMP110 Program."""

__author__ = "730658017"


def w_sum(values: list[float]) -> float:
    """Takes values, returns sum via while loop."""
    total = 0.0
    curr = 0
    while curr < len(values):
        total += values[curr]
        curr += 1
    return total


def f_sum(values: list[float]) -> float:
    """Takes values, returns sum via for loop."""
    total = 0.0
    for val in values:
        total += val
    return total


def f_range_sum(values: list[float]) -> float:
    """Takes values, returns sum via for loop using the range function."""
    total = 0.0
    for i in range(0, len(values)):
        total += values[i]
    return total