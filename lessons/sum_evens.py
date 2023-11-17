"""Practice summing over lists"""

def sum_even_of_list(input_list: list[int]) -> int:
    sum_total: int = 0
    idx: int = 0
    while idx < len(input_list):
        if input_list[idx] % 2 == 0:
            sum_total += input_list[idx]
            idx += 1
    return sum_total
