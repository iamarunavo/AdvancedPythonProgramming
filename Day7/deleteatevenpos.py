def delete_at_even_position(x):
    for i in range(len(x) - 1, 0, -1):
        if (i + 1) % 2 == 0:
            del x[i]
    return x
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
delete_at_even_position(d)
print(d)