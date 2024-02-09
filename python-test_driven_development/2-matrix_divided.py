#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number

    Args:
        matrix (list of lists): matrix to be divided
        div (int or float): number to divide the matrix by

    Raises:
        TypeError: if matrix is not a list, is empty, or contains non-integer/float elements
        ValueError: if rows of matrix are of different sizes
        TypeError: if div is not an int or a float
        ZeroDivisionError: if div is 0

    Returns:
        new_matrix (list of lists): a new matrix with elements divided by div
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a non-empty list of lists")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix
