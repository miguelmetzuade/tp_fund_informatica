try:
    from data_ingestion.students_scores_from_csv import read_scores_from_csv
except (ImportError, ModuleNotFoundError):
    import os
    import sys
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(1, path)

from data_ingestion.students_scores_from_csv import read_scores_from_csv


def calcular_nota_final(matriz):
    """
    Para caad alumno calcula la nota final como promedio de Nota1, Nota2, Nota3,
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
            fila.append(str(promedio))
        else:
            fila[5] = str(promedio)
    return matriz


if __name__ == "__main__":
    path = "data_input/alumnos_test_001.csv"
    matriz = read_scores_from_csv(path)
    matriz_con_promedios = calcular_nota_final(matriz)
    for fila in matriz_con_promedios:
        print(",".join(fila))
