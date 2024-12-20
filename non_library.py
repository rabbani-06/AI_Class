# MUH. RAFI RABBANI_F55123038

# Define matrices A, B, and C
A = [[2, 0, -3], [1, 4, 5]]
B = [[3, 1], [-1, 0], [4, 2]]
C = [[4, 7], [2, 1], [1, -1]]

# Function to multiply two matrices
def matrix_multiply(X, Y):
    result = [[0] * len(Y[0]) for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Function to add two matrices
def matrix_add(X, Y):
    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result

# Calculate AB and AC
AB = matrix_multiply(A, B)
AC = matrix_multiply(A, C)

# Calculate the result of AB + AC
result = matrix_add(AB, AC)

# Print the result
for row in result:
    print(row)
