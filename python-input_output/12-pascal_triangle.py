#!/usr/bin/python3
""" Pascal's triangle function """


def pascal_triangle(n):
    """ Represent Pascal's triangle of size n
    Returns:
        list of lists of int representing the triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):  # génération des lignes du triangle jusqu'à la size n
        if i == 0:
            triangle.append([1])  # ajout d'un 1 si triangle est vide (1er rg)
        else:
            row = [1]  # ajout du premier nb de la ligne

            for j in range(1, i):
                # ajout sum ligne prec en parcourant les nbs (sauf le dernier)
                previous_row = triangle[i - 1]
                new_value = previous_row[j - 1] + previous_row[j]
                row.append(new_value)

            row.append(1)  # ajout du dernier nb de la ligne
            triangle.append(row)

    return triangle
