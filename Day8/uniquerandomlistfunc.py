from random import randint
def generaterandomlist(m, n, k):
    mylist = []
    for i in range(k):
        n=randint(m,n)
        while n in mylist:
            n = randint(m,n)
        mylist.append(n)

    max = mylist[0]
    for i in range(len(mylist)):
        if max < mylist[i]:
            max = mylist[i]

    print(mylist)
    print(max)

generaterandomlist(5, 26, 3)