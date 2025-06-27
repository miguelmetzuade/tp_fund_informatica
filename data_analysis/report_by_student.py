try:
    from data_storage.read_historical_data import __get_historical_data
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from data_storage.read_historical_data import __get_historical_data


"""
This file creates a report of the scores by student.
"""

STUDENT_NAME_COLUMN = 0
SUBJECT_COLUMN = 1
SCORE_1_COLUMN = 2
SCORE_2_COLUMN = 3
SCORE_3_COLUMN = 4
FINAL_SCORE_COLUMN = 5


def __filter_data_by_student(data: list, student_name: str) -> list:
    """Filters the data for a specific student.

    Args:
        data (list): The complete dataset.
        student_name (str): The name of the student to filter by.

    Returns:
        list: The filtered dataset for the specific student.
    """
    filtered_data = list()
    index = 0
    for record in data:
        index += 1
        if index == 1:
            filtered_data.append(record)
        if record[STUDENT_NAME_COLUMN] == student_name:
            filtered_data.append(record)
    return filtered_data


def __display_report(data: list, student_name: str) -> None:
    """Displays the report for the student.

    Args:
        data (list): The filtered dataset for the specific student.
        student_name (str): The name of the student to generate the report for.
    """
    if not data:
        print(f"No data available for student: {student_name}.")
        return
    n = 20
    print(f"\n{'-'*100}\n\nReport for {student_name}:\n")

    print(f"\n{'Final Scores:'.center(45)} \n{'Subject'.ljust(n)} {'Score'.rjust(n)}")
    print("-" * 45)
    for record in data[1:]:
        subject = record[SUBJECT_COLUMN]
        final_score = str(record[FINAL_SCORE_COLUMN])
        print(f"{subject.ljust(n)} {final_score.rjust(n)}")
    print("-" * 45)

    print(f"\n\n{'Scores Evolution:'.center(45)} \n{'Subject'.ljust(n)} {'Scores'.rjust(n)}")
    print("-" * 45)
    for record in data[1:]:
        subject = record[SUBJECT_COLUMN]
        scores = [str(record[SCORE_1_COLUMN]).rjust(2), str(record[SCORE_2_COLUMN]).rjust(2), str(record[SCORE_3_COLUMN]).rjust(2)]
        print(f"{subject.ljust(n)} {' - '.join(scores).rjust(n)}")
    print("-" * 45)

    print(f"\n\n{'-'*100}\n\n")


def show_report_for_student(student_name: str) -> None:
    """Generates a report for a specific student.

    Args:
        student_name (str): The name of the student to generate the report for.
    """
    data = __get_historical_data("alumnos_test_003.csv")
    data = __filter_data_by_student(data, student_name)
    if not data:
        print(f"No data found for student: {student_name}")
        return
    __display_report(data, student_name)


show_report_for_student(student_name="Juanita Graciela Torralba Castell")
