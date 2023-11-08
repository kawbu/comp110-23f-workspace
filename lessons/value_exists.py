def value_exists(given_dict: dict[str, int], target: int) -> bool:
    for i in given_dict:
        if given_dict[i] == target:
            return True
    return False