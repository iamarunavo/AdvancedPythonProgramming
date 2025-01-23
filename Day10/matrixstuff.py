def diag_diff(x):
    if len(x) != len(x[0]):
        raise Exception("Not a square matrix.")

    d1 = [x[i][i] for i in range(len(x))]
    d2 = [x[i][len(x) - 1 - i] for i in range(len(x))]

    return sum(d1) - sum(d2)

def matrix_add(x,y):
    if len(x) != len(x[0]):
        raise Exception("Not a square matrix.")
    
    sum_matrix=[]
    for i in range(len(x)):
        row = []
        for j in range(len(x)):
            row.append(x[i][j]+y[i][j])
        sum_matrix.append(row)

    return sum_matrix

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

result = matrix_add(matrix1, matrix2)
print(result)

def sum_col(x, i):
    return sum(row[i] for row in x)

def matrix_multi(x, y):
    if len(x) != len(x[0]) or len(y) != len(y[0]):
        raise Exception("Invalid matrix. Both must be square matrices.")
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        raise Exception("Both matrices must be the same size.")
    
    result = [[0 for i in range(len(x[0]))] for j in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            result[i][j] = sum(x[i][k] * y[k][j] for k in range(len(y)))
            
    return result