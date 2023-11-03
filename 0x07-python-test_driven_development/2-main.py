#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

try:
    matrix = [[3, "9"], [12, 3]]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)

try:
    matrix = [[3, 9], [12, 3]]
    print(matrix_divided(matrix, "2"))
    print(matrix)
except Exception as e:
    print(e)

print("checker 14")
try:
    print(matrix_divided([[4, 20], ["4", 2]], 2))
except Exception as e:
    print(e)

print("checker 15")
try:
    print(matrix_divided([[4, 20], [4, 3, 2]], 2))
except Exception as e:
    print(e)
