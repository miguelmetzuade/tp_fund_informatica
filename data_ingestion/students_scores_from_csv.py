"""
This file reads students scores data from a csv file.
"""


def __read_file(file_path: str, tries: int=5) -> list:
    """Reads the content of a file and returns it as a list of strings, each representing a line.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        list: A list of strings, each representing a line in the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs while reading the file.
        Exception: If an unexpected error occurs.

    Returns example:
        [
            'Nombre,Materia,Nota1,Nota2,Nota3\n', 
            'Roberta Samper Aznar,Matemática,10,3,4\n', 
            'Juanita Graciela Torralba Castell,Arte,4,1,4\n', 
            'Juanita Graciela Torralba Castell,Historia,8,6,9\n'
        ]
    """
    last_error = None
    file = None
    while tries > 0:
        tries -= 1
        try:
            file = open(file_path, 'r', encoding='utf-8')
            lines = file.readlines()
            return lines
        except FileNotFoundError as e:
            print(f"File not found: {file_path}")
            last_error = e
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
            last_error = e
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            last_error = e
        finally:
            file.close() if file else None
    if last_error:
        raise last_error


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
    content = __read_file(file_path, tries)
    lines = [ line.strip() for line in content ]
    lines = [  line for line in lines if line!="" ]
    return lines


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
    content = __read_csv(file_path)
    if not content:
        raise Exception(f"The file {file_path} is empty or does not contain valid data.")
    matrix_data = list()
    for line in content:
        line_data = line.split(',')
        line_data = [ item.strip() for item in line_data ]
        matrix_data.append(line_data)

    return matrix_data

