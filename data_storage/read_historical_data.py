try:
    from handler_files.csv_manager import confread_csv_as_matrixig
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from handler_files.csv_manager import read_csv_as_matrix


def __get_historical_data(filename: str) -> list:
    """Retrieves historical data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of lists representing the CSV file content.
    """
    filename = f"./data_output/{filename}"
    content = read_csv_as_matrix(filename)
    if not content:
        raise Exception(f"The file {file_path} is empty or does not contain valid data.")
    return content
