def get_max_among_i(x, i):
    maximum = x[0]
    maximumIndex = 0
    for idx in range(i):
        if x[idx] > maximum:
            maximum = x[idx]
            maximumIndex = idx
    return (maximum, maximumIndex)

a = [4, 2, 7, 1, 45, 23]
print(get_max_among_i(a, 4))
print(get_max_among_i(a, 6))