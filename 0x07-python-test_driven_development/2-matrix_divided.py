#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

        Args:
            matrix (list): A list of lists of ints or floats.
            div (int/float): The divisor.
        Raises:
            TypeError: If the matrix contains non-numbers.
            TypeError: If the matrix contains rows of different sizes.
            TypeError: If div is not an int or float.
            ZeroDivisionError: If div is 0.
        Returns:
            A new matrix representing the result of the division.
        """
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
