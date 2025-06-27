"""
This file reads students scores data from terminal, receiving manual input.
"""


def __ask_for_input(value_name: str) -> str:
    """Prompts the user for input and returns the entered value.

    Args:
        value_name (str): The name of the value to be requested from the user.

    Returns:
        str: The value entered by the user.

    Raises:
        e: If an unexpected error occurs.
    """
    try:
        value_input = input(f"Enter {value_name}: ")
        value_input = value_input.strip()
        if not value_input:
            print(f"{value_name} cannot be empty.")
            return __ask_for_input(value_name)
        return value_input
    except Exception as e:
        print(f"An unexpected error occurred while requesting '{value_name}' value to user: {e}")
        raise e


def __ask_for_students_record(value_names) -> list:
    """Asks the user for a student's record.

    Args:
        value_names (list): The names of the values to be requested.

    Returns:
        list: A list of values entered by the user, corresponding to the requested names.

    Returns example:
        ['Roberta Samper Aznar', 'Matemática', '10', '3', '4']
    """
    values_list = list()
    for value_name in value_names:
        value = __ask_for_input(value_name)
        values_list.append(value)
    return values_list


def __ask_for_continuing() -> bool:
    """Asks the user if they want to continue entering more records.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    
    Raises:
        e: If an unexpected error occurs.
    """
    try:
        response = input("Do you want to enter another student's record? (yes/no): ")
        response = response.strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")
            return __ask_for_continuing()
    except Exception as e:
        print(f"An unexpected error occurred while asking for continuation: {e}")
        raise e


def read_scores_from_terminal() -> list:
    """Reads students scores data from terminal input.

    Returns:
        list: A list of strings, each representing a line of input.
    
    Raises:
        Exception: If an unexpected error occurs.
    
    Returns example:
        [
            ['Nombre', 'Materia', 'Nota1', 'Nota2', 'Nota3'],
            ['Roberta Samper Aznar', 'Matemática', '10', '3', '4'],
            ['Juanita Graciela Torralba Castell', 'Arte', '4', '1', '4'],
            ['Juanita Graciela Torralba Castell', 'Historia', '8', '6', '9']
        ]
    """
    value_names = ['Nombre', 'Materia', 'Nota1', 'Nota2', 'Nota3']
    data = [ value_names ]
    continue_input = True

    try:
        while continue_input:
            student_values = __ask_for_students_record(value_names)
            data.append(student_values)
            continue_input = __ask_for_continuing()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e

    if len(data) == 1:
        # data only contains the header
        print("No data was entered. Exiting.")
        return None
    return data
