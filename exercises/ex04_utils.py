"""Exercise 4: Lists."""

__author__ = "730658017"


def main() -> None:
    """Test Function."""
    print(all([1, 1, 1], 1))
    print(all([1, 2, 3], 1))
    print(max([0, 1, 2, 3, 4, 10]))
    print(is_equal([1, 2, 3], [1, 2, 3]))


def all(given_list: list[int], given_num: int) -> bool:
    """Returns a boolean regarding the equality of all integers in a list to a given integer."""
    if not given_list:
        return False
    counter = 0
    while counter < len(given_list):
        if given_list[counter] != given_num:
            return False
        counter += 1
    return True


def max(given_list: list[int]) -> int:
    """Returns the max integer in a list of integers, or returns an error if an empty list is given."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = given_list[0]
    counter = 0
    while counter < len(given_list):
        if max_value < given_list[counter]:
            max_value = given_list[counter]
        counter += 1
    return max_value


def is_equal(given_list_1: list[int], given_list_2: list[int]) -> bool:
    """Returns a boolean regarding the deep equality of two lists (all values in each index are the same)."""
    if len(given_list_1) != len(given_list_2):
        return False
    counter = 0
    while counter < len(given_list_1):
        if given_list_1[counter] != given_list_2[counter]:
            return False
        counter += 1
    return True


if __name__ == "__main__":
    main()