import os

"""
This file updates scores data on the CSV that contains historic data.
"""


def __file_exists(filename: str) -> bool:
    """Checks if the specified file exists.

    Args:
        filename (str): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)


def __get_file_columns(filename: str) -> list:
    """Retrieves the columns of a CSV file.

    Args:
        filename (str): The name of a CSV existing file.

    Returns:
        list: A list of column names.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        header = file.readline().strip()
        columns = header.split(',')
    return columns


def __check_columns(columns: list, filename: str) -> None:
    """Checks if the data has the correct columns.

    Args:
        data (list): The data to check.
        filename (str): The name of the CSV file.

    Raises:
        ValueError: If the data does not have the correct columns.
    """
    existing_columns = __get_file_columns(filename)
    if existing_columns != columns:
        raise ValueError(f"Columns in {filename} do not match the expected columns.")


def __create_file(columns: list, filename: str) -> None:
    """Creates a new CSV file with the specified columns.

    Args:
        columns (list): The columns to write in the file.
        filename (str): The name of the CSV file to create.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        columns_line = ','.join(columns)
        file.write(columns_line + '\n')


def __append_data_to_file(filename: str, data: list) -> None:
    """Appends data to an existing CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (list): The data to append to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        for student_data in data[1:]: # Skip header
            line = ','.join(student_data)
            file.write(line + '\n')


def update_hits_data_csv(filename: str, data: list) -> None:
    """Updates the hits data in the specified CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (list): The updated data to write to the file.
    """
    filename = f"./data/{filename}"
    columns = data[0]
    if not __file_exists(filename):
        __create_file(columns, filename)
    else:
        __check_columns(columns, filename)
    __append_data_to_file(filename, data)
