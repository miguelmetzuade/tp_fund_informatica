try:
    from data_storage.read_historical_data import __get_historical_data
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from data_storage.read_historical_data import __get_historical_data
from data_analysis.sort_processes import sort_matrix_by_bubblesort, sort_matrix_by_insertionsort


"""
This file creates a report of the scores by subject.
"""

STUDENT_NAME_COLUMN = 0
SUBJECT_COLUMN = 1
SCORE_1_COLUMN = 2
SCORE_2_COLUMN = 3
SCORE_3_COLUMN = 4
FINAL_SCORE_COLUMN = 5


def __filter_data_by_subject(data: list, subject: str) -> list:
    """Filters the data for a specific subject.

    Args:
        data (list): The complete dataset.
        subject (str): The name of the subject to filter by.

    Returns:
        list: The filtered dataset for the specific subject.
    """
    filtered_data = list()
    index = 0
    for record in data:
        index += 1
        if index == 1:
            filtered_data.append(record)
        if record[SUBJECT_COLUMN] == subject:
            filtered_data.append(record)
    return filtered_data


def __display_report(data: list, subject: str) -> None:
    """Displays the report for the subject.

    Args:
        data (list): The filtered dataset for the specific subject.
        subject (str): The name of the subject to generate the report for.
    """
    if not data:
        print(f"No data available for subject: {subject}.")
        return
    n = 20
    print(f"\n{'-'*100}\n\nReport for {subject}:\n")

    data_sort_by_final_score = sort_matrix_by_bubblesort(data, FINAL_SCORE_COLUMN, ascending=False)
    print(f"\n{'Final Scores:'.center(45)} \n{'Student'.ljust(n+20)} {'Score'.rjust(n)}")
    print("-" * 70)
    for record in data_sort_by_final_score[1:]:
        student = record[STUDENT_NAME_COLUMN]
        final_score = str(record[FINAL_SCORE_COLUMN])
        print(f"{student.ljust(n+20)} {final_score.rjust(n)}")
    print("-" * 70)

    data_sort_by_first_score = sort_matrix_by_insertionsort(data, STUDENT_NAME_COLUMN, ascending=True)
    print(f"\n\n{'Scores Evolution:'.center(45)} \n{'Student'.ljust(n+20)} {'Scores'.rjust(n)}")
    print("-" * 45)
    for record in data_sort_by_first_score[1:]:
        student = record[STUDENT_NAME_COLUMN]
        scores = [str(record[SCORE_1_COLUMN]).rjust(2), str(record[SCORE_2_COLUMN]).rjust(2), str(record[SCORE_3_COLUMN]).rjust(2)]
        print(f"{student.ljust(n+20)} {' - '.join(scores).rjust(n)}")
    print("-" * 45)

    print(f"\n\n{'-'*100}\n\n")


def show_report_for_subject(subject_name: str) -> None:
    """Generates a report for a specific subject.

    Args:
        subject_name (str): The name of the subject to generate the report for.
    """
    data = __get_historical_data("alumnos_test_003.csv")
    data = __filter_data_by_subject(data, subject_name)
    if not data:
        print(f"No data found for subject: {subject_name}")
        return
    __display_report(data, subject_name)


show_report_for_subject(subject_name="Matemática")
