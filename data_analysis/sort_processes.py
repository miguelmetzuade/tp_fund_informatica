from copy import deepcopy


def sort_matrix_by_bubblesort(data: list, col_to_compare: int, ascending: bool=True) -> list:

    data = deepcopy(data)

    columns = data.pop(0)
    i, j = 0, 0
    n = len(data)

    for i in range(n):
        j = 0
        for j in range(n - i - 1):
            element = data[j]
            value_1 = element[col_to_compare]
            # value_1 = float(value_1) if value_1 else 0
            element_2 = data[j+1]
            value_2 = element_2[col_to_compare]
            # value_2 = float(value_2) if value_2 else 0
            if (value_1 > value_2 and ascending) or (value_1 < value_2 and not ascending):
                data[j], data[j+1] = element_2, element

    data.insert(0, columns)
    return data


def sort_matrix_by_insertionsort(data: list, col_to_compare: int, ascending: bool=True) -> list:

    data = deepcopy(data)

    columns = data.pop(0)
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i - 1

        value_1 = key[col_to_compare]
        # value_1 = float(value_1) if value_1 else 0

        while j >= 0:
            element_2 = data[j]
            value_2 = element_2[col_to_compare]
            # value_2 = float(value_2) if value_2 else 0

            if (value_2 < value_1 and ascending) or (value_2 > value_1 and not ascending):
                break
            data[j + 1] = element_2
            j -= 1
        data[j + 1] = key

    data.insert(0, columns)
    return data
