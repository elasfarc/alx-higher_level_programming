def matrix_divided(matrix, div):
    is_valid_matrix = (
        type(matrix) is list
        and all([type(row) is list for row in matrix])
        and all(
            [
                all(valid_row)
                for valid_row in [
                    [n == n and type(n) in [int, float] for n in row]
                    for row in matrix
                ]
            ]
        )
    )
    if not is_valid_matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    is_rectangular_matrix = all([len(row) == len(matrix[0]) for row in matrix])
    if not is_rectangular_matrix:
        raise TypeError("Each row of the matrix must have the same size")

    is_valid_divisor = type(div) in [float, int] and div == div and div != 0
    if not is_valid_divisor:
        raise ZeroDivisionError("division by zero") if div == 0 else TypeError(
            "div must be a number"
        )

    return [[round(n / div, 2) for n in row] for row in matrix]
