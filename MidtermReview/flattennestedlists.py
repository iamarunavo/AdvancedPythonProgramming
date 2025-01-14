def flatten(mylist: list) -> list:
    flatlist = []
    for i in mylist:
        if isinstance(i, list):
            flatlist.extend(flatten(i))
        else:
            flatlist.append(i)

    return flatlist

nested_list = [[1, [2, 3]], 4, [5, [6, 7]]]
flat_list = flatten(nested_list)
print(flat_list)
# Expected Output: [1, 2, 3, 4, 5, 6, 7]