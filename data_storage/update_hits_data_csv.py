import os

try:
    from handler_files.file_manager import file_exists
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from handler_files.file_manager import file_exists
from handler_files.csv_manager import create_file_with_columns, append_data_to_file, \
                                        check_columns

"""
This file updates scores data on the CSV that contains historic data.
"""


def update_hits_data_csv(filename: str, data: list) -> None:
    """Updates the hits data in the specified CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (list): The updated data to write to the file.
    """
    filename = f"./data_output/{filename}"
    columns = data[0]
    if not file_exists(filename):
        create_file_with_columns(columns, filename)
    else:
        check_columns(columns, filename)
    append_data_to_file(filename, data)
