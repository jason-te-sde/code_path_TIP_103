"""
Write a function add_matrices() that accepts two n x m matrices matrix1 and matrix2. The function should return an n x m matrix sum_matrix that is the sum of the given matrices such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

def add_matrices(matrix1, matrix2):
    pass
Example Usage

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)
Example Output:

[
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]
"""

def add_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2:
        return False
    
    n = len(matrix1)
    m = len(matrix1[0])
    if len(matrix2) != n or len(matrix2[0]) != m:
        return False
    
    new_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return new_matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))
            
            

