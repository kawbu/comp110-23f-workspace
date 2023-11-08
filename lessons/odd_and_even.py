def odd_and_even(given_list: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in range(len(given_list)):
        if i % 2 == 0:
            if given_list[i] % 2 != 0:
                new_list.append(given_list[i])
    return new_list