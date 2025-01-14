def my_clear(lst):
    for i in range(len(lst)-1, -1, -1):
        del lst[i]

    print(lst)
a = [1, 2]
b = [3, 4]
c = [a, 5, b, 6]

my_clear(a)
my_clear(c)
my_clear(b)