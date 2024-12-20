# MUH. RAFI RABBANI_F55123038

# WITH NUMPY

import numpy as np

A = np.array([[2, 0, -3], [1, 4, 5]])
B = np.array([[3, 1], [-1, 0], [4, 2]])
C = np.array([[4, 7], [2, 1], [1, -1]])

AB = np.dot(A, B)
AC = np.dot(A, C)

result = AB + AC
print("Hasil menggunakan library numpy:")
print(result)

# NO NUMPY

A = [[2, 0, -3], [1, 4, 5]]
B = [[3, 1], [-1, 0], [4, 2]]
C = [[4, 7], [2, 1], [1, -1]]

def matrix_multiply(X, Y):
    result = [[0] * len(Y[0]) for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def matrix_add(X, Y):
    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result

AB = matrix_multiply(A, B)
AC = matrix_multiply(A, C)

result = matrix_add(AB, AC)

print("Hasil tanpa library numpy:")
for row in result:
    print(row)
