"""
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

3x3 matrix before and after being transposed

def transpose(matrix):
    pass
Example Usage

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)
Example Output:

[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
[
    [1, 4],
    [2, 5],
    [3, 6]
]
"""
def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            res[j][i] = matrix[i][j]
    
    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))