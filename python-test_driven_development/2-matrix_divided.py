def matrix_divided(matrix, div):
    """
    Divide all elts of a matrix by a number

    Args:
        matrix (list of lists): matrix to be divided
        div (int or float): number to divide the matrix by
    Raises:
        TypeError: if matrix is not a list or is empty
        TypeError: if matrix contains non int or float elts
        TypeError: if rows of matrix are of differents sizes
        TypesError: if div is not an int or a float
        ZeroDivisionError: if div is 0
    Return:
        new_matrix (list of lists):a new matrix w/ elts divided by div
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []

    for row in matrix:
        for num in row:
            new_matrix.append(round(num / div, 2))

    return new_matrix
