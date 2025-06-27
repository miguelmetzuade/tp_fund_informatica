try:
    from handler_files.csv_manager import read_csv_as_matrix
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from handler_files.csv_manager import read_csv_as_matrix


STUDENT_NAME_COLUMN = 0
SUBJECT_COLUMN = 1
SCORE_1_COLUMN = 2
SCORE_2_COLUMN = 3
SCORE_3_COLUMN = 4
FINAL_SCORE_COLUMN = 5


def __parse_scores_to_int(matriz):
    for index, record in enumerate(matriz):
        if index == 0:
            continue
        record[SCORE_1_COLUMN] = int(record[SCORE_1_COLUMN]) if record[SCORE_1_COLUMN] else 0
        record[SCORE_2_COLUMN] = int(record[SCORE_2_COLUMN]) if record[SCORE_2_COLUMN] else 0
        record[SCORE_3_COLUMN] = int(record[SCORE_3_COLUMN]) if record[SCORE_3_COLUMN] else 0
        if len(record) >= FINAL_SCORE_COLUMN:
            record[FINAL_SCORE_COLUMN] = float(record[FINAL_SCORE_COLUMN]) if record[FINAL_SCORE_COLUMN] else 0
    return matriz

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
        raise Exception(f"The file {filename} is empty or does not contain valid data.")
    content = __parse_scores_to_int(content)
    return content
