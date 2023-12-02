"""Dictionary related utility functions."""
from csv import DictReader
__author__ = "730658017"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dictionaries with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(data: list[dict[str, str]], key: str) -> list[str]:
    """Returns all values for associated keys in a list of dictionaries."""
    result: list[str] = []
    for item in data:
        result.append(item[key])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with colmn headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if rows >= len(table):
        return table
    for col_key in table:
        temp: list[str] = []
        for i in range(rows):
            temp.append(table[col_key][i])
        result[col_key] = temp
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = table[name]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for col_key in table_one:
        result[col_key] = table_one[col_key]
    for col_key in table_two:
        if col_key in result:
            for item in table_two[col_key]:
                result[col_key].append(item)
        else:
            result[col_key] = table_two[col_key]
    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Returns a dictionary representing the number of instances each element appears in a list."""
    result: dict[str, int] = {}
    for item in given_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result