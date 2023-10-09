#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for line in matrix:
        for col in range(len(line)):
            if col < len(line)-1:
                print("{}".format(line[col]), end=' ')
            else:
                print("{}".format(line[col]), end='')
        print(".format()")
