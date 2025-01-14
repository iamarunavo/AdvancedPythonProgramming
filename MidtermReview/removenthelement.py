def remove_every_nth_element(lst: list[int], n: int) -> list[int]:
    for i in range(len(lst)-1, 0, -1):
        del(lst[i])

    return lst
mylist = [1, 2, 3, 4, 5, 6]
remove_every_nth_element(mylist, 2)
print(mylist)
# Expected Output: [1, 3, 5]