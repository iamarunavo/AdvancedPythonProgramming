mylist = [5, 4, 21, 20, 39]
mylist.sort(key=lambda x: x % 10)
print(mylist) # output: [20, 21, 4, 5, 39]