from random import randint
mylist = []
for i in range(10):
    mylist.append(randint(1,10))

print(mylist)
print(max(mylist))

mylist1 = []
for i in range(10):
    mylist1.append(randint(1,10))

max = mylist1[0]
for i in range(10):
    if max < mylist1[i]:
        max = mylist1[i]

print(mylist1)
print(max)