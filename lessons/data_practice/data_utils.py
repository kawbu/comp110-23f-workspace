"""Working with csv data."""
from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dictionaries with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(data: list[dict[str, str]], key: str) -> list[str]:
    """Returns all values for associated keysin a list of dictionaries"""
    result: list[str] = []
    for item in data:
        result.append(item[key])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with colmn headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_vals(table, key)
    return result