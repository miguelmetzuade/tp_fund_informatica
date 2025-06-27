try:
    from data_ingestion.students_scores_from_csv import read_scores_from_csv
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from data_ingestion.students_scores_from_csv import read_scores_from_csv
from data_ingestion.students_scores_manual import read_scores_from_terminal
from data_storage.update_hits_data_csv import update_hits_data_csv
from data_validation.students_scores_input_validation import validate_all_students

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
        if len(record) > FINAL_SCORE_COLUMN:
            record[FINAL_SCORE_COLUMN] = float(record[FINAL_SCORE_COLUMN]) if record[FINAL_SCORE_COLUMN] else 0
    return matriz

def calcular_nota_final(matriz):
    """
    Para cada alumno calcula la nota final como promedio de Nota1, Nota2, Nota3,
    y la pone en la columna NotaFinal (columna 5, índice 5).
    Si la fila ya tiene la columna, la sobreescribe, si no la tiene, la agrega.
    """
    for i, fila in enumerate(matriz):
        if i == 0 or fila[0].strip().lower() == "nombre":
            if len(fila) == 5:
                fila.append("NotaFinal")
            elif len(fila) >= 6:
                fila[5] = "NotaFinal"
            continue
        notas = fila[2:5]  # Toma las columnas 2,3,4
        # Verificar que hay 3 notas y son numéricas
        try:
            notas_float = [float(n) for n in notas]
            promedio = round(sum(notas_float)/3, 2)
        except Exception:
            promedio = ""  # Si falta alguna nota o no es número, dejar vacío
        # Escribir/Agregar la nota final
        if len(fila) < 6:
            fila.append(promedio)
        else:
            fila[5] = promedio
    return matriz


if __name__ == "__main__":

    # path = "data_input/alumnos_test_003.csv"
    # matriz = read_scores_from_csv(path)
    # matriz = __parse_scores_to_int(matriz)
    # matriz, errores = validate_all_students(matriz)
    # matriz_con_promedios = calcular_nota_final(matriz)
    # update_hits_data_csv(data=matriz_con_promedios, filename="alumnos_test_003.csv")

    matriz = read_scores_from_terminal()
    matriz = __parse_scores_to_int(matriz)
    matriz, errores = validate_all_students(matriz)
    matriz_con_promedios = calcular_nota_final(matriz)
    update_hits_data_csv(data=matriz_con_promedios, filename="alumnos_test_004.csv")
