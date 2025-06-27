def is_valid_score(score):
    #Verifica si una nota está entre 0 y 10.
    try:
        score = float(score)
        return 0 <= score <= 10
    except ValueError:
        return False

def validate_student_row(row):
    #Valida una fila del archivo CSV.
    #Formato esperado: Nombre, Materia, Nota1, Nota2, Nota3, NotaFinal
    #Devuelve (True, "") si es válida, o (False, mensaje de error).
    
    if len(row) != 5:
        return False, f"Cantidad incorrecta de columnas: {row}"

    nombre, materia, *notas = row

    for i, nota in enumerate(notas):
        if not is_valid_score(nota):
            return False, f"Nota inválida en columna {i+3}: {nota}"

    # # Validación opcional: verificar que NotaFinal sea el promedio correcto
    # try:
    #     nota1, nota2, nota3, nota_final = map(float, notas)
    #     promedio = round((nota1 + nota2 + nota3) / 3, 2)
    #     if round(nota_final, 2) != promedio:
    #         return False, f"Nota final incorrecta. Esperado {promedio}, encontrado {nota_final}."
    # except ValueError:
    #     return False, f"Error convirtiendo notas a número en: {row} -- {}"

    return True, ""

def validate_all_students(data):
    #Valida todas las filas de una lista de estudiantes (lista de listas).
    #Devuelve dos listas: válidos y errores.
    cols = data[0]
    validos = [ cols ]
    errores = [ cols ]

    for i, row in enumerate(data):
        if i == 0:
            continue
        valido, mensaje = validate_student_row(row)
        if valido:
            validos.append(row)
        else:
            errores.append((i + 1, mensaje))  # fila, error

    return validos, errores

if __name__ == "__main__":
    test_data = [
        ["Juan", "Matemática", "8", "7", "9", "8.00"],  # válido
        ["Ana", "Física", "10", "11", "9", "10.00"],    # inválida (nota > 10)
        ["Luis", "Historia", "7", "6", "7", "6.5"],     # inválida (nota final mal calculada)
        ["Sofía", "Química", "9", "9", "9", "9.00"]     # válido
    ]

    valids, errors = validate_all_students(test_data)

    print(" Válidos:")
    for row in valids:
        print(row)

    print("\n Errores:")
    for line, error in errors:
        print(f"Fila {line}: {error}")
