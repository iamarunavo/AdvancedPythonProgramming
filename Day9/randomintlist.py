from random import randint

n = int(input("Enter amount of rows: "))
m = int(input("Enter amount of columns: "))
k = int(input("Enter max value for elements: "))
x = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(1, k))
    x.append(row)
for row in x:
    print(row)