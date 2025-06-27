try:
    from handler_files.csv_manager import confread_csv_as_matrixig
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from handler_files.csv_manager import read_csv_as_matrix


"""
This file reads students scores data from a csv file.
"""


def read_scores_from_csv(file_path: str) -> list:
    """Reads students scores from a CSV file and returns a matrix (list if lists) whose first element is the header.

    Args:
        file_path (str): Path to the CSV file.

    Raises:
        Exception: If the file is empty or does not contain valid data.

    Returns:
        list: A matrix (list of lists) representing the CSV file content.

    Returs example:
        [
            ['Nombre', 'Materia', 'Nota1', 'Nota2', 'Nota3'],
            ['Roberta Samper Aznar', 'Matemática', '10', '3', '4'], 
            ['Juanita Graciela Torralba Castell', 'Arte', '4', '1', '4'], 
            ['Juanita Graciela Torralba Castell', 'Historia', '8', '6', '9']
        ]
    """

    content = read_csv_as_matrix(file_path)
    if not content:
        raise Exception(f"The file {file_path} is empty or does not contain valid data.")
    return content
