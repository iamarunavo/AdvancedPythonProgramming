def get_col(x, i):
    return [row[i] for row in x]
y = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(get_col(y, 2))

from random import randint
def diagonalSum(x):
    if len(x) != len(x[0]):
        raise Exception("Matrix must be square.")
    for row in x:
        print(row)
    total = 0
    for i in range(len(x)):
        for j in range(len(x[0])):
            if i == j:
                total += x[i][j]
    return total
print(diagonalSum([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,
14, 15, 16]]))