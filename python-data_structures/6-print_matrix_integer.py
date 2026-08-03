#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        elements = []
        for integer in row:
            elements.append("{:d}".format(integer))
        print(" ".join(elements))
