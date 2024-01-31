#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        square = []
        for number in row:
            square.append(number ** 2)
        result.append(square)
    return result
