import os


def file_exists(filename: str) -> bool:
    """Checks if the specified file exists.

    Args:
        filename (str): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)


def create_file(filename: str) -> None:
    """Creates a new CSV file with the specified columns.

    Args:
        columns (list): The columns to write in the file.
        filename (str): The name of the CSV file to create.
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('')
    except Exception as e:
        print(f"An error occurred while creating the file {filename}: {e}")
        raise e


def read_file(file_path: str, tries: int=5) -> list:
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

