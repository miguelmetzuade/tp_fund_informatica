import os

try:
    from handler_files.file_manager import file_exists, create_file, read_file
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from handler_files.file_manager import file_exists, create_file, read_file


def __read_csv(file_path: str, tries: int=5) -> list:
    """Reads a CSV file and returns its content as a list of strings.

    Args:
        file_path (str): Path to the CSV file to be read.
        tries (int): Number of attempts to read the file.

    Returns:
        list: A list of strings, each representing a line in the CSV file.
    
    Raises:
        FileNotFoundError: If the file does not exist, from __read_file.
        IOError: If an I/O error occurs while reading the file, from __read_file.
        Exception: If an unexpected error occurs, from __read_file.

    Returns example:
        [
            'Nombre,Materia,Nota1,Nota2,Nota3', 
            'Roberta Samper Aznar,Matemática,10,3,4', 
            'Juanita Graciela Torralba Castell,Arte,4,1,4', 
            'Juanita Graciela Torralba Castell,Historia,8,6,9'
        ]
    """
    content = read_file(file_path, tries)
    lines = [ line.strip() for line in content ]
    lines = [  line for line in lines if line!="" ]
    return lines


def read_csv_as_matrix(file_path: str) -> list:
    """Reads data from a CSV file and returns a matrix (list if lists) whose first element is the header.

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
    content = __read_csv(file_path)
    if not content:
        raise Exception(f"The file {file_path} is empty or does not contain valid data.")
    matrix_data = list()
    for line in content:
        line_data = line.split(',')
        line_data = [ item.strip() for item in line_data ]
        matrix_data.append(line_data)

    return matrix_data


def __get_file_columns(filename: str) -> list:
    """Retrieves the columns of a CSV file.

    Args:
        filename (str): The name of a CSV existing file.

    Returns:
        list: A list of column names.
    """
    content = __read_csv(filename)
    columns = content[0]
    columns = columns.split(',')
    columns = [ column.strip() for column in columns ]
    return columns


def check_columns(columns: list, filename: str) -> None:
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


def create_file_with_columns(columns: list, filename: str) -> None:
    """Creates a new CSV file with the specified columns.

    Args:
        columns (list): The columns to write in the file.
        filename (str): The name of the CSV file to create.
    """
    create_file(filename)
    with open(filename, 'a', encoding='utf-8') as file:
        columns_line = ','.join(columns)
        file.write(columns_line + '\n')


def append_data_to_file(filename: str, data: list) -> None:
    """Appends data to an existing CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (list): The data to append to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        for student_data in data[1:]: # Skip header
            line = ','.join(student_data)
            file.write(line + '\n')

