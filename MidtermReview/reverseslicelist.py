def reverse_slice(lst: list[int], start: int, end: int) -> list[int]:
    mylist = lst[start:end+1]
    mylist.reverse()
    return mylist

lst = [10, 20, 30, 40, 50]
print(reverse_slice(lst, 1, 3))