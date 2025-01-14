def transpose(matrix: list[list[int]]) -> list[list[int]]:
    transposematrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposematrix.append(row)

    return transposematrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose(matrix)
print(transposed)
# Expected Output:
# [[1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]]
