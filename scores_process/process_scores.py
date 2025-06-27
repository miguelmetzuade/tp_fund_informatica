from data_ingestion.students_scores_from_csv import read_scores_from_csv

def calcular_nota_final(matriz):
    """
    Recibe la matriz de alumnos. Calcula y actualiza la nota final (columna 5) como el promedio de las 3 notas.
    Si la fila tiene valores vacíos en las notas, deja la nota final vacía.
    Salta la cabecera si existe.
    """
    for i, fila in enumerate(matriz):
        # Si es la cabecera, seguir
        if i == 0 or fila[0].lower() == "nombre":
            continue
        if len(fila) < 5:
            continue  # fila incompleta
        n1, n2, n3 = fila[2], fila[3], fila[4]
        # Si alguna nota está vacía, dejar nota final vacía
        if n1 == "" or n2 == "" or n3 == "":
            if len(fila) >= 6:
                fila[5] = ""
            else:
                fila.append("")
            continue
        try:
            n1 = float(n1)
            n2 = float(n2)
            n3 = float(n3)
            promedio = round((n1 + n2 + n3) / 3, 2)
            if len(fila) >= 6:
                fila[5] = str(promedio)
            else:
                fila.append(str(promedio))
        except Exception as e:
            if len(fila) >= 6:
                fila[5] = ""
            else:
                fila.append("")
    return matriz

if __name__ == "__main__":
    path = "data_input/alumnos_test_002.csv"  
    matriz = read_scores_from_csv(path)
    matriz_con_promedios = calcular_nota_final(matriz)
    for fila in matriz_con_promedios:
        print(fila)