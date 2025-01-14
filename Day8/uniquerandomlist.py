from random import randint
mylist = []
for i in range(10):
    n=randint(1,10)
    while n in mylist:
        n = randint(1,10)
    mylist.append(n)

print(mylist)
